variable "project_id" {}
variable "cluster_name" {}
variable "region" {}
variable "network" {}
variable "subnetwork" {}
variable "node_count" { default = 1 }
variable "tags" { type = map(string) }
