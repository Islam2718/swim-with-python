import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="krishikhamar"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM categories")

myresult = mycursor.fetchall()
for x in myresult:
    print(x)
