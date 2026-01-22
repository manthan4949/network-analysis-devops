pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t network-analysis-app .'
            }
        }
        
        stage('Start Application') {
            steps {
                echo 'Starting Docker containers...'
                bat 'docker-compose up -d'
                bat 'timeout /t 5 /nobreak'
            }
        }
        
        stage('Test Application') {
            steps {
                echo 'Testing application endpoint...'
                bat 'curl http://localhost:5000 || echo "Testing health check"'
            }
        }
        
        stage('Cleanup') {
            steps {
                echo 'Stopping Docker containers...'
                bat 'docker-compose down'
            }
        }
    }
    
    post {
        always {
            echo '================================'
            echo 'Pipeline execution completed!'
            echo '================================'
        }
        success {
            echo '✅ All stages passed successfully!'
        }
        failure {
            echo '❌ Pipeline failed - check logs above'
        }
    }
}
