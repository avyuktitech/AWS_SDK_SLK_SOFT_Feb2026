resource "aws_db_instance" "sample" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  username             = "admin"
  password             = "password123"
  parameter_group_name = "default.mysql8.0"
  skip_final_snapshot  = true
  db_subnet_group_name = "ajayslkdbsubnetgroup111" # Replace with your actual subnet group name if needed
  vpc_security_group_ids = ["sg-0e32ceb390ef3604a"]
}
