pipeline {
    environment {
        registry = "clrosier/auth"
        registryCredential = 'dockerhub'
    }

    agent any

    stages {
        stage ('Building image') {
            steps {
                script {
                    image = docker.build registry + ":$VERSION.$BUILD_NUMBER"
                }
            }
        }

        stage ('Push image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        image.push()
                        image.push('latest')
                    }
                }
            }
        }

        stage ('Cleanup') {
            steps {
                script {
                    sh "docker rmi $registry:$VERSION.$BUILD_NUMBER"
                    sh "docker rmi $registry:latest"
                }
            }
        }
    }
}
