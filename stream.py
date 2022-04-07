# view a kinesis stream
import boto3
import time

# TODO env var
my_stream_name = 'justin-poc-stream'
# my_stream_name = 'com.heyes-jones.stream-cdp_stream_in'
# dev = boto3.session.Session(profile_name='dev-backend')
# print(dev)

kinesis_client = boto3.client('kinesis')

response = kinesis_client.describe_stream(StreamName=my_stream_name)
print(response)

my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']

shard_iterator = kinesis_client.get_shard_iterator(StreamName=my_stream_name,
                                                      ShardId=my_shard_id,
                                                      ShardIteratorType='LATEST')

my_shard_iterator = shard_iterator['ShardIterator']

record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator,
                                              Limit=2)

while 'NextShardIterator' in record_response:
    record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'],
                                                  Limit=2)

    print(record_response)

    # wait for 5 seconds
    time.sleep(5)
