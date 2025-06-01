![DockerPythonKubernetes](https://miro.medium.com/v2/resize:fit:1400/1*YwBcLMOQsPMcscrXPXLFyw.png)

# CI/CD Pipeline para Aplicación Flask con Docker y Kubernetes en Azure

---

## Descripción

En esta segunda parte, construiremos un **pipeline** básico para una aplicación desarrollada en Python (Flask) basada en contenedores. El flujo consistirá en:

1. **Repositorio en GitHub**  
   - Código fuente de la app Flask.  
   - `Dockerfile` para construir la imagen.

2. **Servidor CI/CD** (Jenkins o Azure DevOps)  
   - Se conecta al repositorio y, ante cada push, dispara la construcción y publicación de la imagen Docker.

3. **Despliegue en Kubernetes en Azure**  
   - Cluster AKS (Azure Kubernetes Service).  
   - Hace pull de la imagen y corre la aplicación en contenedores.

---

## Flujo de Trabajo

1. **Push** al repo en GitHub →  
2. CI/CD detecta el cambio →  
3. Clona el repo, construye la imagen y la publica en Docker Hub (o ACR) →  
4. Actualiza y aplica los manifiestos en AKS →  
5. La aplicación Flask queda corriendo en Azure Kubernetes Service.

---

## Requisitos Previos

- Cuenta y repo en **Docker Hub** o **Azure Container Registry**.  
- **Jenkins** o **Azure DevOps** con acceso al repo de GitHub.  
- **Azure CLI** instalado y autenticado.  
- Cluster **AKS** ya creado o listo para crear.

---

## Estructura del Repositorio

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
```
## Documentación

Puedes ver la documentación completa en nuestra [Wiki](https://github.com//Dylalva/Proyecto2Redes/wiki).
