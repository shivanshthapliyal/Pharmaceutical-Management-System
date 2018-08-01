import pymysql
import user
# import customer
con = pymysql.connect(user='root', password='', database='pms_try')

class admin(user):
    admin_pass='root'

#     Check inventory for all medicines and their availability.
#     A query will be generated for the admin to see all the medicines,
#     their expiry date, the manufacturers info and all the other info.

    def checkInventory(self):
        cur=con.cursor()
        stmt=""""Select mid,mname,price,qty,manin, exp_date from medicine"""
        cur.execute(stmt)
        res=cur.fetchall()
        print("Inventory Details :-\n")
        print("MedicineID\tName\tPrice\tQuantity\tManufacturerID\tExpiry date")
        for i in res:
            print(i[0]+"/t"+i[1]+"/t"+i[2]+"/t"+i[3]+"/t"+i[4]+"/t"+i[5])


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
    def __init__(self,aid='root'):
        super.__init__(self,aid)
        pass

obj = admin()
obj.checkInventory()
