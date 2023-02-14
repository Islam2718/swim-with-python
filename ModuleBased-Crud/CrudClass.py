class CrudClass:

    def __init__(self):
        print("---------------------------------------")

    def saveData(self, company, model, price):
        try:
            import mysql.connector
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="db_python"
            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO mobile (company, model, price) VALUES (%s, %s, %s)"
            val = (company, model, price)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")

        except:
            print("Error.")

        finally:
            print("---------------------------------------")
            print("Insert New: ")
            print("---------------------------------------")
            self.inputValue()

    def inputValue(self):
        company = input("Company Name: ")
        model = input("Model : ")
        price = input("Price : ")
        self.saveData(company, model, price)
