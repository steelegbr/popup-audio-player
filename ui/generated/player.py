# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'player.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 240)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 182, 791, 51))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(24)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(-1, -9, 191, 191))
        self.fileLabel = QLabel(self.centralwidget)
        self.fileLabel.setObjectName(u"fileLabel")
        self.fileLabel.setGeometry(QRect(200, 10, 58, 16))
        self.filePath = QLineEdit(self.centralwidget)
        self.filePath.setObjectName(u"filePath")
        self.filePath.setGeometry(QRect(200, 30, 471, 21))
        self.filePath.setReadOnly(True)
        self.fileBrowse = QPushButton(self.centralwidget)
        self.fileBrowse.setObjectName(u"fileBrowse")
        self.fileBrowse.setGeometry(QRect(680, 20, 100, 41))
        self.soundCardLabel = QLabel(self.centralwidget)
        self.soundCardLabel.setObjectName(u"soundCardLabel")
        self.soundCardLabel.setGeometry(QRect(200, 80, 81, 16))
        self.soundCard = QComboBox(self.centralwidget)
        self.soundCard.setObjectName(u"soundCard")
        self.soundCard.setGeometry(QRect(190, 100, 591, 32))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Player", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Play / Pause", None))
        self.fileLabel.setText(QCoreApplication.translate("MainWindow", u"File:", None))
        self.fileBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.soundCardLabel.setText(QCoreApplication.translate("MainWindow", u"Sound Card:", None))
    # retranslateUi

