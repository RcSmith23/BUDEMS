#!/bin/python
import serial

def main(args):
   srl  = serial.Serial('/dev/ttyUSB0',115200)
   srl.write("L,W,3,E,,1;")
   for line in srl:
      if line.startswith('#d'):
         print(line)

main(0)
