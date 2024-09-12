# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 450)
        MainWindow.setMinimumSize(QSize(700, 450))
        MainWindow.setStyleSheet(u"QWidget {\n"
"	font: 8pt \"Bahnschrift\";\n"
"	color: rgb(60, 66, 92);\n"
"	background-color: rgb(161, 204, 210);\n"
"}\n"
"\n"
"QFrame {\n"
"	color: rgb(60, 66, 92);\n"
"	background-color: rgba(255, 255, 255, 70);\n"
"	border: none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 2px solid rgba(255, 255, 255, 70);\n"
"	border-radius: 3px;\n"
"	color: rgb(60, 66, 92);\n"
"	background-color: rgb(161, 204, 210);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgba(255, 255, 255, 70);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	font: 12pt \"Bahnschrift\";\n"
"	border-radius: 3px;\n"
"	color: rgb(60, 66, 92);\n"
"	background-color: rgb(255, 145, 132);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font: 12pt \"Bahnschrift\";\n"
"	border: 1px solid rgb(253, 252, 76);\n"
"	border-radius: 3px;\n"
"	color: rgb(253, 252, 76);\n"
"	background-color: rgb(255, 184, 172);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	font: 12pt \"Bahnschrift\";\n"
"	color: rgb(253, 252"
                        ", 76);\n"
"	border: 2px solid rgb(60, 66, 92);\n"
"	background-color: rgba(56, 27, 85, 60);\n"
"}\n"
"\n"
"QProgressBar:chunk {\n"
"	background-color: rgb(255, 145, 132);\n"
"    width: 5px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTableView {\n"
"	font-size: 12px;\n"
"	border: none;\n"
"	gridline-color: rgba(255, 255, 255, 70);\n"
"	selection-color: rgb(253, 252, 76);\n"
"	selection-background-color: rgb(255, 145, 132);\n"
"}\n"
"\n"
"QTableWiew:section {\n"
"	border: none;\n"
"	padding-bottom: 5px;\n"
"	padding-top: 5px;\n"
"}\n"
"\n"
"QTableWiew:item {\n"
"	border-style: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMinimumSize(QSize(410, 0))
        self.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView.verticalHeader().setVisible(False)

        self.horizontalLayout.addWidget(self.tableView)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"font: 10pt \"Times New Roman\";")
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u0440\u043e\u043b\u043e\u0433 \u043a\u043b\u0438\u0435\u043d\u0442", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0418", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0418\u041e", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u041e", None))
    # retranslateUi

