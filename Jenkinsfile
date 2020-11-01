pipeline {
    agent { docker { image 'python:latest' } }
    stages {
        stage('install_enigma') {
            steps {
                sh 'python -m pip -U install --upgrade pip'
                sh 'python -m pip -U install poetry'
                sh 'poetry install'
            }
        }
	    stage('run_unit_tests') {
            steps {
		        sh 'poetry run pytest tests/'
            }
        }
    }
}