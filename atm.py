import mysql.connector
from mysql.connector import Error

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12340",
    database="batch54_db"
)
mycursor = mydb.cursor()
#Command for creating table
#mycursor.execute("CREATE TABLE data(my_name VARCHAR(255), pass_word int, de_po int, i_d int)")
#mydb.commit()

print("Welcome to atm")
n=int(input("Press 1 for login and 0 for register"))

password=""
myname=""
depo=""
id=""

if n==0:
    name=input("Enter name: ")
    accn=int(input("Enter account no: "))
    t=int(input("Enter Deposit Amount"))
    pw=int(input("Set Your Password:"))

    myname=name
    password=pw
    deposit=t
    id=accn

    val=(myname,password,depo,id)

    sql= "insert into data(my_name, pass_word, de_po, i_d) values(%s,%s,%s,%s) "

   
    mycursor.execute(sql,val)
    mydb.commit()
    print("success")
    
 
