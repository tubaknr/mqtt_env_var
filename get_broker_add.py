#!/usr/bin/env python3
import subprocess

def get_local_broker_info():
    cmd = ("netstat -tuln | grep '1883\|8883'")
    output = subprocess.check_output(cmd, shell=True).decode("utf-8")
    lines = output.strip().split("\n")
    if len(lines) > 0:
        address_port = lines[0].split()[3]
        address, port = address_port.split(":")
        return address, int(port)
    else:
        return None, None

# Get the local broker address and port
broker_address, broker_port = get_local_broker_info()
print("address:",broker_address) #0.0.0.0
print("port:",broker_port) #1883
print("type of address:",type(broker_address))
