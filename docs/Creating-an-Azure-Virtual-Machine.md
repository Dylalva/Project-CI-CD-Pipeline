---
title: Creating an Azure Virtual Machine
description: Step-by-step guide to set up a CI/CD pipeline for a Flask app using Jenkins and AKS on Azure, including prerequisites and environment setup.
---
## 📖 Project Description

In this second part of the **Networks Project**, we implement a **CI/CD pipeline** for a **Python (Flask)** web application, fully **containerized** and deployed on **Azure Kubernetes Service (AKS)**. The overall flow is:

1. The source code lives in a **GitHub repository**.
2. A **Jenkins server**, hosted on an **Azure virtual machine**, detects each push and:

   * Builds the Docker image of the application.
   * Pushes it to **Docker Hub** (or **Azure Container Registry**).
3. An **AKS cluster** pulls the new image and automatically deploys the application.

With this pipeline, we achieve faster, more reliable, and reproducible deliveries of our Flask app.

---

## 🔍 Workflow

1. **Push** to GitHub →
2. **Jenkins (Azure VM)** detects the change →
3. Builds and pushes the **Docker image** →
4. Updates your **AKS cluster** →
5. App Running on Azure.

---

## 🧰 Technologies and Tools

* **Python 3.x** and **Flask**
* **Docker** (for building images and containers)
* **Jenkins** (installed on an Azure VM) / **GitHub Actions**
* **Docker Hub**
* **Azure Kubernetes Service (AKS)**
* **Azure CLI** and **kubectl**

---

## 📋 Prerequisites

Before getting started, make sure you have:

1. An active **Azure Subscription**.
2. An **Azure VM** with Jenkins installed and accessible.
3. A **Docker Hub account** (or ACR) and credentials ready.
4. An **AKS Cluster** created, with `kubectl` configured on the Jenkins VM.
5. **Azure CLI** and **kubectl** installed wherever you’ll run the commands.
6. Access to the **GitHub repository** containing your Flask code and a ready `Dockerfile`.

---

## 🚀 Steps to Set Up the Entire Environment

1. ### Clone the Repository

   ```bash
   git clone https://github.com/Dylalva/Parte2Redes.git
   cd Parte2Redes
   ```

   Here you’ll find:

   ```
   .
   ├── app.py
   ├── Dockerfile
   ├── requirements.txt
   ├── .dockerignore
   ├── static/
   └── templates/
   ```

2. ### Configure Jenkins on Your Azure VM

   #### Create the **Azure VM**

   [Create VM in Azure](Creación-de-la-VM-en-Azure)

   #### Install and Set Up Jenkins on the **Azure VM**

   [Jenkins Installation and Configuration](Instalación-y-Configuración-de-Jenkins)

   * Install the **Docker**, **Git**, and **Azure CLI** plugins.
   * Create **Credentials** for:

     * **Docker Hub** (username/password).
     * **Azure Service Principal** (for `az aks get-credentials`).
     * **GitHub** (if your repo is private).

3. ### Define the Pipeline in Jenkins

   * Use either a **Freestyle Job** or a **Pipeline Job** with a `Jenkinsfile`.

   > In this repository, you’ll find a `Jenkinsfile`.

   > Note: [Link GitHub Repository with Jenkins](Link-GitHub-Repository-with-Jenkins)

4. ### Create the Kubernetes Cluster

   * [Create Kubernetes Cluster in Azure](Creación-de-Kubernetes-Cluster-en-Azure)

5. ### Final Test

   * Make a **PUSH** to the main branch of your GitHub repo.
   * Watch Jenkins trigger the pipeline.
   * Once it finishes, go to your **Load Balancer** or configured domain to see the Flask app running in production.

