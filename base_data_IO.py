from PySide6 import QtWidgets, QtSql


class Data_IO:
    def __init__(self):
        super(Data_IO, self).__init__()

        self.create_connection_IO()

    def create_connection_IO(self):
        db2 = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db2.setDatabaseName('database_SI.db')

        if not db2.open():
            QtWidgets.QMessageBox.critical(None, 'Cannot open database',
                                           'IO data cannot open', QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec('CREATE TABLE IF NOT EXISTS database_IO (ID integer primary key AUTOINCREMENT, Инв\xa0номер TEXT, '
                   'Наименование TEXT, Краткое\xa0наименование TEXT, Зав\xa0номер TEXT, Помещение TEXT, '
                   'Изготовитель TEXT, Право\xa0собственности TEXT, Дата\xa0ввода TEXT, Паспорт TEXT, Аттестация TEXT, '
                   'Объекты\xa0испытаний TEXT, Виды\xa0испытаний TEXT, Характеристики TEXT, Темп TEXT, Влажн TEXT, '
                   'Давл TEXT, Напр TEXT, Част TEXT, ТО TEXT, clean TEXT)')

        return db2

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)
        else:
            QtWidgets.QMessageBox.critical(None, 'Ой', 'Введите все значения', QtWidgets.QMessageBox.Cancel)

        query.exec()
        return query

    def v_sostave(self, in_what):
        sql_query = ("SELECT Инв\xa0номер, Наименование FROM database_SI WHERE В\xa0составе=?")
        self.execute_query_with_params(sql_query, [in_what])
