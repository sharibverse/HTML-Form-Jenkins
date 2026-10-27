
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sharibverse/HTML-Form-Jenkins.git'
            }
        }

        stage('Test HTML Form') {
            steps {
                bat 'py -m unittest test_form.py'
            }
        }
    }
}
