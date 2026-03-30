import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='varun@123',database='attendance_db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM student")
# count = cursor.fetchall()
print(cursor.fetchone())
# print(count)
# next_id = count + 1
# print(next_id)
conn.close()