import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView
from PySide6.QtSql import QSqlTableModel

from MainWindow import Ui_MainWindow
from base_data_SI import Data_SI
from base_data_IO import Data_IO
from base_data_VO import Data_VO


class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)

        self.conn_SI = Data_SI()
        self.conn_IO = Data_IO()
        self.conn_VO = Data_VO()

        self.a = 1
        self.tablewiew()
        self.table_update_SI()

    def tablewiew(self):
        # self.ui_main.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui_main.pushButton_2.clicked.connect(lambda: self.table_update_SI())
        self.ui_main.pushButton_3.clicked.connect(lambda: self.table_update_IO())
        self.ui_main.pushButton_4.clicked.connect(lambda: self.table_update_VO())

    def table_update_SI(self):
        self.model_SI = QSqlTableModel(self, db=self.conn_SI.create_connection_SI())
        self.model_SI.setTable('database_SI')
        self.model_SI.select()
        self.ui_main.tableView.setModel(self.model_SI)
        self.ui_main.tableView.setFixedWidth(427)
        self.ui_main.tableView.setColumnHidden(0, True)
        self.ui_main.tableView.setColumnHidden(1, False)
        self.ui_main.tableView.setColumnWidth(1, 60)
        self.ui_main.tableView.setColumnHidden(2, False)
        self.ui_main.tableView.setColumnWidth(2, 200)
        self.ui_main.tableView.setColumnHidden(3, False)
        self.ui_main.tableView.setColumnWidth(3, 150)
        self.ui_main.tableView.setColumnHidden(4, True)
        self.ui_main.tableView.setColumnHidden(5, True)
        self.ui_main.tableView.setColumnHidden(6, True)
        self.ui_main.tableView.setColumnHidden(7, True)
        self.ui_main.tableView.setColumnHidden(8, True)
        self.ui_main.tableView.setColumnHidden(9, True)
        self.ui_main.tableView.setColumnHidden(10, True)
        self.ui_main.tableView.setColumnHidden(11, True)
        self.ui_main.tableView.setColumnHidden(12, True)
        self.ui_main.tableView.setColumnHidden(13, True)
        self.ui_main.tableView.setColumnHidden(14, True)
        self.ui_main.tableView.setColumnHidden(15, True)
        self.ui_main.tableView.setColumnHidden(16, True)
        self.ui_main.tableView.setColumnHidden(17, True)
        self.ui_main.tableView.setColumnHidden(18, True)
        self.ui_main.tableView.setColumnHidden(19, True)
        self.ui_main.tableView.setColumnHidden(20, True)
        self.ui_main.tableView.setColumnHidden(21, True)
        self.ui_main.pushButton_2.setStyleSheet(u"QPushButton {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "border: 2px solid rgba(170, 80, 0, 150);\n"
                                        "background-color: rgba(255, 202, 128, 120);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "border: 2px solid rgba(170, 80, 0, 150);\n"
                                        "background-color: rgba(255, 202, 128, 120);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "background-color: rgba(255, 202, 128, 60);\n"
                                        "}")
        self.ui_main.pushButton_3.setStyleSheet(u"QPushButton {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "background-color: rgb(255, 202, 128);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "border: 2px solid rgba(170, 80, 0, 150);\n"
                                        "background-color: rgba(255, 202, 128, 120);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "background-color: rgba(255, 202, 128, 60);\n"
                                        "}")
        self.ui_main.pushButton_4.setStyleSheet(u"QPushButton {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "background-color: rgb(255, 202, 128);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "border: 2px solid rgba(170, 80, 0, 150);\n"
                                        "background-color: rgba(255, 202, 128, 120);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "background-color: rgba(255, 202, 128, 60);\n"
                                        "}")
        self.a = 1
        return self.a

    def table_update_IO(self):
        self.model_IO = QSqlTableModel(self, db=self.conn_IO.create_connection_IO())
        self.model_IO.setTable('database_IO')
        self.model_IO.select()
        self.ui_main.tableView.setModel(self.model_IO)
        self.ui_main.tableView.setFixedWidth(277)
        self.ui_main.tableView.setColumnHidden(0, True)
        self.ui_main.tableView.setColumnHidden(1, False)
        self.ui_main.tableView.setColumnWidth(1, 60)
        self.ui_main.tableView.setColumnHidden(2, True)
        self.ui_main.tableView.setColumnHidden(3, False)
        self.ui_main.tableView.setColumnWidth(3, 200)
        self.ui_main.tableView.setColumnHidden(4, True)
        self.ui_main.tableView.setColumnHidden(5, True)
        self.ui_main.tableView.setColumnHidden(6, True)
        self.ui_main.tableView.setColumnHidden(7, True)
        self.ui_main.tableView.setColumnHidden(8, True)
        self.ui_main.tableView.setColumnHidden(9, True)
        self.ui_main.tableView.setColumnHidden(10, True)
        self.ui_main.tableView.setColumnHidden(11, True)
        self.ui_main.tableView.setColumnHidden(12, True)
        self.ui_main.tableView.setColumnHidden(13, True)
        self.ui_main.tableView.setColumnHidden(14, True)
        self.ui_main.tableView.setColumnHidden(15, True)
        self.ui_main.tableView.setColumnHidden(16, True)
        self.ui_main.tableView.setColumnHidden(17, True)
        self.ui_main.tableView.setColumnHidden(18, True)
        self.ui_main.tableView.setColumnHidden(19, True)
        self.ui_main.tableView.setColumnHidden(20, True)
        self.ui_main.tableView.setColumnHidden(21, True)
        self.ui_main.pushButton_2.setStyleSheet(u"QPushButton {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "background-color: rgb(255, 202, 128);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "border: 2px solid rgba(170, 80, 0, 150);\n"
                                        "background-color: rgba(255, 202, 128, 120);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "background-color: rgba(255, 202, 128, 60);\n"
                                        "}")
        self.ui_main.pushButton_3.setStyleSheet(u"QPushButton {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "border: 2px solid rgba(170, 80, 0, 150);\n"
                                        "background-color: rgba(255, 202, 128, 120);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "border: 2px solid rgba(170, 80, 0, 150);\n"
                                        "background-color: rgba(255, 202, 128, 120);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "background-color: rgba(255, 202, 128, 60);\n"
                                        "}")
        self.ui_main.pushButton_4.setStyleSheet(u"QPushButton {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "background-color: rgb(255, 202, 128);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "border: 2px solid rgba(170, 80, 0, 150);\n"
                                        "background-color: rgba(255, 202, 128, 120);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "background-color: rgba(255, 202, 128, 60);\n"
                                        "}")
        self.a = 2
        return self.a

    def table_update_VO(self):
        self.model_VO = QSqlTableModel(self, db=self.conn_VO.create_connection_VO())
        self.model_VO.setTable('database_VO')
        self.model_VO.select()
        self.ui_main.tableView.setModel(self.model_VO)
        self.ui_main.tableView.setColumnHidden(0, True)
        self.ui_main.tableView.setColumnHidden(1, False)
        self.ui_main.tableView.setColumnHidden(2, False)
        self.ui_main.tableView.setColumnHidden(3, True)
        self.ui_main.tableView.setColumnHidden(4, True)
        self.ui_main.tableView.setColumnHidden(5, True)
        self.ui_main.tableView.setColumnHidden(6, True)
        self.ui_main.tableView.setColumnHidden(7, True)
        self.ui_main.tableView.setColumnHidden(8, True)
        self.ui_main.tableView.setColumnHidden(9, True)
        self.ui_main.tableView.setColumnHidden(10, True)
        self.ui_main.tableView.setColumnHidden(11, True)
        self.ui_main.tableView.setColumnHidden(12, True)
        self.ui_main.tableView.setColumnHidden(13, True)
        self.ui_main.tableView.setColumnHidden(14, True)
        self.ui_main.tableView.setColumnHidden(15, True)
        self.ui_main.tableView.setColumnHidden(16, True)
        self.ui_main.tableView.setColumnHidden(17, True)
        self.ui_main.tableView.setColumnHidden(18, True)
        self.ui_main.tableView.setColumnHidden(19, True)
        self.ui_main.tableView.setColumnHidden(20, True)
        self.ui_main.tableView.setColumnHidden(21, True)
        self.ui_main.pushButton_2.setStyleSheet(u"QPushButton {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "background-color: rgb(255, 202, 128);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "border: 2px solid rgba(170, 80, 0, 150);\n"
                                        "background-color: rgba(255, 202, 128, 120);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "background-color: rgba(255, 202, 128, 60);\n"
                                        "}")
        self.ui_main.pushButton_3.setStyleSheet(u"QPushButton {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "background-color: rgb(255, 202, 128);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "border: 2px solid rgba(170, 80, 0, 150);\n"
                                        "background-color: rgba(255, 202, 128, 120);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "background-color: rgba(255, 202, 128, 60);\n"
                                        "}")
        self.ui_main.pushButton_4.setStyleSheet(u"QPushButton {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "border: 2px solid rgba(170, 80, 0, 150);\n"
                                        "background-color: rgba(255, 202, 128, 120);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "border: 2px solid rgba(170, 80, 0, 150);\n"
                                        "background-color: rgba(255, 202, 128, 120);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "font: 12pt \"Bahnschrift\";\n"
                                        "background-color: rgba(255, 202, 128, 60);\n"
                                        "}")
        self.a = 3
        return self.a


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec())
