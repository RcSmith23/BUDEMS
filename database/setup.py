#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys
import os

tables = {}

tables[0] = """CREATE TABLE IF NOT EXISTS machines (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    cores INT,
    memory BIGINT
    );"""

tables[1] = '''CREATE TABLE IF NOT EXISTS benchmarks (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    mem_intensive BOOL,
    cpu_intensive BOOL,
    description TEXT
    );'''

tables[2] = '''CREATE TABLE IF NOT EXISTS recordings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    time_stamp TIMESTAMP NOT NULL,
    watts DOUBLE(4,1) NOT NULL,
    amps DOUBLE(4,1) NOT NULL,
    volts DOUBLE(4,1) NOT NULL,
    cpu_usage DOUBLE(3,1) NOT NULL,
    mem_usage DOUBLE(3,1) NOT NULL,
    io_usage DOUBLE(3,1) NOT NULL,
    machine_id INT NOT NULL,
    FOREIGN KEY (machine_id) REFERENCES machines(id)
    );'''

tables[3] = '''CREATE TABLE IF NOT EXISTS instances (
    id INT PRIMARY KEY AUTO_INCREMENT,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    machine_id INT NOT NULL,
    FOREIGN KEY (machine_id) REFERENCES machines(id)
    );'''

tables[4] = '''CREATE TABLE IF NOT EXISTS benchmark_relation (
    id INT PRIMARY KEY AUTO_INCREMENT,
    instance_id INT NOT NULL,
    benchmark_id INT NOT NULL,
    FOREIGN KEY (instance_id) REFERENCES instances(id),
    FOREIGN KEY (benchmark_id) REFERENCES benchmarks(id)
    );'''

   db_host = os.getenv('DB_HOST')
   db_user = os.getenv('DB_USERNAME')
   db_pass = os.getenv('DB_PASS')
   db_name = os.getenv('DB_NAME')
try:
    con = mdb.connect(db_host, db_user, db_pass, db_name)
    cur = con.cursor()
    for t in xrange(len(tables)):
        try:
            cur.execute(tables[t])
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
    con.commit()

except mdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

finally:
     if con:
        con.close()
