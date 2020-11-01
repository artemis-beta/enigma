pipeline {
    agent { docker { image 'python:latest' } }
    stages {
        stage('install_enigma') {
            steps {
                sh 'python -m pip install -U --upgrade pip'
                sh 'python -m pip install -U poetry'
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