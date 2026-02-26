# A simple configuration parameter (Free) - 
resource "aws_ssm_parameter" "db_url" {
  name  = "/training/db_url"
  type  = "String"
  value = "db.ssdn-labs.com"
}

# A secure secret (Costs money per secret)
resource "aws_secretsmanager_secret" "db_password" {
  name        = "slk-ssdn-db-password-unique-2026"
  description = "Database password for interns demo"
}

resource "aws_secretsmanager_secret_version" "pass_val" {
  secret_id     = aws_secretsmanager_secret.db_password.id
  secret_string = "SuperSecret123!"
}