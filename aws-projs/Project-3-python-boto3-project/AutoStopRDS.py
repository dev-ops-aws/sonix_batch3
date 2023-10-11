import boto3
import datetime

def lambda_handler(event, context):
    # AWS clients
    rds_client = boto3.client('rds', region_name='ap-south-1')  # Replace 'your-rds-region' with your region.
    sns_client = boto3.client('sns')

    # Check if the current hour is 20 (8 PM in 24-hour format)
    current_hour = datetime.datetime.utcnow().hour

    if current_hour == 20:
        # Describe RDS instances with the 'auto-stop' tag set to 'true' and 'available' state
        response = rds_client.describe_db_instances()

        # Initialize a list to store DB instance identifiers
        instance_ids = []

        # Extract DB instance identifiers with the 'auto-stop' tag
        for instance in response['DBInstances']:
            for tag in instance.get('TagList', []):
                if tag['Key'] == 'auto-stop' and tag['Value'] == 'true':
                    instance_ids.append(instance['DBInstanceIdentifier'])

        if instance_ids:
            # Stop the RDS instances
            for instance_id in instance_ids:
                rds_client.stop_db_instance(DBInstanceIdentifier=instance_id)

            # Send a notification
            sns_client.publish(
                TopicArn='arn:aws:sns:ap-south-1:264638186531:ResourceSummaryTopic',  # Replace with your SNS topic ARN.
                Message='RDS instances auto-stopped successfully!',
                Subject='AWS Resource Auto-Stop'
            )

            return {
                'statusCode': 200,
                'body': 'RDS instances auto-stopped successfully!'
            }
    else:
        return {
            'statusCode': 200,
            'body': 'Not the scheduled time for stopping instances.'
        }
