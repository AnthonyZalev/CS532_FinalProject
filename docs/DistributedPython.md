# Intructions for running the Distributed Python Files on EDLab.

## Coordinator
### Setup
After running n (the number of workers) nodes on EDLab, each will output which machine they are on. You should change line 9 (the HOST) variable to reflect this.
### Running
Simply run the command in the src/distr_nat_py/ directory: python coordinator.py

## Worker Nodes
### Setup
Ensure that wherever a node is ran from that there are the following files:

shakespeare_processed_1_X.txt

shakespeare_processed_16_X.txt

shakespeare_processed_64_X.txt

shakespeare_processed_256_X.txt

shakespeare_processed_1024_X.txt

shakespeare_processed_2048_X.txt

Where X ranges from 0 to n, where n is the number of workers. In simpler terms, there should be n copies of each file so that each node can process the file separately.
### Running
In the same directory that you have the files in run the command: python worker.py \<Port Number> \<Worker Number>

Where \<Port Number> is one of the ports specified in coordinator.py and \<Worker Number> is one of the six X values from the setup section.
