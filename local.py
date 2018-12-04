import cx_Oracle

class OracleDatabase:
    ''' Classe responsável por fornecer a conexão com o banco Oracle '''

    def __init__(self, connectionString : str, user : str, password : str):
        ''' Construtor da classe '''
        self.__ORACLE_SESSION__ = cx_Oracle.SessionPool(
            user,
            password,
            connectionString,
            2,
            5,
            1,
            threaded = True)

    def get_cursor(self, query, parameters):
        """ Executar a query e retornar o cursor """
        connection = self.__ORACLE_SESSION__.acquire()
        cursor = connection.cursor()
        return cursor.execute(query, parameters)
