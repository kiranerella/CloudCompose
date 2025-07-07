variable "resource_group_name" {}
variable "kubernetes_version" {}
variable "cluster_name" {}
variable "node_count" { default = 1 }
variable "node_vm_size" { default = "Standard_DS2_v2" }
variable "tags" { type = map(string) }
