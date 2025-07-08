module "cloudsql" {
  source  = "terraform-google-modules/sql-db/google"
  version = "10.0.0"

  project        = var.project_id
  name           = var.db_name
  database_version = "POSTGRES_15"
  region         = var.region

  settings = {
    tier             = var.tier
    backup_configuration = {
      enabled = true
      start_time = "02:00"
    }
    ip_configuration = {
      ipv4_enabled = true
    }
  }

  root_password = var.admin_password

  tags = var.tags
}
