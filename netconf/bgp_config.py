from ncclient import manager
from connection_info import *
from get_loopback_IP import *



config = ''' 
    <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router>
          <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp">
            <id>11111</id>
            <address-family>
              <no-vrf>
                <ipv4>
                <af-name>unicast</af-name>
                  <ipv4-unicast>
                    <network>
                      <with-mask>
                        <number>{network}</number>
                        <mask>{mask}</mask>
                      </with-mask>
                    </network>
                  </ipv4-unicast>
                </ipv4>
              </no-vrf>
            </address-family>
          </bgp>
        </router>
      </native>
    </config>
'''
def get_bgp_instance():
    pass


def bgp_config(config):

  with manager.connect(**R1) as m:
    if m.connected:
        m.edit_config(config, target='running')
    

if __name__ == '__main__':
    with manager.connect(**R1) as m:
        list_interfaces = retrieve_list_of_loopback_interfaces(m)
        network, mask = get_ip(m,list_interfaces)
        print(network + mask)
    print('Now adding the loopback network to BGP')
    bgp_config(config=config.format(network=network,mask=mask))