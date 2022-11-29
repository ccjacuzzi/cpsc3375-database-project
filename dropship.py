#This is the python script for my database project

#include the mysql connector library????
import mysql.connector

#Establish the connection using the connect() constructor
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="37Pickle$82"
)

#print the connection name like this <mysql.connector.connection...>
#This is just to confirm we have a connection
print(mydb)

#Create a cursor object using the cursor() method of the connect class???
mycursor = mydb.cursor()

#execute() method of the connect class. These execute mysql commands
#mycursor.execute("CREATE DATABASE mydatabase")  #comment this line out after table is created

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

