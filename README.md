# COMPSCI532 - Final Project

## High Level Goal
The goal of this project is the better understand how each of the four method chosen - Pyspark RDD, Pyspark DF, native Python, and native SQL - approach data processing by analyzing the results from running work-counter in each configuration. In addition, we will also explore the runtime differences between using a single machine and using a distributed system.


## AWS Configuration.

Anthony Zalev

Using provided credits from a AWS learning lab.

Steps to get this configured:

### Credentials

1. Load up learners lab. Go to `$Home/.aws/credentials` and add the access_key, secret_access_key, and session_token from the lab. Then `aws configure` in console.

2. Download the ssh key and add it to the working directory of the project.

### Master Node Setup

1. Now we create our EC2 instance. In terminal run:

```bash
aws ec2 run-instances --image-id ami-0d73480446600f555 --instance-type m4.large --key-name vockey > instance.json
```

Now understand this cost .10 cents per hour. So if you leave it running for 24 hours, that's $2.40. So make sure to terminate the instance when you're done.

Later we will be running around 10 instances at once. So make sure that once you are done with the project, you stop all instances.

A instance.json file will be created.

2. Configure ssh authorization. In terminal run:

```bash
$chmod 400 labsuser.pem
```

```bash
aws ec2 authorize-security-group-ingress --group-name default --protocol tcp --port 22 --cidr 0.0.0.0/0
```

3. Create the cluster. This will take a few minutes to complete. The cluster will be created with a single node.

    ```bash
    aws emr create-cluster --name "Spark cluster" --release-label emr-5.36.0 --applications Name=Spark --ec2-attributes KeyName=myKey --instance-type m4.large  --instance-count 1 --use-default-roles
    ```

    Why m4.large? Because it's the cheapest option. We don't need a lot of computing power for this project. Also learners lab only allows for instance types at most size large. a m4.large instance has 2 vCPUs and 8GB of memory. It has EBS storage only