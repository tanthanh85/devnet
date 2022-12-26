import requests
import urllib3
urllib3.disable_warnings()


headers = {
    'Accept': 'application/yang-data+xml',
}

def nso_get_all():
    url = 'https://sandbox-nso-1.cisco.com/restconf/data/ietf-restconf-monitoring:restconf-state'
    response = requests.get(url=url,headers=headers,auth=('developer','Services4Ever'),verify=False)
    return response.status_code, response.text

if __name__ == '__main__':
    code, response = nso_get_all()

    print(code)
    print(response)