![DockerPythonKubernetes](https://miro.medium.com/v2/resize:fit:1400/1*YwBcLMOQsPMcscrXPXLFyw.png)
   
   # CI/CD Pipeline for Flask Application with Docker and Kubernetes on Azure
   
   ---
   
   ## Description
   
   In this project, we will build a **basic pipeline** for an application developed in Python (Flask) based on containers. The workflow will consist of:
   
   1. **GitHub Repository**
      - Flask app source code.
      - `Dockerfile` to build the image.
   
   2. **CI/CD Server** (Jenkins or Azure DevOps)
      - Connects to the repository and, on each push, triggers the build and publishing of the Docker image.
   
   3. **Deployment on Kubernetes in Azure**
      - AKS cluster (Azure Kubernetes Service).
      - Pulls the image and runs the application in containers.
   
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
   ├── .github/
   │   └── workflows/
   │       └── docker-push.yml
   ├── app.py
   ├── cafe-data.csv
   ├── Dockerfile
   ├── .dockerignore
   ├── requirements.txt
   ├── static/
   │   └── css/
   │       └── styles.css
   ├── templates/
   │   ├── add.html
   │   ├── base.html
   │   ├── blog.html
   │   ├── cafes.html
   │   ├── guess.html
   │   └── index.html
   └── README.md