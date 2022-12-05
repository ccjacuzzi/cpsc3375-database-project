
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
    print("-------Blog Database----\n")
    print("----User Menu-----------")
    print(" 1. Sign Up")
    print(" 2. Sign In")
    print(" 3. Create Blog Post")
    print(" 4. Delete Blog Post")
    print(" 5. View All Blog Posts")
    print(" 0. Exit")
    print("------------------------\n")


def exit():
    n = int(input(" Are you sure you want to exit? 0=yes 1=no: "))
    if n == 0:
       #os.system('cls') # For Windows
       global mainProgram
       mainProgram = 1
    elif n == 1:
        os.system('cls')
        run()
    else:
       print("Invalid Option")
       exit()

def signUp():
    global activeUserID
    if activeUserID == 0:    
        mycursor = mydb.cursor()
        print("---Sign Up for the Blog-------\n")
        name = input("Please enter your name (First Last): ")
        email = input("Please enter your email address: ")
        phone = input("Please enter your phone number: ")
        password = input("Please create a password: ")
        sql = "INSERT INTO blog_user (name, email, phone, password) values (%s, %s, %s,%s)"
        val = (name, email, phone, password)
        mycursor.execute(sql,val)
        mydb.commit()
        sql2 = "SELECT user_id FROM blog_user WHERE email = %s AND password = %s"
        val = (email, password)
        mycursor.execute(sql2, val)
        myresult = mycursor.fetchall()        
        activeUserID = myresult[0][0]
        print("\n----Welcome New User---------")
    else:
        print("You already have an account and are logged in.")
        
   

def signIn():
    global activeUserID
    if activeUserID == 0:   
        mycursor = mydb.cursor()
        print("---Sign In to your Account---\n")
        email = input("Email: ")
        password = input("Password: ")
        sql = "SELECT user_ID FROM blog_user WHERE email = %s AND password = %s"
        val = (email, password)
        mycursor.execute(sql,val)
        #To get just the user_ID value into my activeUserID variable
        #Use .fetchall()
        #This returns a list of tuples. This search should only return one result
        #and user id is the first element in that result. That's why we use [0][0]
        myresult = mycursor.fetchall()    
        activeUserID = myresult[0][0]
        print("\n------Welcome!---------------\n")
    else:
        print("You are already logged in.")
    
    
def newBlogPost():
    mycursor = mydb.cursor()
    user_id = activeUserID
    if activeUserID == 0:
        print("\nYou must sign in first.\n")
        signIn()
    elif activeUserID > 0:
        print("-----Create New Blog Post-------------------\n")
        title = input("\nEnter the title of your post: ")
        content = input("\nEnter your blog post content: ")
        sql = "INSERT INTO blog_post (title, content, user_id) VALUES (%s, %s, %s)"
        val = (title, content, user_id)
        mycursor.execute(sql,val)
        mydb.commit()
        print("-----New Blog Post Created Successfully-----\n")

def deletePost():
    mycursor = mydb.cursor()
    user_id = activeUserID
    if activeUserID == 0:
        print("\nYou must sign in first.\n")
        signIn()
        deletePost()
    elif activeUserID > 0:
       print("-----Delete A Post (ID, Titlt, Content)-----\n") 
       sql = "SELECT post_id, title, content FROM blog_post WHERE user_id = %s"
       mycursor.execute(sql,(activeUserID,))
       results = mycursor.fetchall()
       #Formatting could use work
       for x in results:
            print(x)
       
       print("\n-----------------------------------------\n")
       selection = input("Enter the ID of the post you would like to delete: ")
       sql = "DELETE FROM blog_post WHERE post_id = %s"
       mycursor.execute(sql,(selection,))
       print("\nThis post has been deleted.") 

def viewAllPosts():
    mycursor = mydb.cursor()
    
    user_id = activeUserID
    if activeUserID == 0:
        print("\nYou must sign in first.\n")
        signIn()
        viewAllPosts()
    elif activeUserID > 0:
        print("\n-------Your Blog Posts (Title, Content)-----\n")
        sql = "SELECT title, content FROM blog_post WHERE user_id = %s"
        mycursor.execute(sql,(activeUserID,))
        results = mycursor.fetchall()
        #Formatting could use work
        for x in results:
            print(x)
        print("\n--------------------------------------------\n")


def run():
    displayMainMenu()
    n = int(input("Enter option: "))
    if n == 1:
        os.system('cls')
        signUp()
    elif n == 2:
        os.system('cls')
        signIn()
    elif n == 3:
        os.system('cls')
        newBlogPost()
    elif n ==4:
        os.system('cls')
        deletePost()
    elif n == 5:
        os.system('cls')
        viewAllPosts()
    elif n == 0:
        os.system('cls')
        exit()
    else:
        os.system('cls')
        run()

###_____Global Variables_____###########################################################
activeUserID = 0
mainProgram = 0

###_______Main Program Function______####################################################
def main():
    initializeDB()
    os.system('cls')

    while mainProgram == 0:
        run()
        

    print("\nGoodbye!\n")

if __name__ == '__main__':
    main()
