from flask import Flask, request, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def index():
    return render_template('validate.html')

@app.route('/', methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) < 4:
        username_error = "Invalid username"
    elif len(username) > 20:
        username_error = "Invalid username"
    elif username == " ":
        username_error = "Invalid username"
    elif ' ' in username:
        username_error = "Invalid username"
    else: username_error = ''

    if len(password) < 4:
        password_error = "Invalid password"
    elif len(password) > 20:
        password_error = "Invalid password"
    elif password == " ":
        password_error = "Invalid password"
    elif ' ' in password:
        password_error = "Invalid password"
    else: password_error = ''

    if verify != password:
        verify_error = "Passwords do not match"
    elif verify_error == " ":
        verify_error = "Passwords do not match"
    else: verify_error = ''

    
    if 1 < len(email) < 4 or len(email) > 20:
        email_error = "Invalid email"
    elif ' ' in email:
        email_error = "Invalid email"
    elif len(email) > 0 and "@" not in email or len(email) > 0 and "." not in email:
        email_error = "Invalid email"
    else: email_error = ''
     
    if not username_error and not password_error and not verify_error and not email_error:
        return welcome()
    else:
        return render_template('validate.html', username_error=username_error, username=username, password_error=password_error,
        verify_error=verify_error, email_error=email_error, email=email)

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)

app.run()
