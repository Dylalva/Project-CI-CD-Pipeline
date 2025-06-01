# 📋 Requisitos:

Antes de empezar, asegúrate de tener:

1. **Azure Subscription** activa.
2. Una **VM en Azure** con Jenkins instalado y accesible.
3. **Cuenta en Docker Hub** (o ACR) y credenciales disponibles.
4. **Cluster AKS** creado, con `kubectl` configurado en **Azure**.

# Instalación de **Jenkins**

Para este proyecto vamos a utilizar Jenkins desde una imagen de docker, por lo que necesitamos instalarlo en la máquina virtual.
## 1. Descargar Docker en la VM

```Bash
sudo apt-get update
sudo apt-get install -y docker.io
```

## 2. Descargar la imagen de Jenkins
```bash
sudo docker pull jenkins/jenkins
```

### 3. Ejecución del contenedor con la imagen de Jenkins
```Bash
sudo docker run -d \
  --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts
```

### 4. Verificar si esta corriendo el contenedor:

```Bash
sudo docker ps
```

### 5. Entrar en el contenedor:

```Bash
sudo docker exec -u 0 -it jenkins bash
```

### 6. Instalar **kubectl** en el Contenedor

```Bash
curl -LO "https://dl.k8s.io/release/$(curl -sL https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
mv kubectl /usr/local/bin/
```

### 7. Instalar *az** en el contenedor

```Bash
curl -sL https://aka.ms/InstallAzureCLIDeb | bash
```

## 8. Descargar Docker en el contenedor

```Bash
apt-get update
apt-get install -y docker.io
```
---

# Configuración de **Jenkins**

Para realizar la configuración de Jenkins desde su máquina local utilice la dirección ip pública que utilizo para conectarse a la VM y agrege `:8080`.
Esto le solicitara una contraseña inicial la cuál puede obtener desde la máquina virtual con el siguiente comando:

```Bash
sudo docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Al entrar por primera vez en **Jenkins** dele la opción de descargar los `plugins` recomendados, luego cree su usuario.
El registrar el usuario **Jenkins** le dará la dirección con la cual puede acceder, Ej: `http://40.90.193.112:8080/`

---

## Creación y configuración de un Pipeline en Jenkins

1. **Crear nueva tarea (job)**

   * En el Dashboard de Jenkins, da clic en **"Create a job"** o **"Nueva Tarea"**.
   * Escribe el nombre del proyecto (por ejemplo: `ci-cd-kube`).
   * Selecciona el tipo de proyecto **Pipeline**.
   * Da clic en **OK**.

2. **Configurar repositorio Git**

   * En la sección de configuración del pipeline, bajo **SCM**, selecciona **Git**.
   * Introduce la URL del repositorio: `https://github.com/Dylalva/PruebasRedes.git`.
   * Selecciona las credenciales si es necesario (en este caso no se usaron).

3. **Configurar triggers**

   * En la pestaña **Triggers**, habilita la opción **GitHub hook trigger for GITScm polling** para que el pipeline se ejecute automáticamente con cada push al repositorio.

4. **Definir pipeline desde SCM**

   * En la sección de **Pipeline**, cambia la definición de **Pipeline script** a **Pipeline script from SCM**.
   * Esto indica que Jenkins usará un `Jenkinsfile` ubicado en el repositorio para definir las etapas del pipeline.

5. **Guardar la configuración**

   * Finalmente, haz clic en **Save** o **Apply** para guardar la configuración y activar el pipeline.

---

¡Claro que sí! Aquí tienes un resumen paso a paso de lo que hiciste en Jenkins para la instalación de plugins, para que quede bien clarito en tu wiki:

---

## Instalación de Plugins en Jenkins

1. **Entrar a la administración de Jenkins**

   * Desde el panel principal de Jenkins, selecciona **Administrar Jenkins**.

2. **Acceder a la sección de Plugins**

   * Dentro de la administración, haz clic en **Plugins** para gestionar los plugins instalados o disponibles.

3. **Buscar plugins disponibles**

   * Ve a la pestaña **Available plugins** (plugins disponibles).
   * Usa la barra de búsqueda para encontrar plugins específicos, en este caso, buscaste `azure`.

