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
                bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" build -t network-analysis-app .'
            }
        }
        
        stage('Start Application') {
            steps {
                echo 'Starting Docker containers...'
                bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" compose up -d'
            }
        }
        
        stage('Verify Running') {
            steps {
                echo 'Verifying containers are running...'
                bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" ps'
            }
        }
        
        stage('Cleanup') {
            steps {
                echo 'Stopping Docker containers...'
                bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" compose down'
            }
        }
    }
    
    post {
        success {
            echo '✅ All stages passed successfully!'
        }
        failure {
            echo '❌ Pipeline failed - check logs above'
        }
    }
}
