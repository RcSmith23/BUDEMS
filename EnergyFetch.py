#!/bin/python
import serial

def main(args):
   meter  = serial.Serial('/dev/ttyUSB0',115200)
   meter.write("L,W,3,E,,1;")
   for line in meter:
      if line.startswith('#d'):
         fields = line.split(',')
         watts = fields[3] / 10
         volts = fields[4] / 10
         amps = fields[5] / 1000

         print("W: " + str(watts))
         print("V: " + str(volts))
         print("A: " + str(amps))
                    
    
main(0)
