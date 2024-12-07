from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QAudioOutput, QMediaDevices, QMediaPlayer
from services.logging import get_logger, Logger
from typing import Callable, List


class AudioPlayer:
    __callback: Callable[[int, int], None]
    __logger: Logger
    __output: QAudioOutput
    __player: QMediaPlayer

    LOG_PREFIX = "Audio Player"

    def __init__(self, logger: Logger = get_logger(__name__)):
        self.__logger = logger

    def load(
        self, filename: str, output: QAudioOutput, callback: Callable[[int, int], None]
    ):
        self.__logger.info(
            "%s: load %s to play on %s", self.LOG_PREFIX, filename, output
        )

        self.__callback = callback

        # We have to keep an handle to the output
        # If it gets GC'd, we lose audio

        self.__output = output
        self.__output.setVolume(100)

        self.__player = QMediaPlayer()
        self.__player.mediaStatusChanged.connect(self.__handle_status_change)
        self.__player.errorOccurred.connect(self.__handle_error)
        self.__player.errorChanged.connect(self.__handle_error)
        self.__player.positionChanged.connect(self.__handle_position_changed)

        self.__player.setAudioOutput(self.__output)
        self.__player.setSource(QUrl.fromLocalFile(filename))

    def __handle_error(self, error: QMediaPlayer.Error, message: str):
        print(f"ERROR: {error} occurred in the player. Message: {message}")

    def __handle_status_change(self, status: QMediaPlayer.MediaStatus):
        print(f"Change media status to {status}")

    def __handle_position_changed(self, position: int):
        self.__callback(position, self.__player.duration())

    def play(self):
        self.__player.play()

    def pause(self):
        self.__player.pause()

    def isPlaying(self):
        return self.__player and self.__player.isPlaying()


class AudioService:
    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super(AudioService, cls).__new__(cls)
        return cls.instance

    def get_sound_outputs(self) -> List[str]:
        return [device.description() for device in QMediaDevices.audioOutputs()]

    def get_player(
        self, filename: str, soundcard: str, callback: Callable[[int, int], None]
    ) -> AudioPlayer:
        output = [
            QAudioOutput(device)
            for device in QMediaDevices.audioOutputs()
            if soundcard in device.description()
        ][0]
        player = AudioPlayer()
        player.load(filename, output, callback)
        return player
