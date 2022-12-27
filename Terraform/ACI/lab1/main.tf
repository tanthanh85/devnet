terraform {
  required_providers {
    aci = {
      source = "CiscoDevNet/aci",

    }
  }
}

provider "aci" {
  # APIC Username
  username = var.user.username
  # APIC Password
  password = var.user.password
  # APIC URL
#   cert_name   = "andy_cert"
#   private_key = "admin.key"
  url         = var.user.url
  insecure    = true
}

# resource "aci_tenant" "devnet" {
#   for_each = toset(var.tenant)
#   name = each.value
# }

resource "aci_tenant" "devnet" {
  for_each = {for t in var.tenant: t => t}
  name = each.value
}

output "test" {
  value = {for t in var.tenant: t => t}
}

output "ACI_TENANTS" {
  value = resource.aci_tenant.devnet["DEVNET_ANDY"].id
}




# data "aci_tenant" "ex-tenant" {
#     for_each = var.vrf
#     name = each.key
  
# }

# data "aci_tenant" "TN-ANDY" {
#   name = "DEVNET_ANDY"
# }

# data "aci_tenant" "TN-NICKY" {
#   name = "DEVNET_NICKY"
# }

# data "aci_tenant" "TN-KEVIN" {
#   name = "DEVNET_KEVIN"
# }




# resource "aci_vrf" "devnet-vrf" {
#   tenant_dn = data.aci_tenant.TN-ANDY.id
#   for_each = toset(var.vrf["DEVNET_ANDY"])
#   name = each.value
# }

resource "aci_vrf" "ANDY-VRF" {
  tenant_dn = resource.aci_tenant.devnet["DEVNET_ANDY"].id
  for_each = toset(var.VRF["DEVNET_ANDY"])
  name = each.value
}

resource "aci_vrf" "NICKY-VRF" {
  tenant_dn = resource.aci_tenant.devnet["DEVNET_NICKY"].id
  for_each = toset(var.VRF["DEVNET_NICKY"])
  name = each.value
}

resource "aci_vrf" "KEVIN-VRF" {
  tenant_dn = resource.aci_tenant.devnet["DEVNET_KEVIN"].id
  for_each = toset(var.VRF["DEVNET_KEVIN"])
  name = each.value
}

