
variable "user" {
  description = "ACI login information"
  type        = map(any)
  default = {
    username = "admin"
    password = "!v3G@!4@Y"
    url      = "https://sandboxapicdc.cisco.com"
  }
}

variable "tenant" {
  type = list(string)
  default = ["DEVNET_ANDY", "DEVNET_NICKY", "DEVNET_KEVIN"]
  
}

variable "VRF" {
  type = map(any)
  default = {
    "DEVNET_ANDY" = ["PRODUCTION", "DEVELOPMENT", "GUEST"]
    "DEVNET_NICKY" = ["PRODUCTION", "DEVELOPMENT", "FACTORY"]
    "DEVNET_KEVIN" = ["PRODUCTION", "DEVELOPMENT", "SALES"]
  }
}

