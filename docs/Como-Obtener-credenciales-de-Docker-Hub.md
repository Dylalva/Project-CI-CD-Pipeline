# Crear Credenciales en Docker Hub (Personal Access Token)

1. **Ingresar a Docker Hub:**

   * Accede a [Docker Hub](https://hub.docker.com) e inicia sesión con tu usuario.

2. **Ir a la Configuración de Cuenta:**

   * En la esquina superior derecha, haz clic en tu avatar o inicial.
   * Selecciona **Account settings** o **Configuración de cuenta**.

3. **Seleccionar "Personal access tokens":**

   * En el menú lateral izquierdo, haz clic en **Personal access tokens**.

4. **Crear un nuevo token:**

   * Haz clic en el botón **Generate new token** o **Generar nuevo token**.

5. **Configurar el token:**

   * Escribe una descripción para identificarlo (ejemplo: `credencial-Jenkins`).
   * Selecciona la fecha de expiración (puede ser "None" para que no expire).
   * Elige el permiso, normalmente **Read & Write** para poder subir imágenes.

6. **Generar el token:**

   * Haz clic en **Generate**.
   * Copia el token generado y guárdalo en un lugar seguro, ya que no podrás verlo otra vez.

7. **Usar el token:**

   * En lugar de tu contraseña, usa este token para autenticarte en Docker CLI o integrarlo en herramientas como Jenkins.

## Anexos
![Screenshot 2025-05-26 103149](https://github.com/user-attachments/assets/18b27d1a-c505-49c8-8508-182313f7aae5)


![Screenshot 2025-05-26 103223](https://github.com/user-attachments/assets/4c4b9f86-024b-4936-8635-43c656c23204)

![Screenshot 2025-05-26 103238](https://github.com/user-attachments/assets/a60d366c-9c37-40f5-a7ce-df5df451afe5)

![Screenshot 2025-05-26 103306](https://github.com/user-attachments/assets/e654dc96-f35e-4753-8135-03744d824389)