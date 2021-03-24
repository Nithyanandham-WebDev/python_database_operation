
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Python _MySQL Crud Operation.
Things to know Before Getting into the coding.
What is Database?
A database is an organized collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a database management system (DBMS). Together, the data and the DBMS, along with the applications that are associated with them, are referred to as a database system, often shortened to just database.

What is Structured Query Language (SQL)?
SQL is a programming language used by nearly all relational databases to query, manipulate, and define data, and to provide access control.

What is a Database Driver/Connector ?
Connector/Driver enables programs to access databases.

What is pip?
pip is the standard package manager for Python. It allows you to install and manage additional packages that are not part of the Python standard library.

Using pip We Can Install the Required Drivers/connectors to access Database.

What is Cursor?
Cursor,It Helps Python to Interact with the MySQL Server.An instance of the MySQLCursor class is also called a cursor

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   
# In[]  pip install mysql-connector-python



Connecting Database (MySQL) from Python.


In [ ]:
# Before Connecting Check 

# Database Software is Installed.
# Wheather appropriate Connectors/Drivers are Installed.
# Database Server Running are !.
# Authentication Method Used at Database Server Side(i.e naive password,sha256.,).
# Valid Server Address and Port no.(IP_Add:Port_No) to Establish Connection.
# A Valid UserName/Password to Access Database.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import Required Connectors:

In [ ]:
from mysql.connector import connect,Error,errorcode
Establishing a Connection Using Connection String.


Method #1:  Using try/with block

Method #2:  Using Connection Object.



#     Method #1:  Using try block

from getpass import getpass

try:
    with connect( 
        
    host = "localhost",
        
    port = "3306",
        
    user = 'Py_MySQL_User',
        
    password = getpass("Enter Password"),
        
    database="classicmodels",    
        
    auth_plugin = "mysql_native_password"
        
    ) as Python_MySQL_Conn_try:
        print(Python_MySQL_Conn_try)
except Error as  Python_MySQL_Conn_Err:
    if Python_MySQL_Conn_Err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        
        print("Invalid UserName Password")
        
    elif Python_MySQL_Conn_Err.errno == errorcode.ER_BAD_DB_ERROR:
        
        print("Database does not exist")


Python_MySQL_Conn = connect(
    
    host = "localhost",
        
    port = "3306",
        
    user = 'Py_MySQL_User',
        
    password = getpass("Enter Password"),
        
    database="classicmodels",    
        
    auth_plugin = "mysql_native_password"
        
    )
    
Python_MySQL_Conn




Conn_String = {
                    "host":"localhost",

                    "port" : "3306",

                    "user" : 'Py_MySQL_User',

                    "password" : 'rootUser',

#                     'database':"classicmodels",    

                    'auth_plugin' : "mysql_native_password"
                }

Python_MySQL_Conn = connect(**Conn_String)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Above code is now able to establish a connection to Mysql Server from Python.In that code,

host -->It takes a IP_Address as a Value.It tells Where the actual Mysql Server is running which is going to be accessed.

port -->A port is a virtual point where network connections start and end.Ports are software-based and managed by a computer's operating system. Each port is associated with a specific process or service.Here Mysql Server is running on port #3306(Default).

user -->The Actual Mysql Username to Gain Access to Server.

password -->The Actual Mysql Password to Gain Access to Server.

database -->The Actual Mysql Database Name which is going to be Accessed.(Optional)

auth_plugin -->Authentication Method Used to Secure Database from anonymous access.[mysql_native_password|caching_sha2_password]

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# The Connection to the Database is Now established.
# From Here I am Going to Perform the Below Operation From Python.
# Create User and Privileges Granting.
# Create Database.
# Perform DDL/DML Operations.



# Lets Check Whether Server Connected or ! .
if Python_MySQL_Conn:
    print("Connected")
    Python_MySQL_Conn.reset_session()



Creating User,Granting Access,Removing User from Python

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# We Need an Intermediate to Perform Database Operations.
# Here cursor Comes in action to act as an Intermediate between Python and Database Server.
# to Create a cursor object We need an Active Database Connection.

# Actual Syntax:

# Cursor_Name = Connection_Object.cursor()

# In Our Case:

Python_MySQL_Conn_Cursor = Python_MySQL_Conn.cursor()

     
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Create User:

