# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'launcher.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(330, 82)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.launchLabel = QLabel(self.centralwidget)
        self.launchLabel.setObjectName(u"launchLabel")
        self.launchLabel.setGeometry(QRect(20, 10, 58, 16))
        self.detailLabel = QLabel(self.centralwidget)
        self.detailLabel.setObjectName(u"detailLabel")
        self.detailLabel.setGeometry(QRect(140, 10, 181, 16))
        self.instanceCount = QSpinBox(self.centralwidget)
        self.instanceCount.setObjectName(u"instanceCount")
        self.instanceCount.setGeometry(QRect(80, 10, 42, 22))
        self.instanceCount.setMinimum(1)
        self.instanceCount.setMaximum(5)
        self.launchButton = QPushButton(self.centralwidget)
        self.launchButton.setObjectName(u"launchButton")
        self.launchButton.setGeometry(QRect(10, 40, 301, 32))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simple Audio Player Launcher", None))
        self.launchLabel.setText(QCoreApplication.translate("MainWindow", u"Launch", None))
        self.detailLabel.setText(QCoreApplication.translate("MainWindow", u"instances of an audio player", None))
        self.launchButton.setText(QCoreApplication.translate("MainWindow", u"Go!", None))
    # retranslateUi

