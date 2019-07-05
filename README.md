# AWS Lambda in Python with SAM

A sample project for building and deploying Python functions on AWS Lambda.

* AWS: Lambda
* Python 3.7

## Prerequisites
* AWS Account
* AWS CLI
* SAM CLI
* Python 3.7

## Deployment

Follow the article [AWS Lambda in Python with SAM](https://fnattic.com/aws-lambda-in-python-with-sam/) for deploying the app.

## Running the app

```[STACK_NAME]``` is the name of the stack used for deployment.

```shell
aws cloudformation describe-stacks --stack-name [STACK_NAME]
```

Grab the ```RootUrl``` from the output and use it in the next command to run the test.

```shell
curl -X GET [RootUrl]/hn/story/top
```

You should see the title, author and URL for the top HackerNews story in plain text.