# MySQL Query to Create New User.

MySQL_Query_Create_New_User = "CREATE USER IF NOT EXISTS 'User_Created_From_Python_15'@'localhost' IDENTIFIED BY 'root'"

# Now Using execute() Cursor Fn to Execute the Above Query.

try:
    Python_MySQL_Conn_Cursor.execute(MySQL_Query_Create_New_User)
        
except Error as MySQL_Query_Create_New_User_Execute:
    print(MySQL_Query_Create_New_User_Execute)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# SELECT user FROM mysql.user where user = "User_Created_From_Python";
# Python_MySQL_Conn_Cursor.execute("SELECT user FROM mysql.user")

MySQL_Query_Get_All_Users = "SELECT user FROM mysql.user"
Python_MySQL_Conn_Cursor.execute(MySQL_Query_Get_All_Users)

print(Python_MySQL_Conn_Cursor.fetchall())

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# MySQL Query to Grant Privileges.

# MySQL Syntax_To_Grant Permissions

# GRANT <type_of_permission> ON <database_name.table_name> TO <'username'>@<'localhost'>;

# ALL PRIVILEGES- as we saw previously, this would allow a MySQL user full access to a designated database (or if no database is selected, global access across the system)
# CREATE- allows them to create new tables or databases
# DROP- allows them to them to delete tables or databases
# DELETE- allows them to delete rows from tables
# INSERT- allows them to insert rows into tables
# SELECT- allows them to use the SELECT command to read through databases
# UPDATE- allow them to update table rows
# GRANT OPTION- allows them to grant or remove other users’ privileges

Python_MySQL_Conn.reset_session()

MySQL_Query_Grant_Access = "GRANT ALL ON *.* TO 'User_Created_From_Python_1'@'localhost'"

# Above Query Gives All Access to Our Created User User_Created_From_Python_1.

try:
    Python_MySQL_Conn_Cursor.execute(MySQL_Query_Grant_Access)
    
except Error as MySQL_Query_Grant_Access_Execute:
    print(MySQL_Query_Grant_Access_Execute)


 ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# MySQL Query to View Privileges.

# MySQL Syntax_To_View Granted Permissions

# SHOW GRANTS FOR  <'username'>@<'localhost'>;

MySQL_Query_View_Access = "SHOW GRANTS FOR 'User_Created_From_Python_1'@'localhost'"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_View_Access)

Result_Set_Permission = Python_MySQL_Conn_Cursor.fetchall()

print(Result_Set_Permission)


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# MySQL Query to Delete/Remove/Drop User.

# MySQL Syntax_To_Delete/Remove/Drop User.

# DROP USER <User_Name>;

MySQL_Query_Drop_User = "DROP USER IF EXISTS 'User_Created_From_Python_1'@'localhost'"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Drop_User)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# SELECT user FROM mysql.user where user = "User_Created_From_Python";
# Python_MySQL_Conn_Cursor.execute("SELECT user FROM mysql.user")

MySQL_Query_Get_All_Users = "SELECT user FROM mysql.user"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Get_All_Users)

result = Python_MySQL_Conn_Cursor.fetchall()

print(result)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Create/Drop Database.


# MySQL Query to Create Database.

# MySQL Syntax_To_Create_Database.

# CREATE <DATABASE> IF NOT EXISTS <Database_Name>;

# IF NOT EXISTS is used it creates only if given name does not conflict with an existing database's name.If ! it throws an error. 

MySQL_Query_Create_Database = "CREATE DATABASE IF NOT EXISTS Library_DataBase"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Create_Database)


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# MySQL Query to list Available Databases.

# MySQL Syntax_To_View_Available_Databases.

# SHOW DATABASES;

MySQL_Query_Show_Database = "SHOW DATABASES"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Database)

print(Python_MySQL_Conn_Cursor.fetchall())

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# MySQL Query to Drop Database.

# MySQL Syntax_To_Drop_Database.

# DROP DATABASE DATABASE_NAME;

MySQL_Query_Drop_Database = "DROP DATABASE IF EXISTS DATABASE_CREATED_FROM_PYTHON"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Drop_Database)


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


MySQL_Query_Show_Database = "SHOW DATABASES"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Database)

