import os
import requests
import urllib3
urllib3.disable_warnings()


token = os.getenv("ACI_TOKEN")

TENANT_NAME = "Tenant_Andy"

headers = {"Cookie": f"APIC-Cookie={token}"}

payload = {"fvTenant": {"attributes": {"name": TENANT_NAME}}}

# payload = {"fvTenant": {"attributes": {"name": "Nicky"}}}

URL = "https://sandboxapicdc.cisco.com/api/mo/uni.json"

# curl -X POST -H Cookie:APIC-Cookie=$ACI_TOKEN -d '{"fvTenant": {"attributes": {"name": "Kevin"}}}' https://sandboxapicdc.cisco.com/api/mo/uni.json

def create_tenants():
    response = requests.post(
        url=URL, headers=headers, json=payload, verify=False, timeout=15
    )
    return response.status_code


if __name__ == "__main__":
    status_code = create_tenants()
    print(status_code)
