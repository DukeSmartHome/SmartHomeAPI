
import serial
PORT = ""
ser = serial.Serial(PORT)

def change(status, whichLights):
    if status == "ON":
        for light in whichLights:
            tempHex = hex(light)
            if (tempHex.length == 1):
                tempHex = "0" + tempHex;
            chksum = bin((182 + light) % 256)
            newsum = ""
            for i in list(checksum):
                if i=="1":
                    newsum += "1"
                else:
                    newsum += "0"
            cSum = hex(1+int(newsum,2))
            fullStr = ("\\05380079" + tempHex + cSum).upper()
            finalStr = ""
            for i in list(fullStr):
                finalStr+= hex(ord(i))
            finalStr+="0D"
            ser.write(finalStr)
