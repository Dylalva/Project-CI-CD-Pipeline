# Usamos una imagen base con Python preinstalado
FROM python:3.12-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo requirements.txt al contenedor
COPY requirements.txt .

# Actualizamos pip a la última versión
RUN pip install --upgrade pip

# Instalamos las dependencias desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todos los archivos de la aplicación al contenedor
COPY . .

# Exponemos el puerto que utilizará Flask (5000 por defecto)
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
