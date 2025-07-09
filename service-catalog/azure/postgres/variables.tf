variable "db_name" {}
variable "resource_group_name" {}
variable "location" {}
variable "admin_username" {}
variable "admin_password" {}
variable "sku_name" { default = "GP_Gen5_2" }
variable "storage_mb" { default = 5120 }
variable "backup_retention_days" { default = 7 }
variable "geo_redundant_backup" { default = "Disabled" }
variable "tags" { type = map(string) }
