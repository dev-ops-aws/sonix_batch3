import boto3
import datetime

# AWS Resource Clients
def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    rds_client = boto3.client('rds')
    sns_client = boto3.client('sns')

    # Phase-1: Email Summary at 6 PM
    now = datetime.datetime.utcnow()
    if now.hour == 18:
        ec2_instances = ec2_client.describe_instances()
        rds_instances = rds_client.describe_db_instances()

        # Initialize empty lists to store instance information
        instance_info = []

        # Extract and summarize EC2 instance information
        for reservation in ec2_instances['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_name = ""
                instance_state = instance['State']['Name']

                # Retrieve the instance name from tags if available
                for tag in instance['Tags']:
                    if tag['Key'] == 'Name':
                        instance_name = tag['Value']

                # Append the EC2 instance information to the list
                instance_info.append({
                    'Type': 'EC2',
                    'InstanceID': instance_id,
                    'Name': instance_name,
                    'State': instance_state,
                })

        # Extract and summarize RDS instance information
        for rds_instance in rds_instances['DBInstances']:
            instance_id = rds_instance['DBInstanceIdentifier']
            instance_name = rds_instance.get('DBInstanceIdentifier', '')
            instance_state = rds_instance['DBInstanceStatus']

            # Append the RDS instance information to the list
            instance_info.append({
                'Type': 'RDS',
                'InstanceID': instance_id,
                'Name': instance_name,
                'State': instance_state,
            })

        # Compose email message
        email_message = "\n".join([f"Type: {info['Type']}, Instance ID: {info['InstanceID']}, Name: {info['Name']}, State: {info['State']}" for info in instance_info])

        # Debugging statement to check the email_message
        print(email_message)

        # Check if email_message is empty before sending
        if email_message:
            sns_client.publish(
                TopicArn='arn:aws:sns:ap-south-1:264638186531:ResourceSummaryTopic',
                Message=email_message,
                Subject='AWS Resource Summary'
            )
        else:
            print("No instances found, so no email message to send.")