print(Python_MySQL_Conn_Cursor.fetchall())


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Once Database is Created We Need To Use it By Using 'use' Command.

# MySQL Syntax_To_Use_Database.

# USE DATABASE_NAME;

MySQL_Query_Use_Database = "USE Library_DataBase"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Use_Database)


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Create/Drop Table.



Here We are Going to Perform Create/Alter Table and its Attributes (i.e Columns)



# MySQL Query to Create Table.

# MySQL Syntax_To_Create_Table.

# CREATE  TABLE [IF NOT EXISTS] <TableName> (Column#1 <dataType>,Column#2 <dataType>,Column#n <dataType>;

MySQL_Query_Create_Table = "CREATE TABLE IF NOT EXISTS Table_Created_From_Python(Book_Id int,Book_Name varchar(30),Book_Edition varchar(30),Book_Author varchar(30),No_Of_Copies int,is_Available boolean,Book_Dept varchar(30),Book_ISBN varchar(30))"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Create_Table)


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# MySQL Query to list Available Tables.

# MySQL Syntax_To_View_Available_Tables.

# SHOW TABLES;

MySQL_Query_Show_Table = "SHOW TABLES"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Table)

print(Python_MySQL_Conn_Cursor.fetchall())

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# MySQL Query to View Table Structure.

# MySQL Syntax_To_View_Table_Structure.

# DESC <TableName>;

MySQL_Query_Describe_Table = "DESC Table_Created_From_Python"
Python_MySQL_Conn_Cursor.execute(MySQL_Query_Describe_Table)
print(Python_MySQL_Conn_Cursor.fetchall())


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# MySQL Query to Drop/Delete/Remove Table.

# MySQL Syntax_To_Drop_Table.

# DROP TABLE [IF EXISTS] <TableName>;

MySQL_Query_Drop_Table = "DROP TABLE IF EXISTS Table_Created_From_Python_3"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Drop_Table)

MySQL_Query_Show_Table = "SHOW TABLES"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Table)

print(Python_MySQL_Conn_Cursor.fetchall())

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Table ALTER Operations.


# Tables are now created.Now We Gonna Perform Some Table Operations Using ALTER Command.

# --> Alter/Change Column Datatype.

# --> Alter/Change Column Datatype Size.

# --> Alter/Change Table/Column Name.

# --> Add a New Column.

# --> Drop Column.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# --> Alter/Change Column Datatype.

# Basic Syntax:

# ALTER TABLE table_name
#   MODIFY column_name column_definition
#     [ FIRST | AFTER column_name ],
#   MODIFY column_name column_definition
#     [ FIRST | AFTER column_name ],
#   ...
# ;

MySQL_Query_ALTER_Table_DataType = "ALTER TABLE Table_Created_From_Python MODIFY Book_Id varchar(10)"


Python_MySQL_Conn_Cursor.execute(MySQL_Query_ALTER_Table_DataType)

MySQL_Query_Describe_Table = "DESC Table_Created_From_Python"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Describe_Table)

print(Python_MySQL_Conn_Cursor.fetchall())

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# --> Alter/Change Column Datatype Size.

MySQL_Query_ALTER_Table_DataType_Size = "ALTER TABLE Table_Created_From_Python_1 MODIFY Book_Id_Renamed varchar(20)"


Python_MySQL_Conn_Cursor.execute(MySQL_Query_ALTER_Table_DataType_Size)

MySQL_Query_Describe_Table = "DESC Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Describe_Table)

print(Python_MySQL_Conn_Cursor.fetchall())


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# --> Alter/Change Table/Column Name.

# Basic Syntax For Column Rename:

# Basic Syntax For Table Rename:

# ALTER TABLE table_name
#   RENAME TO new_table_name;

# MySQL_Query_ALTER_Table_Rename = "ALTER TABLE Table_Created_From_Python RENAME TO Table_Renamed_From_Python"


# Python_MySQL_Conn_Cursor.execute(MySQL_Query_ALTER_Table_Rename)

MySQL_Query_Show_Table = "SHOW TABLES"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Table)

print(Python_MySQL_Conn_Cursor.fetchall())


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ALTER TABLE table_name
#   CHANGE COLUMN old_name new_name 
#     column_definition
#     [ FIRST | AFTER column_name ]


