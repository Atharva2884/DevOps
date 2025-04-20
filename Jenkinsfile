pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/yourusername/student-feedback-flask.git'
            }
        }
        stage('Install Requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Unit Test') {
            steps {
                sh 'python -m unittest test_app.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t student-feedback:latest .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 student-feedback:latest'
            }
        }
    }
}
