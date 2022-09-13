import mysql.connector
from mysql.connector import Error #To ignore all the errors

#creating connection to the database:
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12340",
    database="batch57_db"
)
mycursor = mydb.cursor()
#Command for creating table
#mycursor.execute("CREATE TABLE data(my_name VARCHAR(255), pass_word int, de_po int, i_d int)")
#mydb.commit()

print("Welcome to atm")
n=int(input("Press 1 for login and 0 for register"))

#Declaring variables globally
password=""
myname=""
depo=""
id=""

if n==0:
    name=input("Enter name: ")
    accn=int(input("Enter account no: "))
    t=int(input("Enter Deposit Amount"))
    pw=int(input("Set Your Password:"))

    #Four parameters will be stored in four variables.
    myname=name
    password=pw
    deposit=t
    id=accn

    val=(myname,password,depo,id)

    #sql query is executed.
    sql= """insert into data(my_name, pass_word, de_po, i_d) 
           values(%s,%s,%s,%s) """

    mycursor.execute(sql,val)

    #Apply changes that we created in sql program.
    mydb.commit()
    #display success if there is no error
    print("success")

if n==1:
    info= int(input("Enter ur id: "))
    passw=int(input("Enter the password: "))

    #info is the id  given by the user
    mycursor.execute("select * from atm.data where i_d=%s" %(info))

    #fetchone() is used to fetch the row 
    row=mycursor.fetchone()

    if mycursor.rowcount==1:

        #verifying the password given by the user
        mycursor.execute("select * from atm.data where pass_word= %s"%(passw))
        row=mycursor.fetchone()

        if mycursor.rowcount==1:
            print("login successful")
            d=int(input("Enter 1 for withdrawl or 0 for deposit and 3 for exit: "))

            if d==1:
                a= int(input("How much you want to withdrawl?: "))

                #passw is the password given by the user previously
                mycursor.execute("select de_po from atm.data where pass_word=%s"%(passw))
                col=mycursor.fetchone()
                x=list(col)

                for i in x:

                    #z is current amout
                    z=(int(i))

                    #a is the withdrawal amount
                    #all the updates are stored in c
                    c=z+a

                #Update the current amount after transaction.    
                mycursor.execute("update data set de_po=%s"%(c,passw))

            if d==3:
                #Exit the program
                exit(0)

        else:
            print("invalid password")

    else:
        print("Account does't exist") 

    mydb.commit()   
    
 

 
