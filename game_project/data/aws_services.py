"""
AWSサービスのリスト
各サービスは以下の形式で定義:
{
    "name": "サービス名（Amazon/AWSの接頭辞を含む）",
    "prefix": "Amazon" または "AWS",
    "service": "接頭辞を除いたサービス名",
    "icon_path": "アイコンへのパス"
}
"""

AWS_SERVICES = [
    {
        "name": "Amazon S3",
        "prefix": "Amazon",
        "service": "S3",
        "icon_path": "assets/images/amazon_s3.png"
    },
    {
        "name": "Amazon EC2",
        "prefix": "Amazon",
        "service": "EC2",
        "icon_path": "assets/images/amazon_ec2.png"
    },
    {
        "name": "AWS Lambda",
        "prefix": "AWS",
        "service": "Lambda",
        "icon_path": "assets/images/aws_lambda.png"
    },
    {
        "name": "Amazon DynamoDB",
        "prefix": "Amazon",
        "service": "DynamoDB",
        "icon_path": "assets/images/amazon_dynamodb.png"
    },
    {
        "name": "AWS CloudFormation",
        "prefix": "AWS",
        "service": "CloudFormation",
        "icon_path": "assets/images/aws_cloudformation.png"
    },
    {
        "name": "Amazon RDS",
        "prefix": "Amazon",
        "service": "RDS",
        "icon_path": "assets/images/amazon_rds.png"
    },
    {
        "name": "AWS CloudTrail",
        "prefix": "AWS",
        "service": "CloudTrail",
        "icon_path": "assets/images/aws_cloudtrail.png"
    },
    {
        "name": "Amazon SNS",
        "prefix": "Amazon",
        "service": "SNS",
        "icon_path": "assets/images/amazon_sns.png"
    },
    {
        "name": "AWS IAM",
        "prefix": "AWS",
        "service": "IAM",
        "icon_path": "assets/images/aws_iam.png"
    },
    {
        "name": "Amazon SQS",
        "prefix": "Amazon",
        "service": "SQS",
        "icon_path": "assets/images/amazon_sqs.png"
    },
    {
        "name": "AWS Step Functions",
        "prefix": "AWS",
        "service": "Step Functions",
        "icon_path": "assets/images/aws_step_functions.png"
    },
    {
        "name": "Amazon CloudWatch",
        "prefix": "Amazon",
        "service": "CloudWatch",
        "icon_path": "assets/images/amazon_cloudwatch.png"
    },
    {
        "name": "AWS Glue",
        "prefix": "AWS",
        "service": "Glue",
        "icon_path": "assets/images/aws_glue.png"
    },
    {
        "name": "Amazon ECS",
        "prefix": "Amazon",
        "service": "ECS",
        "icon_path": "assets/images/amazon_ecs.png"
    },
    {
        "name": "AWS Fargate",
        "prefix": "AWS",
        "service": "Fargate",
        "icon_path": "assets/images/aws_fargate.png"
    }
]
