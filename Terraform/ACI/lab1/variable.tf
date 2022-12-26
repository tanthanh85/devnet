
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

variable "ANDY_VRF" {
  type = map(any)
  default = {
    "DEVNET_ANDY" = ["PRODUCTION", "DEVELOPMENT"]
  }
}

variable "NICKY_VRF" {
  type = map(any)
  default = {
    "DEVNET_NICKY" = ["PRODUCTION", "DEVELOPMENT"]
  }
}

variable "KEVIN_VRF" {
  type = map(any)
  default = {
    "DEVNET_KEVIN" = ["PRODUCTION", "DEVELOPMENT"]
  }
}