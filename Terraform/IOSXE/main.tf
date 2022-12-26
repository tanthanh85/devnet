terraform {
  required_providers {
    iosxe = {
      source  = "registry.terraform.io/ciscodevnet/iosxe"
    }
  }
} 

provider "iosxe" {
  host = "https://192.168.50.61"
  device_username = "admin"
  device_password = "cisco"
  insecure = true
  request_timeout = 30
}

# resource "iosxe_rest" "getall" {
#   method = "GET"
#   path = "/data/ietf-interfaces:interfaces"
#   payload = ""
# }

# data "iosxe_rest" "example" {
#   path = "/data/ietf-interfaces:interfaces"
# }

# output "test" {
#   value = resource.iosxe_rest.getall
# }

resource "iosxe_rest" "config_eigrp" {
  method = "PATCH"
  path = "/data/Cisco-IOS-XE-native:native/router/router-eigrp/eigrp/classic-mode"
  payload = var.eigrp_12
}

resource "iosxe_rest" "config_ospf" {
  method = "PATCH"
  path = "/data/Cisco-IOS-XE-native:native/interface/Loopback=222/ip/Cisco-IOS-XE-ospf:router-ospf/ospf/process-id"
  payload = var.ospf_222
}

