'''
Created on 07-Aug-2018

@author: Shivansh Thapliyal
'''

import pymysql

class database:
    conn=None
    curs=None
    @staticmethod
    def connection():
        database.conn = pymysql.connect(user='root', password='1234', database='pharmacy')
        return database.conn
    @staticmethod
    def cursor():
        database.curs=database.conn.cursor()
        return database.curs
    @staticmethod
    def close():
        database.curs.close()
        database.conn.close()
