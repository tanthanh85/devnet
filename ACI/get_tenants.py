from aci_login import get_token
import requests

token = get_token()

headers = {
    'Cookie': f'APIC-Cookie={token}'
}

url = "https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json"

def get_tenants():
    response = requests.get(url=url,headers=headers,verify=False)
    return response.json()['imdata']

if __name__ == '__main__':
    tenants = get_tenants()
    for tenant in tenants:
        print(tenant['fvTenant']['attributes']['name'])