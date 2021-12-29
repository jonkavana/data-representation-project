# If things go wrong with DR9.5 video, just go to 8.3 - all detailed in there
# Will also need to review the client side server
from flask import Flask, url_for, request, redirect, abort, jsonify 

app = Flask(__name__, static_url_path='', static_folder='staticPages')

@app.route('/')
def index():
    return redirect (url_for('login'))

@app.route('/login')
def login():
    abort(401)
    return "Served by the login function"

@app.route('/user')
def getUser():
    return "Served by the getUser function"

@app.route('/user/<int:id>')
def getById(id):
    return "Served by the getById function with id = "+str(id) 

@app.route('/user', methods=['POST'])
def createUser():
    return "Served by the createUser function"

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
    print("in if")
    app.run(debug=True)