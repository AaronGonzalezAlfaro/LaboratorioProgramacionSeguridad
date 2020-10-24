#!/bin/bash

ip address
hostname -I

curl ifconfig.me

nmap -Pn --script vuln 10.0.2.15
nmap -Pn --script default 189.153.37.133
