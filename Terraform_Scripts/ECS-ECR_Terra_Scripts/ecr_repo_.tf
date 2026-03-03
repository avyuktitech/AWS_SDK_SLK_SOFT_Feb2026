#First, you need a place to push your Docker images. 
#This is the "Docker Hub" of your private AWS account
resource "aws_ecr_repository" "demo_app" {
  name                 = "ssdn-demo-app"
  image_tag_mutability = "MUTABLE"
  force_delete         = true # Helpful for demos so you can delete it easily

  image_scanning_configuration {
    scan_on_push = true
  }
}

output "ecr_repository_url" {
  value = aws_ecr_repository.demo_app.repository_url
}