#!/usr/bin/python3

import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
s = [0,1]
while True:
    read_serial = ser.readline()
    print(read_serial)
    
'''
Parse this string

b' 16:29:50\r\n'
b'Temp: 24.73\t\tHum: 25.83\r\n'
b'Pressure(Pa):98968.50 Temp(f):73.62\r\n'
b': 25.82\r\n'
b'Pressure(Pa):98962.75 Temp(f):73.51\r\n'
b'2018/4/30 16:29:50\r\n'
b'Temp: 24.73\t\tHum: 25.83\r\n'
b'Pressure(Pa):98968.50 Temp(f):73.62\r\n'
b': 25.82\r\n'
b'Pressure(Pa):98962.75 Temp(f):73.51\r\n'
b'2018/4/30 16:29:50\r\n'
b'Temp: 24.73\t\tHum: 25.83\r\n'
b'Pressure(Pa):98968.50 Temp(f):73.62\r\n'
b'2018/4/30 16:29:29\r\n'
b'Temp: 24.82\t\tHum: 25.96\r\n'
b'Pressure(Pa):98962.50 Temp(f):73.51\r\n'

'''