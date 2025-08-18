# Usar imagen base oficial de Node.js (versión LTS)
FROM node:18-alpine

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Copiar archivos de dependencias primero (para aprovechar cache de Docker)
COPY package*.json ./

# Instalar dependencias de producción
RUN npm ci --only=production && npm cache clean --force

# Crear usuario no privilegiado para mayor seguridad
RUN addgroup -g 1001 -S nodejs && adduser -S fintech -u 1001

# Copiar el código fuente de la aplicación
COPY --chown=fintech:nodejs . .

# Cambiar al usuario no privilegiado
USER fintech

# Exponer el puerto en el que la API escucha
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["node", "server.js"]