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


resource "aci_tenant" "devnet" {
  for_each = {for tenant in var.tenants: tenant.name => tenant}
  name = each.key
}

# output "test" {
#   value = {for tenant in var.tenants: tenant.name => tenant}
# }

resource "aci_vrf" "devnet0" {
    for_each = {for tenant in var.tenants: tenant.name => tenant}
    name = each.value.vrf[0]
    tenant_dn = aci_tenant.devnet[each.key].id
}
  

  