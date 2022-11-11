from IOSXE import *


iosxe = IOSXE()

# native YANG
# uri = 'Cisco-IOS-XE-native:native/version'

# IETF YANG
uri = 'Cisco-IOS-XE-native:native/router/router-eigrp/eigrp/classic-mode'

response = iosxe.get_data(uri)

print(response.text)