pipeline {
    
    agent { docker { image 'python:latest' } }
    stages {
        stage('Poetry Configuration') {
            steps {
                sh "curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python"
                sh "$HOME/.poetry/bin/poetry install --no-root"
            }
        }
	    stage('run_unit_tests') {
            steps {
		        sh '$HOME/.poetry/bin/poetry run pytest tests/'
            }
        }
    }
}