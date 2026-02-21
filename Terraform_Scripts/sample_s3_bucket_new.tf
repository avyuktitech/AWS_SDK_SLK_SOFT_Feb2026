resource "aws_s3_bucket" "sample_bucket" {
  bucket = "my-sample-bucket-20260220-unique"
  force_destroy = true
}