MySQL_Query_ALTER_Table_Column_Rename = "ALTER TABLE Table_Created_From_Python_1 CHANGE COLUMN Book_Id_Renamed Book_Id_Renamed_1 varchar(20)"


Python_MySQL_Conn_Cursor.execute(MySQL_Query_ALTER_Table_Column_Rename)

MySQL_Query_Describe_Table = "DESC Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Describe_Table)

print(Python_MySQL_Conn_Cursor.fetchall())

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# --> Add a New Column.

# Add a Single Column.

# ALTER TABLE table_name
#   ADD COLUMN new_column_name column_definition
#     [ FIRST | AFTER column_name ];

# By Default Adds New Column as Last Column.

MySQL_Query_ALTER_Table_Column_Add = "ALTER TABLE Table_Created_From_Python_1 ADD New_Added_column_1 varchar(20) AFTER Book_Id_Renamed_1"


Python_MySQL_Conn_Cursor.execute(MySQL_Query_ALTER_Table_Column_Add)

MySQL_Query_Describe_Table = "DESC Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Describe_Table)

print(Python_MySQL_Conn_Cursor.fetchall())

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Add a Multiple Columns.

# ALTER TABLE table_name
#   ADD COLUMN new_column_name column_definition
#     [ FIRST | AFTER column_name ],
#   ADD COLUMN new_column_name column_definition
#     [ FIRST | AFTER column_name ],
#   ...
# ;

MySQL_Query_ALTER_Table_Columns_Add = "ALTER TABLE Table_Created_From_Python_1 ADD COLUMN New_Added_column_3 varchar(20) AFTER Book_Id_Renamed,ADD COLUMN New_Added_column_6 int AFTER Book_Dept"


Python_MySQL_Conn_Cursor.execute(MySQL_Query_ALTER_Table_Columns_Add)

MySQL_Query_Describe_Table = "DESC Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Describe_Table)

print(Python_MySQL_Conn_Cursor.fetchall())


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# --> Drop a Column.

# Drops a Single Column.
# ALTER TABLE table_name
#   DROP COLUMN column_name;


MySQL_Query_ALTER_Table_Column_Drop = "ALTER TABLE Table_Created_From_Python_1 DROP COLUMN New_Added_column_1"


Python_MySQL_Conn_Cursor.execute(MySQL_Query_ALTER_Table_Column_Drop)

MySQL_Query_Describe_Table = "DESC Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Describe_Table)

print(Python_MySQL_Conn_Cursor.fetchall())


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Drops Multiple Columns.

# ALTER TABLE table_name
#   DROP COLUMN new_column_name column_definition
#     [ FIRST | AFTER column_name ],
#   DROP COLUMN new_column_name column_definition
#     [ FIRST | AFTER column_name ],
#   ...
# ;

MySQL_Query_ALTER_Table_Columns_Drop = "ALTER TABLE Table_Created_From_Python_1 DROP COLUMN New_Added_column_6"


Python_MySQL_Conn_Cursor.execute(MySQL_Query_ALTER_Table_Columns_Drop)

MySQL_Query_Describe_Table = "DESC Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Describe_Table)

print(Python_MySQL_Conn_Cursor.fetchall())

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Table Insert/Update Operations.



# Tables are now created and Altered.Now We Gonna Perform Some Table Operations Using INSERT Command.

# --> Single Row Insert.

# --> Insert Into Specific Columns.

#  --> Multiple Row Insert



# --> Single Row Insert.

# Basic Syntax.

# INSERT INTO table
# (column1, column2, ... )
# VALUES
# (expression1, expression2, ... ) ;

# o/p = ['Book_Id_Renamed',Book_Name','Book_Edition','Book_Author','No_Of_Copies','is_Available','Book_Dept','Book_ISBN']


MySQL_Query_ALTER_Table_Insert_One = "INSERT INTO Table_Created_From_Python_1(Book_Id_Renamed,Book_Name,Book_Edition,Book_Author,No_Of_Copies,is_Available,Book_Dept,Book_ISBN) VALUES (12,'Python_Basics',5,'Lutz',6,1,'CSE','456'-12378-56)"


Python_MySQL_Conn_Cursor.execute(MySQL_Query_ALTER_Table_Insert_One)

MySQL_Query_Describe_Table = "SELECT * FROM Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Describe_Table)

