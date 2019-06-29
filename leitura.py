#!/usr/bin/env python
import minimalmodbus
import serial
import time

instrument = minimalmodbus.Instrument('COM3', 1) # port name, slave address (in decimal)
instrument.serial.baudrate = 9600   # Baud
instrument.serial.bytesize = 8
instrument.serial.parity   = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.debug = True
# instrument.handle_local_echo = True
# instrument.serial.dsrdtr = False
# instrument.close_port_after_each_call = True
# instrument.serial.timeout  = 0.5 # seconds
instrument.serial.xonxoff = False
# instrument.serial.rtscts = True
instrument.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode

# instrument.write_register(682,0x0014,functioncode=6)
time.sleep(2)
# instrument.write_register(682,19, functioncode=6)
# time.sleep(1)

# instrument.write_register(100,70, functioncode=6)
# instrument.write_register(101,50, functioncode=6)
# instrument.write_register(134,100, functioncode=6)
# instrument.write_register(133,0, functioncode=6)

# instrument.write_register(683,50*8045/885, functioncode=6)
# time.sleep(6)
# instrument.write_register(683,0, functioncode=6)
# time.sleep(6)

# instrument.write_register(100,100, functioncode=6)
# instrument.write_register(101,60, functioncode=6)
# instrument.write_register(134,120, functioncode=6)

# instrument.write_register(683,70*8045/885, functioncode=6)
# time.sleep(6)
# instrument.write_register(683,0, functioncode=6)
# time.sleep(8)

instrument.write_register(682,20,functioncode=6)
