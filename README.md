Python script to read SensorPush HT.w data

To read Temperature or Humidity, first write 32-bit value to appropriate characteristic then read value from 
characteristic. Values are little-endian, least significant byte first. 

Interesting characteristics:

## Temperature:
    Characteristic: EF090080-11D6-42BA-93B8-9DD7EC090AA9   
    4 bytes int32  Degrees Celsius

To read data, write any 32-bit value to the characteristic (e.g. 
0x01000000). This triggers a sensor read. Once the read is 
complete (typically less than 100ms later), the data will be 
available to read, in hundredths of degrees Celsius (e.g. 21.34 
degrees C will read 2134).

This read will also populate the relative humidity data, so if 
desired, it can be read immediately after without the need for a
separate read command

## Humidity:
    Characteristic: EF090081-11D6-42BA-93B8-9DD7EC090AA9
    4 bytes uint32 Percent Relative Humidity

To read data, write any 32-bit value to the characteristic (e.g. 
0x01000000). This triggers a sensor read. Once the read is 
complete (typically less than 100ms later), the data will be 
available to read, in hundredths of percent relative humidity (e.g. 
21.34% will read 2134).

This read will also populate the temperature data, so if desired, it 
can be read immediately after without the need for a separate 
read command.

## Battery Voltage
     Characteristic: EF090007-11D6-42BA-93B8-9DD7EC090AA9
     4 bytes uint16[2] Voltage in millivolts; Temperature at time of voltage reading

batteryVoltage[0]: Battery voltage in mV. The device can function down to around 2.4V (2,400mV)

batteryVoltage[1]: The temperature in degrees C at the time of the last battery voltage reading. The battery voltage data is updated each time a connection is established to the device
