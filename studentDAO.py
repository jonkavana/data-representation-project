import mysql.connector

class StudentDAO:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = "datarepresentation"
        )
        # Test the initial connection between central file and testing script
        print("connection established")

    def create(self, student):
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
        print(results)
        
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def convertToDict(self, result):
        colNames = ['id', 'name', 'age']
        student = {}
        
        if result:
            for i , colName in enumerate(colNames):
                value = result[i]
                student[colName] = value
        return student
                
    #def findById(self, id):
        #cursor = self.db.cursor()
        #sql="select * from student where id = %s"
        #values = (id,)
        #cursor.execute(sql, values)
        #result = cursor.fetchone()
        #return result

    #def updateRecord(self, values):
        #cursor = self.db.cursor()
        #sql="update student set name= %s, age=%s where id = %s"
        #cursor.execute(sql, values)
        #self.db.commit()

    #def deleteRecord(self, id):
        #cursor = self.db.cursor()
        #sql="delte from student where id = %s"
        #values = (id,)
        #cursor.execute(sql, values)
        #self.db.commit()
        #print("Deletion completed")

secondDao = StudentDAO()


# from DAO video
# do i need to make the initdb.sql file? 
# create function used different parameter