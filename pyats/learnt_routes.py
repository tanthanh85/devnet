from genie.testbed import load
from pyats.topology.loader import load as load_tb
from pyats import aetest


tb = load_tb("testbed.yaml")

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def load_testbed(self,testbed):
        testbed = load(tb)       
        self.parent.parameters.update(testbed=testbed)
    @aetest.subsection
    def connect_to_devices(self,testbed):
        testbed.connect()

class CheckRoutes(aetest.Testcase):
    @aetest.setup
    def Learn_Routes(self,testbed):
        self.learnt_ip_routes = {}
        for device_name,device in testbed.devices.items():
            self.learnt_ip_routes[device_name] = device.learn('routing')
    @aetest.test
    def Count_Routes(self,steps):
        self.connected_routes = {}
        self.ospf_routes = {}
        self.bgp_routes = {}
        
        for device_name, details in self.learnt_ip_routes.items():
            connected_route_list = {}
            ospf_route_list = {}
            bgp_route_list = {}
            ospf_count = 0
            connected_count = 0
            bgp_count = 0
            routes = details.to_dict()['info']['vrf']['default']['address_family']['ipv4']['routes']
            with steps.start(f'Counting the no of routes for {device_name}', continue_=True) as device_step:
                for prefix in routes:
                    if routes[prefix]['source_protocol'] == 'connected':
                        connected_route_list[routes[prefix]['route']] = routes[prefix]['next_hop']
                        connected_count +=1
                    if routes[prefix]['source_protocol'] == 'ospf':
                        ospf_route_list[routes[prefix]['route']] = routes[prefix]['next_hop']
                        ospf_count +=1
                    if routes[prefix]['source_protocol'] == 'bgp':
                        bgp_route_list[routes[prefix]['route']] = routes[prefix]['next_hop']
                        bgp_count +=1
                if device_name == 'R1':
                    if connected_count == 12:
                        device_step.passed('no change in the number of routes on {device_name}'.format(device_name=device_name))
                    else:
                        device_step.failed('the no of Connected routes changed from 12 to {count}'.format(count=connected_count))  
                    if ospf_count == 1:
                        device_step.passed('no change in the number of routes on {device_name}'.format(device_name=device_name))
                    else:
                        device_step.failed('the no of OSPF routes changed from 1 to {count}'.format(count=ospf_count))   
                    if bgp_count == 1:
                        device_step.passed('no change in the number of routes on {device_name}'.format(device_name=device_name))
                    else:
                        device_step.failed('the no of BGP routes changed from 1 to {count}'.format(count=bgp_count))    

                if device_name == 'R2':
                    if connected_count == 5:
                        device_step.passed('no change in the number of routes on {device_name}'.format(device_name=device_name))
                    else:
                        device_step.failed('the no of Connected routes changed from 5 to {count}'.format(count=connected_count))  
                    if ospf_count == 2:
                        device_step.passed('no change in the number of routes on {device_name}'.format(device_name=device_name))
                    else:
                        device_step.failed('the no of OSPF routes changed from 1 to {count}'.format(count=ospf_count))   
                    if bgp_count == 1:
                        device_step.passed('no change in the number of routes on {device_name}'.format(device_name=device_name))
                    else:
                        device_step.failed('the no of BGP routes changed from 1 to {count}'.format(count=bgp_count))      

            self.connected_routes['{device_name} has total {count} connected routes'.format(device_name=device_name, count=connected_count)] = connected_route_list
            self.ospf_routes['{device_name} has total {count} OSPF routes'.format(device_name=device_name, count=ospf_count)] = ospf_route_list            
            self.bgp_routes['{device_name} has total {count} BGP routes'.format(device_name=device_name, count=bgp_count)] = bgp_route_list        
                    
        with open('connected_routes.json', 'w') as f:
            f.write(str(self.connected_routes))
        with open('ospf_routes.json', 'w') as f:
            f.write(str(self.ospf_routes))
        with open('bgp_routes.json', 'w') as f:
            f.write(str(self.bgp_routes))

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect(self,testbed):
        testbed.disconnect()

if __name__ == '__main__':
    aetest.main(testbed=tb)

