#!/bin/bash
LOGFILE=/dev/null #/home/pi/switch_handler/on_log
date  >>$LOGFILE
sudo killall dhcpcd >>$LOGFILE
sudo ifconfig eth0 inet 10.0.95.99 >>$LOGFILE
sudo /usr/sbin/udhcpd >>$LOGFILE

