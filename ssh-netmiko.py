#!/usr/bin/env python
from netmiko import SSHDetect, Netmiko
import datetime
import sys
import getpass

args = sys.argv

if len(args) >= 2:
    password = getpass.getpass()
    device = {
        "device_type": "linux",
        "host": args[1],
        "username": args[2],
        "password": password,
    }
else:
    host = input("hosname or ip: ")
    username = input("username: ")
    password = getpass.getpass()
    device = {
        "device_type": "linux",
        "host": host,
        "username": username,
        "password": password,
    }

connection = Netmiko(**device)
path = '/Users/tak/work/logs/' + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + "_TeamKujira.txt"
log = []
while(True):
        cmd = input(connection.find_prompt() + " ")
        log.append("[" + datetime.datetime.now().strftime("%a %b %d %H:%M:%S.%f %Y") + "] " + connection.find_prompt() + " " + cmd)
        if cmd == "endssh":
            break
        if cmd == "exit" and device.get("username") in connection.find_prompt():
            break
        elif "sudo" or "su" in cmd:
            output = connection.send_command_timing(cmd)
            if "Password:" in output:
                output += connection.send_command_timing(
                    device.get("password"), strip_prompt=False, strip_command=False
                )
            print(output)
            lines = output.splitlines()
            for line in lines:
                log.append("[" + datetime.datetime.now().strftime("%a %b %d %H:%M:%S.%f %Y") + "] " + line)
        else:
            output = connection.send_command(cmd)
            print(output)
            lines = output.splitlines()
            for line in lines:
                log.append("[" + datetime.datetime.now().strftime("%a %b %d %H:%M:%S.%f %Y") + "] " + line)
with open(path,mode='w') as f:
    f.write("\n".join(log))
connection.disconnect()
