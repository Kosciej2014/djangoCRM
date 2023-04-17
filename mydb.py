import mysql.connector

dataBase = mysql.connector.connect(
    host= '',
    user = '',
    passwd = ''

)


cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE")

print("Done!")
