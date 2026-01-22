pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 1, unit: 'HOURS')
        timestamps()
    }

    environment {
        REGISTRY = 'docker.io'
        IMAGE_NAME = 'network-analysis-app'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('1. Build') {
            steps {
                echo '========== Stage 1: Build =========='
                sh 'echo "Building Docker image..."'
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
                sh 'docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest'
                sh 'echo "Build stage completed successfully"'
            }
        }

        stage('2. Test') {
            steps {
                echo '========== Stage 2: Test =========='
                sh 'echo "Running unit tests..."'
                sh 'python -m pytest tests/unit_tests.py -v --cov=. --cov-report=xml'
                sh 'echo "Test stage completed successfully"'
            }
        }

        stage('3. Code Quality') {
            steps {
                echo '========== Stage 3: Code Quality =========='
                sh 'echo "Analyzing code quality..."'
                sh 'pip install pylint flake8 > /dev/null 2>&1 || true'
                sh 'flake8 app.py database_utils.py || true'
                sh 'pylint app.py --disable=all --enable=E,F -j 4 || true'
                sh 'echo "Code quality analysis completed"'
            }
        }

        stage('4. Security') {
            steps {
                echo '========== Stage 4: Security =========='
                sh 'echo "Performing security scan..."'
                sh 'pip install bandit safety > /dev/null 2>&1 || true'
                sh 'bandit -r . -f json -o bandit-report.json || true'
                sh 'safety check --json || true'
                sh 'echo "Security scan completed"'
            }
        }

        stage('5. Deploy') {
            steps {
                echo '========== Stage 5: Deploy =========='
                sh 'echo "Deploying application with Docker Compose..."'
                sh 'docker-compose up -d'
                sh 'sleep 5'
                sh 'docker ps -a | grep network-analysis'
                sh 'echo "Deployment completed"'
            }
        }

        stage('6. Release') {
            steps {
                echo '========== Stage 6: Release =========='
                sh 'echo "Creating release tags..."'
                sh 'docker tag ${IMAGE_NAME}:latest ${IMAGE_NAME}:v${BUILD_NUMBER}'
                sh 'echo "Release stage completed"'
            }
        }

        stage('7. Monitoring') {
            steps {
                echo '========== Stage 7: Monitoring =========='
                sh 'echo "Verifying application health..."'
                sh 'curl -f http://localhost:5000 || echo "Waiting for app to start..."'
                sh 'sleep 3'
                sh 'curl -f http://localhost:5000/health || true'
                sh 'echo "Monitoring checks completed"'
                sh 'docker-compose down || true'
            }
        }
    }

    post {
        always {
            echo '========== Pipeline Cleanup =========='
            sh 'echo "Pipeline execution completed at $(date)"'
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
