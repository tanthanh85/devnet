from ncclient import manager
from connection_info import *
import xmltodict

  
def get_ip(m, list_interfaces):
  loopback_number = input("what is the loopback interface?: ")
  if loopback_number in list_interfaces:
    xpath_filter = f"/native/interface/Loopback[name={loopback_number}]/ip/address/primary"
    lo = m.get(('xpath',xpath_filter))
    print(lo.xml)
    lo_dict = xmltodict.parse(lo.xml)
    print(lo_dict)
    print(f"here is the IP address and subnet mask of interface loopback{loopback_number}")
    print(lo_dict['rpc-reply']['data']['native']['interface']['Loopback']['ip']['address']['primary']['address'])
    print(lo_dict['rpc-reply']['data']['native']['interface']['Loopback']['ip']['address']['primary']['mask'])
    return lo_dict['rpc-reply']['data']['native']['interface']['Loopback']['ip']['address']['primary']['address'], lo_dict['rpc-reply']['data']['native']['interface']['Loopback']['ip']['address']['primary']['mask']
  else:
    print("invalid input")

def retrieve_list_of_loopback_interfaces(m):
  xpath_filter = "/native/interface/Loopback/name"
  interface_list = m.get(('xpath',xpath_filter))
  interface_dict = xmltodict.parse(interface_list.xml)
  loopback_list = []
  for interface in interface_dict['rpc-reply']['data']['native']['interface']['Loopback']:
    # print(interface['name'])
    loopback_list.append(interface['name'])
  return loopback_list


if __name__ == '__main__':

  with manager.connect(**R1) as m:
    print(m.connected)
    print("here are the available loopback interfaces on R1: ")
    list_interfaces = retrieve_list_of_loopback_interfaces(m)
    for number in list_interfaces:
      print(number)
    get_ip(m,list_interfaces)

