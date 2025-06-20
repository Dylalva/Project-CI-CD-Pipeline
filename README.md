
![DockerPythonKubernetes](https://miro.medium.com/v2/resize:fit:1400/1*YwBcLMOQsPMcscrXPXLFyw.png)
![Python Version](https://img.shields.io/badge/python-3.10+-blue)
![GitHub issues](https://img.shields.io/github/issues/Dylalva/Project-CI-CD-Pipeline)
![GitHub top language](https://img.shields.io/github/languages/top/Dylalva/Project-CI-CD-Pipeline)
![License](https://img.shields.io/github/license/Dylalva/Project-CI-CD-Pipeline)
![Docker Image Size](https://img.shields.io/docker/image-size/dylalva/project-ci-cd/latest)
<details>
<summary><h2>English</h2></summary>
   
# CI/CD Pipeline for Flask Application with Docker and Kubernetes on Azure

---

## Description

In this project, we build a **basic pipeline** for a Python (Flask) application based on containers. The workflow is as follows:

1. **GitHub Repository**
   - Flask app source code.
   - `Dockerfile` to build the image.

2. **CI/CD Server** (Jenkins or Azure DevOps)
   - Connects to the repository and, on each push, triggers the build and publishing of the Docker image.

3. **Deployment on Kubernetes in Azure**
   - AKS cluster (Azure Kubernetes Service).
   - Pulls the image and runs the application in containers.

---

## Technologies Used

This project leverages the following core technologies and tools:

- **Python**: Main language for the application, using the Flask web framework.
- **HTML and CSS**: For frontend and user interface.
- **Docker**: For containerization and application deployment.
- **Jenkins**: Continuous Integration server to automate building, testing, and deployment.
- **Azure Kubernetes Service (AKS)**: Container orchestrator for cloud deployment.
- **Azure CLI**: For Azure resource management via command line.
- **Terraform (HCL)**: Infrastructure as Code for provisioning resources in Azure.
- **GitHub Actions**: Workflow automation directly from the repository (alternative/support to Jenkins).
- **Docker Hub / Azure Container Registry (ACR)**: Storage and management for container images.
- **Firebase**: Used for authentication (login) and as a database for managing application data.

---

## Workflow

1. **Push** to the GitHub repo →
2. CI/CD detects the change →
3. Clones the repo, builds the image, and publishes it to Docker Hub (or ACR) →
4. Updates and applies the manifests in AKS →
5. The Flask application runs on Azure Kubernetes Service.

---

## Prerequisites

- Account and repo in **Docker Hub** or **Azure Container Registry**.
- **Jenkins** or **Azure DevOps** with access to the GitHub repo.
- **Azure CLI** installed and authenticated.
- **AKS** cluster already created or ready to create.

---

## Repository Structure

```plaintext
.
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── app.py
├── firebase_auth.py
├── cafe-data.csv
├── requirements.txt
├── .github/
│   └── workflows/
│       ├── aks-k8s-setup.yml
│       ├── conf-jenkins.yml
│       ├── deploy-azure.yml
│       ├── jekyll.yml
│       └── publish-package.yml
├── docs/
├── infrastructure/
│   ├── VM-Jenkins_key
│   ├── VM-Jenkins_key.pub
│   ├── hosts.ini
│   ├── jenkins-configure.yml
│   ├── jenkins-credentials.yml
│   ├── jenkins-install.yml
│   ├── jenkins-setup.yml
│   └── main.tf
├── infrastructurek8s/
│   ├── cert-manager-setup.yml
│   └── main.tf
├── manifests/
│   ├── cluster-issuer.yaml
│   ├── deployment.yaml
│   ├── ingress.yaml
│   └── service.yaml
├── static/
│   └── css/
│       └── styles.css
├── templates/
│   ├── add.html
│   ├── base.html
│   ├── blog.html
│   ├── cafes.html
│   ├── guess.html
│   ├── index.html
│   └── login.html
```

Thank you very much for taking the time to visit this repository! I am always open to suggestions, comments, or feedback that could help improve this project. Please feel free to open an issue or contact me if you have ideas for optimization, fixes, or new features. Your input is highly appreciated!

</details>

<details>
<summary><h2>Español</h2></summary>

# Canalización CI/CD para una aplicación Flask con Docker y Kubernetes en Azure

---

## Descripción

En este proyecto se construye una **canalización básica** para una aplicación desarrollada en Python (Flask) basada en contenedores. El flujo de trabajo es el siguiente:

1. **Repositorio de GitHub**
   - Código fuente de la aplicación Flask.
   - `Dockerfile` para construir la imagen.

2. **Servidor CI/CD** (Jenkins o Azure DevOps)
   - Se conecta al repositorio y, en cada push, dispara la construcción y publicación de la imagen Docker.

3. **Despliegue en Kubernetes en Azure**
   - Cluster AKS (Azure Kubernetes Service).
   - Descarga la imagen y ejecuta la aplicación en contenedores.

---

## Tecnologías Utilizadas

Este proyecto utiliza las siguientes tecnologías y herramientas principales:

- **Python**: Lenguaje principal de la aplicación, usando el framework Flask.
- **HTML y CSS**: Para la interfaz de usuario y el frontend.
- **Docker**: Para contenerización y despliegue de la aplicación.
- **Jenkins**: Servidor de Integración Continua para automatizar construcción, pruebas y despliegue.
- **Azure Kubernetes Service (AKS)**: Orquestador de contenedores para despliegue en la nube.
- **Azure CLI**: Para la gestión de recursos en Azure desde la línea de comandos.
- **Terraform (HCL)**: Infraestructura como código para el aprovisionamiento de recursos en Azure.
- **GitHub Actions**: Automatización de flujos de trabajo desde el repositorio (alternativa/soporte a Jenkins).
- **Docker Hub / Azure Container Registry (ACR)**: Almacenamiento y gestión de imágenes de contenedor.
- **Firebase**: Utilizado para autenticación (login) y como base de datos para el manejo de datos de la aplicación.

---

## Flujo de Trabajo

1. **Push** al repositorio de GitHub →
2. El CI/CD detecta el cambio →
3. Clona el repo, construye la imagen y la publica en Docker Hub (o ACR) →
4. Actualiza y aplica los manifiestos en AKS →
5. La aplicación Flask corre en Azure Kubernetes Service.

---

## Prerrequisitos

- Cuenta y repositorio en **Docker Hub** o **Azure Container Registry**.
- **Jenkins** o **Azure DevOps** con acceso al repositorio de GitHub.
- **Azure CLI** instalada y autenticada.
- **Cluster AKS** ya creado o listo para crearse.

---

## Estructura del Repositorio

```plaintext
.
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── app.py
├── firebase_auth.py
├── cafe-data.csv
├── requirements.txt
├── .github/
│   └── workflows/
│       ├── aks-k8s-setup.yml
│       ├── conf-jenkins.yml
│       ├── deploy-azure.yml
│       ├── jekyll.yml
│       └── publish-package.yml
├── docs/
├── infrastructure/
│   ├── VM-Jenkins_key
│   ├── VM-Jenkins_key.pub
│   ├── hosts.ini
│   ├── jenkins-configure.yml
│   ├── jenkins-credentials.yml
│   ├── jenkins-install.yml
│   ├── jenkins-setup.yml
│   └── main.tf
├── infrastructurek8s/
│   ├── cert-manager-setup.yml
│   └── main.tf
├── manifests/
│   ├── cluster-issuer.yaml
│   ├── deployment.yaml
│   ├── ingress.yaml
│   └── service.yaml
├── static/
│   └── css/
│       └── styles.css
├── templates/
│   ├── add.html
│   ├── base.html
│   ├── blog.html
│   ├── cafes.html
│   ├── guess.html
│   ├── index.html
│   └── login.html
```
¡Gracias por visitar este repositorio!  
Estoy abierto a cualquier sugerencia, comentario o recomendación que ayude a mejorar este proyecto. No dudes en abrir un issue o contactarme si tienes ideas para optimizar, corregir o extender la funcionalidad. ¡Tu retroalimentación es siempre bienvenida!
</details>
