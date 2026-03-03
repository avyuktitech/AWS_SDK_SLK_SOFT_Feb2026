# MSK Serverless Cluster
resource "aws_msk_serverless_cluster" "demo_kafka" {
  cluster_name = "ssdn-msk-serverless"

  vpc_config {
    # Ensure these subnets are in at least 2 different Availability Zones
    subnet_ids         = ["subnet-xxxxxx", "subnet-yyyyyy"] 
    security_group_ids = ["sg-xxxxxx"]
  }

  client_authentication {
    sasl {
      iam {
        enabled = true
      }
    }
  }
}

output "msk_arn" {
  value = aws_msk_serverless_cluster.demo_kafka.arn
}