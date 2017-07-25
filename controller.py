import pyrebase
import firebase_config

config = firebase_config.config

firebase = pyrebase.initialize_app(config)
db = firebase.database()


def stream_handler(message):
    print(message["event"])
    print(message["path"])
    print(message["data"])

my_stream = db.child("lighting").stream(stream_handler)
