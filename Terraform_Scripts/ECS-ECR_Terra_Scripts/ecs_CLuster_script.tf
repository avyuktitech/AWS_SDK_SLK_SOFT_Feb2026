# ----------------------------
# Provider
# ----------------------------
provider "aws" {
  region = "us-east-1"
}

# ----------------------------
# 1. VPC (if not existing, otherwise reference your existing VPC)
# ----------------------------
resource "aws_vpc" "ssdn_vpc" {
  cidr_block           = "10.20.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "ssdn-vpc"
  }
}

# ----------------------------
# 2. Subnets (two private subnets for Fargate)
# ----------------------------
resource "aws_subnet" "ssdn_subnet_a" {
  vpc_id            = aws_vpc.ssdn_vpc.id
  cidr_block        = "10.20.1.0/24"
  availability_zone = "us-east-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "ssdn-subnet-a"
  }
}

resource "aws_subnet" "ssdn_subnet_b" {
  vpc_id            = aws_vpc.ssdn_vpc.id
  cidr_block        = "10.20.2.0/24"
  availability_zone = "us-east-1b"
  map_public_ip_on_launch = true

  tags = {
    Name = "ssdn-subnet-b"
  }
}

# ----------------------------
# 3. Security Group for ECS Service
# ----------------------------
resource "aws_security_group" "ecs_app_sg" {
  name   = "ssdn-ecs-app-sg"
  vpc_id = aws_vpc.ssdn_vpc.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "ssdn-ecs-app-sg"
  }
}

# ----------------------------
# 4. ECS Cluster
# ----------------------------
resource "aws_ecs_cluster" "main" {
  name = "ssdn-training-cluster"
}

# ----------------------------
# 5. IAM Role for ECS Task Execution
# ----------------------------
resource "aws_iam_role" "ecs_task_execution_role" {
  name = "ecsTaskExecutionRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "ecs-tasks.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "ecs_policy" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

# ----------------------------
# 6. ECS Task Definition
# ----------------------------
resource "aws_ecs_task_definition" "app" {
  family                   = "ssdn-app-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"  # 0.25 vCPU
  memory                   = "512"  # 0.5 GB
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn

  container_definitions = jsonencode([{
    name      = "demo-container"
    image     = "${aws_ecr_repository.demo_app.repository_url}:latest" # Reference your existing ECR repo
    essential = true
    portMappings = [{
      containerPort = 80
    }]
  }])
}

# ----------------------------
# 7. ECS Service
# ----------------------------
resource "aws_ecs_service" "main" {
  name            = "ssdn-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = [aws_subnet.ssdn_subnet_a.id, aws_subnet.ssdn_subnet_b.id]
    assign_public_ip = true
    security_groups  = [aws_security_group.ecs_app_sg.id]
  }

  depends_on = [aws_iam_role_policy_attachment.ecs_policy]
}

# ----------------------------
# 8. Output ECS Service Info
# ----------------------------
output "ecs_service_name" {
  value = aws_ecs_service.main.name
}

output "ecs_task_definition_arn" {
  value = aws_ecs_task_definition.app.arn
}