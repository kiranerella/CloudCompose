module "aks" {
  source  = "Azure/aks/azurerm"
  version = "9.0.0"

  resource_group_name = var.resource_group_name
  kubernetes_version  = var.kubernetes_version
  prefix              = var.cluster_name

  default_node_pool = {
    name       = "default"
    node_count = var.node_count
    vm_size    = var.node_vm_size
  }

  tags = var.tags
}
