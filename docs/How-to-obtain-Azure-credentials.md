---
title: How to Obtain Azure Credentials
description: Step-by-step guide to create and obtain Azure credentials for CI/CD integrations like Jenkins.
---
# How to Obtain Azure Credentials

## Creating Azure Credentials for Jenkins

1. **Log in to the Azure Active Directory portal**

   * Access the Azure portal and go to the **Azure Active Directory** section.

2. **Register a new application**

   * In the **Overview** tab, click **Add > App registration**.
   * Fill in the application name (e.g., `CI-CD-K8S`).
   * Select the supported account types (usually "Accounts in this organizational directory only").
   * Optionally add a Redirect URI if needed.
   * Click **Register** to create the application.

3. **Obtain essential IDs**

   * Copy the **Application (client) ID** and **Directory (tenant) ID** shown in the registered app overview.

4. **Create a client secret**

   * Go to the **Certificates & secrets** section.
   * Create a new **Client Secret** and save the generated value (this will be needed for Jenkins).

---

And that’s it! With this, you have the necessary credentials for Jenkins.

---

## Attachments

![Screenshot 1](https://github.com/user-attachments/assets/200667e9-f69c-4620-8181-c194eb83e9a4)
![Screenshot 2](https://github.com/user-attachments/assets/0aa51849-f445-4bc3-9b1f-6e28d87d6549)
![Screenshot 3](https://github.com/user-attachments/assets/f10f3838-63fe-4634-8667-ab6a6b4b11c5)
![Screenshot 4](https://github.com/user-attachments/assets/c7af339e-1a7f-419b-ae53-17e2ff164b61)
![Screenshot 5](https://github.com/user-attachments/assets/ffe74b31-71f1-42e4-9f6b-338ae656c5a2)
![Screenshot 6](https://github.com/user-attachments/assets/be69d5c6-3744-4c4f-8428-2c4349bfad58)

