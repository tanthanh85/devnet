from IOSXE import *


iosxe = IOSXE()

# native YANG
# uri = 'Cisco-IOS-XE-native:native/version'

# IETF YANG
uri = 'ietf-interfaces:interfaces'

response = iosxe.get_data(uri)
for interface in response.json()['ietf-interfaces:interfaces']['interface']:
    if interface['ietf-ip:ipv4']:
        for ip in interface['ietf-ip:ipv4']['address']:
            print(interface['name'] + ' has an IP address ' + ip['ip'])
    else:
        print(interface['name'] + ' does not have an IP address')
