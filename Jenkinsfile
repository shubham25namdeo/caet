pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo '$PATH'
                sh 'pip install -r requirements.txt'
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}