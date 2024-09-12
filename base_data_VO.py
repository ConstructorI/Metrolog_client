from PySide6 import QtWidgets, QtSql

class Data_VO:
    def __init__(self):
        super(Data_VO, self).__init__()
        self.create_connection_VO()

    def create_connection_VO(self):
        db3 = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db3.setDatabaseName('database_SI.db')

        if not db3.open():
            QtWidgets.QMessageBox.critical(None, 'Cannot open database',
                                           'VO data cannot open', QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec('CREATE TABLE IF NOT EXISTS database_VO (ID integer primary key AUTOINCREMENT, Инв\xa0номер TEXT, '
                   'Наименование TEXT, Зав\xa0номер TEXT, Помещение TEXT, Изготовитель TEXT, '
                   'Право\xa0собственности TEXT, Дата\xa0ввода TEXT, Предназначение TEXT, ПО TEXT, Темп TEXT, '
                   'Влажн TEXT, Давл TEXT, Напр TEXT, Част TEXT, ТО TEXT, clean TEXT)')

        return db3

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

