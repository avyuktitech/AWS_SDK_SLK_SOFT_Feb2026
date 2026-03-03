provider "aws" {
  region = "us-east-1"
}

# ----------------------------
# 1. Create VPC
# ----------------------------
resource "aws_vpc" "redis_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "redis-vpc"
  }
}

# ----------------------------
# 2. Create Two Subnets (Required for ElastiCache)
# ----------------------------
resource "aws_subnet" "subnet_a" {
  vpc_id                  = aws_vpc.redis_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = false

  tags = {
    Name = "redis-subnet-a"
  }
}

resource "aws_subnet" "subnet_b" {
  vpc_id                  = aws_vpc.redis_vpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = false

  tags = {
    Name = "redis-subnet-b"
  }
}

# ----------------------------
# 3. Security Group (Allow Redis inside VPC only)
# ----------------------------
resource "aws_security_group" "redis_sg" {
  name   = "redis-security-group"
  vpc_id = aws_vpc.redis_vpc.id

  ingress {
    from_port   = 6379
    to_port     = 6379
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "redis-sg"
  }
}

# ----------------------------
# 4. ElastiCache Subnet Group
# ----------------------------
resource "aws_elasticache_subnet_group" "redis_subnet_group" {
  name = "redis-subnet-group-demo"

  subnet_ids = [
    aws_subnet.subnet_a.id,
    aws_subnet.subnet_b.id
  ]
}

# ----------------------------
# 5. Redis Cluster (Single Node)
# ----------------------------
resource "aws_elasticache_cluster" "redis" {
  cluster_id           = "redis-demo"
  engine               = "redis"
  engine_version       = "7.0"
  node_type            = "cache.t3.micro"
  num_cache_nodes      = 1
  parameter_group_name = "default.redis7"
  port                 = 6379

  subnet_group_name  = aws_elasticache_subnet_group.redis_subnet_group.name
  security_group_ids = [aws_security_group.redis_sg.id]
}

# ----------------------------
# 6. Output Redis Endpoint
# ----------------------------
output "redis_endpoint" {
  value = aws_elasticache_cluster.redis.cache_nodes[0].address
}