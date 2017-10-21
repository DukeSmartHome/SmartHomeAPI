from flask import Flask, request
import pyrebase
import firebase_config

config = firebase_config.config
firebase = pyrebase.initialize_app(config)
db = firebase.database()


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Docs'

@app.route('/lights/<int:light>', methods = ['POST'])
def change(light):
    status = request.form['status']
    db.child("lights").push({light:status})
    print(light,status)

    return 'Success'


@app.route('/lights', methods=['GET'])
def current():
    show_the_login_form()


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
