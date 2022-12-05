
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
    print(" 3. Create Blog Post")
    print(" 4. Delete Blog Post")
    print(" 5. View All Blog Posts")
    print(" 6. Search Blog Posts")
    print(" 7. View All Users")
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

def signUp():
    mycursor = mydb.cursor()
    print("---Sign Up for the Blog---\n")
    name = input("Please enter your name (First Last): ")
    email = input("Please enter your email address: ")
    phone = input("Please enter your phone number: ")
    password = input("Please create a password: ")
    sql = "INSERT INTO blog_user (name, email, phone, password) values (%s, %s, %s,%s)"
    val = (name, email, phone, password)
    mycursor.execute(sql,val)
    mydb.commit()
    print("----Welcome New User----")
    exit()

def signIn():
    mycursor = mydb.cursor()
    print("---Sign In to your Account---")
    email = input("Email: ")
    password = input("Password: ")
    sql = "SELECT user_ID FROM blog_user WHERE email = %s AND password = %s"
    val = (email, password)
    mycursor.execute(sql,val)
    #How to get just the user_ID value into my activeUserID variable?
    myresult = mycursor.fetchall()
    
    print("UserID: ", activeUserID)
    print("---Sign In Successful!---")
    


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
        signUp()
    elif n == 2:
        os.system('cls')
        signIn()
    elif n == 0:
        os.system('cls')
        exit()
    else:
        os.system('cls')
        run()

###_____Global Variables_____###########################################################
activeUserID = 0

###_______Main Program Function______####################################################
def main():
    initializeDB()
    run()

if __name__ == '__main__':
    main()
