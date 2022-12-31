from aci_login import get_token
import requests

token = get_token()

tenant_name = "Tenant_Andy"

headers = {
    'Cookie': f'APIC-Cookie={token}'
}

payload = {"fvCtx":{"attributes":{"dn":"uni/tn-Tenant_Andy/ctx-UAT","name":"UAT","rn":"ctx-UAT","status":"created"}}}

url = "https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-Tenant_Andy/ctx-UAT.json"

def create_vrfs():
    response = requests.post(url=url,headers=headers,json=payload,verify=False)
    return response.status_code

if __name__ == '__main__':
    status_code = create_vrfs()
    print(status_code)