pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling the latest code from GitHub...'
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
            // This deletes the downloaded files so your laptop drive stays clean
            cleanWs()
        }
    }
}
