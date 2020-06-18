pipeline {
    environment {
        registry = "clrosier/auth"
        registryCredential = 'dockerhub'
    }
    agent {
        label 'docker-node'
    }
    stages {
        stage ('build Dockerfile') {
            steps {
                echo 'Building Dockerfile...'
                script {
                    dockerImage = docker.build registry + ":1.0.$BUILD_NUMBER"
                    dockerImage_latest = docker.build registry + ":latest"
                }
            }
        }
        stage ('build Dockerfile-arm64') {
            steps {
                echo 'Building Docker image for arm64...'
                script {
                    dockerImage_arm64 = docker.build(registry + ":arm64-1.0.$BUILD_NUMBER", "-f Dockerfile-arm64 .")
                    dockerImage_arm64_latest = docker.build(registry + ":arm64-latest", "-f Dockerfile-arm64 .")
                }
            }
        }
        stage ('push images to dockerhub') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                        dockerImage_latest.push()
                        dockerImage_arm64.push()
                        dockerImage_arm64_latest.push()
                    }
                }
            }
        }
        stage ('remove images from host') {
            steps {
                sh "docker rmi $registry:1.0.$BUILD_NUMBER"
                sh "docker rmi $registry:arm64-1.0.$BUILD_NUMBER"
            }
        }
    }
}