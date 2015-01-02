#!/bin/bash

cp EnergyFetch.py /usr/bin/EnergyFetch

chmod 755 /usr/bin/EnergyFetch

cp daemons/energy-monitor.conf /etc/init/energy-monitor.conf

chmod 644 /etc/init/energy-monitor.conf
