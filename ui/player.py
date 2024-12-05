from PySide6.QtWidgets import QMainWindow
from services.audio import AudioService
from ui.generated.player import Ui_MainWindow as RawPlayerWindow


class PlayerWindow(QMainWindow, RawPlayerWindow):
    __audio_service: AudioService
    __selected_sound_output: str

    def __init__(self, audio_service: AudioService = AudioService()) -> None:
        super().__init__()
        self.setupUi(self)
        self.__audio_service = audio_service

        sound_outputs = self.__audio_service.get_sound_outputs()
        self.soundCard.addItems(sound_outputs)
        if sound_outputs:
            self.__selected_sound_output = sound_outputs[0]
