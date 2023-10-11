import boto3
import datetime

def lambda_handler(event, context):
    # AWS clients
    ec2_client = boto3.client('ec2', region_name='ap-south-1')  # Replace 'your-ec2-region' with your region.
    sns_client = boto3.client('sns')

    # Check if the current hour is 20 (8 PM in 24-hour format)
    current_hour = datetime.datetime.utcnow().hour

    if current_hour == 20:
        # Describe EC2 instances with the 'auto-stop' tag set to 'true' and 'running' state
        instances = ec2_client.describe_instances(
            Filters=[
                {
                    'Name': 'tag:auto-stop',
                    'Values': ['true']
                },
                {
                    'Name': 'instance-state-name',
                    'Values': ['running']
                }
            ]
        )

        # Initialize a list to store instance IDs
        instance_ids = []

        # Extract instance IDs
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                instance_ids.append(instance['InstanceId'])

        if instance_ids:
            # Stop the running EC2 instances
            ec2_client.stop_instances(InstanceIds=instance_ids)

            # Send a notification
            sns_client.publish(
                TopicArn='arn:aws:sns:ap-south-1:264638186531:ResourceSummaryTopic',  # Replace with your SNS topic ARN.
                Message='EC2 instances auto-stopped successfully!',
                Subject='AWS Resource Auto-Stop'
            )

            return {
                'statusCode': 200,
                'body': 'EC2 instances auto-stopped successfully!'
            }
    else:
        return {
            'statusCode': 200,
            'body': 'Not the scheduled time for stopping instances.'
        }
