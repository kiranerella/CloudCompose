variable "project_id" {}
variable "db_name" {}
variable "region" {}
variable "tier" { default = "db-custom-1-3840" }
variable "admin_password" {}
variable "tags" { type = map(string) }
