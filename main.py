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
        self.ui_main.pushButton_2.clicked.connect(lambda: self.table_update_SI())
        self.ui_main.pushButton_3.clicked.connect(lambda: self.table_update_IO())
        self.ui_main.pushButton_4.clicked.connect(lambda: self.table_update_VO())
        self.ui_main.tableView.clicked.connect(lambda: self.info_SI() if self.a == 1
                                               else self.info_IO() if self.a == 2
                                               else self.info_VO())

    def table_update_SI(self):
        self.ui_main.plainTextEdit.clear()
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
        self.ui_main.plainTextEdit.clear()
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
        self.ui_main.plainTextEdit.clear()
        self.model_VO = QSqlTableModel(self, db=self.conn_VO.create_connection_VO())
        self.model_VO.setTable('database_VO')
        self.model_VO.select()
        self.ui_main.tableView.setModel(self.model_VO)
        self.ui_main.tableView.setFixedWidth(297)
        self.ui_main.tableView.setColumnHidden(0, True)
        self.ui_main.tableView.setColumnHidden(1, False)
        self.ui_main.tableView.setColumnWidth(1, 60)
        self.ui_main.tableView.setColumnHidden(2, False)
        self.ui_main.tableView.setColumnWidth(2, 220)
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

    def info_SI(self):
        if self.ui_main.tableView.selectedIndexes()[0].row() is not None:
            sel_id = self.ui_main.tableView.selectedIndexes()[0].row()
        else:
            sel_id = 0
        if self.a == 1:
            naim = self.model_SI.record(sel_id).value("Наименование")
            mod = self.model_SI.record(sel_id).value("Модификация")
            inv_num = self.model_SI.record(sel_id).value("Инв\xa0номер")
            zav_num = self.model_SI.record(sel_id).value("Зав\xa0номер")

            range_text = self.model_SI.record(sel_id).value("Диапазоны")
            range_text_split = range_text.split("@")
            if len(range_text_split) == 5:
                range = 'от ' + str(range_text_split[-4]) + ' до ' + str(range_text_split[-3]) + " " + str(range_text_split[-1])
                pogr = str(range_text_split[-2])
                if str(range_text_split[-4]) == " ":
                    range = str(range_text_split[-3]) + " " + str(range_text_split[-1])
            elif len(range_text_split) == 10:
                r_1 = 'от ' + str(range_text_split[-9]) + ' до ' + str(range_text_split[-8]) + " " + str(range_text_split[-6])
                po_1 = str(range_text_split[-7])
                r_2 = 'от ' + str(range_text_split[-4]) + ' до ' + str(range_text_split[-3]) + " " + str(range_text_split[-1])
                po_2 = str(range_text_split[-2])
                range = r_1 + '\n' + r_2
                pogr = po_1 + '\n' + po_2
            elif len(range_text_split) == 15:
                r_1 = 'от ' + str(range_text_split[-14]) + ' до ' + str(range_text_split[-13]) + " " + str(range_text_split[-11])
                po_1 = str(range_text_split[-12])
                r_2 = 'от ' + str(range_text_split[-9]) + ' до ' + str(range_text_split[-8]) + " " + str(range_text_split[-6])
                po_2 = str(range_text_split[-7])
                r_3 = 'от ' + str(range_text_split[-4]) + ' до ' + str(range_text_split[-3]) + " " + str(range_text_split[-1])
                po_3 = str(range_text_split[-2])
                range = r_1 + '\n' + r_2 + "\n" + r_3
                pogr = po_1 + '\n' + po_2 + "\n" + po_3
            elif len(range_text_split) == 20:
                r_1 = 'от ' + str(range_text_split[-19]) + ' до ' + str(range_text_split[-18]) + " " + str(range_text_split[-16])
                po_1 = str(range_text_split[-17])
                r_2 = 'от ' + str(range_text_split[-14]) + ' до ' + str(range_text_split[-13]) + " " + str(range_text_split[-11])
                po_2 = str(range_text_split[-12])
                r_3 = 'от ' + str(range_text_split[-9]) + ' до ' + str(range_text_split[-8]) + " " + str(range_text_split[-6])
                po_3 = str(range_text_split[-7])
                r_4 = 'от ' + str(range_text_split[-4]) + ' до ' + str(range_text_split[-3]) + " " + str(range_text_split[-1])
                po_4 = str(range_text_split[-2])
                range = r_1 + '\n' + r_2 + "\n" + r_3 + "\n" + r_4
                pogr = po_1 + '\n' + po_2 + "\n" + po_3 + "\n" + po_4
            elif len(range_text_split) == 25:
                r_1 = 'от ' + str(range_text_split[-24]) + ' до ' + str(range_text_split[-23]) + " " + str(range_text_split[-21])
                po_1 = str(range_text_split[-22])
                r_2 = 'от ' + str(range_text_split[-19]) + ' до ' + str(range_text_split[-18]) + " " + str(range_text_split[-16])
                po_2 = str(range_text_split[-17])
                r_3 = 'от ' + str(range_text_split[-14]) + ' до ' + str(range_text_split[-13]) + " " + str(range_text_split[-11])
                po_3 = str(range_text_split[-12])
                r_4 = 'от ' + str(range_text_split[-9]) + ' до ' + str(range_text_split[-8]) + " " + str(range_text_split[-6])
                po_4 = str(range_text_split[-7])
                r_5 = 'от ' + str(range_text_split[-4]) + ' до ' + str(range_text_split[-3]) + " " + str(range_text_split[-1])
                po_5 = str(range_text_split[-2])
                range = r_1 + '\n' + r_2 + "\n" + r_3 + "\n" + r_4 + "\n" + r_5
                pogr = po_1 + '\n' + po_2 + "\n" + po_3 + "\n" + po_4 + '\n' + po_5
            elif len(range_text_split) == 30:
                r_1 = 'от ' + str(range_text_split[-29]) + ' до ' + str(range_text_split[-28]) + " " + str(range_text_split[-26])
                po_1 = str(range_text_split[-27])
                r_2 = 'от ' + str(range_text_split[-24]) + ' до ' + str(range_text_split[-23]) + " " + str(range_text_split[-21])
                po_2 = str(range_text_split[-22])
                r_3 = 'от ' + str(range_text_split[-19]) + ' до ' + str(range_text_split[-18]) + " " + str(range_text_split[-16])
                po_3 = str(range_text_split[-17])
                r_4 = 'от ' + str(range_text_split[-14]) + ' до ' + str(range_text_split[-13]) + " " + str(range_text_split[-11])
                po_4 = str(range_text_split[-12])
                r_5 = 'от ' + str(range_text_split[-9]) + ' до ' + str(range_text_split[-8]) + " " + str(range_text_split[-6])
                po_5 = str(range_text_split[-7])
                r_6 = 'от ' + str(range_text_split[-4]) + ' до ' + str(range_text_split[-3]) + " " + str(range_text_split[-1])
                po_6 = str(range_text_split[-2])
                range = r_1 + '\n' + r_2 + "\n" + r_3 + "\n" + r_4 + "\n" + r_5 + "\n" + r_6
                pogr = po_1 + '\n' + po_2 + "\n" + po_3 + "\n" + po_4 + '\n' + po_5 + '\n' + po_6
            elif len(range_text_split) == 35:
                r_1 = 'от ' + str(range_text_split[-34]) + ' до ' + str(range_text_split[-33]) + " " + str(range_text_split[-31])
                po_1 = str(range_text_split[-32])
                r_2 = 'от ' + str(range_text_split[-29]) + ' до ' + str(range_text_split[-28]) + " " + str(range_text_split[-26])
                po_2 = str(range_text_split[-27])
                r_3 = 'от ' + str(range_text_split[-24]) + ' до ' + str(range_text_split[-23]) + " " + str(range_text_split[-21])
                po_3 = str(range_text_split[-22])
                r_4 = 'от ' + str(range_text_split[-19]) + ' до ' + str(range_text_split[-18]) + " " + str(range_text_split[-16])
                po_4 = str(range_text_split[-17])
                r_5 = 'от ' + str(range_text_split[-14]) + ' до ' + str(range_text_split[-13]) + " " + str(range_text_split[-11])
                po_5 = str(range_text_split[-12])
                r_6 = 'от ' + str(range_text_split[-9]) + ' до ' + str(range_text_split[-8]) + " " + str(range_text_split[-6])
                po_6 = str(range_text_split[-7])
                r_7 = 'от ' + str(range_text_split[-4]) + ' до ' + str(range_text_split[-3]) + " " + str(range_text_split[-1])
                po_7 = str(range_text_split[-2])
                range = r_1 + '\n' + r_2 + "\n" + r_3 + "\n" + r_4 + "\n" + r_5 + "\n" + r_6 + "\n" + r_7
                pogr = po_1 + '\n' + po_2 + "\n" + po_3 + "\n" + po_4 + '\n' + po_5 + '\n' + po_6 + '\n' + po_7
            elif len(range_text_split) == 40:
                r_1 = 'от ' + str(range_text_split[-39]) + ' до ' + str(range_text_split[-38]) + " " + str(range_text_split[-36])
                po_1 = str(range_text_split[-37])
                r_2 = 'от ' + str(range_text_split[-34]) + ' до ' + str(range_text_split[-33]) + " " + str(range_text_split[-31])
                po_2 = str(range_text_split[-32])
                r_3 = 'от ' + str(range_text_split[-29]) + ' до ' + str(range_text_split[-28]) + " " + str(range_text_split[-26])
                po_3 = str(range_text_split[-27])
                r_4 = 'от ' + str(range_text_split[-24]) + ' до ' + str(range_text_split[-23]) + " " + str(range_text_split[-21])
                po_4 = str(range_text_split[-22])
                r_5 = 'от ' + str(range_text_split[-19]) + ' до ' + str(range_text_split[-18]) + " " + str(range_text_split[-16])
                po_5 = str(range_text_split[-17])
                r_6 = 'от ' + str(range_text_split[-14]) + ' до ' + str(range_text_split[-13]) + " " + str(range_text_split[-11])
                po_6 = str(range_text_split[-12])
                r_7 = 'от ' + str(range_text_split[-9]) + ' до ' + str(range_text_split[-8]) + " " + str(range_text_split[-6])
                po_7 = str(range_text_split[-7])
                r_8 = 'от ' + str(range_text_split[-4]) + ' до ' + str(range_text_split[-3]) + " " + str(range_text_split[-1])
                po_8 = str(range_text_split[-2])
                range = r_1 + '\n' + r_2 + "\n" + r_3 + "\n" + r_4 + "\n" + r_5 + "\n" + r_6 + "\n" + r_7 + '\n' + r_8
                pogr = po_1 + '\n' + po_2 + "\n" + po_3 + "\n" + po_4 + '\n' + po_5 + '\n' + po_6 + '\n' + po_7 + '\n' + po_8

            pov_text = self.model_SI.record(sel_id).value("Поверки")
            pov_text_split = pov_text.split("@")
            pov_last = pov_text_split[-1]

            if len(pov_text_split) == 1:
                pov_last = "бессрочно"
                all_pov = "нет"

            if len(pov_text_split) == 4:
                p_1 = "от " + pov_text_split[-4] + " до " + pov_text_split[-1]
                all_pov = p_1
            elif len(pov_text_split) == 8:
                p_1 = "от " + pov_text_split[-8] + " до " + pov_text_split[-5]
                p_2 = "от " + pov_text_split[-4] + " до " + pov_text_split[-1]
                all_pov = p_1 + '\n' + p_2
            elif len(pov_text_split) == 12:
                p_1 = "от " + pov_text_split[-12] + " до " + pov_text_split[-9]
                p_2 = "от " + pov_text_split[-8] + " до " + pov_text_split[-5]
                p_3 = "от " + pov_text_split[-4] + " до " + pov_text_split[-1]
                all_pov = p_1 + '\n' + p_2 + "\n" + p_3
            elif len(pov_text_split) == 16:
                p_1 = "от " + pov_text_split[-16] + " до " + pov_text_split[-13]
                p_2 = "от " + pov_text_split[-12] + " до " + pov_text_split[-9]
                p_3 = "от " + pov_text_split[-8] + " до " + pov_text_split[-5]
                p_4 = "от " + pov_text_split[-4] + " до " + pov_text_split[-1]
                all_pov = p_1 + '\n' + p_2 + "\n" + p_3 + "\n" + p_4
            elif len(pov_text_split) == 20:
                p_1 = "от " + pov_text_split[-20] + " до " + pov_text_split[-17]
                p_2 = "от " + pov_text_split[-16] + " до " + pov_text_split[-13]
                p_3 = "от " + pov_text_split[-12] + " до " + pov_text_split[-9]
                p_4 = "от " + pov_text_split[-8] + " до " + pov_text_split[-5]
                p_5 = "от " + pov_text_split[-4] + " до " + pov_text_split[-1]
                all_pov = p_1 + '\n' + p_2 + "\n" + p_3 + "\n" + p_4 + "\n" + p_5
            elif len(pov_text_split) == 24:
                p_1 = "от " + pov_text_split[-24] + " до " + pov_text_split[-21]
                p_2 = "от " + pov_text_split[-20] + " до " + pov_text_split[-17]
                p_3 = "от " + pov_text_split[-16] + " до " + pov_text_split[-13]
                p_4 = "от " + pov_text_split[-12] + " до " + pov_text_split[-9]
                p_5 = "от " + pov_text_split[-8] + " до " + pov_text_split[-5]
                p_6 = "от " + pov_text_split[-4] + " до " + pov_text_split[-1]
                all_pov = p_1 + '\n' + p_2 + "\n" + p_3 + "\n" + p_4 + "\n" + p_5 + "\n" + p_6

            self.ui_main.plainTextEdit.clear()
            self.ui_main.plainTextEdit.appendPlainText(naim + " " + mod + "\n\nзав. № " + zav_num + "\nинв. № " + inv_num + "\n\n" + range + '\n\n' + pogr + '\n\n' + pov_last + '\n\nВсе поверки:\n' + all_pov)

        else:
            pass

    def info_IO(self):
        if self.ui_main.tableView.selectedIndexes()[0].row() is not None:
            sel_id = self.ui_main.tableView.selectedIndexes()[0].row()
        else:
            sel_id = 0
        if self.a == 2:
            naim = self.model_IO.record(sel_id).value("Наименование")
            inv_num = self.model_IO.record(sel_id).value("Инв\xa0номер")
            zav_num = self.model_IO.record(sel_id).value("Зав\xa0номер")

            att_text = self.model_IO.record(sel_id).value("Аттестация")
            att_text_split = att_text.split("@")

            att_1 = att_text_split[-1]
            att_2 = att_text_split[-2]

            if len(att_text_split) == 4:
                p_1 = "от " + att_text_split[-4] + " до " + att_text_split[-1] + "   Протокол № " + att_text_split[-2]
                all_pov = p_1
            elif len(att_text_split) == 8:
                p_1 = "от " + att_text_split[-8] + " до " + att_text_split[-5] + "   Протокол № " + att_text_split[-6]
                p_2 = "от " + att_text_split[-4] + " до " + att_text_split[-1] + "   Протокол № " + att_text_split[-2]
                all_pov = p_1 + '\n' + p_2
            elif len(att_text_split) == 12:
                p_1 = "от " + att_text_split[-12] + " до " + att_text_split[-9] + "   Протокол № " + att_text_split[-10]
                p_2 = "от " + att_text_split[-8] + " до " + att_text_split[-5] + "   Протокол № " + att_text_split[-6]
                p_3 = "от " + att_text_split[-4] + " до " + att_text_split[-1] + "   Протокол № " + att_text_split[-2]
                all_pov = p_1 + '\n' + p_2 + "\n" + p_3
            elif len(att_text_split) == 16:
                p_1 = "от " + att_text_split[-16] + " до " + att_text_split[-13] + "   Протокол № " + att_text_split[-14]
                p_2 = "от " + att_text_split[-12] + " до " + att_text_split[-9] + "   Протокол № " + att_text_split[-10]
                p_3 = "от " + att_text_split[-8] + " до " + att_text_split[-5] + "   Протокол № " + att_text_split[-6]
                p_4 = "от " + att_text_split[-4] + " до " + att_text_split[-1] + "   Протокол № " + att_text_split[-2]
                all_pov = p_1 + '\n' + p_2 + "\n" + p_3 + "\n" + p_4
            elif len(att_text_split) == 20:
                p_1 = "от " + att_text_split[-20] + " до " + att_text_split[-17] + "   Протокол № " + att_text_split[-18]
                p_2 = "от " + att_text_split[-16] + " до " + att_text_split[-13] + "   Протокол № " + att_text_split[-14]
                p_3 = "от " + att_text_split[-12] + " до " + att_text_split[-9] + "   Протокол № " + att_text_split[-10]
                p_4 = "от " + att_text_split[-8] + " до " + att_text_split[-5] + "   Протокол № " + att_text_split[-6]
                p_5 = "от " + att_text_split[-4] + " до " + att_text_split[-1] + "   Протокол № " + att_text_split[-2]
                all_pov = p_1 + '\n' + p_2 + "\n" + p_3 + "\n" + p_4 + "\n" + p_5
            elif len(att_text_split) == 24:
                p_1 = "от " + att_text_split[-24] + " до " + att_text_split[-21] + "   Протокол № " + att_text_split[-22]
                p_2 = "от " + att_text_split[-20] + " до " + att_text_split[-17] + "   Протокол № " + att_text_split[-18]
                p_3 = "от " + att_text_split[-16] + " до " + att_text_split[-13] + "   Протокол № " + att_text_split[-14]
                p_4 = "от " + att_text_split[-12] + " до " + att_text_split[-9] + "   Протокол № " + att_text_split[-10]
                p_5 = "от " + att_text_split[-8] + " до " + att_text_split[-5] + "   Протокол № " + att_text_split[-6]
                p_6 = "от " + att_text_split[-4] + " до " + att_text_split[-1] + "   Протокол № " + att_text_split[-2]
                all_pov = p_1 + '\n' + p_2 + "\n" + p_3 + "\n" + p_4 + "\n" + p_5 + "\n" + p_6

            self.ui_main.plainTextEdit.clear()
            self.ui_main.plainTextEdit.appendPlainText(naim + "\n\nзав. № " + zav_num + "\nинв. № " + inv_num + '\n\nПротокол №\n' + att_2 + '\n\nдо ' + att_1 + '\n\nВсе аттестации:\n' + all_pov)
        else:
            pass

    def info_VO(self):
        if self.ui_main.tableView.selectedIndexes()[0].row() is not None:
            sel_id = self.ui_main.tableView.selectedIndexes()[0].row()
        else:
            sel_id = 0
        if self.a == 3:
            naim = self.model_VO.record(sel_id).value("Наименование")
            inv_num = self.model_VO.record(sel_id).value("Инв\xa0номер")
            zav_num = self.model_VO.record(sel_id).value("Зав\xa0номер")

            self.ui_main.plainTextEdit.clear()
            self.ui_main.plainTextEdit.appendPlainText(naim + "\n\nзав. № " + zav_num + "\nинв. № " + inv_num + '\n\nвспомогательное, не применимо')

        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec())
