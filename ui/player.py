from pathlib import Path
from PySide6.QtWidgets import QFileDialog, QMainWindow
from services.audio import AudioPlayer, AudioService
from ui.generated.player import Ui_MainWindow as RawPlayerWindow


class PlayerWindow(QMainWindow, RawPlayerWindow):
    __audio_service: AudioService = None
    __selected_sound_output: str = None
    __audio_filename: str = None
    __player: AudioPlayer = None

    def __init__(self, audio_service: AudioService = AudioService()) -> None:
        super().__init__()
        self.setupUi(self)
        self.__audio_service = audio_service

        # Sound card selection

        sound_outputs = self.__audio_service.get_sound_outputs()
        self.soundCard.addItems(sound_outputs)
        self.soundCard.currentTextChanged.connect(self.__handle_sound_output_changed)
        if sound_outputs:
            self.__selected_sound_output = sound_outputs[0]

        # File browse button

        self.fileBrowse.clicked.connect(self.__handle_browse_clicked)

        # Play/pause

        self.pushButton.clicked.connect(self.__handle_play_pause)

    def __handle_sound_output_changed(self, output: str):
        self.__selected_sound_output = output

    def __handle_browse_clicked(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open Sound File", str(Path.home()), "Audio Files (*.wav *.mp3)"
        )
        if filename:
            self.__audio_filename = filename
            self.filePath.setText(self.__audio_filename)

    def __handle_play_pause(self):
        if not self.__player:
            if not (self.__audio_filename and self.__selected_sound_output):
                return
            self.__player = self.__audio_service.get_player(
                self.__audio_filename,
                self.__selected_sound_output,
                self.__position_callback,
            )

        if self.__player.isPlaying():
            self.__player.pause()
        else:
            self.__player.play()

    def __position_callback(self, position: int, duration: int):
        self.progressBar.setMaximum(duration)
        self.progressBar.setValue(position)
