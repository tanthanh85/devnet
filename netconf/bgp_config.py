from ncclient import manager
from connection_info import *
from get_loopback_IP import *
import xmltodict



config = ''' 
    <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router>
          <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp">
            <id>{id}</id>
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

filter = '''
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router>
          <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp">
            <id/>
          </bgp>
        </router>
</native>
'''

def get_bgp_instance(m): 
    if m.connected: 
        reply = m.get(('subtree', filter))
        reply_dict = xmltodict.parse(reply.xml)
        return reply_dict['rpc-reply']['data']['native']['router']['bgp']['id']
    
def bgp_config(config,m):
    if m.connected:
        m.edit_config(config, target='running')
    
if __name__ == '__main__':
    with manager.connect(**R1) as m:
        id = get_bgp_instance(m)
        list_interfaces = retrieve_list_of_loopback_interfaces(m)
        network, mask = get_ip(m,list_interfaces)
        print('adding the loopback network to BGP now...')
        if id:
            bgp_config(config=config.format(network=network,mask=mask,id=id),m=m)
        
   