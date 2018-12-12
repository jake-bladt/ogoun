# Ogoun

Ogoun is a distributed framework for finding and processing assets on the World Wide Web. Its initial implementation is contract based and includes the following components:

* a website for tracking jobs and building contracts
* a serverless function set for storing contracts
* a serverless function set for managing jobs
* one or more serverless functions for retrieving and processing assets
* a datastore for tracking work
* a deploy script
* a teardown script

## Core functioning

At its core, Ogoun runs a retrieve-analyze-process loop. A typical task would be to retrieve the text of a web page, find all the links in that page, and queue new jobs to recurse through those links.

## Usage

* A user logs into the site and creates a contract for handling a particular type of asset. This may include calls to other contracts for assets discovered during handling. For example:

```javascript
{
  "contract-name": "store in s3",
  "assets-required": "$s3-bucket",
  "action": "store"
}
```

AND

```javascript
{
  "contract-name": "find-links",
  "handle-assets": {
    "asset-type": "link",
	"handler": "store in s3"
  }
}
```

## Resource Links

* [How to read and write to SQS with a Lambda](http://blog.epsagon.com/how-to-setup-aws-lambda-with-sqs-everything-you-should-know)
* [Lambda with SQS Example](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs-example.html)
* [Authenication in Node with Passport JS](https://medium.freecodecamp.org/learn-how-to-handle-authentication-with-node-using-passport-js-4a56ed18e81e)
* [Common ways to create Lambda functions](https://medium.freecodecamp.org/aws-lambda-offering-developers-ultimate-flexibility-d8939ff4220)
* [Learn Lambda](https://github.com/dwyl/learn-aws-lambda#hello-world-example-api-gateway)
* [Create and upload a Lambda function in node](http://dev.splunk.com/view/event-collector/SP-CAAAE6Z)
