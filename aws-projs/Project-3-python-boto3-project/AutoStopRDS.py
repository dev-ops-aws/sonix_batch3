import boto3

def lambda_handler(event, context):
    rds_client = boto3.client('rds')

    # Describe all RDS instances
    all_instances = rds_client.describe_db_instances()

    # Filter RDS instances with the 'auto-stop' tag set to 'true'
    instances_to_stop = []

    for instance in all_instances['DBInstances']:
        # Get the list of tags for the RDS instance
        tags = instance.get('TagList', [])

        # Check if the 'auto-stop' tag is present and set to 'true'
        for tag in tags:
            if tag['Key'] == 'auto-stop' and tag['Value'] == 'true':
                # Add the instance to the list of instances to stop
                instances_to_stop.append(instance['DBInstanceIdentifier'])
                break  # Break the inner loop if the tag is found

    # Stop the RDS instances in the 'instances_to_stop' list
    for instance_id in instances_to_stop:
        rds_client.stop_db_instance(DBInstanceIdentifier=instance_id)

    return {
        'statusCode': 200,
        'body': 'RDS instances auto-stopped successfully!'
    }
