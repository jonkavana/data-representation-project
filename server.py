# If things go wrong with DR9.5 video, just go to 8.3 - all detailed in there
# Will also need to review the client side server
from flask import Flask, url_for, request, redirect, abort, jsonify 
from StudentDAO import secondDao

app = Flask(__name__, static_url_path='', static_folder='staticPages')

# Create a decorator that allows the home page to be visible from first view.
@app.route('/')
def index():
    return redirect("home.html")

# If entered incorrectly, a standard abort error displayed.
@app.route('/login')
def login():
    abort(401)
    return "Served by the login function"

# Get All records for students 
@app.route('/student')
def getAll():
    return jsonify(secondDao.getAll())

# Get user by id
@app.route('/student/<int:id>')
def findById(id):
    return jsonify(secondDao.findById(id))

# code that was run in order to return create testing correctly
# curl -X POST -d "{\"id\":10, \"name\": \"test\", \"age\":89}" -H Content-Type:application/json http://127.0.0.1:5000/student
# Create a user
@app.route('/student', methods=['POST'])
def createUser():
    if not request.json:
        abort(400)
    studen = {
        "id": request.json["id"],
        "name": request.json["name"],
        "age": request.json["age"]
    }
    return jsonify(secondDao.createUser(studen))

# code that was run in order to return update testing correctly
# λ curl -X PUT -d "{\"name\": \"test2\", \"age\":56}" -H Content-Type:application/json http://127.0.0.1:5000/student/123
# Update a id
@app.route('/student/<int:id>', methods=['PUT'])
def updateRecord(id):
    foundBook = secondDao.findById(id)
    if foundBook == {}:
        return jsonify({}), 404
    currentBook = foundBook
    if 'name' in request.json:
        currentBook['name'] = request.json['name']
    if 'age' in request.json:
        currentBook['age'] = request.json['age']
    secondDao.updateRecord(currentBook)
    return jsonify(currentBook)

# code that was run in order to return DELETE testing correctly
# curl -X DELETE http://127.0.0.1:5000/student/123
# delete by id
@app.route('/student/<int:id>', methods=['DELETE'])
def deleteRecord(id):
    secondDao.deleteRecord(id)
    return jsonify({"done":True})

@app.route("/demo_url_for")
def demoUrlFor():
    returnString = "url for index is "+ url_for('index')
    returnString += "<br/>"
    returnString += "url for getById " + url_for('getById', id=12) 
    return returnString 

@app.route("/demo_request", methods=['POST','GET', 'DELETE'])
def demoRequest():
    return request.method

if __name__ == "__main__":
    app.run(debug=True)