4. **Seleccionar e instalar plugins**

   * Marca los plugins que deseas instalar, como **Azure Credentials**, **Azure CLI**, **Docker** y **Docker Pipeline**.
   * Haz clic en el botón **Install** para comenzar la instalación de los plugins seleccionados.

5. **Esperar a que finalice la instalación**

   * Jenkins descargará e instalará los plugins.
   * Una vez instalados, puedes configurarlos según sea necesario.
> Nota: Si es necesario debe reiniciar el docker desde la máquina virtual, usar: `sudo docker restart jenkins`

---

## Agregar Credenciales en Jenkins

1. **Ir a Administración de Jenkins**

   * Desde el panel principal, selecciona **Administrar Jenkins**.

2. **Acceder a la sección de Credenciales**

   * Dentro de la administración, haz clic en **Credentials** para gestionar las credenciales.

3. **Seleccionar el dominio global**

   * En la vista de credenciales, selecciona el dominio **Global credentials (unrestricted)** para añadir credenciales disponibles globalmente.

4. **Agregar nuevas credenciales**

   * Haz clic en **Add Credentials** o **+ Add Credentials**.

5. **Completar la información de la nueva credencial**

   * En **Kind**, selecciona el tipo de credencial: **Username with password**.
   * En **Scope**, selecciona el alcance, generalmente **Global**.
   * Ingresa el **Username** y **Password** correspondientes.
   * Asigna un **ID** identificador único para la credencial (ejemplo: `dockerhub-cred`).
   * Opcionalmente, agrega una descripción para identificarla mejor.
> Nota: [Como Obtener credenciales de Docker Hub](Como-Obtener-credenciales-de-Docker-Hub)

6. **Guardar las credenciales**

   * Haz clic en **Create** para guardar la nueva credencial.

7. **Agregar credenciales específicas para Azure**
   * En **Kind**, selecciona el tipo de credencial: **Azure Service Principal**
   * Similarmente, para credenciales de Azure, añade Client Secret, Tenant ID, y configura el entorno de Azure.
   * Asigna un ID único como `azure-service-principal` para usar en pipelines.
> Nota: Los ID de los credenciales deben ser el mismo nombre que se usa en el `Jenkinsfile`

> Nota: [Como Obtener credenciales de Azure](Como-Obtener-Credenciales-de-Azure)
---

Y **Listo** ya tienes tu **pipeline**!!
![Screenshot 2025-05-26 004708](https://github.com/user-attachments/assets/5edd6ec8-c0dd-4cb4-a0ba-e4132d4c2977)

![Screenshot 2025-05-26 004744](https://github.com/user-attachments/assets/e40c2019-2e65-454e-bc4b-845101eeb279)

![Screenshot 2025-05-26 004829](https://github.com/user-attachments/assets/09e9a015-8e21-4b71-b2d2-80244975f0d9)

![Screenshot 2025-05-26 004902](https://github.com/user-attachments/assets/90fddfdd-b457-4950-a4ef-4a183b0b8b87)

![Screenshot 2025-05-26 005144](https://github.com/user-attachments/assets/2edc197a-7fb8-420d-b055-c55e5e4ce4db)

![Screenshot 2025-05-26 005202](https://github.com/user-attachments/assets/2ab1aba1-ba37-4cdf-a514-1bfe56bd2e4d)

![Screenshot 2025-05-26 005251](https://github.com/user-attachments/assets/0f4d76c6-6ce5-4b2d-8633-edbc46c8592e)

![Screenshot 2025-05-26 005610](https://github.com/user-attachments/assets/ffc97811-69e2-4668-b563-9bec84aacbad)

![Screenshot 2025-05-26 005623](https://github.com/user-attachments/assets/ee39aec0-de35-4056-9be4-be8ecc54484c)

![Screenshot 2025-05-26 005633](https://github.com/user-attachments/assets/e1698ab7-5584-40a9-ae5a-49d9f42d7557)

![Screenshot 2025-05-26 005642](https://github.com/user-attachments/assets/fbf3d04c-40c4-46e0-8532-45ec907a0898)

![Screenshot 2025-05-26 005743](https://github.com/user-attachments/assets/ef62b3b1-59e2-4314-9e4f-5fc0a38d9281)

![Screenshot 2025-05-26 011334](https://github.com/user-attachments/assets/3745fe3b-b6ef-4b81-a593-f5bcfecc2cfa)