
# ----------------------------
# 1. VPC
# ----------------------------
resource "aws_vpc" "slkdemo_vpc" {
  cidr_block           = "10.30.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "slkdemo-vpc"
  }
}

# ----------------------------
# 2. Subnets (two subnets for Fargate)
# ----------------------------
resource "aws_subnet" "slkdemo_subnet_a" {
  vpc_id                  = aws_vpc.slkdemo_vpc.id
  cidr_block              = "10.30.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "slkdemo-subnet-a"
  }
}

resource "aws_subnet" "slkdemo_subnet_b" {
  vpc_id                  = aws_vpc.slkdemo_vpc.id
  cidr_block              = "10.30.2.0/24"
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = true

  tags = {
    Name = "slkdemo-subnet-b"
  }
}

# ----------------------------
# 3. Security Group for ECS Service
# ----------------------------
resource "aws_security_group" "slkdemo_sg" {
  name   = "slkdemo-ecs-sg"
  vpc_id = aws_vpc.slkdemo_vpc.id

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
    Name = "slkdemo-ecs-sg"
  }
}

# ----------------------------
# 4. ECS Cluster
# ----------------------------
resource "aws_ecs_cluster" "slkdemo_cluster" {
  name = "slkdemoecs222"
}

# ----------------------------
# 5. IAM Role for ECS Task Execution
# ----------------------------
resource "aws_iam_role" "slkdemo_task_execution_role" {
  name = "slkdemoecs-task-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "ecs-tasks.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "slkdemo_ecs_policy" {
  role       = aws_iam_role.slkdemo_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

# ----------------------------
# 6. ECS Task Definition
# ----------------------------
resource "aws_ecs_task_definition" "slkdemo_task" {
  family                   = "slkdemoecs-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  execution_role_arn       = aws_iam_role.slkdemo_task_execution_role.arn

  container_definitions = jsonencode([{
    name      = "slkdemo-container"
    image     = "${aws_ecr_repository.demo_app.repository_url}:latest" # Reference existing ECR repo
    essential = true
    portMappings = [{
      containerPort = 80
    }]
  }])
}

# ----------------------------
# 7. ECS Service-manager
# ----------------------------
resource "aws_ecs_service" "slkdemo_service" {
  name            = "slkdemoecs-service"
  cluster         = aws_ecs_cluster.slkdemo_cluster.id
  task_definition = aws_ecs_task_definition.slkdemo_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = [aws_subnet.slkdemo_subnet_a.id, aws_subnet.slkdemo_subnet_b.id]
    assign_public_ip = true
    security_groups  = [aws_security_group.slkdemo_sg.id]
  }

  depends_on = [aws_iam_role_policy_attachment.slkdemo_ecs_policy]
}

# ----------------------------
# 8. Output ECS Service Info
# ----------------------------
output "slkdemo_service_name" {
  value = aws_ecs_service.slkdemo_service.name
}

output "slkdemo_task_definition_arn" {
  value = aws_ecs_task_definition.slkdemo_task.arn
}