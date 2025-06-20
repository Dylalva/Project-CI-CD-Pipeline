# Contributing Guide / Guía de Contribución

Thank you for your interest in contributing to this project! Your help is greatly appreciated. Please read the following guidelines to make the contribution process smooth for everyone.

¡Gracias por tu interés en contribuir a este proyecto! Tu ayuda es muy apreciada. Por favor, lee las siguientes pautas para facilitar el proceso de colaboración para todos.

---

<details>
<summary><strong>English</strong></summary>

## How to Contribute

1. **Fork this repository** and clone it locally.
2. **Create a new branch** for your feature or fix:
   ```bash
   git checkout -b my-feature
   ```
3. **Make your changes**:
    - Follow the existing code style.
    - Add comments where necessary.
    - Update or add documentation in `docs/` if it helps the community.
    - Add or update tests in the `tests/` directory if you add/modify code logic.
4. **Test your changes** locally before submitting.
5. **Commit and push** your changes:
   ```bash
   git add .
   git commit -m "Brief description of your changes"
   git push origin my-feature
   ```
6. **Open a Pull Request** on GitHub and describe your changes in detail. Reference any related issues.

### Types of Contributions

- **Bug fixes**: Help us improve reliability and fix errors.
- **New features**: Add new functionality to the application, infrastructure, or CI/CD process.
- **Documentation**: Improve or expand any part of the documentation.
- **Tests**: Add or improve automated tests.
- **CI/CD Improvements**: Enhance the workflows, Docker, Jenkins, or Terraform configurations.

### Code of Conduct

Please be respectful and constructive in all interactions. For details, review the [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) (if present).

### Pull Request Guidelines

- Use clear and descriptive titles.
- Explain the motivation and context for your change.
- Reference any related issues by number (e.g., `Closes #12`).
- Ensure your code passes all automated workflows (GitHub Actions).
- Try to keep pull requests focused and atomic (one purpose per PR).

### Reporting Issues

If you find a bug or have a feature request:

- Search [existing issues](https://github.com/Dylalva/Project-CI-CD-Pipeline/issues) first.
- Open a new issue with clear details, steps to reproduce, and any relevant logs or screenshots.

### Development Tips

- This project uses Python (Flask), Docker, Jenkins, Terraform, and Azure Kubernetes Service (AKS).
- Make sure to keep sensitive information (like secrets) out of your code and configuration files.
- Use `.env.example` as a reference for environment variables.
- When updating infrastructure as code (Terraform), document your changes in the appropriate `docs/` files.

We appreciate your help in making this project better. Thank you for contributing!

</details>

---

<details>
<summary><strong>Español</strong></summary>

## Cómo Contribuir

1. **Haz un fork de este repositorio** y clónalo localmente.
2. **Crea una nueva rama** para tu funcionalidad o corrección:
   ```bash
   git checkout -b mi-funcionalidad
   ```
3. **Realiza tus cambios**:
    - Sigue el estilo de código existente.
    - Agrega comentarios cuando sea necesario.
    - Actualiza o agrega documentación en `docs/` si puede ayudar a la comunidad.
    - Agrega o actualiza pruebas en el directorio `tests/` si modificas la lógica del código.
4. **Prueba tus cambios** localmente antes de enviar.
5. **Haz commit y push** de tus cambios:
   ```bash
   git add .
   git commit -m "Descripción breve de tus cambios"
   git push origin mi-funcionalidad
   ```
6. **Abre un Pull Request** en GitHub y describe tus cambios en detalle. Haz referencia a los issues relacionados si corresponde.

### Tipos de Contribuciones

- **Corrección de errores**: Ayuda a mejorar la confiabilidad y corregir errores.
- **Nuevas funcionalidades**: Agrega nuevas funcionalidades a la aplicación, infraestructura o proceso CI/CD.
- **Documentación**: Mejora o expande cualquier parte de la documentación.
- **Pruebas**: Agrega o mejora pruebas automatizadas.
- **Mejoras a CI/CD**: Optimiza los flujos de trabajo, Docker, Jenkins o configuraciones de Terraform.

### Código de Conducta

Por favor, mantén una actitud respetuosa y constructiva en todas las interacciones. Para más detalles, revisa el archivo [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) (si existe).

### Pautas para Pull Requests

- Usa títulos claros y descriptivos.
- Explica la motivación y el contexto de tu cambio.
- Haz referencia a los issues relacionados por número (ejemplo: `Closes #12`).
- Asegúrate de que tu código pase todos los flujos de trabajo automatizados (GitHub Actions).
- Intenta mantener los pull requests enfocados y atómicos (un propósito por PR).

### Reportar Problemas

Si encuentras un bug o tienes una solicitud de funcionalidad:

- Revisa primero los [issues existentes](https://github.com/Dylalva/Project-CI-CD-Pipeline/issues).
- Abre un nuevo issue con detalles claros, pasos para reproducir y logs o capturas relevantes.

### Consejos para el Desarrollo

- Este proyecto utiliza Python (Flask), Docker, Jenkins, Terraform y Azure Kubernetes Service (AKS).
- Asegúrate de mantener la información sensible (como secretos) fuera del código y archivos de configuración.
- Usa `.env.example` como referencia para variables de entorno.
- Cuando actualices infraestructura como código (Terraform), documenta tus cambios en los archivos correspondientes de `docs/`.

¡Agradecemos tu ayuda para mejorar este proyecto! ¡Gracias por contribuir!

</details>
