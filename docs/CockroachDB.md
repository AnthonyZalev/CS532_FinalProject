# COMPSCI532 - Final Project CockroachDB Setup

## CockroachDB Installation. 
1. Install Homebrew
2. ```bash
    brew install cockroachdb/tap/cockroach
    ```
3. Verify installation. Ensure it's the latest version because Nodelocal (used later) is a recent update.
    ```bash
    cockroach --version
    ```

## Single Node Setup
1. Setup:
```bash
    cockroach start \
    --insecure \
    --store=node1 \
    --listen-addr=localhost:26257 \
    --http-addr=localhost:8080 \
    --join=localhost:26257,localhost:26258,localhost:26259 \
    --background
```
The insecure flag instructs CockroachDB to start the node in an insecure state, meaning no encryption or authentication. This is typically fine for local development. 

2. Cluster Initialization: Only have to do this one time for the cluster even if nodes are added later.
```bash
cockroach init --insecure --host=localhost:26257
```

3. Open the local host on a browser to use the CockroachDB nodes dashboard. This contains helpful information about the nodes, security, and metrics. 

## Opening SQL
CockroachDB has a built-in SQL client. Open SQL on one of the nodes in the cluster. CockroachDB's distributed architecture will ensure data replication across all nodes in the cluster.
```bash
cockroach sql --insecure --host=localhost:26257
```
Now you can run SQL commands in the CLI (i.e. Create, Select, Insert...)

To quit SQL console: 
```bash
\q
```
## Nodelocal
Nodelocal is a useful CockroachDB tool to upload local files to the CockroachDB cluster. 
```bash
cockroach nodelocal upload <location/of/file> <destination/of/file> [flags]
```
The flags are typically the local host and insecure. See CockroachDB documentation for more flags. Example:
```bash
cockroach nodelocal upload ./shakespeare.csv shakespeare.csv --host=localhost:26257 --insecure
```
Nodelocal upload takes some time especially for large files. 

Once the file has been uploaded you should see the following message:
```bash
successfully uploaded to nodelocal:<filepath>
```

To use the uploaded file, you can use SQL's IMPORT INTO command. Use the nodelocal filepath that you got in the success message:
```bash
IMPORT INTO table (columns) CSV DATA ('nodelocal:<filepath>');
```



## Multiple Node Setup
To scale the cluster, you can simply add more nodes. CockroachDB will automatically distribute the workload among the nodes as it sees fit.

Run the same cockroach start command from above but with different flag values for store, listen-addr, and http-addr.
Examples:
```bash
    cockroach start \
    --insecure \
    --store=node2 \
    --listen-addr=localhost:26258 \
    --http-addr=localhost:8081 \
    --join=localhost:26257,localhost:26258,localhost:26259 \
    --background
```
```bash
    cockroach start \
    --insecure \
    --store=node3 \
    --listen-addr=localhost:26259 \
    --http-addr=localhost:8082 \
    --join=localhost:26257,localhost:26258,localhost:26259 \
    --background
```

## Killing Nodes
Run the following command to get the process IDs of the nodes:
```bash
ps -ef | grep cockroach | grep -v grep
```
Then kill the nodes one by one using their PID:
```bash
kill -9 <PID>
```
To restart a deleted node, you can run the same cockroach start command from above. If you have no plans on restarting the cluster, the node/ folders can be deleted in your local directory and remove the cockroach-data/ directory.


