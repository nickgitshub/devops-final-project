pipeline {
  agent any
  environment {
        REPO_LATEST = """${sh(
                returnStdout: true,
                script: 'REPOSITORY=$(aws ecr describe-repositories --query repositories[0].repositoryUri --region us-west-2 --output text) && Output="${REPOSITORY}:latest" && echo $Output'
            )}"""
        REPO_VERSION = """${sh(
                returnStdout: true,
                script: 'REPOSITORY=$(aws ecr describe-repositories --query repositories[0].repositoryUri --region us-west-2 --output text) && VERSION=$(cat version) && Output="${REPOSITORY}:${VERSION}" && echo $Output'
            )}"""
  }
  stages {
    stage('Pull and Lint Index.html and Dockerfile'){
        
        steps{
            dir ('web-app') {
                sh 'hadolint Dockerfile'
                sh 'tidy index.html'
            }
        }
    }
    stage('Build Docker Container and commit to ECR') {
        
        steps {
            dir ('web-app') {
                sh 'sudo docker build . -t webapp:latest' 
                sh 'sudo $(aws ecr get-login --no-include-email --region us-west-2)'
                sh 'sudo docker tag webapp:latest ${REPO_VERSION}'
                sh 'sudo docker push ${REPO_VERSION}'
                sh 'sudo docker tag webapp:latest ${REPO_LATEST}'
                sh 'sudo docker push ${REPO_LATEST}'  
            }
        }
    }
    stage('Build Kubernetes cluster / rollout new image'){
        steps{
            dir ('web-app') {
                sh 'python generateECR.py ${REPO_VERSION} > executesed.sh'
                sh 'chmod 755 executesed.sh'
                sh 'cat executesed.sh'
                sh './executesed.sh'
                sh 'cat webapp-modified.yaml'
                sh 'kubectl apply -f webapp-modified.yaml'
                sh 'kubectl apply -f webapp.service.yaml'
            }
        }
    }
  }
}
