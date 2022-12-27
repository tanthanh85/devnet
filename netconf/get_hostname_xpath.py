from ncclient import manager
from connection_info import *
import xmltodict

# filter = '''
# <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
#         <hostname/>
#       </native>
# '''
xpath_filter = "/native/hostname"
try: 
    with manager.connect(**R1) as m1:
        reply = m1.get(('xpath',xpath_filter))
    hostname_dict = xmltodict.parse(reply.xml)
    print(hostname_dict['rpc-reply']['data']['native']['hostname'])
    # print(reply.xml)

except:
    print('something went wrong')