from PySide6.QtWidgets import QApplication
from sys import argv
from ui.launcher import Launcher

app = QApplication(argv)

window = Launcher()
window.show()

app.exec()
