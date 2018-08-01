<<<<<<< HEAD


# run dbqueries.py file first which will contain the databse creation queries.
x
=======
# class ClassName(object):
#     """docstring for ."""
#     def __init__(self, arg):
#         super(, self).__init__()
#         self.arg = arg

import pymysql
import user
import customer
con = pymysql.connect("localhost","testuser","test123","TESTDB" )

class admin(user):
    admin_pass='root'
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
>>>>>>> 1b3514e1f5e9605c2b6e0f38d5ff7183c74385ff
