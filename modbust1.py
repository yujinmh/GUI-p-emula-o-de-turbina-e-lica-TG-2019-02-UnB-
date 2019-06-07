#!/usr/bin/env python
import minimalmodbus
import serial
import time

instrument = minimalmodbus.Instrument('COM4', 1) # port name, slave address (in decimal)
instrument.serial.baudrate = 9600   # Baud
instrument.serial.bytesize = 8
instrument.serial.parity   = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.debug = False
# instrument.serial.dsrdtr = False
# instrument.close_port_after_each_call = True
instrument.serial.timeout  = 0.5 # seconds
instrument.serial.xonxoff = False
# instrument.serial.rtscts = True
instrument.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
print(instrument)

i = 0
sleep_time = 5
# instrument.write_register(683,900)

try:
    print(instrument.read_register(1, 0), i)
    instrument.write_register(133,30)
    i = i + 1
    print(instrument.read_register(1, 0), i)
    time.sleep(sleep_time)
    i = i+1
    print(instrument.read_register(1, 0), i)
    instrument.write_register(133,10)
    time.sleep(sleep_time)
    i = i+1
    print(instrument.read_register(1, 0), i)
    instrument.write_register(133,0)
    time.sleep(sleep_time)
    i = i+1
    print(instrument.read_register(1, 0), i)
    instrument.write_register(133,40)
    time.sleep(sleep_time)
    i = i+1
    print(instrument.read_register(1, 0), i)
    instrument.write_register(133,30)
    i = i+1
    # instrument.write_register(683,0)
    # instrument.write_registers(100, [10,20]) # seconds multiply by 10 (1s is equal to 10) P0100(seconds)
    # instrument.write_registers(133, [0,1800]) # P0133(velo.)

except IOError:
    print("Failed to read from instrument")