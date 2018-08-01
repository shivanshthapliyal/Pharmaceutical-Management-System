import user

class customer(user):
    def __init__(self):
        self.cust_details={}


    def placeOrder(self):
        pass

    def previousOrder(self):
        pass

    def updateProfile(self): #DONE
        name = input("Enter your Name:")
        password = input("Enter password:")
        phone = input("Enter phone number:")
        email = input("Enter email address:")
        address = input("Enter address:")
        #SQL QUERY TO UPDATE RECORD IN DATABASE
        pass

    def getDiscount(self):
        pass

    def fetchDetails(self,name,password,phone,email,address):
        self.cust_details['Name'] = name
        self.cust_details['Password'] = password
        self.cust_details['Phone'] = phone
        self.cust_details['Email'] = email
        self.cust_details['Address'] = address
        print(self.cust_details)
        super().signup(self.cust_details)