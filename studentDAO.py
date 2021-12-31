import mysql.connector
import dbconfig as cfg

class StudentDAO:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
        host=   cfg.mysql['host'],
        user=   cfg.mysql['user'],
        password=   cfg.mysql['password'],
        database=   cfg.mysql['database']
        )
        # Test the initial connection between central file and testing script
        # print("connection established")

    def createUser(self, student):
        cursor = self.db.cursor()
        sql="insert into student (id, name, age) values (%s,%s,%s)"
        values = [
            student['id'],
            student['name'],
            student['age']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from student"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        # Test the initial connection between the funciton and the db.
        # print(results)
        
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray
              
    def findById(self, id):
        cursor = self.db.cursor()
        sql="select * from student where id = %s"
        values = [ id ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)

    def updateRecord(self, student):
        cursor = self.db.cursor()
        sql="update student set name= %s, age=%s where id = %s"
        values = [
            student['name'],
            student['age'],
            student['id']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return student

    def deleteRecord(self, id):
        cursor = self.db.cursor()
        sql="delete from student where id = %s"
        values = [id]
        cursor.execute(sql, values)
        self.db.commit()
        # Test the initial deletion function.
        # print("Deletion completed")
        return {}

    def convertToDict(self, result):
        colNames = ['id', 'name', 'age']
        student = {}
        
        if result:
            for i , colName in enumerate(colNames):
                value = result[i]
                student[colName] = value
        return student

secondDao = StudentDAO()


# from DAO video
# do i need to make the initdb.sql file? 
# create function used different parameter