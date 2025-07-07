variable "cluster_name" {
  description = "Name of the ECS cluster"
  type        = string
}

variable "capacity_providers" {
  description = "Optional ECS capacity providers"
  type        = list(string)
  default     = ["FARGATE"]
}

variable "tags" {
  description = "Custom tags"
  type        = map(string)
  default     = {}
}
