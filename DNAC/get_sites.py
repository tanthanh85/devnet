import requests
from dnac_login import get_token
from prettytable import PrettyTable

table = PrettyTable()

status_code, token = get_token()


def get_sites(token):
    headers = {
        'Content-Type': 'application/json',
        'x-auth-token': token
    }
    
    # export token=$(curl -s -X POST https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token -H "Authorization: Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE=" | jq -r .Token)
    # export dnac_headers=x-auth-token:$token
    # curl -H $dnac_headers https://sandboxdnac2.cisco.com/dna/intent/api/v1/site
    url = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/site'

    response = requests.get(url=url,headers=headers,verify=False)
    return response.status_code, response.json()['response']

if __name__ == '__main__':
    status_code, sites = get_sites(token=token)
    table.field_names = ['Site\'s ID', 'Site\'s name']
    for site in sites:
        table.add_row([site['id'], site['name']])

    print(table)
    
