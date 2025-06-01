## How to Add a Webhook in GitHub

1. **Go to Repository Settings**
   Navigate to the **Settings** tab inside your repository.

2. **Select the Webhooks Section**
   In the side menu, find and select **Webhooks**.

3. **Add a New Webhook**
   Click the **Add webhook** button.

4. **Configure the Webhook**

   * In **Payload URL**, enter the URL where you want to receive the events (for example, `http://ip-jenkins:port/github-webhook/`).
   * In **Content type**, select `application/json`.
   * Optional: You can add a secret to validate the requests.
   * In **SSL verification**, keep SSL verification enabled (recommended) or disable it if you don’t have an SSL certificate.

5. **Select Events to Listen To**
   You can choose to trigger the webhook only on **push** events (default) or select other events as needed.

6. **Activate and Save**
   Check the **Active** box to enable the webhook, then click **Add webhook** to create it.

---

## Attachments

![setting](https://github.com/user-attachments/assets/ff6d8aa3-adb2-4779-ad8a-766cc1c46719)
![setting](https://github.com/user-attachments/assets/33f4660f-be35-48be-8d28-998aecf4b30d)
![setting](https://github.com/user-attachments/assets/ea448061-49ad-49db-bb05-9fd055f60f2c)
![link](https://github.com/user-attachments/assets/6b932c98-0060-41c3-a48b-7d80c5cc711d)
