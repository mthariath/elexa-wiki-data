#!/usr/bin/env python
################################################################################
#                               _______                                        #
#                              /_______\                                       #
#                      _____     _____   _______   _____                       #
#                     | ___ \   / ___ \ /  _ _  \ / ___ \                      #
#                     | |  \ \ | /   \ || || || |/ /   / |                     #
#                     |_|   | || |   | || || || || |  (_/                      #
#                      ____/ / | \___/ || || || |\ \_____                      #
#                     |_____/   \_____/ |_||_||_| \______\                     #
#                                                                              #
################################################################################
#        File: MAC-HAMMER                                                      #
#      Author: MICHAEL SKIBA                                                   #
#        Date: 04-12-2018                                                      #
# Description: PRINTS IP AND MAC ADDRESS OF DEVICES ON SUBNET                  #
################################################################################
# Version 0.0.1  - First try
#
################################################################################
# Make an EXE:
# pyinstaller --onefile --icon=gicon.ico --name=MACHammer machammer.py

import ctypes
import socket
import struct
import threading
from time import sleep

def get_macaddress(host):
    """ Returns the MAC address of a network host, requires >= WIN2K. """
    
    # Check for api availability
    try:
        SendARP = ctypes.windll.Iphlpapi.SendARP
    except:
        raise NotImplementedError('Usage only on Windows 2000 and above')
        
    # Doesn't work with loopbacks, but let's try and help.
    if host == '127.0.0.1' or host.lower() == 'localhost':
        host = socket.gethostname()
    
    # gethostbyname blocks, so use it wisely.
    try:
        inetaddr = ctypes.windll.wsock32.inet_addr(host)
        if inetaddr in (0, -1):
            raise Exception
    except:
        hostip = socket.gethostbyname(host)
        inetaddr = ctypes.windll.wsock32.inet_addr(hostip)
    
    buffer = ctypes.c_buffer(6)
    addlen = ctypes.c_ulong(ctypes.sizeof(buffer))
    if SendARP(inetaddr, 0, ctypes.byref(buffer), ctypes.byref(addlen)) != 0:
        raise WindowsError('Retreival of mac address(%s) - failed' % host)
    
    # Convert binary data into a string.
    macaddr = ''
    for intval in struct.unpack('BBBBBB', buffer):
        if intval > 15:
            replacestr = '0x'
        else:
            replacestr = 'x'
        macaddr = ''.join([macaddr, hex(intval).replace(replacestr, '')])
    
    return macaddr.upper()
results = []
def arpanet(iptry, j):
    try:
        macaddy = get_macaddress(iptry)
        #print str(iptry) + ' = ' + str(macaddy) 
        result = str(iptry) + ' = ' + str(macaddy) 
        results.append(result)
        sleep(1)
    except WindowsError:
        pass
    
if __name__ == '__main__':
    goodip = str(socket.gethostbyname(socket.gethostname()))
    print 'Your IP address is ' + goodip
    print 'Your mac address is %s' % get_macaddress('localhost')
    subnettemp = goodip
    subnetsplit = subnettemp.split('.')
    subnet = subnetsplit[0]+'.'+subnetsplit[1]+'.'+subnetsplit[2]+'.'
    ipaddy = subnet
    threads = []
    for j in range(1,255):
        newguy = ipaddy + str(j)
        try:
            g = threading.Thread(target = arpanet, args = (newguy, j))
            threads.append(g)
            g.start()
            if j == 254:
                for threadz in threads:
                    threadz.join()
        except WindowsError:
            pass
    #g.join()
    for i in results:
        print i
    raw_input("Press Enter when you're done looking at this stuff")