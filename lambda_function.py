import json
import boto3




def lambda_handler(event, context):
    # TODO implement
    print(event['action'])
    msg = event['action']
    if(msg=="Start"):
        client = boto3.client('ec2')
        response = client.start_instances(
            InstanceIds=[
                'i-09d1320124c910df2',
            ],
        )
        print(response)
    else:
        client = boto3.client('ec2')
        response = client.stop_instances(
            InstanceIds=[
                'i-09d1320124c910df2',
            ],
        )
        print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
