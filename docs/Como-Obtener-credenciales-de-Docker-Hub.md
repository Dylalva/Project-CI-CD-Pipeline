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

![Screenshot 2025-05-26 103149](https://github.com/user-attachments/assets/aee70388-6d94-4636-93e9-a34d2b0c5547)
![Screenshot 2025-05-26 103223](https://github.com/user-attachments/assets/1051d264-ab14-4640-93d3-43bea0c28c7b)
![Screenshot 2025-05-26 103238](https://github.com/user-attachments/assets/a5a5ad24-f0c8-4a4d-b1c6-dae0bcd8c1aa)
![Screenshot 2025-05-26 103306](https://github.com/user-attachments/assets/30ccfd37-a39a-4aae-b809-5c8dccc7ab8b)
