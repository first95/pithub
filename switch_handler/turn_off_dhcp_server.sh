#!/bin/bash
LOGFILE=/dev/null #/home/pi/switch_handler/off_log
date  >>$LOGFILE
sudo killall udhcpd >>$LOGFILE
sudo /sbin/dhcpcd -q -b >>$LOGFILE
sudo /sbin/dhcpd eth0 >>$LOGFILE
ifconfig  >>$LOGFILE
