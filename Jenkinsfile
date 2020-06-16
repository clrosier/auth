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
                    sh 'hostname -I'
                    dockerImage = docker.build registry + ":1.0.$BUILD_NUMBER"
                }
            }
        }
        stage ('build Dockerfile-arm64') {
            steps {
                echo 'Building Docker image for arm64...'
                script {
                    dockerImage_arm64 = docker.build registry + ":arm64-1.0.$BUILD_NUMBER"
                }
            }
        }
        stage ('push images to dockerhub') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                        dockerImage_arm64.push()
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