

import hvac
from hvac.exceptions import *
import urllib3
urllib3.disable_warnings()
from requests.exceptions import SSLError
import os

VAULT_ADDRESS = 'https://vault.example.com:8200'
VAULT_TOKEN = 'hvs.rjvceBBfSDK19HKi4D08eiwo'
try:
    os.environ['REQUESTS_CA_BUNDLE'] = '/Users/thandoan/devnet/jinja2_lab/ca.cert'
    
    client = hvac.Client(url=VAULT_ADDRESS,token=VAULT_TOKEN,cert=('jinja2_lab/client.cert','jinja2_lab/client.key'))
    rs = client.session
    rs.verify='/Users/thandoan/devnet/jinja2_lab/server.cert'

    if client.is_authenticated():
        print('successfully authenticated to Vault server')
        print("getting R1's login information from Vault server")
        R1 = client.secrets.kv.v2.read_secret_version(mount_point='kv',path='R1')
        print("getting R2's login information from Vault server")
        R2 = client.secrets.kv.v2.read_secret_version(mount_point='kv',path='R2')
        
    else:
        print('authentication failed to Vault server')


except InvalidPath as e:
    print(e)

except SSLError as e:
  print(e)

connection_info = {

    'R1': {

      'device_type': R1['data']['data']['device_type'],

      'host': R1['data']['data']['host'],

      'port': R1['data']['data']['port'],

      'username': R1['data']['data']['username'],

      'password': R1['data']['data']['password']
    },
    'R2': {

      'device_type': R2['data']['data']['device_type'],

      'host': R2['data']['data']['host'],

      'port': R2['data']['data']['port'],

      'username': R2['data']['data']['username'],

      'password': R2['data']['data']['password']
    }


}

if __name__ == '__main__':
  print(connection_info)