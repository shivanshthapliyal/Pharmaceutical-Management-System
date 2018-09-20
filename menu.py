import pymysql
import prettytable
import datetime
from database import *
from user import *
from customer import *
from order import *
from admin import *
import re
conn=database.connection()
curs=database.cursor()


#Program Menu
mainlogger=True
while mainlogger ==True:
    r3=False
    print("===== Welcome to GSBT Pharmaceuticals =====")
    print("1.Customer")
    print("2.Admin")
    print("3.Exit.")
    while(r3==False):
        c1 = input("Enter Choice:")
        if not re.match(r"[1-3]",c1):
            print("Enter proper Choice!!!")
        else:
            r3=True
    choice1=int(c1)
    if choice1 == 1:
        r4=False
        print("1.Signup")
        print("2.Signin")
        while(r4==False):
            c2 = input("Enter Choice:")
            if not re.match(r"[1-2]",c2):
                print("Enter proper Choice!!!")
            else:
                r4=True
        choice2=int(c2)
        if choice2 == 1:
            r1=False
            r2=False
            name = input("Enter your Name:")
            password = input("Enter password:")
            while(r1==False):
                phone = input("Enter phone number:")
                if(phone.isnumeric()==True):
                    if(len(phone)==10):
                        r1=True
                    else:
                        print("Enter 10 digit number correctly!!!")  
                else:
                    print("Enter 10 digit number correctly!!!")
            while(r2==False):
                email = input("Enter email address:")
                if not re.match(r"[^@]+@[^@]+\.[^@]+",email):
                    print("Enter Valid Email!!!")
                else:
                    r2=True
            address = input("Enter address:")
            obj = customer()
            obj.fetchDetails(name, password, phone, email, address)
        elif choice2 == 2:
            tf = False
            while tf != True:
                uname = input("Enter Username(Email):")
                password = input("Enter Password:")
                obj = customer()
                tf = obj.signin(uname, password)
                if tf == True:
                    print("Login Successful!")
                    curs.execute(""" SELECT cid,cname, address, phone, email from pharmacy.customer WHERE email=%s""",
                                 (uname,))
                    r = curs.fetchall()
                    cid = r[0][0]
                    print("\nWELCOME " + r[0][1] + "!")
                    curs.execute("SELECT CONNECTION_ID()")
                    rows = curs.fetchall()
                    conid = rows[0][0]
                    tg = False
                    while tg != True:
                        r5=False
                        print("==== Main Menu ====")
                        print("1.View profile details.")
                        print("2.Update profile details.")
                        print("3.Order new items.")
                        print("4.Previous orders.")
                        print("5.Show Offers.")
                        print("6.Log Out.")
                        while(r5==False):
                            c3 = input("Enter choice:")
                            if not re.match(r"[1-6]",c3):
                                print("Enter proper Choice!!!")
                            else:
                                r5=True
                        choice3=int(c3)
                        if choice3 == 1:
                            print("==== Cutomer Details ====")
                            print("Customer Name:", r[0][1])
                            print("Customer ID:", r[0][0])
                            print("Customer address:", r[0][2])
                            print("Customer Email:", r[0][4])
                            print("Customer phone:", r[0][3])
                        elif choice3 == 2:
                            print("==== Update Profile ====")
                            obj.updateProfile(cid)
                            print("\n")
                        elif choice3 == 3:
                            print("==== Place New Order ====")
                            obj.placeOrder(cid,conid)
                            print("\n")
                            conid=conid+1
                        elif choice3 == 4:
                            print("==== Previous Orders ====")
                            obj.previousOrder(cid)
                            print("\n")
                        elif choice3 == 5:
                            print("=== CURRENT OFFERS ===")
                            print("1.5% discount for customers who has done more than 5 orders in the store.")
                            print("1.10% discount for customers who has done more than 10 orders in the store.")
                            print("\n")
                        elif choice3 == 6:
                            tg = True
                else:
                    print("Login Unsuccessful!")

    if choice1 == 2:
        name = input("Enter your Name:")
        password = input("Enter password:")
        if(name=="admin" and password=="pass"):
            tg=False
            while tg != True:
                print("1.Display inventory for all medicines and their availability.")
                print("2.Check all user details.")
                print("3.Check the order queue right now.")
                print("4.Check expiry dates of medicines.")
                print("5.Check medicines sold between a certain timeframe.")
                print("6.Order stock.")
                print("7.Update Order Status")
                print("8.Logout.")
                choice2 = int(input("Enter choice:"))
                obj = admin()
                if choice2 == 1:
                    obj.checkInventory()
                elif choice2 == 2:
                    obj.printUserDetails()
                elif choice2 == 3:
                    obj.printorderqueue()
                elif choice2 == 4:
                    obj.checkexpirydates()
                elif choice2 == 5:
                    obj.checkmedicinessold()
                elif choice2 == 6:
                    obj.stockOrder()
                elif choice2 == 7:
                    order().setStatus()
                elif choice2 == 8:
                    tg=True
                else:
                    print("Wrong Input Choice. Try entering from the given choices.")
        else:
            print("Wrong Password/Username Combination")
    if choice1 == 3:
        mainlogger=False

database.close()
