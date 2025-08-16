# 📦 Resumen: Implementación mediante Contenedores de Aplicación

## Introducción 🧑‍💻

Este manual aborda la **implementación de contenedores de aplicación**
utilizando **Docker**, cubriendo desde conceptos básicos hasta el
despliegue en la nube mediante **ECS (Elastic Container Service)** de
AWS.

El objetivo es **implementar una arquitectura monolítica escalable en la
nube** para responder a necesidades organizacionales.

------------------------------------------------------------------------

## 🎯 Aprendizaje esperado

Ser capaz de implementar una arquitectura monolítica escalable en la
nube utilizando contenedores.

------------------------------------------------------------------------

## 📘 Contenido

### 1. Conceptos Básicos de Docker

-   **Contenedor**: Instancia aislada de aplicación con dependencias.
-   **Imagen**: Plantilla inmutable para crear contenedores.
-   **Dockerfile**: Instrucciones para construir imágenes.
-   **Docker Engine**: Motor para ejecutar y gestionar contenedores.
-   **Docker Hub**: Repositorio de imágenes.
-   **Volúmenes**: Persistencia de datos.
-   **Redes**: Comunicación entre contenedores y host.
-   **Orquestadores**: Ej. Docker Compose.
-   **Capas de Imagen**: Optimización y reutilización.

### 2. Implementación de un Contenedor Docker

-   Instalación en Linux, Windows y macOS.
-   Configuración inicial y verificación (`docker --version`).
-   Beneficios: aislamiento, consistencia, portabilidad.

### 3. Creación de Imágenes con Dockerfile

-   Definir base, dependencias y aplicación.
-   Construcción: `docker build -t nombre-imagen .`
-   Buenas prácticas: usar imágenes ligeras, reducir capas, limpiar
    temporales.

### 4. Ejecución y Operación

-   Comando: `docker run`
-   Opciones: puertos (`-p`), volúmenes (`-v`), variables (`-e`).
-   Monitoreo: `docker ps`, `docker logs`, `docker events`.
-   Gestión de errores y reinicios automáticos.

### 5. Acceso Remoto, Copia de Archivos y Redes

-   `docker exec` para ejecutar comandos en contenedores.
-   `docker cp` para transferir archivos.
-   Redes personalizadas (`docker network create`).

### 6. Servicios Comunes con Docker

-   **NGINX**: despliegue de servidor web.
-   **Bases de Datos**: MySQL, PostgreSQL con persistencia.
-   **Aplicaciones monolíticas**: empaquetadas en contenedores.

### 7. Despliegue en la Nube (ECS - AWS)

-   Creación de clúster en ECS.
-   Registro de imágenes en **Amazon ECR**.
-   Configuración de servicios con balanceo y escalabilidad.
-   Beneficios: alta disponibilidad, monitoreo, seguridad e integración
    con AWS.

------------------------------------------------------------------------

## 📌 Cierre

El manual proporciona fundamentos y prácticas para implementar
aplicaciones en **Docker**, desde lo básico hasta el despliegue en la
nube con ECS, asegurando **escalabilidad y buenas prácticas**.

------------------------------------------------------------------------

## 📚 Referencias

-   [AWS ECS Documentation](https://docs.aws.amazon.com/ecs/)
-   [Docker Compose](https://docs.docker.com/compose/)
-   [Docker Get Started](https://docs.docker.com/get-started/)
-   [Docker Engine](https://docs.docker.com/engine/)
-   [Dockerfile Best
    Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
