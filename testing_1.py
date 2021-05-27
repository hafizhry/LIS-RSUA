import mysql.connector

try:
  cnx = mysql.connector.connect(user='root', database='laravel_crud2')
  cursor = cnx.cursor()
  cursor.execute("SELECT * FORM employees")   # Syntax error in query
  cnx.close()
except mysql.connector.Error as err:
  print("Something went wrong: {}".format(err))