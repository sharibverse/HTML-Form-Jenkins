
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/sharibverse/HTML-Form-Jenkins.git'
            }
        }

        stage('Test HTML Form') {
            steps {
                bat '"C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m unittest test_form.py'
            }
        }
    }
}
