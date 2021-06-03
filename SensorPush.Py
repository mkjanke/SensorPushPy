#!/usr/bin/python3
#
# Read current temperature from SensorPush (model HT.W)
# Note: Does not work with older models.
# 
# Uses bluepy
#
import sys
import time
from bluepy.btle import Peripheral, BTLEException

if len(sys.argv) != 2:
  print ("Fatal, must pass device address:", sys.argv[0], " aa.bb.cc.dd.ee")
  quit()

# Create bluepy Peripheral object
try:
  p = Peripheral(sys.argv[1])

except BTLEException as ex:
  print("Read failed. ", ex)
  exit

else:
  # read device charateristics, filtered on single SensorPush characteristic
  chList = p.getCharacteristics(uuid="ef090080-11d6-42ba-93b8-9dd7ec090aa9")
  ch = chList[0]

  # Write a byte to sensor to trigger sensor read
  # Wait a bit and read temperature
  ch.write(bytes([1,0,0,0]))
  time.sleep(1)
  tempC = int.from_bytes(ch.read(), byteorder="little", signed=True )/100

  # Output Temp in F
  tempF = tempC * 1.8 + 32
  print ("{:.1f}".format(tempF))

