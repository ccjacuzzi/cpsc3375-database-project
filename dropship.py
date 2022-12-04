
#include 
import mysql.connector
import os

#Establish the connection to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="37Pickle$82"
)

#print the connection name to confirm connection
print(mydb)

#Initialize Database
def initializeDB():
    mycursor = mydb.cursor()
    mycursor.execute('USE dropship')

### Function Definitions ####
def displayMainMenu():
    print("----Menu----")
    print(" 1. Register a New User")
    print(" 2. All Items ")
    print(" 3. All Orders")
    print(" 4. All Suppliers")
    print(" 5. All Customers ")
    print(" 0. End")
    print("------------")

def run():
    print("under construction")

def exit():
    n = int(input(" Press 0 to exit : "))
    if n == 0:
       os.system('cls') # For Windows
       run()
    else:
       print("Invalid Option")
       exit()

def newUser():
    mycursor = mydb.cursor()
    print("---User Registration---\n")
    userType = int(input("User type - 1. Customer or 2. Employee?  "))
    if userType == 1:
        newCustomer()
    elif userType == 2:
        newSupplier()
    else:
        print("Invalid Selection")
        exit()

def newCustomer():
    mycursor = mydb.cursor()
    print("-----New Customer-----")
    name = input("Enter name: ")
    email = input("Enter email: ")
    #birthday = input("Enter Birthday: ")
    sql = "INSERT INTO customer (name, email) VALUES (%s, %s)"
    val = (name, email)
    mycursor.execute(sql,val)
    mydb.commit()
    print("-----New Customer Created Successfully-----")
    exit()

def newSupplier():
    print("Under Construction")

def run():
    displayMainMenu()
    n = int(input("Enter option: "))
    if n == 1:
        os.system('cls')
        newUser()
    elif n == 0:
        os.system('cls')
        exit()
    else:
        os.system('cls')
        run()

if __name__ == '__main__':
    initializeDB()
    run()
