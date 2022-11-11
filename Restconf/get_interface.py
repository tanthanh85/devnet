from IOSXE import *


iosxe = IOSXE()

# native YANG
# uri = 'Cisco-IOS-XE-native:native/version'

# IETF YANG
uri = 'ietf-interfaces:interfaces'

response = iosxe.get_data(uri)

print(type(response))
