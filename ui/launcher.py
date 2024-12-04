from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget
from ui.generated.launcher import Ui_MainWindow as RawLauncher


class Launcher(QMainWindow, RawLauncher):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.launchButton.clicked.connect(self.handle_button_clicked)

    def handle_button_clicked(self):
        instances = self.instanceCount.value()
        print(f"Asked to launch {instances} instance(s)")
