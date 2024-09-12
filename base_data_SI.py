from PySide6 import QtWidgets, QtSql


class Data_SI:
    def __init__(self):
        super(Data_SI, self).__init__()
        self.create_connection_SI()

    def create_connection_SI(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('database_SI.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'Cannot open database',
                                           'SI data cannot open', QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec('CREATE TABLE IF NOT EXISTS database_SI (ID integer primary key AUTOINCREMENT, Инв\xa0номер TEXT, '
                   'Наименование TEXT, Модификация TEXT, №\xa0в\xa0реестре TEXT, Зав\xa0номер TEXT, Помещение TEXT, '
                   'В\xa0составе TEXT, ПО TEXT, Изготовлено TEXT, Право\xa0собственности TEXT, '
                   'Дата\xa0ввода TEXT, Диапазоны TEXT, Поверки TEXT, ФГИС TEXT, Темп TEXT, Влажн TEXT, Давл TEXT, '
                   'Напр TEXT, Част TEXT, ТО TEXT, clean TEXT)')
        return db

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

    def si_pov(self, in_what):
        sql_query = ("SELECT Инв\xa0номер, Наименование FROM database_SI WHERE В\xa0составе=?")
        self.execute_query_with_params(sql_query, [in_what])
