pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling the latest code from GitHub...'
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Installing required python packages...'
                # This installs the tools locally inside Jenkins
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Python Tests') {
            steps {
                echo 'Running python test script...'
                bat 'python test_app.py'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up the workspace...'
            cleanWs()
        }
    }
}
