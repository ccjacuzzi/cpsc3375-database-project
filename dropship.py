
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
    mycursor.execute('USE blog')

### Function Definitions ####
def displayMainMenu():
    print("----Menu----")
    print(" 1. Sign Up")
    print(" 2. Sign In")
    print(" 3. New Blog Post")
    print(" 4. View All Blog Posts")
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

def newBlogPost():
    mycursor = mydb.cursor()
    print("-----Create New Blog Post-----")
    title = input("Enter the title of your post: ")
    content = input("Enter your blog post content: ")
    user_id = input("Enter your user ID: ")
    sql = "INSERT INTO blog_post (title, content) VALUES (%s, %s, %s)"
    val = (title, content, user_id)
    mycursor.execute(sql,val)
    mydb.commit()
    print("-----New Blog Post Created Successfully-----")
    exit()

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
