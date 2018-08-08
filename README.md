# Pharmaceutical-Management-System
The purpose of the system is to ease the process of ordering/purchasing medicines online as well as directly. The system manages the customers and their orders as well as all the details of medicines (Manufacturer info, Expiry Date, etc.). The system is being developed in python and is based on relational database MySQL. The system will be made available across all the branches of the store along with the users.


##1.1) PURPOSE:
The purpose of this document is to build a system for managing the pharmaceutical stores and also an interface for the customers so that they can order the medicines online from their homes with ease.


1.2) DOCUMENT CONVENTIONS:
The conventions being used by this document are given below:


 MySQL: MySQL database is being used to store information about the customers and the products and different kind of information.
MySQL workbench is used to connect with the database.


1.3) INTENDED AUDIENCE AND READING SUGGESTIONS:
The system is being made for both the customers and the admins. The software will be made available to the customers for ordering medicines, managing their profiles and prescriptions, etc.
The admins will be able to keep track of the sales and the stock of the medicines.


1.4) PROJECT SCOPE:
The purpose of the system is to ease the process of ordering/purchasing medicines online as well as directly.
The system manages the customers and their orders as well as all the details of medicines (Manufacturer info, Expiry Date,etc.). The system is being
developed in python and is based on relational database MySQL.
The system will be made available across all the branches of the store along with the users.


2.Overall Description:

2.1) PRODUCT PERSPECTIVE:

The pharmacy management system will store information about the following:

 Customer Details:
The profiles of the existing customers are being stored along with their contact details and address.
Prescriptions of the customers are also being stored if the customer wants to.

 Order Details:
The system keeps track of all the previous orders of the customer in order to provide discounts to the filtered customers according to store rules.

 Manufacturer and Product Details:
The system also contains information about the products along with their manufacturers so that they can be contacted when the medicines go out of stock.
The database also keeps track of the present stock of the medicines.


2.2) PRODUCT FEATURES:
The Entity-Relationship Model given below gives a clear description of the major features of the pharmaceutical management system database:


2.3) PRODUCT FUNCTIONALITIES:
The product at first gives the option to choose whether the user is a customer or an admin or if the user wants to sign up as a new user. After the logging up process, the product functionalities are divided into two parts based on the type of the user:

2.3.1) CUSTOMER:
 Order Medicines:
Customer can buy new medicines on this page by choosing them from the list. They can also modify the amount of particular medicine to order.

 See Previous Orders:
Here the customer can see his previous orders which they have done for fast access and reminders. (If any)

 Change Profile Details:
Here the Customer can maintain his profile details. He can change his saved addresses and maintain his prescriptions (optional).

 Get monthly/weekly discounts on medicines:
This is an automated functionality that will ensure that customers who have ordered above a certain amount in a certain time frame gets a legit discount.


2.3.2) ADMIN:
 Check inventory for all medicines and their availability.
A query will be generated for the admin to see all the medicines, their expiry date, the manufacturer’s info and all the other info.

 Check all user details.
The admin will be able to see all the users who have ordered/ placed an order/ or purchased anything from the shop.

 Check the order queue right now
The admin will be able to see the order queue at present and all the details pertaining to the same.

 Check expiry date of medicines
A query will be generated for the admin to see the expiry date of all thevmedicines.
This is an important step in any pharmacy as expired medicines are not sold.

 Manufacturer’s Info i.e. orders for new stock
The admin can easily organize from where the stock is coming and who is the manufacturer and the supplier.

 Check medicines sold between a certain timeframe
The admin can supervise the medicines sold within a certain timeframe.

 Check users with monthly/weekly discounts and offers.
A query will be generated for the admin to see all users who have special monthly discounts availed.
