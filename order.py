import pymysql
from prettytable import PrettyTable
import datetime
from database import *
from customer import *
conn=database.connection()
curs=database.cursor()


class order:
    def __init__(self):
        self.status="pending"
        self.curdate=None


    def dispOrderDetails(self,conid):
        curs.execute("SELECT oid,cid,mid,qty from orders where oid=%s",(conid))
        rows=curs.fetchall()
        print("Your Order Details are!!")
        print("Order-ID   :",rows[0][0])
        print("Customer-ID:",rows[0][1])
        print("Medicine-ID  Quantity")
        for row in rows:
            print(row[2],"        ",row[3])


    def addItems(self,cid,conid):
        self.setOrderDate()
        total_cost=0
        wm = True
        while wm != False:
            medId = int(input("Enter MedicineID of medicine you want to purchase:"))
            quan = int(input("Enter Quantity:"))
            curs.execute("SELECT qty from medicine where mid=%s", medId)
            q = curs.fetchall()
            qold = q[0][0]
            qnew = qold - quan
            curs.execute("UPDATE medicine SET qty=%s WHERE mid=%s", (qnew, medId))
            curs.execute("select price from medicine where mid=%s", medId)
            price = curs.fetchall()
            total_cost = total_cost + quan * price[0][0]
            curs.execute("Insert into orders values(%s,%s,%s,%s,%s,%s)",(conid, cid, medId,self.status,self.curdate,quan))
            conn.commit()
            wmc = input("Want more medicine(Y/N):")
            if wmc == 'Y' or wmc == 'y':
                wm = True
            else:
                wm = False
        return total_cost

    def setOrderDate(self):
        self.curdate=datetime.datetime.now()

    def setStatus(self):
        pass
