

import hvac
from hvac.exceptions import InvalidPath
import urllib3
urllib3.disable_warnings()

VAULT_ADDRESS = 'https://192.168.50.27:8200'
VAULT_TOKEN = 'hvs.gbTTZLMI0canwYJpsKtN8bLR'
try:
    client = hvac.Client(url=VAULT_ADDRESS,token=VAULT_TOKEN,verify=False)
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