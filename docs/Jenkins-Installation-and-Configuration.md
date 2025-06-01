# 📋 Requirements:

Before starting, make sure you have:

1. An active **Azure Subscription**.
2. An **Azure VM** with Jenkins installed and accessible.
3. A **Docker Hub account** (or ACR) and available credentials.
4. An **AKS cluster** created, with `kubectl` configured on **Azure**.

---

# Installing **Jenkins**

For this project, we will use Jenkins from a Docker image, so we need to install it on the virtual machine.

## 1. Install Docker on the VM

```bash
sudo apt-get update
sudo apt-get install -y docker.io
```

## 2. Pull the Jenkins image

```bash
sudo docker pull jenkins/jenkins
```

### 3. Run the Jenkins container

```bash
sudo docker run -d \
  --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts
```

### 4. Verify if the container is running:

```bash
sudo docker ps
```

### 5. Enter the container:

```bash
sudo docker exec -u 0 -it jenkins bash
```

### 6. Install **kubectl** inside the container

```bash
curl -LO "https://dl.k8s.io/release/$(curl -sL https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
mv kubectl /usr/local/bin/
```

### 7. Install **az** CLI inside the container

```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | bash
```

## 8. Install Docker inside the container

```bash
apt-get update
apt-get install -y docker.io
```

---

# Jenkins Configuration

To configure Jenkins from your local machine, use the public IP address you use to connect to the VM and add `:8080`.
You will be prompted for an initial password which you can get from the VM with the following command:

```bash
sudo docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

When you log in to **Jenkins** for the first time, choose to install the recommended plugins, then create your user.
Registering the Jenkins user will provide you the URL to access Jenkins, e.g., `http://40.90.193.112:8080/`

---

## Creating and Configuring a Pipeline in Jenkins

1. **Create a new job**

   * On the Jenkins Dashboard, click **"Create a job"** or **"New Item"**.
   * Enter the project name (for example: `ci-cd-kube`).
   * Select the project type **Pipeline**.
   * Click **OK**.

2. **Configure Git repository**

   * In the pipeline configuration section, under **SCM**, select **Git**.
   * Enter the repository URL: `https://github.com/Dylalva/PruebasRedes.git`.
   * Select credentials if needed (not used in this case).

3. **Configure triggers**

   * Under the **Triggers** tab, enable **GitHub hook trigger for GITScm polling** to automatically run the pipeline on every push.

4. **Define pipeline from SCM**

   * In the **Pipeline** section, change the definition from **Pipeline script** to **Pipeline script from SCM**.
   * This tells Jenkins to use a `Jenkinsfile` located in the repository to define the pipeline stages.

5. **Save the configuration**

   * Finally, click **Save** or **Apply** to save the configuration and activate the pipeline.

---

## Jenkins Plugins Installation Summary

1. **Enter Jenkins management**

   * From Jenkins main panel, select **Manage Jenkins**.

2. **Access plugins section**

   * Inside management, click **Manage Plugins**.

3. **Search available plugins**

   * Go to the **Available** tab.
   * Use the search bar to find plugins, e.g., search for `azure`.

4. **Select and install plugins**

   * Select plugins to install such as **Azure Credentials**, **Azure CLI**, **Docker**, and **Docker Pipeline**.
   * Click **Install** to start the installation.

5. **Wait for installation to finish**

   * Jenkins will download and install the plugins.
   * Once installed, configure them as necessary.

> Note: If needed, restart the Jenkins docker container using:

```bash
sudo docker restart jenkins
```

---

## Adding Credentials in Jenkins

1. **Go to Jenkins Management**

   * From the main panel, select **Manage Jenkins**.

2. **Access Credentials section**

   * Inside management, click **Credentials**.

3. **Select global domain**

   * In credentials view, select **Global credentials (unrestricted)** to add credentials available globally.

4. **Add new credentials**

   * Click **Add Credentials** or **+ Add Credentials**.

5. **Fill out new credential information**

   * For **Kind**, select **Username with password**.
   * For **Scope**, select usually **Global**.
   * Enter the **Username** and **Password**.
   * Provide a unique **ID** for the credential (e.g., `dockerhub-cred`).
   * Optionally add a description for easier identification.

> Note: [How to obtain Docker Hub credentials](How-to-obtain-Docker-Hub-credentials)

6. **Save credentials**

   * Click **Create** to save.

7. **Add Azure-specific credentials**

   * For **Kind**, select **Azure Service Principal**.
   * Add Client Secret, Tenant ID, and configure Azure environment.
   * Assign a unique ID like `azure-service-principal` to be used in pipelines.

> Note: Credential IDs must match those used in the `Jenkinsfile`.
> Note: [How to obtain Azure credentials](How-to-obtain-Azure-credentials)

---

And **Done**, now you have your **pipeline**!!

## Attachments

![Screenshot 1](https://github.com/user-attachments/assets/5edd6ec8-c0dd-4cb4-a0ba-e4132d4c2977)
![Screenshot 2](https://github.com/user-attachments/assets/e40c2019-2e65-454e-bc4b-845101eeb279)
![Screenshot 3](https://github.com/user-attachments/assets/09e9a015-8e21-4b71-b2d2-80244975f0d9)
![Screenshot 4](https://github.com/user-attachments/assets/90fddfdd-b457-4950-a4ef-4a183b0b8b87)
![Screenshot 5](https://github.com/user-attachments/assets/2edc197a-7fb8-420d-b055-c55e5e4ce4db)
![Screenshot 6](https://github.com/user-attachments/assets/2ab1aba1-ba37-4cdf-a514-1bfe56bd2e4d)
![Screenshot 7](https://github.com/user-attachments/assets/0f4d76c6-6ce5-4b2d-8633-edbc46c8592e)
![Screenshot 8](https://github.com/user-attachments/assets/ffc97811-69e2-4668-b563-9bec84aacbad)
![Screenshot 9](https://github.com/user-attachments/assets/ee39aec0-de35-4056-9be4-be8ecc54484c)
![Screenshot 10](https://github.com/user-attachments/assets/e1698ab7-5584-40a9-ae5a-49d9f42d7557)
![Screenshot 11](https://github.com/user-attachments/assets/fbf3d04c-40c4-46e0-8532-45ec907a0898)
![Screenshot 12](https://github.com/user-attachments/assets/ef62b3b1-59e2-4314-9e4f-5fc0a38d9281)
![Screenshot 13](https://github.com/user-attachments/assets/3745fe3b-b6ef-4b81-a593-f5bcfecc2cfa)