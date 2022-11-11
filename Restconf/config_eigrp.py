from IOSXE import IOSXE

ios = IOSXE()


uri = 'Cisco-IOS-XE-native:native/router/router-eigrp/eigrp/classic-mode'

payload = {
  "Cisco-IOS-XE-eigrp:classic-mode": [
    {
      "autonomous-system": 12345,
      "network": {
        "address": [
          {
            "ipv4-address": "192.168.12.0"
          }
        ]
      }
    }
  ]
}

response = ios.patch_data(uri=uri,payload=payload)

print(response)
