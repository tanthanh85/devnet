import requests
import os

token = os.getenv("ACI_TOKEN")

tenant_name = "Tenant_Andy"

headers = {"Cookie": f"APIC-Cookie={token}"}

payload = {
    "fvCtx": {
        "attributes": {
            "dn": "uni/tn-Tenant_Andy/ctx-UAT",
            "name": "UAT",
            "rn": "ctx-UAT",
            "status": "created",
        }
    }
}

url = "https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-Tenant_Andy/ctx-UAT.json"


def create_vrfs():
    response = requests.post(url=url, headers=headers, json=payload, verify=False)
    return response.json()


if __name__ == "__main__":
    response = create_vrfs()
    # print(response)
    if response["imdata"][0]["error"]["attributes"]["code"] == "103":
        print("object uni\/tn-Tenant_Andy\/ctx-UAT already exists.")
