terraform {
  required_providers {
    cml2 = {
      source  = "registry.terraform.io/ciscodevnet/cml2"
    }
  }
} 


provider "cml2" {
  address     = "https://192.168.50.100/"
  username    = "test"
  password    = "Cisco123!"
  skip_verify = true
} 

# resource "cml2_lifecycle" "this" {
#   topology = templatefile("devnet_topo.yaml", { toponame = "yolo lab" })
# }

resource "cml2_lab" "this" {
}

resource "cml2_node" "ext" {
  lab_id         = cml2_lab.this.id
  nodedefinition = "external_connector"
  label          = "Internet"
  configuration  = "bridge0"
}

resource "cml2_node" "r1" {
  lab_id         = cml2_lab.this.id
  label          = "R1"
  nodedefinition = "alpine"
}

resource "cml2_node" "r2" {
  lab_id         = cml2_lab.this.id
  label          = "R2"
  nodedefinition = "alpine"
}

resource "cml2_link" "l1" {
  lab_id = cml2_lab.this.id
  node_a = cml2_node.ext.id
  node_b = cml2_node.r1.id
} 

resource "cml2_lifecycle" "top" {
  lab_id = cml2_lab.this.id
  elements = [
    cml2_node.ext.id,
    cml2_node.r2.id,
    cml2_link.l1.id,
  ]
}
