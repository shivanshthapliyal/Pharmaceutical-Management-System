import pymysql
from prettytable import PrettyTable
import datetime
from database import *
from user import *
from order import *
conn=database.connection()
curs=database.cursor()

class customer(user): #completed
    def __init__(self):
        self.cust_details={}
        self.orderobj = order()

    def placeOrder(self,cid,conid):
        curs.execute("SELECT mid,mname,qty,price FROM pharmacy.medicine")
        rows=curs.fetchall()
        x = PrettyTable(["MedicineID", "Name", "Quantity", "Price"])
        for row in rows:
            x.add_row(row)
        print(x)
        total_cost=self.orderobj.addItems(cid,conid)
        print("-------------------------------------------------")
        self.orderobj.dispOrderDetails(conid)
        discount=self.getDiscount(cid)
        final_amount=total_cost-(discount/100)*total_cost
        print("Total Cost  :",total_cost)
        print("Discount    :",discount,"%")
        print("Final Amount:",final_amount)
        print("-------------------------------------------------")



    def previousOrder(self,cid):
        curs.execute("SELECT * from pharmacy.orders WHERE cid=%s ORDER BY oid", cid)
        rows = curs.fetchall()
        x = PrettyTable(["OrderID", "CustomerID", "MedicineID", "Status", "Date", "Quantity"])
        for row in rows:
            x.add_row(row)
        print(x)


    def updateProfile(self, cid):  # DONE    #added uname for condition
        name = input("Enter your Name:")
        password = input("Enter password:")
        phone = input("Enter phone number:")
        email = input("Enter email address:")
        address = input("Enter address:")
        curs.execute(""" UPDATE pharmacy.customer set cname=%s, password=%s, phone=%s, email=%s, address=%s WHERE cid=%s""",
        (name, password, phone, email, address, cid))
        print(curs.rowcount,"record updated successfully!")
        conn.commit()

    def getDiscount(self,cid):
        curs.execute(""" SELECT COUNT(*) from (SELECT cid,oid, count(*) AS count FROM pharmacy.orders GROUP BY oid, cid) as t WHERE cid=%s""",
            cid)
        d = curs.fetchall()
        if (d[0][0] >= 5 and d[0][0] <10):
            return 5
        elif (d[0][0] >= 10):
            return 10
        else:
            return 0

    def fetchDetails(self,name,password,phone,email,address): # DONE
        self.cust_details['Name'] = name
        self.cust_details['Password'] = password
        self.cust_details['Phone'] = phone
        self.cust_details['Email'] = email
        self.cust_details['Address'] = address
        super().signup(self.cust_details)
