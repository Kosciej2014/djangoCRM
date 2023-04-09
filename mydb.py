import mysql.connector

dataBase = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    passwd = 'Djangocrm1234'

)


cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE")

print("Done!")