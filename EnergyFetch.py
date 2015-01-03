#!/usr/bin/python

import MySQLdb as mdb
import os
import serial

def main():

   #Get DB Information from host
   db_host = os.getenv('DB_HOST')
   db_user = os.getenv('DB_USERNAME')
   db_pass = os.getenv('DB_PASS')
   db_name = os.getenv('DB_NAME')
   
   #Open up meter and set configure it
   meter  = serial.Serial('/dev/ttyUSB0',115200)
   meter.write("L,W,3,E,,1;")

   try:
      con = mdb.connect(db_host, db_user, db_pass, db_name)
      cur = con.cursor()
      
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
                    
   except mdb.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])
      sys.exit(1)

   finally:
      if con:
         con.close()

if __name__ == "__main__":
   main()
