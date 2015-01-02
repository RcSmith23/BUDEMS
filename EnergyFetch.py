#!/usr/bin/python
import serial

def main(args):
   meter  = serial.Serial('/dev/ttyUSB0',115200)
   meter.write("L,W,3,E,,1;")
   for line in meter:
      if line.startswith('#d'):
         fields = line.split(',')
         watts = float(fields[3]) / 10
         volts = float(fields[4]) / 10
         amps = float(fields[5]) / 1000
         #pf = float(fields[16]) / 100

         print("W: " + str(watts))
         print("V: " + str(volts))
         print("A: " + str(amps))
         #print("Power Factor: " + str(pf))
                    
    
main(0)
