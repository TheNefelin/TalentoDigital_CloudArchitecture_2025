# 💪 Análisis de Caso: Implementación mediante Contenedores de Aplicación

## 📍 Situación Inicial

La empresa **FinTechPlus**, dedicada a servicios financieros, ejecuta
actualmente su aplicación **monolítica en servidores locales**.\
Los principales problemas detectados son:\
- Inconsistencias entre entornos de desarrollo, prueba y producción.\
- Dificultades de mantenimiento y escalabilidad.

Para resolverlo, se decide **migrar la aplicación a contenedores con
Docker**, logrando:\
- Homogeneidad en los entornos.\
- Despliegues más rápidos.\
- Mayor flexibilidad operativa.

------------------------------------------------------------------------

## 🔎 Descripción del Caso

Como ingeniero DevOps encargado del proceso, las responsabilidades
incluyen:\
1. Analizar los desafíos actuales.\
2. Diseñar y crear un **Dockerfile** con todas las dependencias.\
3. Configurar **volúmenes y redes**.\
4. Documentar ventajas, limitaciones y proponer recomendaciones.

------------------------------------------------------------------------

## 💡 Desarrollo del Caso

### 1. Análisis

**Ventajas de contenerizar una aplicación:**\
- ✅ Portabilidad entre diferentes entornos.\
- ✅ Consistencia en desarrollo, pruebas y producción.\
- ✅ Despliegues rápidos y repetibles.\
- ✅ Escalabilidad horizontal con múltiples instancias.

**Limitaciones posibles:**\
- ⚠️ Curva de aprendizaje para el equipo.\
- ⚠️ Complejidad en la gestión de múltiples contenedores.\
- ⚠️ Dependencia de orquestadores (ej. Docker Compose, Kubernetes).

------------------------------------------------------------------------

### 2. Implementación del Dockerfile

Ejemplo de **Dockerfile** para una aplicación Java:

``` dockerfile
# Imagen base oficial de OpenJDK
FROM openjdk:17-jdk-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo JAR de la aplicación al contenedor
COPY target/fintechplus-app.jar fintechplus-app.jar

# Exponer el puerto en el que la aplicación escucha
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["java", "-jar", "fintechplus-app.jar"]
```

🔎 **Explicación:**\
- `FROM`: Define la imagen base oficial.\
- `WORKDIR`: Establece el directorio de trabajo.\
- `COPY`: Copia el artefacto de la aplicación al contenedor.\
- `EXPOSE`: Permite la comunicación externa en el puerto 8080.\
- `CMD`: Inicia la aplicación dentro del contenedor.

------------------------------------------------------------------------

### 3. Gestión de Volúmenes y Redes

-   **Volúmenes:**
    -   Permiten la **persistencia de datos** fuera del ciclo de vida
        del contenedor.\

    -   Ejemplo:

        ``` bash
        docker run -d -v /data/fintech:/var/lib/fintechplus fintechplus-app
        ```

        Aquí los datos quedan almacenados en el host, incluso si el
        contenedor se elimina.
-   **Redes:**
    -   Docker crea redes virtuales para conectar contenedores entre sí
        y con el host.\

    -   Ejemplo:

        ``` bash
        docker network create fintech-net
        docker run -d --name fintech --network fintech-net fintechplus-app
        ```

        Esto asegura que los contenedores puedan comunicarse de manera
        interna y con el exterior.

------------------------------------------------------------------------

### 4. Reflexión

La **contenerización con Docker** aporta grandes beneficios:\
- Escalabilidad mejorada gracias a la ejecución de múltiples instancias
balanceadas.\
- Mayor consistencia entre entornos, evitando errores de configuración
manual.\
- Reducción del tiempo de despliegue.

**Retos encontrados:**\
- Gestión de múltiples contenedores (solucionable con Docker Compose o
Kubernetes).\
- Necesidad de capacitar al equipo en Docker.

**Recomendaciones:**\
- Adoptar **Docker Compose** para gestionar entornos de desarrollo y
pruebas.\
- Migrar gradualmente a un orquestador como **Kubernetes** para
producción.\
- Implementar buenas prácticas de seguridad (imágenes oficiales, escaneo
de vulnerabilidades).

------------------------------------------------------------------------

## 📬 Entregables

-   ✅ Análisis de situación y desafíos.\
-   ✅ Código del Dockerfile documentado.\
-   ✅ Explicación de volúmenes y redes en Docker.\
-   ✅ Reflexión con ventajas, limitaciones y recomendaciones.

------------------------------------------------------------------------

## 📊 (Opcional) Diagrama de Arquitectura

``` mermaid
flowchart TD
    A[Aplicación Monolítica en Servidor Local] -->|Migración| B[Contenedor Docker]
    B --> C[Volumen Persistente]
    B --> D[Red Docker - fintech-net]
    D --> E[Base de Datos Contenerizada]
    D --> F[Servicios Externos]
```

Este diagrama ilustra cómo la aplicación monolítica se ejecuta en un
**contenedor Docker** con persistencia de datos y conectividad en red.

------------------------------------------------------------------------

✅ Con esta propuesta, **FinTechPlus** obtiene un sistema más
consistente, escalable y flexible, preparado para entornos modernos en
la nube.
