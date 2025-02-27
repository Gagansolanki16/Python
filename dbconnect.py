import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    
)

my=mydb.cursor()
my.execute("CREATE DATABASE temp")
print(mydb)