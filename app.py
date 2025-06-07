from flask import Flask, render_template

app = Flask(__name__)

users = {}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/reg/')
def register():
    return "please, enter your nickname, example : /reg/nickname/"

@app.route('/log/')
def login():
    return "please, enter your nickname, example : /log/nickname/"

@app.route('/reg/<nickname>/')
def register_password(nickname):
    return "please, enter your password, example : /reg/nickname/password"

@app.route('/log/<nickname>/')
def log_password(nickname):
    return "please, enter your password, example : /log/nickname/password"

@app.route('/reg/<nickname>/<password>/')
def registered(nickname, password):
    users[nickname] = password

    return render_template("index.html")

@app.route('/log/<nickname>/<password>/')
def logined(nickname, password):
    if users.get(nickname) == password:
        return "You are succesfully logined!"
    return "Invalid password or nickname"

if __name__ == "__main__":
    app.run()
