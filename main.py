import flask
import json
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
with open('users.json') as f:
    bd = json.load(f)
app = flask.Flask(__name__)
@app.route('/')
def get_zapros():
    return flask.render_template('index.html')
@app.route('/login', methods=['POST'])
def post_zapros():
    login = request.form.get('login')
    password = request.form.get('password')
    if login in bd and check_password_hash(bd[login], password):
        return flask.render_template('welcome.html')
    else:
        return flask.render_template('unknown.html')


@app.route('/register', methods=['POST'])
def post_register():
    login = request.form.get('login')
    password = request.form.get('password')
    if login not in bd:
        bd[login] = generate_password_hash(password)
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(bd, f, ensure_ascii=False, indent=4)
        return flask.render_template('welcome.html')
    else:
        return flask.render_template('unknown.html')
@app.route('/welcome')
def welcome():
    return flask.render_template('welcome.html')
@app.route('/unknown')
def unknown():
    return flask.render_template('unknown.html')
if __name__ == '__main__':
    app.run(debug=True)