# import connector
import mysql.connector
conn = None

# open connection
try:
    conn = mysql.connector.Connect(host="myhost",user="myuser",password="mypw",database="mydb")
    print('{:*^40}'.format("Connected to MySQL"))
except Exception as ex:
    print("Cannot connect to MySQL: Exception: " + str(ex))

# initialize cursor object
cursor = conn.cursor()

# contruct and send query
query = ("SELECT customerName, payments.paymentDate, payments.amount FROM customers inner join payments ON month(paymentDate) = 12 WHERE customerName = 'Mini Classics' ORDER BY paymentDate")
cursor.execute(query)

# iterate through and print results
print('{:-^40}'.format(""))
print('{:^40}'.format("Payments by Classic Minis in December"))
print('{:-^40}'.format(""))
print('{:<15} {:15} {:15}'.format('Customer', 'Date', 'Amount'))
print('{:-^40}'.format(""))
for row in cursor:
    print("{:<15} {:15} {:5}".format(row[0], str(row[1]), row[2]))

# clean up
print('{:-^40}'.format(""))
cursor.close()
print('{:*^40}'.format("Terminating MySQL Connection"))
conn.close()
