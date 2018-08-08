import pymysql

class database:
    conn=None
    curs=None
    @staticmethod
    def connection():
        database.conn = pymysql.connect("localhost", "root", "1234", "pharmacy")
        return database.conn
    @staticmethod
    def cursor():
        database.curs=database.conn.cursor()
        return database.curs
    @staticmethod
    def close():
        database.curs.close()
        database.conn.close()

