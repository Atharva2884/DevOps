pipeline {
    agent any
    environment {
        DOCKER_USERNAME = credentials('docker-username')
        DOCKER_PASSWORD = credentials('docker-password')
        BUILD_NUMBER = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                // Use the checkout step to ensure clean clone
                checkout([$class: 'GitSCM', 
                    branches: [[name: 'main']], 
                    doGenerateSubmoduleConfigurations: false, 
                    extensions: [[$class: 'CleanBeforeCheckout']], 
                    userRemoteConfigs: [[url: 'https://github.com/Atharva2884/DevOps.git']]
                ])
            }
        }

        stage('Install Requirements') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'python -m unittest test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Add --no-cache to force rebuilding
                bat 'docker build --no-cache -t %DOCKER_USERNAME%/feedback-app:latest -t %DOCKER_USERNAME%/feedback-app:%BUILD_NUMBER% .'
            }
        }

        stage('Push Docker Image') {
            steps {
                bat '''
                    echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin
                    docker push %DOCKER_USERNAME%/feedback-app:latest
                    docker push %DOCKER_USERNAME%/feedback-app:%BUILD_NUMBER%
                '''
            }
        }
    }
}