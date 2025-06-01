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

![setting](https://github.com/user-attachments/assets/ff6d8aa3-adb2-4779-ad8a-766cc1c46719)
![setting](https://github.com/user-attachments/assets/33f4660f-be35-48be-8d28-998aecf4b30d)
![setting](https://github.com/user-attachments/assets/ea448061-49ad-49db-bb05-9fd055f60f2c)
![vinvular](https://github.com/user-attachments/assets/6b932c98-0060-41c3-a48b-7d80c5cc711d)