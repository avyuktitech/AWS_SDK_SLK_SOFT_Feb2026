resource "aws_dynamodb_table" "basic_table" {
  name           = "ssdn-demo-orders"
  billing_mode   = "PAY_PER_REQUEST" # Best for unpredictable workloads
  hash_key       = "OrderId"         # Partition Key
  range_key      = "OrderDate"       # Sort Key

  # You only define attributes used for Keys or Indexes
  attribute {
    name = "OrderId"
    type = "S" # S = String, N = Number, B = Binary
  }

  attribute {
    name = "OrderDate"
    type = "N" # Store as Unix timestamp
  }

  tags = { Environment = "Training" }
}