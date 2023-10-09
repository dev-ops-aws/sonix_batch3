import boto3
import datetime

# AWS Resource Clients
ec2_client = boto3.client('ec2')
rds_client = boto3.client('rds')
sns_client = boto3.client('sns')

# AWS Account ID and Gmail address
aws_account_id = '264638186531'
gmail_address = 'pavankumargudipati18@gmail.com'

def email_summary(event, context):
    # Phase-1: Email Summary at 6 PM
    now = datetime.datetime.utcnow()
    if now.hour == 18:
        ec2_instances = ec2_client.describe_instances()
        rds_instances = rds_client.describe_db_instances()

        # Extract and summarize instance information

        # Compose email message
        email_message = f"EC2 Instances:\n{ec2_summary}\n\nRDS Instances:\n{rds_summary}"

        # Send email using SNS
        sns_client.publish(
            TopicArn='arn:aws:sns:ap-south-1:264638186531:ResourceSummaryTopic',
            Message=email_message,
            Subject='AWS Resource Summary'
        )
