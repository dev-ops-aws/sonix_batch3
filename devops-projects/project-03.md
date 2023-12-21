## Project Title: Run Ansible Playbook From Jenkins
### Project Description: Run Ansible Playbook from Jenkins using three different methods.
You can run the Ansible playbook through Jenkins in multiple ways:
- Method #1. Using default method which needs Ansible to be configured on Jenkins Master: best and the recommended method to run Ansible job.
- Method #2. Executing Ansible playbook as Shell command or Windows batch command: can be used for testing purposes to run Ansible Playbook on remote host.
- Method #3. Running Job on a separate Node/Agent where you can install Ansible: suited to cases where Jenkins master doesn’t allow Ansible installation or is already having performance crunch.
### AWS Services involved: AWS EC2, Jenkins, Ansible.


### Pre-requisites
1. 3 EC2 Instance ( 1 for Jenkins Master-Node, 1 for Ansible)
2. Jenkins and Java Installation in Master-Node
3. Ansible Installation on Jenkins Master


### Ref Links -
[How to Run Ansible Playbook From Jenkins](https://devopsbuzz.com/run-ansible-playbook-from-jenkins/)

[Ansible Playbook with Jenkins Pipeline](https://medium.com/appgambit/ansible-playbook-with-jenkins-pipeline-2846d4442a31)

[How to Integrate Ansible With Jenkins](https://www.youtube.com/watch?v=xQ_yKp8SdDk)
