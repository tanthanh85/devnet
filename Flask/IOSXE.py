import requests
import json
import urllib3


urllib3.disable_warnings()

class IOSXE:
    def __init__(self):
        self.username = 'admin'
        self.password = 'cisco'
        self.headers = {
            'Accept': 'application/yang-data+json',
            'Content-Type': 'application/yang-data+json',
            }
        self.base_url = 'https://192.168.50.61/restconf/data/'

    def get_data(self,uri):
        response = requests.get(url=self.base_url+uri, auth=(self.username, self.password), headers=self.headers, verify=False)
        return(response)
   
    def post_data(self,uri,payload):
        response = requests.post(url=self.base_url+uri, auth=(self.username, self.password), headers=self.headers, data=json.dumps(payload),verify=False)
        return response.status_code

    def patch_data(self,uri,payload):
        response = requests.patch(url=self.base_url+uri, auth=(self.username, self.password), headers=self.headers, data=json.dumps(payload),verify=False)
        return response.status_code

    def delete_data(self,uri):
        response = requests.delete(url=self.base_url+uri, auth=(self.username, self.password), headers=self.headers,verify=False)
        return response.status_code
    def put_data(self,uri,payload):
        response = requests.put(url=self.base_url+uri, auth=(self.username, self.password), headers=self.headers, data=json.dumps(payload),verify=False)
        return response.status_code

    

if __name__ == '__main__':
    # response = get_data(uri='Cisco-IOS-XE-native:native')
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

    
