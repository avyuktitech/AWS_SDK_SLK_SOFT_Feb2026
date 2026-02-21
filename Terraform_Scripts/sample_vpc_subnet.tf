resource "aws_vpc" "sample_vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = "sample-vpc"
  }
}

resource "aws_subnet" "sample_subnet" {
  vpc_id     = aws_vpc.sample_vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "us-east-1a"
  tags = {
    Name = "sample-subnet"
  }
}
