## Cómo agregar un Webhook en GitHub

1. **Ir a Configuración del Repositorio**
   Entra a la pestaña **Settings** (Configuración) dentro de tu repositorio.

2. **Seleccionar la sección Webhooks**
   En el menú lateral, busca y selecciona **Webhooks**.

3. **Agregar un nuevo Webhook**
   Haz clic en el botón **Add webhook**.

4. **Configurar el Webhook**

   * En **Payload URL**, escribe la URL donde quieres recibir los eventos (por ejemplo, `http://ip-jenkins:puerto/github-webhook/`).
   * En **Content type**, selecciona `application/json`.
   * Opcional: Puedes agregar un secreto para validar las peticiones.
   * En **SSL verification**, mantén habilitada la verificación SSL (recomendado) o desactívala si no tienes certificado SSL.

5. **Seleccionar eventos a escuchar**
   Puedes elegir que el webhook se active solo con el evento **push** (por defecto) o seleccionar otros eventos según lo que necesites.

6. **Activar y guardar**
   Marca la opción **Active** para que el webhook esté habilitado y finalmente haz clic en **Add webhook** para crear el webhook.

## Anexos

![Screenshot2025-05-26104134](https://github.com/user-attachments/assets/a20a5719-da09-4010-8c64-531dc9eb6d76)

![Screenshot2025-05-26104145](https://github.com/user-attachments/assets/29c8db77-650a-4a24-b86f-07a9406b7c4f)

![Screenshot 2025-05-26 104354](https://github.com/user-attachments/assets/0234d807-aa14-456c-8230-26915bef7e74)

![Screenshot 2025-05-26 104402](https://github.com/user-attachments/assets/487e97d4-90a7-4390-a14a-29157531a4c1)
