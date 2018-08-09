import pymysql
import prettytable
import datetime
from database import *
from user import *
from customer import *
from order import *
from admin import *
conn=database.connection()
curs=database.cursor()


#Program Menu
mainlogger=True
while mainlogger ==True:
    print("1.Press 1 for Customer")
    print("2.Press 2 for Admin")
    print("3.Press 3 to Exit.")
    choice1 = int(input("Enter Choice:"))
    if choice1 == 1:
        print("1.Press 1 for Signup")
        print("2.Press 2 for signin")
        choice2 = int(input("Enter choice:"))
        if choice2 == 1:
            name = input("Enter your Name:")
            password = input("Enter password:")
            phone = input("Enter phone number:")
            email = input("Enter email address:")
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
                    print("WELCOME " + r[0][1] + "!")
                    curs.execute("SELECT CONNECTION_ID()")
                    rows = curs.fetchall()
                    conid = rows[0][0]
                    tg = False
                    while tg != True:
                        print("1.Press 1 to view profile details.")
                        print("2.Press 2 to update profile details.")
                        print("3.Press 3 to order new items.")
                        print("4.Press 4 to see previous orders.")
                        print("5.Press 5 to log Out.")
                        choice3 = int(input("Enter choice:"))
                        if choice3 == 1:
                            print("Customer Name:", r[0][1])
                            print("Customer ID:", r[0][0])
                            print("Customer address:", r[0][2])
                            print("Customer Email:", r[0][4])
                            print("Customer phone:", r[0][3])
                        elif choice3 == 2:
                            obj.updateProfile(cid)
                        elif choice3 == 3:
                            obj.placeOrder(cid,conid)
                            conid=conid+1
                        elif choice3 == 4:
                            obj.previousOrder(cid)
                        elif choice3 == 5:
                            tg = True
                else:
                    print("Login Unsuccessful!")

    if choice1 == 2:
        name = input("Enter your Name:")
        password = input("Enter password:")
        if(name=="admin" and password=="pass"):
            tg=False
            while tg != True:
                print("1.Press 1 for displaying inventory for all medicines and their availability.")
                print("2.Press 2 to check all user details.")
                print("3.Press 3 to check the order queue right now.")
                print("4.Press 4 to check expiry dates of medicines.")
                print("5.Press 5 to check medicines sold between a certain timeframe.")
                print("6.Press 6 to order stock.")
                print("7.Press 7 to logout.")
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
                    tg=True
                else:
                    print("Wrong Input Choice. Try entering from the given choices.")
        else:
            print("Wrong Password/Username Combination")
    if choice1 == 3:
        mainlogger=False

database.close()
