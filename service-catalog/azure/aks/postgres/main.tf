module "postgres" {
  source  = "Azure/postgresql/azurerm"
  version = "4.7.0"

  name                = var.db_name
  resource_group_name  = var.resource_group_name
  location            = var.location
  administrator_login = var.admin_username
  administrator_password = var.admin_password
  sku_name            = var.sku_name
  storage_mb          = var.storage_mb
  backup_retention_days = var.backup_retention_days
  geo_redundant_backup = var.geo_redundant_backup

  tags = var.tags
}
