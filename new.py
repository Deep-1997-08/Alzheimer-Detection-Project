from flask import Flask

app = Flask(__name__) 

@app.route('/')

def hello():
    return "Hello"

@app.route('/admin')

def hello1():
    return "Hello Admin"

@app.route('/admin2')

def hello2():
    return "Hello Admin2"

app.run()
