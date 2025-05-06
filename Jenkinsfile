pipeline {
    agent any
    environment {
        IMAGE_NAME = 'dylalva/parte2redes'
        DOCKERHUB_CREDS = 'dockerhub-cred'  // Cambia esto por el ID de tu credencial de Docker Hub en Jenkins
        AZURE_CREDS = 'azure-service-principal'   // Cambia esto por el ID de tus credenciales de Azure en Jenkins
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout del código fuente desde Git
                checkout scm
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    // Realizar login directamente con el comando 'sh' para evitar problemas de seguridad
                    withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDS, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login --username $DOCKER_USERNAME --password-stdin'
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Construir la imagen Docker con el tag 'latest'
                    docker.build("${IMAGE_NAME}:latest", ".")
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    // Push de la imagen construida a Docker Hub
                    withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDS, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'docker push ${IMAGE_NAME}:latest'
                    }
                }
            }
        }

        stage('Azure Login') {
            steps {
                script {
                    // Iniciar sesión en Azure usando las credenciales de Jenkins
                    azureLogin(credId: AZURE_CREDS)
                }
            }
        }

        stage('Deploy to AKS') {
            steps {
                script {
                    // Configuración de kubectl para Azure Kubernetes Service (AKS)
                    sh 'az aks get-credentials --resource-group k8spruebas --name PRUEBA'

                    // Desplegar los manifiestos de Kubernetes
                    sh 'kubectl apply -f manifests/deployment.yaml'
                    sh 'kubectl apply -f manifests/service.yaml'

                    // Reiniciar el deployment
                    sh 'kubectl rollout restart deployment parte2redes-deployment -n default'
                }
            }
        }
    }
}
