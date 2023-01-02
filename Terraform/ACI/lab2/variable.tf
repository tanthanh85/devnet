variable "tenants" {
  type = list(object({
    name = string,
    vrf = list(string)

  }))
}

variable "user" {
  description = "ACI login information"
  type        = map(any)
  default = {
    username = "admin"
    password = "!v3G@!4@Y"
    url      = "https://sandboxapicdc.cisco.com"
  }
}

