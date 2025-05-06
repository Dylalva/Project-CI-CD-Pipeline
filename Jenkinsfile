pipeline {
    agent any
    environment {
        IMAGE_NAME = 'dylalva/parte2redes'
        DOCKERHUB_CREDS = 'dockerhub-creds'  // Cambia esto por el ID de tu credencial de Docker Hub en Jenkins
        AZURE_CREDS = 'azure-credentials'   // Cambia esto por el ID de tus credenciales de Azure en Jenkins
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Login to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://docker.io', credentialsId: DOCKERHUB_CREDS) {
                        // Aquí puedes hacer algo si es necesario
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:latest", ".")
                }
            }
        }
        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://docker.io', credentialsId: DOCKERHUB_CREDS) {
                        docker.image("${IMAGE_NAME}:latest").push()
                    }
                }
            }
        }
        stage('Azure Login') {
            steps {
                script {
                    azureLogin(credId: AZURE_CREDS)
                }
            }
        }
        stage('Deploy to AKS') {
            steps {
                script {
                    // Configurar kubectl
                    sh 'az aks get-credentials --resource-group k8spruebas --name PRUEBA'

                    // Desplegar los manifiestos
                    sh 'kubectl apply -f manifests/deployment.yaml'
                    sh 'kubectl apply -f manifests/service.yaml'

                    // Hacer un restart del deployment
                    sh 'kubectl rollout restart deployment parte2redes-deployment -n default'
                }
            }
        }
    }
}
