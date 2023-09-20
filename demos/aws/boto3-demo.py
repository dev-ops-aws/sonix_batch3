import boto3 as bt

def desc_ec2():
    client = bt.client('ec2')
    response = client.describe_instances(
    InstanceIds=[
        'i-0221d066ce32713f7',
    ],
    )
    print(response)

if __name__ == '__main__':
    desc_ec2()
