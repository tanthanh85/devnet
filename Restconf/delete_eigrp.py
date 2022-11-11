from IOSXE import IOSXE

ios = IOSXE()


uri = "Cisco-IOS-XE-native:native/router/router-eigrp/eigrp/classic-mode=12334"



response = ios.delete_data(uri=uri)

print(response)
