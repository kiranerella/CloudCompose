module "ecs" {
  source  = "terraform-aws-modules/ecs/aws"
  version = "~> 5.0"

  name = var.cluster_name

  # optional pass-through
  capacity_providers = var.capacity_providers

  # Example: inject mandatory tags
  tags = merge(var.tags, {
    "ManagedBy" = "CloudCompose"
  })
}
