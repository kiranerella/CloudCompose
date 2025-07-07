module "gke" {
  source  = "terraform-google-modules/kubernetes-engine/google"
  version = "25.0.0"

  project_id     = var.project_id
  name           = var.cluster_name
  region         = var.region
  network        = var.network
  subnetwork     = var.subnetwork
  initial_node_count = var.node_count

  tags = var.tags
}
