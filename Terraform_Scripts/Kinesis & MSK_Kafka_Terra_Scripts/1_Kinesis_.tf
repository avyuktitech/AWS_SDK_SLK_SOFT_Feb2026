# Create a Kinesis Data Stream
resource "aws_kinesis_stream" "demo_stream" {
  name             = "ssdn-kinesis-stream"
  retention_period = 24 # Hours data is stored

  stream_mode_details {
    stream_mode = "ON_DEMAND"
  }

  tags = {
    Environment = "Demo"
  }
}

output "kinesis_arn" {
  value = aws_kinesis_stream.demo_stream.arn
}