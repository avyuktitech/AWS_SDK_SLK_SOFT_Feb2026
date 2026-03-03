
# 1. Create the Hosted Zone (The "Folder" for your DNS records)
resource "aws_route53_zone" "training_zone" {
  name          = "ssdn-labs.com"
  force_destroy = true # Allows Terraform to delete the zone even if it has records
  comment       = "Demo for March 2nd Training"
}

# 2. Create an 'A' Record (Maps a name to an IPv4 address)
resource "aws_route53_record" "web_server" {
  zone_id = aws_route53_zone.training_zone.zone_id
  name    = "web.ssdn-labs.com"
  type    = "A"
  ttl     = "300"
  records = ["192.168.1.10"] # In a real lab, this would be your EC2 Public IP
}

# 3. Create a 'CNAME' Record (Maps a name to another name)
resource "aws_route53_record" "api_alias" {
  zone_id = aws_route53_zone.training_zone.zone_id
  name    = "api.ssdn-labs.com"
  type    = "CNAME"
  ttl     = "300"
  records = ["web.ssdn-labs.com"]
}

# Output the Name Servers to show where the domain is hosted
output "name_servers" {
  value = aws_route53_zone.training_zone.name_servers
}