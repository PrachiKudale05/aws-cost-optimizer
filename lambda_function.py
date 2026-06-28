import boto3
REGION = 'ap-south-1' 
ec2 = boto3.client('ec2', region_name=REGION)

def lambda_handler(event, context):
    print(f"Checking for running EC2 instances in region: {REGION}")
    
    # Filter for instances that are currently 'running'
    filters = [{
        'Name': 'instance-state-name',
        'Values': ['running']
    }]
    
    instances = ec2.describe_instances(Filters=filters)
    instance_ids = []
    
    # Loop through the AWS response to catch the instances
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
            
    # Stop the instances if any were found
    if instance_ids:
        print(f"Found running instances: {instance_ids}. Sending stop command...")
        ec2.stop_instances(InstanceIds=instance_ids)
        return f"Successfully stopped instances: {instance_ids}"
    else:
        print("No running instances found in this region.")
        return "No running instances found to stop."