from IOSXE import IOSXE

ios = IOSXE()


uri = 'Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:router-ospf/ospf/process-id'

payload = {
  "Cisco-IOS-XE-ospf:process-id": [
    {
      "id": 1,
      "router-id": "1.1.1.1"
    }
  ]
}


response = ios.patch_data(uri=uri,payload=payload)

payload = {
  "Cisco-IOS-XE-ospf:process-id": [
    {
      "id": 1,
      "area": [
        {
          "area-id": 0
        }
      ]
    }
  ]
}

uri = 'Cisco-IOS-XE-native:native/interface/GigabitEthernet=1/ip/Cisco-IOS-XE-ospf:router-ospf/ospf/process-id'

response = ios.patch_data(uri=uri,payload=payload)

print(type(response))
