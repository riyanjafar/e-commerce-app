pipeline {
    agent any
    
    stages {
        stage('Kodları Çek') {
            steps {
                checkout scm
            }
        }
        
        stage('Derleme') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                sh 'pytest tests/'
            }
        }
        
        stage('Docker İmajını Oluştur') {
            steps {
                sh 'docker build -t e-commerce-app:latest .'
            }
        }
        
        stage('Yayına Al') {
            steps {
                sh '''
                    docker stop e-commerce-app || true
                    docker rm e-commerce-app || true
                    docker run -d -p 5000:5000 --name e-commerce-app e-commerce-app:latest
                '''
            }
        }
    }
    
    post {
        success {
            echo 'Yayına alma işlemi başarıyla tamamlandı!'
        }
        failure {
            echo 'Yayına alma işlemi sırasında bir hata oluştu'
        }
    }
}