print(Python_MySQL_Conn_Cursor.fetchall())


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# --> Mutiple Row Insert.

# Basic Syntax.

# INSERT INTO table
# (column1, column2, ... )
# VALUES
# (expression1, expression2, ... ),
# (expression1, expression2, ... ),
# ...;

MySQL_Query_ALTER_Table_Insert_One = "INSERT INTO Table_Created_From_Python_1(Book_Id_Renamed,Book_Name,Book_Edition,Book_Author,No_Of_Copies,is_Available,Book_Dept,Book_ISBN) VALUES (12,'Python_Basics',5,'Lutz',6,1,'CSE','456'-12378-56),(12,'Python_Basics',5,'Lutz',6,1,'CSE','456'-12378-56),(12,'Python_Basics',5,'Lutz',6,1,'CSE','456'-12378-56),(12,'Python_Basics',5,'Lutz',6,1,'CSE','456'-12378-56)"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_ALTER_Table_Insert_One)

MySQL_Query_Describe_Table = "SELECT * FROM Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Describe_Table)

print(Python_MySQL_Conn_Cursor.fetchall())


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



MySQL_Query_Empty_Table = "TRUNCATE Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Empty_Table)

print(Python_MySQL_Conn_Cursor.fetchall())


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Task Inserting Values Using For Loop.


from RandomWordGenerator import RandomWord
import random

# RandomWord = RandomWords()
rw = RandomWord()
 
for x in range(25):
    Python_MySQL_Conn_Cursor.execute("INSERT INTO Table_Created_From_Python(Book_Id,Book_Name,Book_Edition,Book_Author,No_Of_Copies,is_Available,Book_Dept,Book_ISBN) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(x+1,rw.generate(),random.randrange(1,30),rw.generate(),random.randrange(5,15),random.choice([0,1]),random.choice(['CSE','IT','EEE','SCEINCE']),random.randrange(560000000,890000000)))
#     Python_MySQL_Conn_Cursor.execute("INSERT INTO Table_Created_From_Python_1(Book_Id_Renamed,Book_Name,Book_Edition,Book_Author,No_Of_Copies,is_Available,Book_Dept,Book_ISBN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",(str(x+1),name,str(x+1),str(x+1),random.randrange(5,15),random.choice([0,1]),name,random.randrange(560000000,890000000)))
        
#     Python_MySQL_Conn_Cursor.commit()
Python_MySQL_Conn.commit()
MySQL_Query_Select_Table = "SELECT * FROM Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Select_Table)

print(Python_MySQL_Conn_Cursor.fetchall())


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Tables are now created and Values Too Inserted.Now We Gonna Perform Some Table Operations Using UPDATE Command.

# --> Single Cell Update.

#  --> Multiple Cell Update


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# --> Single Cell Update.

# -->Basic Syntax.

# UPDATE table
# SET column1 = expression1,
#     column2 = expression2,
#     ...
# [WHERE conditions];

MySQL_Query_Update_Value = "UPDATE Table_Created_From_Python_1 SET Book_Dept = 'General Science' WHERE Book_ISBN = '844152221'"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Update_Value)

Python_MySQL_Conn.commit()





MySQL_Query_Show_Table = "SELECT * FROM Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Table)

print(Python_MySQL_Conn_Cursor.fetchall())


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# --> Multiple Cell Update.

# -->Basic Syntax.

# UPDATE table
# SET column1 = expression1,
#     column2 = expression2,
#     ...
# [WHERE conditions];

MySQL_Query_Update_Multiple_Values = "UPDATE Table_Created_From_Python_1 SET Book_Dept = 'General Science' WHERE Book_Dept = 'SCEINCE'"

MySQL_Query_Update_Multiple_Values = "UPDATE Table_Created_From_Python_1 SET Book_Name = 'Python' WHERE No_Of_Copies < 10"

MySQL_Query_Update_Multiple_Values = "UPDATE Table_Created_From_Python_1 SET Book_Author = 'Mark Lutz' WHERE Book_Name = 'Python'"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Update_Multiple_Values)

Python_MySQL_Conn.commit()





MySQL_Query_Show_Table = "SELECT * FROM Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Table)

print(Python_MySQL_Conn_Cursor.fetchall())


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Table Delete Operations



