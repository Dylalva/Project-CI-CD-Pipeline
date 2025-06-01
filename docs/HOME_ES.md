---
title: Pipeline CI/CD para Flask en Azure
description: Implementación de un pipeline CI/CD para una aplicación Flask contenedorizada y desplegada en Azure Kubernetes Service (AKS).
---
## 📖 Descripción del Proyecto

En este proyecto, implementamos un **pipeline de CI/CD** para una aplicación web en **Python (Flask)**, totalmente **contenedorizada** y desplegada en **Azure Kubernetes Service (AKS)**. El flujo general es:

1. El código fuente vive en un **repositorio GitHub**.
2. Un **servidor Jenkins**, alojado en una **máquina virtual de Azure**, detecta cada *push* y:

   * Construye la imagen Docker de la aplicación.
   * La sube a **Docker Hub** (o **Azure Container Registry**).
3. Un **cluster AKS** extrae la nueva imagen y despliega la aplicación automáticamente.

Con este pipeline logramos entregas más rápidas, confiables y reproducibles de nuestra app Flask.

---

## 🔍 Flujo de Trabajo

1. **Push** en GitHub →
2. **Jenkins (VM Azure)** detecta cambio →
3. Construye y empuja la **imagen Docker** →
4. Actualiza tu **cluster AKS** →
5. App Corriendo en Azure.

---

## 🧰 Tecnologías y Herramientas

* **Python 3.x** y **Flask**
* **Docker** (para construir imágenes y contenedores)
* **Jenkins** (instalado en una VM de Azure) / **GitHub Actions**
* **Docker Hub**
* **Azure Kubernetes Service (AKS)**
* **Azure CLI** y **kubectl**

---

## 📋 Requisitos Previos

Antes de empezar, asegúrate de tener:

1. **Azure Subscription** activa.
2. Una **VM en Azure** con Jenkins instalado y accesible.
3. **Cuenta en Docker Hub** (o ACR) y credenciales disponibles.
4. **Cluster AKS** creado, con `kubectl` configurado en la VM de Jenkins.
5. **Azure CLI** y **kubectl** instalados donde vayamos a ejecutar comandos.
6. Acceso al **repositorio GitHub** con tu código Flask y `Dockerfile` listo.

---

## 🚀 Pasos para Montar Todo el Entorno

1. ### Clona el Repositorio

   ```bash
   git clone https://github.com/Dylalva/Parte2Redes.git
   cd Parte2Redes
   ```

   Aquí encontrarás:

   ```
   .
   ├── app.py
   ├── Dockerfile
   ├── requirements.txt
   ├── .dockerignore
   ├── static/
   └── templates/
   ```

2. ### Configura Jenkins en tu VM de Azure
   #### Creación de la VM de **Azure**
   [Crear VM en Azure](Creación-de-la-VM-en-Azure)
   #### Instalación y creación de Jenkins en la VM de **Azure**
   [Instalación y Configuración de Jenkins](Instalación-y-Configuración-de-Jenkins)

   * Instala los plugins de **Docker**, **Git** y **Azure CLI**.
   * Crea **Credentials** para:

     * **Docker Hub** (usuario/password).
     * **Azure Service Principal** (para `az aks get-credentials`).
     * **GitHub** (si tu repo es privado).

3. ### Define el Pipeline en Jenkins

   * **Freestyle Job** o **Pipeline Job** con un `Jenkinsfile`.
   > En este Repositorio se encuentra un archivo `Jenkinsfile`.

   > Nota: [Vincular Repositorio con Jenkins](Vincular-Repositorio-con-Jenkins)


4. ### Crear Kubernetes Cluster
   * [Crear Kubernetes Cluster en Azure](Creación-de-Kubernetes-Cluster-en-Azure)

5. ### Prueba Final

   * Haz un **PUSH** a la rama principal de tu repo GitHub.
   * Observa en Jenkins cómo se dispara el pipeline.
   * Una vez termine, entra a tu **Load Balancer** o dominio configurado para ver la app Flask en producción.