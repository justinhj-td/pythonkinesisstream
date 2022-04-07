# Generate stream messages
import boto3
import time
import os
import sys
import random

ENDPOINT_URL = os.environ.get('ENDPOINT_URL')
STREAM_NAME = os.environ.get('STREAM_NAME')

if not STREAM_NAME:
    print("You must set STREAM_NAME env var")
    sys.exit(1)

print("Stream", STREAM_NAME, "URL", ENDPOINT_URL)

kinesis_client = boto3.client('kinesis', endpoint_url=ENDPOINT_URL)

response = kinesis_client.describe_stream(StreamName=STREAM_NAME)
print("Writing to", response['StreamDescription']['StreamName'])

while True:
    key = str(random.randrange(0, 256))
    data = ("random message " + key).encode("UTF8")
    response = kinesis_client.put_record(StreamName=STREAM_NAME,
                                         Data=data,
                                         PartitionKey=key)
    print(response)
    time.sleep(2)

# shard_iterator = kinesis_client.get_shard_iterator(StreamName=STREAM_NAME,
#                                                       ShardId=my_shard_id,
#                                                       ShardIteratorType='LATEST')

# my_shard_iterator = shard_iterator['ShardIterator']

# record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator,
#                                               Limit=2)

# while 'NextShardIterator' in record_response:
#     record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'],
#                                                   Limit=2)

#     print(record_response)

#     # wait for 5 seconds
#     time.sleep(5)
