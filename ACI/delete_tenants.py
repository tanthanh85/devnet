import os
import requests


token = os.getenv("ACI_TOKEN")

tenant_name = "Tenant_Andy"

headers = {"Cookie": f"APIC-Cookie={token}"}

payload = {"fvTenant": {"attributes": {"name": tenant_name, "status": "deleted"}}}

url = "https://sandboxapicdc.cisco.com/api/mo/uni.json"


def delete_tenants():
    response = requests.post(url=url, headers=headers, json=payload, verify=False)
    return response.status_code


if __name__ == "__main__":
    status_code = delete_tenants()
    print(status_code)
