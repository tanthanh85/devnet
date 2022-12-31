from aci_login import get_token
import requests

token = get_token()

tenant_name = "Tenant_Andy"

headers = {
    'Cookie': f'APIC-Cookie={token}'
}

payload = {
    "fvTenant": {
        "attributes": {
        "name": tenant_name
        }
    }
}

url = "https://sandboxapicdc.cisco.com/api/mo/uni.json"

def create_tenants():
    response = requests.post(url=url,headers=headers,json=payload,verify=False)
    return response.status_code

if __name__ == '__main__':
    status_code = create_tenants()
    print(status_code)