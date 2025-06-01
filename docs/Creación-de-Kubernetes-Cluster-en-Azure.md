# Pasos para la creación de un Kubernetes Cluster en **Azure**
---

## 📋 Requisitos:

Antes de empezar, asegúrate de tener:

1. **Azure Subscription** activa.
2. Además para efectos de este proyecto, es adecuado tener las otras partes completas. 

---
## Crear el Kubernete 
### 1. Accede al portal de Azure
* Ingresa a [https://portal.azure.com/](https://portal.azure.com)
* Dirígete a **Create a resource** > Selecciona **See more in All services** > **Kubernetes services**
* Selecciona Create y Elige la opcion Kubernetes Cluster

### 2. Configura los detalles básicos del Kubernetes Cluster
* **Subscription:** Selecciona tu suscripción (ejemplo: *Azure for Students*).
* **Resource group:** Selecciona un grupo existente o crea uno nuevo, por ejemplo: `VM-JENKINS`. (Continuando con la linea del proyecto)

* **Cluster preset configuration:**  Selecciona `Dev/Test`.
* **Kubernetes cluster name:** Escribe un nombre adecuado para tu cluste, por ejemplo `KC`.
* **Region:** Elige la región donde se desplegará la el cluster, ej. `(US) West US 2`.
* **Availability zones:** None.
* **AKS pricing tier:** Free.
* **Enable long-term support:** No habilites esta opción.
* **Kubernetes version:** Puedes elegir la versión del kubernetes, en este caso se seleccionara la default (1.31.8).
* **Automatic upgrade:** Disable y en Automatic upgrade scheduler, no schedule
* **Node security channel type:** Node image y en Security channel scheduler, no schedule
* **Authentication and Authorization:** Local accounts with Kubernetes RBAC

Clickea `Next`

### 2. Configura los Node pools
* Selecciona el node pool que aparecera: `agentpool`
* **Node pool name:** En este caso dejaremos el que viene por defecto.
* **Mode:** System.
* **OS SKU:** Ubuntu Linux
* **Availability zones:** None
* **Node size:**
* Clickea: Choose a size y elige el tamaño a conveniencia, en este caso se eligió A2_v2 

* **Scale Method:** Manual
* **Node count:** 1

* **Max pods per node:** 110
* El resto de instrucciones no es necesario que las completes para este caso. 

Clickea `Update`

Y ahora Clickea `Review + Create`








## Anexos.
![KubernetesCreate](https://github.com/user-attachments/assets/6fde9f65-bafb-4206-a276-72f9e13bdbd3)
![Creacion1](https://github.com/user-attachments/assets/2378b96c-8d7f-46a8-abd2-9911d97ef3e1)
![UpdateNodePool](https://github.com/user-attachments/assets/aea9edc8-ae79-415f-8f2a-853d9ed06260)



