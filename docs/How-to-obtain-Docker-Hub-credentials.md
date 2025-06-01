# Creating Credentials in Docker Hub (Personal Access Token)

1. **Log in to Docker Hub:**

   * Go to [Docker Hub](https://hub.docker.com/) and sign in with your account.

2. **Go to Account Settings:**

   * Click your avatar or initials at the top right corner.
   * Select **Account settings**.

3. **Select "Personal access tokens":**

   * In the left sidebar menu, click **Personal access tokens**.

4. **Create a new token:**

   * Click the **Generate new token** button.

5. **Configure the token:**

   * Enter a description to identify it (e.g., `jenkins-credential`).
   * Choose an expiration date (you can select "None" for no expiration).
   * Select the permission, usually **Read & Write** to be able to push images.

6. **Generate the token:**

   * Click **Generate**.
   * Copy the generated token and store it securely, as you won't be able to see it again.

7. **Use the token:**

   * Use this token instead of your password to authenticate on Docker CLI or integrate it with tools like Jenkins.

---

## Attachments

![Screenshot 1](https://github.com/user-attachments/assets/aee70388-6d94-4636-93e9-a34d2b0c5547)
![Screenshot 2](https://github.com/user-attachments/assets/1051d264-ab14-4640-93d3-43bea0c28c7b)
![Screenshot 3](https://github.com/user-attachments/assets/a5a5ad24-f0c8-4a4d-b1c6-dae0bcd8c1aa)
![Screenshot 4](https://github.com/user-attachments/assets/30ccfd37-a39a-4aae-b809-5c8dccc7ab8b)