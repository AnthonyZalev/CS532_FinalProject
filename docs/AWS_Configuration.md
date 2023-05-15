# COMPSCI532 - Final Project AWS Setup


## AWS Configuration. Single Node Setup

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

3. SSH in the cluster

    ```ssh -i labsuser.pem ubuntu@ec2-3-231-209-98.compute-1.amazonaws.com``` (or whatever the public dns is)

4. Install Java

    ```bash
    sudo apt-get update
    sudo apt-get install default-jre
    ```

5. Install Spark

    ```bash
    wget http://apache.claz.org/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz
    tar -xvf spark-2.4.4-bin-hadoop2.7.tgz
    ```

6. Install Python

    ```bash
    sudo apt-get install python3-pip
    ```

7. Install Pyspark

    ```bash
    pip3 install pyspark
    ```

8. Download Github Repo

    ```bash
    git clone https://github.com/AnthonyZalev/CS532_FinalProject
    ```

9. Run the program to create the data files. To do this, navigate to ```src\main.py``` and uncomment the enlarge data set function. This function takes in as a input the number of times the base file should be appeneded to itself.

10. Run the word count programs in the src folder. To do this locally vs from the S3 bucket, navigate to the ```native_python.py, pyspark_df_job.py, and pyspark_rdd_job.py``` files and ensure the "Logfile" is pointed to the file you created in the previous step. Then from the root directory, run the programs as ```python3 src/<program_name_here>```. 

## AWS Configuration. Multi Node Setup

In this section we will be setting up a multi node cluster from the AWS Console.

1. Log on to the AWS Console and Navigate to AWS S3. Create a bucket.

2. Upload the data files and worker files to the bucket.

3. Navigate to AWS EMR.

4. Create a cluster by clicking the "Create Cluster" button.

5. Name the cluster, and select the release label. Then choose the spark application.

6. Optionally choose the S3 bucket you created earlier as a log destination to store your console outputs and error messages.

7. Configure the cluster by choosing Instance Groups. Choose the 'm4.large' node for your Primary, Core, and Task Nodes.

8. Provision 1 Core node and 6 Task nodes. Decide on if you want spot instances or not. If you do, you can save a lot of money. But if you don't, you can be sure that your cluster will be up and running.

9. Configure the security group. Make sure that you allow SSH access from anywhere.

10. Select default service role and default EC2 role.

11. Click create cluster. The cluster can take many minutes to get running.

12. From the cluster page, click on the "Add Step" button.

13. Navigate to the S3 bucket and select the worker file. This will be the file that will be run on the cluster.

14. Click "Add" and wait for the cluster to finish running.

