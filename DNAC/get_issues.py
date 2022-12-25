import requests
from dnac_login import get_token

status_code, token = get_token()

# print(token)

def get_issues(token):
    headers = {
        'Content-Type': 'application/json',
        'x-auth-token': token
    }
    url = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/issues'

    response = requests.get(url=url,headers=headers,verify=False)
    return response.status_code, response.json()

if __name__ == '__main__':
    status_code, issues = get_issues(token=token)
    print(status_code)
    print(issues)

