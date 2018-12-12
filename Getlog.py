from netmiko import ConnectHandler

for i in range (32769,32780):
    cisco = {
        "device_type": "cisco_ios_telnet",
        "ip": "192.168.100.21",
        "port": str(i)
    }
    if i - 32768 >= 11:
        log = open("SW" + str(i -32768) + ".txt", 'wb')
    else:
        log = open("R" + str(i -32768) + ".txt", 'wb')
    net_connect = ConnectHandler(**cisco)
    net_connect.enable()
    
    #net_connect.send_command("en")
    net_connect.send_command("ter len 0")
    output = net_connect.send_command("show run")
    print(output)
    log.write(output.encode("UTF-8"))
    log.close()
    net_connect.disconnect()
