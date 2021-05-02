#!/usr/bin/python3
#Created by Cristian B.
import sys
import pyfiglet
import socket
from IPy import IP
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[ Scanning Target ] ' + str(target))
#Port and socket configuration
    for port in range (1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)
def get_banner(s):
    return s.recv(1024)

#Banner for timer
print("-" * 50)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)

def scan_port(ipaddress, port):
    try:
         sock = socket.socket()
         sock.settimeout(0.5)
         sock.connect((ipaddress, port))
         try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
         except:
             print('[+] Open Port ' + str(port))
    except:
         pass

if __name__ == "__main__":
    targets = input('[+] Enter target/s to scan: (Split multiple target with "," ): ')
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
         scan(targets)