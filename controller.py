import pyrebase
import firebase_config
#import lights

config = firebase_config.config

firebase = pyrebase.initialize_app(config)
db = firebase.database()
#lights.change("ON",["26"])

def stream_handler(message):
	print(message)

	if  isinstance(message["data"], str):
		light = message["path"].replace("/","")
		status = message["data"]
	elif isinstance(message["data"], dict):
		light,status = convert(message["data"])
	else:
		print("del")
		return
	print("changing with status ",status," as ",light)
	if isinstance(light,int):
		print("changing with status ",status," as ",light)

		#lights.change(str(status),[str(light)])


def convert(dic):
	for key in dic:
		return key,dic[key]
my_stream = db.child("lights").stream(stream_handler)
