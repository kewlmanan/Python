#! /usr/bin/env/python

''' Problem Statment 
A log file contains data like :

IP1 drops 10 packets
IP2 drops 2 packets
IP1 drops 2 packets
....

Output log :

IP1 drops 12 packets
IP2 drops 2 packets 
....
'''

import os,re,sys

fp=open("log","r")

ip_pkt={}
for line in fp.readlines():
    m=re.search('((\d{1,3}\.){3}\d{1,3}) drops (\d*)',line)
    if m:
        if m.group(1) in ip_pkt:
            ip_pkt[m.group(1)]=int(ip_pkt[m.group(1)])+int(m.group(3))
        else:
            ip_pkt[m.group(1)]=int(m.group(3))
            
fp.close()

fp=open("output","w")

for key in sorted(ip_pkt.keys()):
    text=key+' drops total '+ str(ip_pkt[key])+' packets\n'
    fp.write(text)

fp.close()
