import boto3
region = 'us-west-1'   #change region with yours
instances = ['i-12345cb6de4f78g9h', 'i-08ce9b2d7eccf6d26']    #change Ec2 Instance ID with yours
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))
