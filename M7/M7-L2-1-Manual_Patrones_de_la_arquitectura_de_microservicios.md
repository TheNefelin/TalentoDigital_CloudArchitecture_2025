# 📘 Resumen: Patrones de la Arquitectura de Microservicios

## 1. ¿Qué es un Patrón Arquitectónico?

-   Solución reusable para problemas recurrentes en sistemas
    distribuidos.
-   Beneficios:
    -   Estandarización (seguridad, balanceo, descubrimiento de
        servicios).
    -   Reducción de complejidad.
    -   Mejores prácticas y agilidad.
-   Son guías adaptables, no recetas infalibles.

## 2. Principales Patrones

### a. API Gateway

-   **Descripción:** Punto único de entrada para solicitudes hacia
    microservicios.
-   **Problemas que resuelve:**
    -   Complejidad de comunicación (múltiples endpoints).
    -   Seguridad y autenticación centralizada.
    -   Balanceo de carga y transformación de mensajes.
    -   Versionado y enrutamiento.
-   **Ventajas:** Simplicidad, seguridad, observabilidad.
-   **Consideración:** Puede ser punto único de fallo.

### b. Circuit Breaker

-   **Descripción:** Protege contra fallos en cascada.
-   **Fases:**
    1.  Cerrado → llamadas normales.
    2.  Abierto → bloquea llamadas tras fallos repetidos.
    3.  Medio abierto → verifica recuperación.
-   **Problemas que resuelve:**
    -   Fallos en cascada.
    -   Tiempo de respuesta elevado.
    -   Permite resiliencia y degradación controlada.

### c. Seguridad

-   **Retos:** múltiples endpoints, protección de datos en tránsito,
    vulnerabilidades.
-   **Soluciones:**
    -   **JWT (JSON Web Token):** autenticación/autorización
        distribuida.
    -   Autenticación centralizada (servidor de identidad).
    -   HTTPS/TLS en comunicaciones.
    -   Principio de privilegios mínimos.

### d. Service Discovery

-   **Descripción:** Permite localizar dinámicamente instancias de
    servicios.
-   **Registro de Servicios (Service Registry):** base con direcciones,
    puertos y estado de servicios activos.
-   **Problemas que resuelve:**
    -   Puntos de acceso dinámicos.
    -   Actualizaciones en caliente.
-   **Implementaciones comunes:** Eureka, Consul, Zookeeper.

### e. Data Management

-   **Problema:** Manejo de datos en microservicios.
-   **Patrones:**
    -   **Base de datos por servicio:**
        -   Ventajas: independencia, libertad tecnológica, aislamiento
            de fallos.
        -   Desventajas: duplicación de datos, consistencia eventual.
    -   **Base de datos compartida:**
        -   Ventajas: integración sencilla, coherencia.
        -   Desventajas: mayor acoplamiento, limitación de escalado.
-   **Problemas que resuelve:** consistencia, escalado, mantenimiento.

## 3. Casos de Uso

-   **API Gateway:** aplicaciones e-commerce (carrito, pagos, usuarios).
-   **Autenticación JWT:** sistemas internos con validación distribuida.
-   **Circuit Breaker:** reservas de vuelos/hoteles para evitar
    saturación.
-   **Service Discovery:** plataformas de streaming con servidores
    dinámicos.
-   **Data Management:** redes sociales con almacenamiento distribuido
    (perfiles, contactos, mensajes).

## 4. Cierre

-   Los patrones son esenciales para asegurar coordinación, resiliencia
    y escalabilidad.
-   API Gateway, Circuit Breaker, Seguridad, Service Discovery y Data
    Management son pilares de la arquitectura de microservicios.
-   Su éxito radica en la correcta elección, adaptación y mejora
    continua.

------------------------------------------------------------------------

📚 **Referencias** - Fowler, M. *Microservices* (2014). - Newman, S.
*Building microservices* (2015). - NGINX. *Microservices reference
architecture*. - Pivotal Software. *Circuit Breaker Pattern*. -
Richardson, C. *Microservices Patterns* (2018).
