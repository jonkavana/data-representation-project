# import the information from the central file in a new instance
from StudentDAO import secondDao

# create test data that shows 3 of the 4 Beatles.
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
# return all records
returnValue = secondDao.getAll()
print(returnValue)
# find a specific id we know is in the table
returnValue = secondDao.findById(student2['id'])
print(returnValue)
# update the same record
returnValue = secondDao.updateRecord(student2)
print(returnValue)
#search for the same id to prove it has been updated
returnValue = secondDao.findById(student2['id'])
print(returnValue)
# delete the same id
returnValue = secondDao.deleteRecord(student2['id'])
print(returnValue)
# retun all records to prove it has been deleted
returnValue = secondDao.getAll()
print(returnValue)