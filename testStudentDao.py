from StudentDAO import secondDao

student1 = {
    'id' : 4,
    'name' : 'Paul',
    'age' : 21
}

student2 = {
    'id' : 5,
    'name' : 'John',
    'age' : 33
}

student3 = {
    'id' : 4,
    'name' : 'George',
    'age' : 73
}

# returnValue = secondDao.createUser(student)
returnValue = secondDao.getAll()
print(returnValue)
returnValue = secondDao.findById(student2['id'])
print(returnValue)
returnValue = secondDao.updateRecord(student2)
print(returnValue)
returnValue = secondDao.findById(student2['id'])
print(returnValue)
returnValue = secondDao.deleteRecord(student2['id'])
print(returnValue)
returnValue = secondDao.getAll()
print(returnValue)