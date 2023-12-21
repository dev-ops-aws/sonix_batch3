## Project Title: Jenkins - Build and Deploy a Node.js app with Docker using CI/CD pipeline
### Project Description: The project aims to set up a Jenkins cluster consisting of a master node, an agent node, and a live server using three AWS EC2 instances. The project requires installing Java, Jenkins, and Docker on the master and agent nodes. The Jenkins cluster distributes the workload across multiple nodes, and the master node controls and assigns jobs to agent nodes. A pipeline is created to deploy a Node.js application using Docker. The pipeline has staged such as checkout, build, test, push, and deploy, which perform different tasks such as fetching source code from GitHub, building a Docker image, testing the image, pushing it to DockerHub, and deploying it to the live server. The project helps in automating the deployment process and saves time and effort by eliminating manual tasks.
### AWS Services involved: AWS EC2, Jenkins, Groovy Scripting, Jenkins file.


### Pre-requisites
1. 3 EC2 Instance ( 1 for Jenkins Master-Node, 1 for Jenkins Agent-Node, and 1 for Deploying live server)
2. Jenkins and Java Installation in Master-Node
3. Only Java Installation in Agent-Node
4. Docker Installation

### Part-01: Set up a Jenkins Cluster (Master Node and Agent Node)
### Part-02: Create a Node-todo-app-deployment Job with Pipeline
### Part-03: Open port 8000 in the Deploying on live server Instance’s security inbound rule
### Part-04: Check if the application is running

### Ref Links -
[Reference Link](https://medium.com/cloud-native-daily/project-on-building-and-deploying-a-node-js-cda2e13235be)
