---
title: Como crear una VM en Azure
description: Guía paso a paso para crear una máquina virtual en Azure, configurar sus detalles básicos, seleccionar el sistema operativo y abrir puertos necesarios.
---
# Pasos para la creación de una VM en **Azure**

---

## 📋 Requisitos:

Antes de empezar, asegúrate de tener:

1. **Azure Subscription** activa.

---

## Crear Máquina Virtual

### 1. Accede al portal de Azure

* Ingresa a [https://portal.azure.com/](https://portal.azure.com)
* Dirígete a **Create a resource** > **Virtual Machine**

### 2. Configura los detalles básicos de la VM

* **Subscription:** Selecciona tu suscripción (ejemplo: *Azure for Students*).
* **Resource group:**

  * Selecciona un grupo existente o crea uno nuevo, por ejemplo: `VM-JENKINS`.
* **Virtual machine name:** Pon un nombre claro, por ejemplo: `VM-Jenkins`.
* **Region:** Elige la región donde se desplegará la VM, ej. `(US) West US 2`.
* **Availability options:**

  * Selecciona `Availability zone`.
* **Zone options:**

  * Selecciona `Self-selected zone`.
* **Availability zone:**

  * Elige `Zone 1` (puedes seleccionar varias zonas si quieres).

### 3. Selecciona la imagen del sistema operativo y tamaño

* **Security type:** Elige `Standard`.
* **Image:** Selecciona `Ubuntu Server 24.04 LTS - x64 Gen2` (o alguna otra versión de **Ubuntu**).
* **VM architecture:** Selecciona `x64`.
* **Size:** Escoge un tamaño acorde a tus necesidades, por ejemplo `Standard_B2s` (2 vCPUs, 4 GiB RAM).

### 4. Configura la cuenta de administrador

* **Authentication type:** Selecciona `SSH public key`.
* **Username:** Pon un nombre de usuario, por ejemplo: `azureuser`.
* **SSH public key source:** Selecciona `Generate new key pair`.
* **Key pair name:** Pon un nombre para la llave SSH, por ejemplo: `VM-Jenkins_key`.

### 5. Configurar reglas de puerto de entrada

* **Public inbound ports:** Selecciona `Allow selected ports`.
* **Select inbound ports:** Escoge `SSH (22)` para permitir acceso remoto vía SSH.

### 6. Revisar y Crear la VM

Una vez completados los pasos anteriores creamos la máquina virtual.
> Si se desea se pueden hacer más configuraciones.

### Abrir puerto 8080
Una vez se creo la Máquina virtual se debe habilitar el puerto 8080, esto con el fin de poder acceder a **Jenkins** desde su máqunina local.

# Cómo agregar una regla de seguridad entrante para abrir el puerto 8080 en Azure VM

1. Dentro de la VM, ve al menú lateral y selecciona **Networking > Network settings**.
2. Haz clic en la **Network interface** listada (ej. `vm-jenkins665_z1`).
3. En la sección **Network security group**, haz clic en el grupo (ej. `VM-Jenkins-nsg`).
4. Haz clic en **+ Create port rule** o **Add inbound security rule**.
5. Configura la regla así:

   * **Source:** Any
   * **Source port ranges:** \*
   * **Destination:** Any
   * **Service:** Custom
   * **Destination port ranges:** 8080
   * **Protocol:** Any (o TCP)
   * **Action:** Allow
   * **Nombre:** Allow-HTTP-8080 (o similar)
6. Da clic en **Add** para guardar la regla.


## Anexos.

![Configuración Inicial](https://github.com/user-attachments/assets/d431ab78-34cf-4650-95e9-99111aaa1529)
![Imagen de SO](https://github.com/user-attachments/assets/d4c00f96-dfaf-49f9-b26b-26b9deaaf583)
![Seguridad](https://github.com/user-attachments/assets/f48f674d-327c-40fd-a7c1-603ac53a55c2)
![Revisión y Creación](https://github.com/user-attachments/assets/625d415b-cc38-474c-b9d4-6e42721dfa8a)
![Reglas de Red](https://github.com/user-attachments/assets/238b1e3a-615e-4f43-b653-3c820b46335b)
![Agregar puerto de entrada](https://github.com/user-attachments/assets/11a145e5-3903-4386-b6f2-03895dc0a1f1)






