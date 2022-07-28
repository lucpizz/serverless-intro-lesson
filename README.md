# Serverless Introduction Lesson

THis is the introduction to the Serverless Framework and the technology. Let's break that down first.

# What is Serverless?

We have been talking about the cloud and how it can be used to build applications that are on these remote servers somewhere else. We also understand that there are many cool things that we can do with this that we could not do back in the day. It was a great opportunity to learn about the cloud and how it can be used to build applications.

Serverless concepts allow users to define their own functions and then deploy them to the cloud. This is a great way to build applications that are scalable and require minimal effort to manage.

## Services

We will be talking about a few of these services.

AWS Lambda

AWS API Gateway

AWS DynamoDB

AWS S3

AWS CloudFormation

These are some of the services that make it easy to build these serverless applications in the cloud. 

There is an open source service called [serverless](https://serverless.com/) that is a great way to build applications that are scalable and require minimal effort to manage.

It does this by managing the deployment through Cloud Formation or what some people call Infrastructure as Code.

This allows us to track our changes to our resources through code changes, not just through the classic "Click Ops" process.

## Getting started

This service relies on users having the following installed:
- awscli - https://aws.amazon.com/cli/
- npm - https://www.npmjs.com/
- yarn - https://yarnpkg.com/

These are all open source packages that you can contribute to if you need extra functionality within your organization.

Within the root directory of this repo, run the following command:

```
yarn
```

This will install all of the needed dependencies. One of those is `serverless`. The Serverless Framework is what we will be using to deploy our applications. 

Serverless is the concept
Serverless Framework is the open soruce framrwork that makes deploying those types of applications easier.

THere are a few main things that we will be talking about throughout this repo, but the main start is this.

This runs on something called CloudFormation.

The rest of this demo will be adding more configuration to the `serverless.yml` file.

This is the file that is used to define the resources that are needed to deploy our application.