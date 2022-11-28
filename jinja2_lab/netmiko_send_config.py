from connection_info import *
from netmiko import ConnectHandler

for device in connection_info:
    with ConnectHandler(**connection_info[device]) as conn:
        conn.send_config_from_file('{device}_bgp_config.txt'.format(device=device))
  

