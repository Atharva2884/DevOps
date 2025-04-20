pipeline {
    agent any
    environment {
        DOCKERHUB_USERNAME = credentials('atharvaurankar')
        DOCKERHUB_PASSWORD = credentials('123456789')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/student-feedback-manager.git'
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
                bat 'docker build -t $DOCKERHUB_USERNAME/feedback-app:latest .'
            }
        }

        stage('Push Docker Image') {
            steps {
                bat '''
                    echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin
                    docker push $DOCKERHUB_USERNAME/feedback-app:latest
                '''
            }
        }
    }
}
