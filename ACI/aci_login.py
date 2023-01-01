import requests
import json
import urllib3
import os

urllib3.disable_warnings()

headers = {"content-type": "application/json"}

payload = {"aaaUser": {"attributes": {"name": "admin", "pwd": "!v3G@!4@Y"}}}

url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"


def get_token():
    response = requests.post(
        url=url, headers=headers, data=json.dumps(payload), verify=False
    )
    return response.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]


if __name__ == "__main__":
    token = get_token()
    # print(token)
    os.environ["ACI_TOKEN"] = token
    print("\n")
    print(f"export ACI_TOKEN={token}\n")
