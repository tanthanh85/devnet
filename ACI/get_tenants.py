import os
import requests
token = os.getenv("ACI_TOKEN")

print(token)

headers = {"Cookie": f"APIC-Cookie={token}"}

url = "https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json"


"curl -H Cookie:APIC-Cookie=$ACI_TOKEN https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json"

def get_tenants():
    response = requests.get(url=url, headers=headers, verify=False)
    return response.status_code, response.json()["imdata"]


if __name__ == "__main__":
    status_code, tenants = get_tenants()
    
    for tenant in tenants:
        print(tenant["fvTenant"]["attributes"]["name"])
