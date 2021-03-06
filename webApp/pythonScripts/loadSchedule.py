from datetime import datetime, date
import sys
import json
import serial
import time
COMPORT = '/dev/ttyACM0'
ahora = datetime.now()
currentTime = ahora.strftime("%H:%M:%S")
hoy = str(date.today())
data = json.loads(sys.argv[1])

for x in data:
    data[x] = str(data[x])

for i in data:
    if data[i] == "":
        data[i] = str(-1)

if not "Day1" in data:
    data["Day1"] = str(0)
if not "Day2" in data:
    data["Day2"] = str(0)
if not "Day3" in data:
    data["Day3"] = str(0)
if not "Day4" in data:
    data["Day4"] = str(0)
if not "Day5" in data:
    data["Day5"] = str(0)
if not "Day6" in data:
    data["Day6"] = str(0)
if not "Day7" in data:
    data["Day7"] = str(0)

if not "Pump1" in data:
    data["Pump1"] = str(-1)
if not "Pump2" in data:
    data["Pump2"] = str(-1)
if not "Pump3" in data:
    data["Pump3"] = str(-1)
if not "Pump4" in data:
    data["Pump4"] = str(-1)
if not "Pump5" in data:
    data["Pump5"] = str(-1)
if not "Pump6" in data:
    data["Pump6"] = str(-1)
if not "Pump7" in data:
    data["Pump7"] = str(-1)
if not "Pump8" in data:
    data["Pump8"] = str(-1)

superStr = data["Sections"] + "," + currentTime.split(":")[0] + "," + currentTime.split(":")[1] + "," + currentTime.split(":")[2] + "," + hoy.split("-")[2] + "," + hoy.split("-")[1] + "," + hoy.split("-")[0] + ","
base = "irrTime"
for j in range(3):
    for i in range(8):
        if data[base + str(i+1)] != "-1":
            superStr += (data[base + str(i+1)].split(":")[j] + ",")
        else:
            superStr += "-1,"

superStr += data["Day1"] + "," + data["Day2"] + "," + data["Day3"] + "," + data["Day4"] + "," + data["Day5"] + "," + data["Day6"] + "," + data["Day7"] + "," +\
data["irrDuration"] + ","

base = "ferTime"
for j in range(3):
    for i in range(8):
        if data[base + str(i+1)] != "-1":
            superStr += (data[base + str(i+1)].split(":")[j] + ",")
        else:
            superStr += "-1,"

superStr += data["ferDuration1"] + "," + data["ferDuration2"] + "," + data["ferDuration3"] + "," + data["ferDuration4"] + "," + data["ferDuration5"] + "," + data["ferDuration6"] + "," + data["ferDuration7"] + "," + data["ferDuration8"] + "," +\
data["Pump1"] + "," + data["Pump2"] + "," + data["Pump3"] + "," + data["Pump4"] + "," + data["Pump5"] + "," + data["Pump6"] + "," + data["Pump7"] + "," + data["Pump8"] + "," +\
data["Day1"] + "," + data["Day2"] + "," + data["Day3"] + "," + data["Day4"] + "," + data["Day5"] + "," + data["Day6"] + "," + data["Day7"] + ","

ser = serial.Serial(COMPORT, baudrate = 9600, timeout = .1)

ser.write(bytes(superStr))
