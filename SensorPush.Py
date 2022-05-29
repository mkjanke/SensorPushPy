#!/usr/bin/python3
#
# Read temperature, humidity, battery volts from SensorPush (model HT.W)
# Note: Does not work with older models.
# 
# Uses bluezero
#
import sys
import time
import struct
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
  chTemp = my_Sensor.add_characteristic("EF090000-11D6-42BA-93B8-9DD7EC090AB0", "ef090080-11d6-42ba-93b8-9dd7ec090aa9")
  chHumid = my_Sensor.add_characteristic("EF090000-11D6-42BA-93B8-9DD7EC090AB0", "ef090081-11d6-42ba-93b8-9dd7ec090aa9")
  chBatt = my_Sensor.add_characteristic("EF090000-11D6-42BA-93B8-9DD7EC090AB0", "EF090007-11D6-42BA-93B8-9DD7EC090AA9")
  my_Sensor.load_gatt()
  my_Sensor.connect()

except:
  exit

else:
  # print(my_Sensor.services_available)
  battVolts, battTemp = struct.unpack_from('<HH', bytes(chBatt.read_raw_value()), 0)
  battVolts = battVolts/1000

  # Write a byte to sensor to trigger sensor read
  # Wait a bit and read temperature and Humidity
  chTemp.write_value(bytes([1,0,0,0]))
  time.sleep(1)
  tempC = int.from_bytes(chTemp.read_raw_value(), byteorder="little", signed=True )/100
  humidity = int.from_bytes(chHumid.read_raw_value(), byteorder="little", signed=True )/100

  # Output Temp in F
  tempF = round( tempC * 1.8 + 32, 1)
  print (timeNow, "{:.1f}F".format(tempF), "{:.1f}%".format(humidity),"{:.3f}V".format(battVolts) )

