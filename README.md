# devops-final-project
 Udacity DevOps Engineering Final Project

The end state of this project is a a very basic website (html only) running on an EKS Cluster in AWS us-west-2 region.  The deployment process will consist of running Jenkins node that will lint and build an Apache web server on a CentOS Docker container, committing the container to a repo on ECR, and rolling out that image on the EKS Cluster via Kubernetes templates. 

Setup steps: 
1. Git pull this repo onto your machine. 
2. Through your CLI, assume the IAM Role that will be assigned to the Jenkins node later. (IMPORTANT: If you do not assume the correct IAM role when setting up the EKS cluster, the setup process for accessing that Kubernetes for Jenkins builds will become significantly more difficult. Do not ignore this step).
3. Using the Assumed Role, run the Cloudformation.yaml file that will stand up the necessary network infrastructure, Security Groups, Jenkins Server, ECR Repository, and EKS Cluster as well installing the software packages required on the Jenkins node. (Optional: If you pass in your current IP address in as a MyIP” parameter, it will restrict the Private Security Group being used for Jenkins to your specific address.) 
4. SSH into the Jenkins node to verify that you can access with the  "aws eks list-clusters --region us-west-2” and the “kubectl get all” commands without issue. 
5. While in the CLI, the Jenkins host will need elevated permissions to execute ‘sudo visudo’ to in to sudoers file and add "jenkins ALL=(ALL) NOPASSWD: ALL” to “ # Allow members of group sudo to execute any command".
6. Go to your browser and access Jenkins over 8080 port. Set up the login and install the suggested plugins. After you’re logged in, add the “Blue Ocean” plugin. 
7.  Enter the Blue Ocean and Create a New Pipeline using this Github project. The pipeline will hadolint your ‘Dockerfile’ and tidy the ‘index.html’ file prior to building a container. 
8. To update your cluster, update the “version” file in the project and initiate another build. 
