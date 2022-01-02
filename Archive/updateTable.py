import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database = "datarepresentation"
)

cursor = db.cursor()
sql = "update student set name=%s, age=%s where id = %s"
values = ("Joe",35,1)

cursor.execute(sql, values)

db.commit()
print("Update completed")