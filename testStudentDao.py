from StudentDAO import secondDao

student = {
    'id' : 4,
    'name' : 'Paul',
    'age' : 21
}

# returnValue = secondDao.create(student)
returnValue = secondDao.getAll()
print(returnValue)