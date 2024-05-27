from flask import Flask
render_template, request,
redirect, url_for

app = Flask(__name__) 
{"id": 1, "name": "Studentlist"}

@app.route('/')
def index():
    return 'Hello World'

@app.route('/home')
def home():
    return 'This is Home'

@app.route('/login')
def login():
    return 'This is a Sample login'

if __name__== '__main__':
    app.run()
