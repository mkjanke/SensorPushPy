#!/usr/bin/python3
#
# Read current temperature from SensorPush (model HT.W)
# Note: Does not work with older models.
# 
# Uses bluezero
#
import sys
import time
from datetime import datetime
from bluezero import central

if len(sys.argv) != 2:
  print ("Fatal, must pass device address:", sys.argv[0], " aa.bb.cc.dd.ee")
  quit()

timeNow = (datetime.now()).strftime("%x %X")

# Create bluezero Central object
try:
  my_Sensor = central.Central(device_addr=sys.argv[1])

  # Sensorpush Temperature device charateristic
  ch = my_Sensor.add_characteristic("EF090000-11D6-42BA-93B8-9DD7EC090AB0", "ef090080-11d6-42ba-93b8-9dd7ec090aa9")
  my_Sensor.load_gatt()
  my_Sensor.connect()

except:
  exit

else:
  # print(my_Sensor.services_available)

  # Write a byte to sensor to trigger sensor read
  # Wait a bit and read temperature
  ch.write_value(bytes([1,0,0,0]))
  time.sleep(1)
  tempC = int.from_bytes(ch.read_raw_value(), byteorder="little", signed=True )/100

  # Output Temp in F
  tempF = round( tempC * 1.8 + 32, 1)
  print (timeNow, "{:.1f}".format(tempF))

