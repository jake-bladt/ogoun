# Ogoun

Ogoun is a distributed framework for finding and processing assets on the World Wide Web. Its initial implementation is contract based and includes the following components:

* a website for tracking jobs and building contracts
* a serverless function set for storing contracts
* a serverless function set for managing jobs
* one or more serverless functions for retrieving and processing assets
* a datastore for tracking work
* a deploy script
* a teardown script

## Usage

* A user logs into the site and creates a contract for handling a particular type of asset. This may include calls to other contracts for assets discovered during handling. For example:

```javascript
{
  contract-name: "store in s3",
  assets-required: "$s3-bucket",
  action: "store"
}
```

```javascript
{
  contract-name: "find-links",
  handle-assets: {
    asset-type": "link",
	handler: "store in s3"
  }
}
```
