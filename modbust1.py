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
# print(instrument)

i = 0
sleep_time = 10
# instrument.write_register(683,900)

# listinha = []

#for i in range (0, 10):
#    listinha.insert(i, i)
# listinha = ["RAMPA", "10", "222x", "100", "RAMPA", "15", "666 CAPETAx", "170", "RAJADA", "10", "2323x", "100" ]

try:
    # acl = (duração*velocidade_final)/(velocidade_final - velocidade_inicial)
    # vel_ref = (vel_usu*8045)/885

    # time.sleep(5)
    instrument.write_register(683,0)
    instrument.write_register(100,5,1)
    instrument.write_register(134,50)
    instrument.write_register(133,0)
    
    durex = instrument.read_register(100, 1)
    print(durex)
    instrument.write_register(682,0x0013)

    instrument.write_register(683,50*8045/885)
    time.sleep(5)
    instrument.write_register(134,70)
    instrument.write_register(100,(5*70)/(70-50),1)
    instrument.write_register(683,70*8045/885)
    time.sleep(5)
    
    instrument.write_register(101,(5*70)/(70-20),1)
    instrument.write_register(683,20*8045/885)
    time.sleep(10)

    instrument.write_register(682,0x0014)

except IOError:
    print("Failed to read from instrument")
