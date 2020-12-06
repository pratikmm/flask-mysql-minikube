import mysql.connector

mydb = mysql.connector.connect(user='root', password='my-secret-pw',
                              host='127.0.0.1')
mycursor = mydb.cursor()

mycursor.execute("SELECT 'Hello World!';")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
print(type(myresult))
mycursor.close()
mydb.close()

# import mysql.connector

# cnx = mysql.connector.connect(user='root', password='my-secret-pw', host='127.0.0.1')
# cnx.close()