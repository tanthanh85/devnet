import requests
from dnac_login import get_token
import json
import time

status_code, token = get_token()

data = {
    "destIP": "10.10.20.166", 
    "sourceIP": "10.10.20.163"
}

def post_pathtrace(token):
    headers = {
        'Content-Type': 'application/json',
        'x-auth-token': token
    }
    url = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/flow-analysis'

    response = requests.post(url=url,headers=headers,data=json.dumps(data),verify=False)
    # response = requests.post(url=url,headers=headers,json=data,verify=False)
    return response.status_code, response.json()['response']['flowAnalysisId']

def get_flow_details(token,flow_id):
    headers = {
        'Content-Type': 'application/json',
        'x-auth-token': token
    }
    url = f'https://sandboxdnac2.cisco.com/dna/intent/api/v1/flow-analysis/{flow_id}'
    response = requests.get(url=url,headers=headers,verify=False)
    return response.json()['response']['request']['status']

if __name__ == '__main__':
    status_code, flow_id = post_pathtrace(token=token)
    print(flow_id)
    time.sleep(5)
    print(status_code)
    if status_code == 202:
        print(get_flow_details(token=token,flow_id=flow_id))

    