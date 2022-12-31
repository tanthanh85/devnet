import requests
import json

headers = {
    'content-type': 'application/json'
}


command = 'show ip int bri'

# This payload is from NXAPI sandbox
payload = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": command,
    "output_format": "json"
  }
}

url = 'http://192.168.50.63/ins'

response = requests.post(url=url,headers=headers,auth=('admin','cisco'),data=json.dumps(payload))

print(response.json())