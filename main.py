from flask import Flask, request, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    #return '<h1>Hello, '+ name + '</h1>'
    return render_template('welcome.html', username=username)

app.run()
