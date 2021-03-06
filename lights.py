import time
from binascii import unhexlify
import serial
PORT = "/dev/ttyUSB0"
# ser = serial.Serial(PORT)

lights = [["Dirty Lab", "26", "labs"], ["Clean Lab Cabinets", "3", "labs"], ["Clean Lab", "4", "labs"], ["South West Bedroom", "6", "living"], ["Downstairs Bedroom", "7", "living"], ["North West Bedroom", "9", "living"], ["North East Bedroom", "21", "living"], ["South East Bedroom", "28", "living"], ["West Balcony", "35", "outside"], ["Front Porch", "35", "outside"], ["Back Porch", "36", "outside"], ["Kitchen", "11", "community"], ["Front Indoor Lights", "12", "community"], ["White Board Lights", "31", "community"], ["Kitchen Cabinets", "38", "community"], ["Main Room", "11", "community"], ["Media Room", "20", "community"], ["Upper Floor", "0", "community"], ["East Upper Bathroom", "17", "bathrooms"], ["West Upper Bathroom", "15", "bathrooms"], ["West Lower Bathroom", "13", "bathrooms"]];

settings = dict()
settings["ON"] = ["182","\\05380079"]
settings["OFF"] = ["62","\\05380001"]



def change(status, whichLights):
    if (status != "ON"):
        status = "OFF"
    for light in whichLights:
        tempHex = str(hex(light)).replace("0x","")
        if (len(tempHex) == 1):
            tempHex = "0" + tempHex
        chksum = bin((int(settings[status][0]) + light) % 256 ).replace("0b","")
        ##print (light,int(settings[status][0]) + light,((int(settings[status][0]) + light) % 256 ), bin((int(settings[status][0]) + light) % 256 ).replace("0b",""))
        newsum = ""
        for i in list(str(chksum)):
            if i=="1":
                newsum += "0"
            else:
                newsum += "1"

        cSum = hex(1+int(newsum,2)).replace("0x","")

        fullStr = str(settings[status][1] + str(tempHex) +str(cSum)).upper()
        finalStr = ""
        print(fullStr)

        for i in list(fullStr):
          finalStr+=hex(ord(i[0])).replace("0x","")
        finalStr+="0D"
        print(light, status, finalStr)
        # ser.write(unhexlify(finalStr))

change("OFF",[15])
change("OFF",[2])
