import pyrebase
import firebase_config
import lights

config = firebase_config.config

firebase = pyrebase.initialize_app(config)
db = firebase.database()
lights.change("ON",["26"])

def stream_handler(message):

	light = message["path"].replace("/","")
	status = message["data"]
	print("changing with status ",status," as ",light)
	if isinstance(light,int):
		lights.change(str(status),[str(light)])


    

my_stream = db.child("lights").stream(stream_handler)
