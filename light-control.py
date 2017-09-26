#
# import serial
# PORT = ""
# ser = serial.Serial(PORT)

lights = [["Dirty Lab", "26", "labs"], ["Clean Lab Cabinets", "3", "labs"], ["Clean Lab", "4", "labs"], ["South West Bedroom", "6", "living"], ["Downstairs Bedroom", "7", "living"], ["North West Bedroom", "9", "living"], ["North East Bedroom", "21", "living"], ["South East Bedroom", "28", "living"], ["West Balcony", "35", "outside"], ["Front Porch", "35", "outside"], ["Back Porch", "36", "outside"], ["Kitchen", "11", "community"], ["Front Indoor Lights", "12", "community"], ["White Board Lights", "31", "community"], ["Kitchen Cabinets", "38", "community"], ["Main Room", "11", "community"], ["Media Room", "20", "community"], ["Upper Floor", "0", "community"], ["East Upper Bathroom", "17", "bathrooms"], ["West Upper Bathroom", "15", "bathrooms"], ["West Lower Bathroom", "13", "bathrooms"]];

def change(status, whichLights):
    if status == "ON":
        for light in whichLights:
            tempHex = light
            if (len(str(tempHex)) == 1):
                tempHex = "0" + tempHex;
            chksum = bin(int("182" + str(light))%256).replace("0b","")
            newsum = ""
            print()
            for i in list(str(chksum)):
                if i=="1":

                    newsum += "0"
                else:
                    newsum += "1"
            # return newsum
            cSum = hex(1+int(newsum,2)).replace("0x","")
            fullStr = ("\\05380079" + tempHex + cSum).upper()
            finalStr = ""
            for i in list(fullStr):
                finalStr+=hex(ord(i[0])).replace("0x","")
            finalStr+="0D"
            return finalStr
    else:
        for light in whichLights:
            # light=int(light)
            tempHex = hex(light)
            if (len(str(tempHex)) == 1):
                tempHex = "0" + tempHex;
            chksum = bin((62 + light) % 256)
            newsum = ""
            for i in list(chksum):
                if i=="1":
                    newsum += "1"
                else:
                    newsum += "0"
            cSum = hex(1+int(newsum,2))
            fullStr = ("\\05380001" + tempHex + cSum).upper()
            finalStr = ""
            for i in list(fullStr):
                finalStr+= hex(ord(i))
            finalStr+="0D"
            return finalStr.replace("0x","")

            # ser.write(finalStr)
ans = "["
for i in lights:
    ans+="\""+str(change("ON",i[1]))+"\""
    ans+=","
    # ans+="\""+change("OFF",i[1])+"\""
    # ans+=","
ans+="]"
print(ans)
