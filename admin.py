'''
Created on 08-Aug-2018

@author: Shivansh Thapliyal
'''
import pymysql
import user

import datetime
from user import *
from order import *
from customer import *
from medicine import Medicine
import random
from prettytable import PrettyTable, MSWORD_FRIENDLY

from database import *
con=database.connection()



class admin():
    admin_pass='root'

#     Check inventory for all medicines and their availability.
#     A query will be generated for the admin to see all the medicines,
#     their expiry date, the manufacturers info and all the other info.

    def checkInventory(self):
        cur=con.cursor()
        stmt="""SELECT * FROM pharmacy.medicine"""
        cur.execute(stmt)
        res=cur.fetchall()
        print("Inventory Details :-\n")
        x = PrettyTable(["MedicineID","Name","Price","Quantity","ManufacturerID","Expiry date"])
        x.align["Name"]="l"
        x.align["MedicineID"]="r"
        x.align["Price"]="r"
        for i in res:
            x.add_row(i)
        print(x)



# Check all user details.
# The admin will be able to see all the users who have ordered/ placed an order/ or purchased anything from the shop.

    def printUserDetails(self):
        cur=con.cursor()
        stmt="""SELECT * FROM pharmacy.customer"""
        cur.execute(stmt)
        res=cur.fetchall()
        print("Inventory Details :-\n")
        x = PrettyTable(["Customer ID","Customer Name","Phone","EMail","Address","Password"])
        x.align["Customer Name"]="l"
        for i in res:
            x.add_row(i)
        print(x)



#  Check the order queue right now.
#  The admin will be able to see the order queue at present and all the details pertaining to the same.

    def printorderqueue(self):
        cur=con.cursor()
        stmt="""SELECT * FROM pharmacy.orders"""
        cur.execute(stmt)
        res=cur.fetchall()
        if(cur.rowcount == 0 ):
            print("Nothing in the order queue.")
        else:
            print("Order Queue :-\n")
            x = PrettyTable(["Order ID","Customer ID","Medicine ID","Status","Date of Order","Quantity"])
            for i in res:
                x.add_row(i)
            print(x)

# Check expiry date of medicines.
# A query will be generated for the admin to see the expiry date of all the medicines.
# This is an important step in any pharmacy as expired medicines are not sold.
    def checkexpirydates(self):
        cur=con.cursor()
        stmt="""SELECT * FROM pharmacy.medicine where exp_date <= CAST(CURRENT_TIMESTAMP AS DATE)"""
        cur.execute(stmt)
        res=cur.fetchall()

        print("Medicines already expired :-\n")
        x = PrettyTable(["MedicineID","Name","Price","Quantity","ManufacturerID","Expiry date"])
        for i in res:
            x.add_row(i)
        print(x)


#     def  pending_orders(self):
#         cur=con.cursor()
#         stmt=""""Select oid,cid,dateoforder from orders where status='pending' group by oid"""
#         cur.execute(stmt)
#         res=cur.fetchall()
#         print("Details of pending orders:-")
#         print("Order id/tCustomer id/tDate Of Order")
#         for i in res:
#             print(i[0]+"/t"+i[1]+"/t"+i[2])


# Manufacturers Info i.e. orders for new stock.
# The admin can easily organize from where the stock is coming and who is the manufacturer and the supplier.


# Check medicines sold between a certain timeframe.
# The admin can supervise the medicines sold within a certain timeframe.
    def checkmedicinessold(self):
        t1=input("Enter the starting date.")
        t2=input("Enter the ending date.")
        cur=con.cursor()
        stmt="""SELECT  * FROM    pharmacy.orders WHERE   dateoforder >= %s AND dateoforder   <= %s"""
        data=[t1,t2]
        cur.execute(stmt,data)
        res=cur.fetchall()

        print("Medicines sold between",t1," and ",t2," :-\n")

        x = PrettyTable(["OrderID","CustomerID","MedicineID","Status","DateOfOrder","Quantity"])
        for i in res:
            x.add_row(i)
        print(x)


    def updateInventory(self,item):
        print("Stock order is placed successfully for your store!")
        print("Billing will be done at your store.")
        print("\n\n")
        print("Updating your inventory>>>")
        for i in item:
            med_obj=Medicine(i[1])
            med_obj.updateQty(int(i[2]))
            date=i[3].split('-')
            y=int(date[0])
            m=int(date[1])
            d=int(date[2])
            med_obj.updateExp(datetime.date(y,m,d))
        print("Inventory successfully updated")




    def stockOrder(self):
        cur=con.cursor()
        print("STOCK\tORDER")
        print("------------")
        stmt="Select * from manufacturer"
        cur.execute(stmt)
        result=cur.fetchall()
        stmt="Select mid,mname from medicine"
        cur.execute(stmt)
        result1=cur.fetchall()
        today=datetime.datetime.today()
        j=[]
        result2=[]
        for i in  result1:
            j=list(i)
            year = random.randint(int(today.year)+1, int(today.year)+2)
            month = random.randint(today.month, 12)
            day = random.randint(today.day, 28)
    #         j.append(datetime.date(year, month, day))
            j.append(str(year)+'-'+str(month)+'-'+str(day))
            j.append(random.randint(13,529))
            result2.append(j)

        print("Here by manufacturer we mean to say distributor ! \n")

        k=PrettyTable(["Med_id","Med_name","exp_date","qty_avail"])
        x = PrettyTable(["ManufacturerID","ManufacturerName"]) #just to test
        x.set_style(MSWORD_FRIENDLY)
        x.align["ManufacturerID"]="r"
        x.align["ManufacturerName"]="l"

        stock=[]
        for i in result:
            x.add_row(i)
            print("The Stock of Manufacturer : ")
            print(x)
            for j in random.sample(range(0, len(result1)-1), random.randint(1,len(result1)%len(result)+1)):
                k.add_row(result2[j])
                stock.append([i[0],i[1],result2[j]])
                print(k)
            k.clear_rows()
            x.clear_rows()
            print("\n\n")

        more='y'
        item=[]
        while more=='y':
            manfid=int(input("Enter manufacturer(distributor) id to buy from"))
            medid=int(input("Enter medicine id to buy"))
            qty=int(input("Enter the quantity to be purchased(Take care of available quantity)"))
            qty=int(qty)

            for i in stock:
                if(i[0]==manfid or i[2][0]==medid):
                    expirydate=i[2][2]
                    item.append([manfid,medid,qty,expirydate])
                    break
            print("Current checkout items :")
    #     printing items
            itemtable = PrettyTable(["Manufacturer ID","Medicine ID","Quantity","Expiry Date"])
            for ii in item:
                itemtable.add_row(ii)
            print(itemtable)

            more=input("Want to buy more items?(y for yes and n for no)")

        ob = admin()
        ob.updateInventory(item)

ob = admin()
ob.checkexpirydates()
