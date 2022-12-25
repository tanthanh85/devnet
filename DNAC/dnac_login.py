import requests
import urllib3
urllib3.disable_warnings()


headers = {
    'Content-Type': 'application/json'   
}
url = 'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token'

def get_token():
    response = requests.post(url=url,headers=headers,auth=('devnetuser','Cisco123!'),verify=False)
    return response.status_code,response.json()['Token']

if __name__ == '__main__':
    status_code, token = get_token()
    print('Status code is ' + str(status_code))
    print('Token is ' + token)