import pymysql
# import user
# import customer
from prettytable import PrettyTable
con = pymysql.connect(user='root', password='', database='pms_try')

class admin():
    admin_pass='root'

#     Check inventory for all medicines and their availability.
#     A query will be generated for the admin to see all the medicines,
#     their expiry date, the manufacturers info and all the other info.

    def checkInventory():
        cur=con.cursor()
        stmt="""SELECT * FROM pms_try.medicine"""
        cur.execute(stmt)
        res=cur.fetchall()
        print("Inventory Details :-\n")
        x = PrettyTable(["MedicineID","Name","Price","Quantity","ManufacturerID","Expiry date"])
        for i in res:
            x.add_row(i)
        print(x)

    def custDetail(self,cust):
        pass

    def  pending_orders(self):
        cur=con.cursor()
        stmt=""""Select oid,cid,dateoforder from orders where status='pending' group by oid"""
        cur.execute(stmt)
        res=cur.fetchall()
        print("Details of pending orders:-")
        print("Order id/tCustomer id/tDate Of Order")
        for i in res:
            print(i[0]+"/t"+i[1]+"/t"+i[2])

    def updateOrderStatus(self,order):
        pass
    def stockOrder(self,manf,med,qty):
        pass
    def UpdateInventoy(self,med):
        pass
#     def __init__(self,aid='root'):
#         super.__init__(self,aid)
#         pass
    def __init__(self):

        pass

admin.checkInventory()
