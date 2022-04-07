# Read a kinesis stream

## Setup

```
pyenv install 3.9.5
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
pyenv local 3.9.5
pip install --upgrade pip
pip install -r requirements.txt
```

## Running

Edit stream.py and enter your stream name
`python writestream.py`
`python readstream.py`

## Config for localstack

Launch localstack with Kinesis 

`SERVICE=kinesis docker run --rm -it -p 4566:4566 -p 4571:4571 localstack/localstack`

Configure environment variables

```
export AWS_ACCESS_KEY_ID="test"
export AWS_SECRET_ACCESS_KEY="test"
export AWS_DEFAULT_REGION="us-east-1"
```

Create a test stream

`aws --endpoint-url=http://localhost:4566 kinesis create-stream --stream-name test1 --shard-count 1`

Verify

`aws --endpoint-url=http://localhost:4566 kinesis list-streams`

Write to the stream.

```
export STREAM_NAME="test1"
export ENDPOINT_URL="http://localhost:4566"
python writestream.py
```

Read from the stream.

```
export STREAM_NAME="test1"
export ENDPOINT_URL="http://localhost:4566"
python readstream.py
```
