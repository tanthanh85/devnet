import requests
from dnac_login import get_token
from prettytable import PrettyTable

table = PrettyTable()

status_code, token = get_token()

site_id = '9e5f9fc2-032e-45e8-994c-4a00629648e8'

def get_site_membership(token):
    headers = {
        'Content-Type': 'application/json',
        'x-auth-token': token
    }
    url = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/membership/{site_id}'.format(site_id=site_id)

    response = requests.get(url=url,headers=headers,verify=False)
    return response.status_code, response.json()['device']

if __name__ == '__main__':
    status_code, members = get_site_membership(token=token)
    # table.field_names = ['Site\'s ID', 'Site\'s name']
    # for site in sites:
    #     table.add_row([site['id'], site['name']])

    # print(table)

    print(members)
    
