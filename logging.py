#!/usr/bin/env python
# -*- coding: utf-8 -*-
import netmiko
from getpass import getpass

class logging:
    ## define some class variables
    __ipaddr = ""
    __protocol = ""
    __software = ""
    __hostname = ""
    __port = ""
    __username = ""
    __password = ""
    __secret = ""
    __dev = {}
    __session

    def __init__(self,ipddr,protocol,software,hostname=None,port=23,username=None,password=None,secret=None):
        self.__ipaddr = ipaddr
        self.__protocol = protocol
        self.__software = software
        self.__hostname = hostname
        self.__port = port
        self.__username = username
        self.__password = password
        self.__secret = secret
        self.__dev = self.__setdev()

    def __del__(self):
        try:
            self.__session.close_session_log()
            self.__session.disconnect()
            print("Session was disconnected.")
        except:
            print("No session was created.")

    def __dev(self,ipaddr,protocol,software,port,username,password,secret):
        dev = {}
        devtype = __settype(protocol,software)
        devinfo = {
            "device_type": devtype,
            "ip": ipaddr,
            "port": port,
            'username': username
            "password": password,
            "secret": secret,
        }
        return devinfo

    def __settype(self,protocol,software):
        dev_type = ""
        if software == "ios" and protocol == "telnet":
            dev_type = "cisco_ios_telnet"
        if software == "ios" and protocol == "ssh":
            dev_type = "cisco_ios_telnet"
        return dev_type

    def FUNC(self,var):
        return var

## The process if this was inplemented directly
if __name__ == '__main__':
    print("Implemented directly")
