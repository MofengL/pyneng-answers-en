# -*- coding: utf-8 -*-
"""
Task 18.2

Create send_config_commands function

The function connects via SSH (using netmiko) to ONE device and executes
a list of commands in configuration mode based on the passed arguments.

Function parameters:
* device - a dictionary with parameters for connecting to a device
* config_commands - list of configuration commands to be executed

The function should return a string with the results of the command:

In [7]: r1
Out[7]:
{'device_type': 'cisco_ios',
 'ip': '192.168.100.1',
 'username': 'cisco',
 'password': 'cisco',
 'secret': 'cisco'}

In [8]: commands
Out[8]: ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']

In [9]: result = send_config_commands(r1, commands)

In [10]: result
Out[10]: 'config term
Enter configuration commands, one per line.  End with CNTL/Z.
         
R1(config)#logging 10.255.255.1
R1(config)#logging buffered 20010

         R1(config)#no logging console
R1(config)#end
R1#'

In [11]: print(result)
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 10.255.255.1
R1(config)#logging buffered 20010
R1(config)#no logging console
R1(config)#end
R1#

The script should send command command to all devices from the devices.yaml file
using the send_config_commands function.
"""
from netmiko import ConnectHandler
import yaml


commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]


def send_config_commands(device, config_commands):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(config_commands)
    return result


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_config_commands(dev, commands))
