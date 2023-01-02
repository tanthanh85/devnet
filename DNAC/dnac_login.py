import requests
import urllib3
urllib3.disable_warnings()


headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='   
}
url = 'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token'


# echo -n "devnetuser:Cisco123!" | base64   >>>>> this for preventing echo to add a new line
# curl -s -X POST \
# https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token \
# -H "Authorization: Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE="


def get_token():
    # response = requests.post(url=url,headers=headers,auth=('devnetuser','Cisco123!'),verify=False)
    response = requests.post(url=url,headers=headers,verify=False)

    return response.status_code,response.json()['Token']

if __name__ == '__main__':
    status_code, token = get_token()
    print('Status code is ' + str(status_code))
    print('Token is ' + token)