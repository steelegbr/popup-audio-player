from PySide6.QtWidgets import QMainWindow
from typing import List
from ui.generated.launcher import Ui_MainWindow as RawLauncher
from ui.player import PlayerWindow


class Launcher(QMainWindow, RawLauncher):
    __players: List[PlayerWindow]

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.launchButton.clicked.connect(self.handle_button_clicked)

    def handle_button_clicked(self):
        instances = self.instanceCount.value()
        print(f"Asked to launch {instances} instance(s)")

        self.__players = [PlayerWindow() for _ in range(instances)]
        for window in self.__players:
            window.show()

        self.launchButton.setDisabled(True)
        self.instanceCount.setDisabled(True)
