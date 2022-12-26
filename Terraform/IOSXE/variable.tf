variable "eigrp_12" {
  type = string
  default = <<EOH
    {
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
EOH
}

variable "ospf_222" {
  type = string
  default = <<EOH
    {
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
EOH
}

