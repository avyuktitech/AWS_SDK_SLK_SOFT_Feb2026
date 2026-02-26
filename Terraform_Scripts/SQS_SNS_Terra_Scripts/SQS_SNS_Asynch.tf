# SQS_SNS_Asynch
# 1. Create the SNS Topic (The Broadcaster)
resource "aws_sns_topic" "user_updates" {
  name = "user-updates-topic"
}

# 2. Create an SQS Queue (The Worker)
resource "aws_sqs_queue" "order_processor_queue" {
  name = "order-processor-queue"
}

# 3. Create the Subscription (Bridge SNS to SQS)
resource "aws_sns_topic_subscription" "sns_to_sqs" {
  topic_arn = aws_sns_topic.user_updates.arn
  protocol  = "sqs"
  endpoint  = aws_sqs_queue.order_processor_queue.arn
}

# 4. Give SNS permission to write to SQS
resource "aws_sqs_queue_policy" "sns_to_sqs_policy" {
  queue_url = aws_sqs_queue.order_processor_queue.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect    = "Allow",
      Principal = "*",
      Action    = "sqs:SendMessage",
      Resource  = aws_sqs_queue.order_processor_queue.arn,
      Condition = {
        ArnEquals = { "aws:SourceArn": aws_sns_topic.user_updates.arn }
      }
    }]
  })
}