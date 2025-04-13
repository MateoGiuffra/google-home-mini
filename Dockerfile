# Imagen base con Python
FROM python:3.13-slim

# Establecer directorio de trabajo
WORKDIR /

# Copiar archivos del proyecto al contenedor
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir flask

# Exponer el puerto en el que corre Flask
EXPOSE 5000

# Comando para correr la aplicación
CMD ["python", "script.pyw"]
