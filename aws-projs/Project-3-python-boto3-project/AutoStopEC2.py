import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')

    # Describe EC2 instances with the 'auto-stop' tag set to 'true'
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

    # Stop the running EC2 instances
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            ec2_client.stop_instances(InstanceIds=[instance['InstanceId']])

    return {
        'statusCode': 200,
        'body': 'EC2 instances auto-stopped successfully!'
    }
