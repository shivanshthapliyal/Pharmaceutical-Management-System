import pymysql
from prettytable import PrettyTable
import datetime
from database import *
conn=database.connection()
curs=database.cursor()

class user:   #completed
    def __init__(self):
        uid=None

    def signup(self,cust_details): #DONE
        curs.execute("""INSERT INTO customer (cname,phone,email,address,password) VALUES(%s,%s,%s,%s,%s)""",(cust_details['Name'], cust_details['Phone'], cust_details['Email'], cust_details['Address'], cust_details['Password']))
        conn.commit()
        print("Signup Successful!")

    def signin(self,uname,password): #DONE
        try:
            curs.execute("""SELECT password from pharmacy.customer WHERE email=%s""", (uname))
            passw=curs.fetchall()
            if password==passw[0][0]:
                return True
            else:
                return False
        except Exception as e:
            print("Wrong Details!")
            return False
