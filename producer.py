import boto3

# Create SQS client
sqs = boto3.client('sqs', aws_access_key_id='access-key', aws_secret_access_key='secret-key')

queue_url = 'https://sqs.ap-south-1.amazonaws.com/xxxxxxxx/xxxxxxx'

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    # DelaySeconds=10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'The Whistler'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'John Grisham'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
    },
    MessageBody=(
        'Information about current NY Times fiction bestseller for '
        'week of 12/11/2016.'
    )
)

print(response['MessageId'])
