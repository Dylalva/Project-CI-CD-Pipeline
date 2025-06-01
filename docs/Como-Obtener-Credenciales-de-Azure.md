# Como Obtener Credenciales de Azure

## Creación de credenciales Azure para Jenkins

1. **Ingresar al portal de Azure Active Directory**

   * Accede al portal de Azure y entra a la sección **Azure Active Directory**.

2. **Registrar una nueva aplicación**

   * En la pestaña **Overview**, haz clic en **Add > App registration**.
   * Completa el nombre de la aplicación (ejemplo: `CI-CD-K8S`).
   * Selecciona el tipo de cuentas soportadas (generalmente "Accounts in this organizational directory only").
   * Opcionalmente agrega un Redirect URI si es necesario.
   * Haz clic en **Register** para crear la aplicación.

3. **Obtener IDs esenciales**

   * Copia el **Application (client) ID** y el **Directory (tenant) ID** que aparecen en el resumen de la aplicación registrada.

4. **Crear un secreto de cliente**

   * Ve a la sección **Certificates & secrets**.
   * Crea un nuevo **Client Secret** y guarda el valor generado (será necesario para Jenkins).

---

Y listo, con eso tienes las credenciales necesarias para que Jenkins.
---
## Anexos
![Screenshot 2025-05-26 010808](https://github.com/user-attachments/assets/200667e9-f69c-4620-8181-c194eb83e9a4)
![Screenshot 2025-05-26 010818](https://github.com/user-attachments/assets/0aa51849-f445-4bc3-9b1f-6e28d87d6549)
![Screenshot 2025-05-26 010844](https://github.com/user-attachments/assets/f10f3838-63fe-4634-8667-ab6a6b4b11c5)
![Screenshot 2025-05-26 010921](https://github.com/user-attachments/assets/c7af339e-1a7f-419b-ae53-17e2ff164b61)
![Screenshot 2025-05-26 011230](https://github.com/user-attachments/assets/ffe74b31-71f1-42e4-9f6b-338ae656c5a2)
![Screenshot 2025-05-26 011300](https://github.com/user-attachments/assets/be69d5c6-3744-4c4f-8428-2c4349bfad58)