# Tables are now created and Values Too Inserted.Now We Gonna Perform Some Table Operations Using DELETE Command.

# With This Delete Query We Can Able To DElete A Single/Multiple Row in Table.

# --> Single Row Delete.

#  --> Multiple Row Delete.

# --> Basix Syntax

# DELETE [ LOW_PRIORITY ] [ QUICK ] [ IGNORE ] FROM table
# [WHERE conditions]
# [ORDER BY expression [ ASC | DESC ]]
# [LIMIT number_rows];

MySQL_Query_Delete_Single_Row = "DELETE FROM Table_Created_From_Python_1 WHERE Book_ISBN = '581874728'"

MySQL_Query_Delete_Multiple_Row = "DELETE FROM Table_Created_From_Python_1 WHERE No_Of_Copies < 8"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Delete_Multiple_Row)

Python_MySQL_Conn.commit()





MySQL_Query_Show_Table = "SELECT * FROM Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Table)

print(Python_MySQL_Conn_Cursor.fetchall())


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Cursor Methods


Lets Discuss Some Built-in Cursor Methods


# -->fetchall()

# fetches all the rows of a query result. It returns all the rows as a list of tuples. An empty list is returned if there is no record to fetch.

# Basic Syntax:

# Cursor.fetchall()  -->Returns a list.

MySQL_Query_Show_Table = "SELECT * FROM Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Table)

Python_MySQL_Conn_Cursor.fetchall()

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# -->fetchmany(size)

# returns the number of rows specified by size argument. 
# Assume a table Of 100 rows and size is 10.When Fetchmany(Size) is called it fetches First 1-10 Rows,if again called it fetches 11-20 rows.

# Basic Syntax:

# Cursor.fetchmany(Size)  -->Returns a list.

MySQL_Query_Show_Table = "SELECT * FROM Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Table)

Python_MySQL_Conn_Cursor.fetchmany(20)

Python_MySQL_Conn_Cursor.rowcount


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# -->fetch()

# returns Single Row. 
# Assume a table Of 100 rows and size is 10.When Fetchone() is called it fetches First Row,if again called it fetches 2nd Rows.

# Basic Syntax:

# Cursor.fetchone()  -->Returns a list.

MySQL_Query_Show_Table = "SELECT * FROM Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Table)

Python_MySQL_Conn_Cursor.fetchone()


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# -->column_names

# returns a Tuple Of Column Names.

MySQL_Query_Show_Table = "SELECT * FROM Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Table)

Python_MySQL_Conn_Cursor.column_names

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# -->description

# returns a Tuple Of Column Names and its Definition.

MySQL_Query_Show_Table = "SELECT * FROM Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Table)

Python_MySQL_Conn_Cursor.description


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# -->description

# returns a Tuple Of Column Names and its Definition.

MySQL_Query_Show_Table = "SELECT * FROM Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Table)

Python_MySQL_Conn_Cursor.arraysize

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# -->execute(operation, params=None, multi=False)

# This method executes the given database operation (query or command). 
# The parameters found in the tuple or dictionary params are bound to the variables in the operation. Specify variables using %s or %(name)s parameter style (that is, using format or pyformat style). 
# execute()  returns an iterator 
# If multi is set to True, execute() is able to execute multiple statements specified in the operation string

MySQL_Query_Show_Table = "SELECT * FROM Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Table,multi = False)

Python_MySQL_Conn_Cursor.fetchall()


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# -->executemany(operation, seq_of_params)

# the executemany() method iterates through the sequence of parameters, each time passing the current parameters to the the execute() method.

# An optimization is applied for inserts: The data values given by the parameter sequences are batched using multiple-row syntax.

