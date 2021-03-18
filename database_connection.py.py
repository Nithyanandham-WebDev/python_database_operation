import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="machine",
  passwd="root",
  auth_plugin='mysql_native_password'
)
print(db_connection)



# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor()
# executing cursor with execute method and pass SQL query
# db_cursor.execute("CREATE DATABASE my_first_db")
# get list of all databases
db_cursor.execute("SHOW DATABASES")
print(type(db_cursor),"mjhgh")
#print all databases
for db in db_cursor:
	print(db)

db_cursor.execute("use classicmodels")
db_cursor.execute("select phone from customers")
s=db_cursor.fetchall()
print((s))