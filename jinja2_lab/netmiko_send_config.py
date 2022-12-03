from connection_info import *
from netmiko import ConnectHandler


for device,details in connection_info.items():
    print('sending BGP configuration to ' + details['host'])

    with ConnectHandler(**details) as conn:
        conn.send_config_from_file('{device}_bgp_config.txt'.format(device=device))
  

