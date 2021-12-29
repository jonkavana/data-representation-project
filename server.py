from flask import Flask, url_for

app = Flask(__name__, static_url_path='', static_folder='staticPages')

@app.route('/')
def index():
    return "Hello World"

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

if __name__ == "__main__":
    print("in if")
    app.run(debug=True)