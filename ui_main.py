# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QDateEdit,
    QFrame, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(469, 500)
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setStrikeOut(True)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(Qt.ClickFocus)
        MainWindow.setAcceptDrops(True)
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 255);")
        MainWindow.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 260, 151, 61))
        self.pushButton.setMinimumSize(QSize(0, 61))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.pushButton.setFont(font1)
        self.pushButton.setMouseTracking(True)
        self.pushButton.setTabletTracking(True)
        self.pushButton.setFocusPolicy(Qt.NoFocus)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 255);\n"
"\n"
"")
        self.pushButton.setInputMethodHints(Qt.ImhHiddenText)
        icon = QIcon()
        iconThemeName = u"500"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.pushButton.setIcon(icon)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setAutoRepeat(True)
        self.pushButton.setAutoExclusive(True)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setFlat(True)
        self.first = QDateEdit(self.centralwidget)
        self.first.setObjectName(u"first")
        self.first.setGeometry(QRect(10, 170, 221, 51))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setUnderline(False)
        self.first.setFont(font2)
        self.first.setLayoutDirection(Qt.LeftToRight)
        self.first.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.first.setAlignment(Qt.AlignCenter)
        self.first.setTimeSpec(Qt.TimeZone)
        self.first.setDate(QDate(1900, 1, 1))
        self.second = QDateEdit(self.centralwidget)
        self.second.setObjectName(u"second")
        self.second.setGeometry(QRect(240, 170, 201, 51))
        self.second.setMaximumSize(QSize(16777215, 16777215))
        self.second.setFont(font1)
        self.second.setMouseTracking(False)
        self.second.setTabletTracking(False)
        self.second.setFocusPolicy(Qt.WheelFocus)
        self.second.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.second.setAcceptDrops(False)
#if QT_CONFIG(tooltip)
        self.second.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.second.setToolTipDuration(0)
#if QT_CONFIG(statustip)
        self.second.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.second.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.second.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.second.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.second.setLayoutDirection(Qt.LeftToRight)
        self.second.setAutoFillBackground(True)
        self.second.setStyleSheet(u"border-color: rgb(0, 0, 255);\n"
"border-color: rgb(0, 0, 255);\n"
"color: rgb(0, 0, 255);")
        self.second.setInputMethodHints(Qt.ImhHiddenText)
        self.second.setWrapping(False)
        self.second.setAlignment(Qt.AlignCenter)
        self.second.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.second.setAccelerated(True)
        self.second.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.second.setProperty("showGroupSeparator", False)
        self.second.setTimeSpec(Qt.LocalTime)
        self.second.setDate(QDate(2022, 1, 1))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 100, 161, 41))
        self.label.setStyleSheet(u"font: 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 100, 141, 41))
        self.label_2.setStyleSheet(u"font: 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 255);")
        self.result = QTextEdit(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(30, 350, 381, 71))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result.sizePolicy().hasHeightForWidth())
        self.result.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(18)
        self.result.setFont(font3)
        self.result.setLayoutDirection(Qt.RightToLeft)
        self.result.setAutoFillBackground(True)
        self.result.setStyleSheet(u"\n"
"border-bottom-color: rgb(0, 85, 255);\n"
"color: rgb(255, 0, 0);")
        self.result.setFrameShape(QFrame.NoFrame)
        self.result.setFrameShadow(QFrame.Plain)
        self.result.setLineWidth(2)
        self.result.setMidLineWidth(0)
        self.result.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.result.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.result.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.result.setAutoFormatting(QTextEdit.AutoBulletList)
        self.result.setTabChangesFocus(False)
        self.result.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 10, 251, 61))
        self.label_3.setStyleSheet(u"font: 28pt \"Segoe UI\";\n"
"color: rgb(255, 0, 0);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Age calcultor", None))
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.second.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Given Date", None))
#if QT_CONFIG(whatsthis)
        self.result.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">gjhgj</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Age Calculator", None))
    # retranslateUi

