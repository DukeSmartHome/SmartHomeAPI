import pyrebase
import firebase_config
#import lights

config = firebase_config.config

firebase = pyrebase.initialize_app(config)
db = firebase.database()


def stream_handler(message):
    light = message["path"].replace("/","")
    status = message["data"]
#	lights.change(status,light)
    print("changing with",status,light)
    
    print(message["path"])
    print(message["data"])
    
    

my_stream = db.child("lights").stream(stream_handler)
