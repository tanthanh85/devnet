from IOSXE import *


iosxe = IOSXE()

# native YANG
# uri = 'Cisco-IOS-XE-native:native/version'

# IETF YANG
uri = 'Cisco-IOS-XE-native:native/interface/GigabitEthernet=1/ip/Cisco-IOS-XE-ospf:router-ospf/ospf/process-id'

response = iosxe.get_data(uri)

print(type(response.json()))