Input_Sequence = [('1',  None,  None,  'SfaszGHeAY',  '20',  'KjyehJdZjn',  11,  0,  'CSE',  '660801281'),
 ('1', None, None, 'Python', '28', 'Mark Lutz', 9, 1, 'CSE', '692991479'),
 ('2', None, None, 'Python', '20', 'Mark Lutz', 8, 1, 'CSE', '610594197'),
 ('3',  None,  None,  'cXfMdqvwRt',  '28',  'rRywsBbRFV',  11,  1,  'CSE',  '647050308'),
 ('4',  None,  None,  'GzUEhpLcPZ',  '10',  'jzqebXjALX',  10,  0,  'CSE',  '684333878'),
 ('6',  None,  None,  'BYMNbjwgmf',  '14',  'sUzKKZoQCX',  11,  1,  'CSE',  '861824773'),
 ('7',  None,  None,  'jOOeaDoDcP',  '12',  'thOYfBBaCK',  13,  0,  'General Science',  '667434824'),
 ('8', None, None, 'Python', '25', 'Mark Lutz', 8, 0, 'CSE', '603005960'),
 ('9',  None,  None,  'qZGGmXYWlt',  '2',  'cRBlQhozaZ',  14,  0,  'General Science',  '785966011'),
 ('10', None, None, 'Python', '27', 'Mark Lutz', 8, 0, 'EEE', '741239710'),
 ('11',  None,  None,  'RyHZcQrTqV',  '1',  'jfQTcXaTbH',  12,  0,  'General Science',  '856999811'),
 ('14',  None,  None,  'idUhQYyarw',  '24',  'ELnlvOPyoF',  12,  1,  'General Science',  '718599219'),
 ('15', None, None, 'Python', '10', 'Mark Lutz', 8, 0, 'IT', '759009895'),
 ('16',  None,  None,  'GQoLalpUpu',  '25',  'AxDEHPLcPc',  12,  0,  'IT',  '712987377'),
 ('17', None, None, 'Python', '13', 'Mark Lutz', 9, 1, 'CSE', '614165436'),
 ('18',  None,  None,  'MtoeodyZkM',  '20',  'aLYegenIeU',  11,  1,  'IT',  '570992861'),
 ('20', None, None, 'Python', '1', 'Mark Lutz', 9, 0, 'EEE', '782935475'),
 ('21',  None,  None,  'ujhfYdUnBT',  '6',  'ceCfODeJPZ',  12,  1,  'General Science',  '678769994'),
 ('22',  None,  None,  'eGQRqmAqFT',  '12',  'fyDnFtuXti',  14,  0,  'EEE',  '678821483'), 
 ('1',  None,  None,  'oRFIfVCOYE',  '12',  'dfhQRFqTaM',  12,  0,  'EEE',  '624124304'),
 ('3', None, None, 'isOJrxMsfK', '17', 'WVuEffxfMR', 12, 1, 'IT', '627914268'),
 ('4', None, None, 'Python', '20', 'Mark Lutz', 8, 0, 'CSE', '727550575'),
 ('5', None, None, 'pCyUTCeDxa', '8', 'tnZkmtwPHe', 11, 1, 'CSE', '610899465')]

MySQL_Query_Execute_Many_Query = "INSERT INTO Table_Created_From_Python_1(Book_Id_Renamed_1,New_Added_column_1,New_Added_column_3,Book_Name,Book_Edition,Book_Author,No_Of_Copies,is_Available,Book_Dept,Book_ISBN) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

Python_MySQL_Conn_Cursor.executemany(MySQL_Query_Execute_Many_Query,Input_Sequence)

MySQL_Query_Show_Table = "SELECT * FROM Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Table)

Python_MySQL_Conn_Cursor.fetchall()

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# returns the value generated for an AUTO_INCREMENT column by the previous INSERT or UPDATE statement …

Python_MySQL_Conn_Cursor.lastrowid

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# -->executemany(operation, seq_of_params)

# the executemany() method iterates through the sequence of parameters, each time passing the current parameters to the the execute() method.

# An optimization is applied for inserts: The data values given by the parameter sequences are batched using multiple-row syntax.

MySQL_Query_Show_Table = "SELECT * FROM Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Table)

Python_MySQL_Conn_Cursor.fetchall()

# Python_MySQL_Conn_Cursor.rowcount


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# -->cursor.statement

# This read-only property returns the last executed statement as a string. 

Python_MySQL_Conn_Cursor.statement

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# cursor.with_rows

# The with_rows property is useful when it is necessary to determine whether a statement produces a result set and you need to fetch rows. 

MySQL_Query_Show_Table = "SELECT * FROM Table_Created_From_Python_1"

Python_MySQL_Conn_Cursor.execute(MySQL_Query_Show_Table)


if Python_MySQL_Conn_Cursor.with_rows:
    print(Python_MySQL_Conn_Cursor.fetchall())

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# cursor.close()

# Used to Disconnect Database Connection

