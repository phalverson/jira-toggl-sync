# jira-toggl-sync

Webhooks to synchronize Jira issues with Toggl project tasks

Includes support for deploying as a AWS Lambda function with an API
Gateway front end.

# Building

## Prerequisites

* [Python](https://www.python.org/) 3.7 or greater
* [pipenv](https://github.com/pypa/pipenv)

## Configuration

    $ pipenv --python 3.7
    $ pipenv install --dev
    $ . .venv/bin/activate

## Unit Tests

    $ PYTHONPATH=jts pytest tests/unit 

## Build
    
    $ sam build
    
## Testing

Running a single lambda in a local container:

    $ sam local invoke -e tests/events/hook-request-1.json     

Start a persistent local container with a web listener:

    $ sam local start-api

## Deploy

    $ sam deploy --profile <aws-profile> --guided 
      
