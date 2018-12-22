
# import connector
import mysql.connector
conn = None

# open connection
try:
    conn = mysql.connector.Connect(host="myhost",user="myuser",password="mypw",database="mydb")
    print('{:*^57}'.format("Connected to MySQL"))
except Exception as ex:
    print("Cannot connect to MySQL: Exception: " + str(ex))

# initialize cursor object
cursor = conn.cursor()

# contruct and send query
query = ("SELECT * FROM payments WHERE month(paymentDate) = 12")
cursor.execute(query)

# iterate through and print results before rebate (raw db data)
print('{:-^57}'.format(""))
print('{:^57}'.format("Original Payment Amount"))
print('{:-^57}'.format(""))
print('{:<15} {:15} {:15} {:15}'.format('customerNumber', 'checkNumber', 'paymentDate', 'amount'))
print('{:-^57}'.format(""))
for row in cursor:
    print("{:<15} {:15} {:15} {:15}".format(row[0], row[1], str(row[2]), str(row[3])))

# contruct and send query again
query = ("SELECT * FROM payments WHERE month(paymentDate) = 12")
cursor.execute(query)

# iterate through and print results after rebate (-1% of 'amount' column)
print('{:-^57}'.format(""))
print('{:^57}'.format("New Payment Amount (-1%)"))
print('{:-^57}'.format(""))
print('{:<15} {:15} {:15} {:15}'.format('customerNumber', 'checkNumber', 'paymentDate', 'amount'))
print('{:-^57}'.format(""))
for row in cursor:
    #initialize newAmount variable (float), set to amount - amount/100 (-1%)
    newAmount = float(row[3])
    newAmount = newAmount - (newAmount / 100)
    print("{:<15} {:15} {:10} {:13.2f}".format(row[0], row[1], str(row[2]), newAmount))

# clean up
print('{:-^57}'.format(""))
cursor.close()
print('{:*^57}'.format("Terminating MySQL Connection"))
conn.close()
