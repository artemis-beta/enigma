pipeline {
    agent { docker { image 'python:latest' } }
    stages {
        stage('install_enigma') {
            steps {
                sh 'python -m pip install --upgrade pip'
		sh 'python -m pip install poetry'
		sh 'poetry install'
            }
	}
	stage('run_unit_tests') {
		sh 'poetry run pytest tests/'
        }
    }
}
