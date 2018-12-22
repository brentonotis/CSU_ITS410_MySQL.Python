#! /usr/bin/env/python

# Step 1: import the connector
import mysql.connector
conn = None

#Step 2: open a connection
try:
    conn = mysql.connector.Connect(host="myhost",user="myuser",password="mypw",database="mydb")
    print("Connected to MySQL!")
except Exception as ex:
    print("Cannot connect to MySQL: Exception: " + str(ex))

#Step 3: obtain a cursor
cursor = conn.cursor()

#Step 4: contruct and send query
query = ("SELECT last_name, first_name FROM actor ORDER BY last_name, first_name LIMIT 10")
cursor.execute(query)

#Step 5: iterate through and print results
for row in cursor:
    print("{:10} {:10}".format(*row))

#Step 6: clean up
cursor.close()
print("Terminating MySQL connection.")
conn.close()
    
