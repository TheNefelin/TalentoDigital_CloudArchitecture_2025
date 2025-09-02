# 📘 Resumen: Introducción a la Arquitectura de Microservicios

## 1. Conceptos Generales

-   Evolución de arquitecturas monolíticas hacia sistemas desacoplados.
-   Microservicios: componentes pequeños, autónomos y con
    responsabilidad única.
-   Comunicación ligera (HTTP/REST, mensajería asíncrona).
-   CI/CD y orquestación (Kubernetes, Docker Swarm).

## 2. Características Fundamentales de un Microservicio

-   Escalabilidad independiente.
-   Despliegue autónomo.
-   Responsabilidad única (Single Responsibility).
-   Comunicación mediante APIs.
-   Heterogeneidad tecnológica opcional.

## 3. Diferencias entre Arquitectura Monolítica y Microservicios

-   **Monolito:** un bloque de código, escalabilidad global,
    mantenimiento complejo.
-   **Microservicios:** servicios pequeños, escalabilidad selectiva,
    despliegue independiente, menor acoplamiento.

## 4. Beneficios

1.  Escalabilidad y flexibilidad.
2.  Agilidad en el desarrollo.
3.  Alineación con procesos de negocio.
4.  Resiliencia ante fallos.
5.  Libertad tecnológica.

## 5. Contras

1.  Complejidad operacional.
2.  Gestión de comunicación entre servicios.
3.  Dificultad en el entendimiento global del negocio.
4.  Mayor infraestructura.
5.  Coordinación entre equipos.

## 6. SOA vs. Microservicios

-   **SOA:** uso de ESB centralizado, mayor acoplamiento.
-   **Microservicios:** descentralización total, autonomía, APIs
    ligeras.

## 7. Casos de Éxito

-   **Netflix:** cientos de microservicios para streaming.
-   **Amazon:** transición del monolito a microservicios en e-commerce y
    AWS.
-   **Spotify:** microservicios para playlists, reproducción, etc.

## 8. Desafíos en el Diseño

-   Definir límites de servicio.
-   Comunicación eficiente (REST/mensajería).
-   Observabilidad (logging, métricas, tracing).
-   Configuración centralizada.
-   Escalabilidad y disponibilidad.
-   Versionado de APIs.

## 9. Cuándo Usar Microservicios

-   Aplicaciones complejas con cambios frecuentes.
-   Necesidad de escalabilidad selectiva.
-   Cultura DevOps y CI/CD.
-   Equipos especializados.

## 10. Descomposición en Servicios

-   Identificar dominios de negocio.
-   Evitar servicios demasiado grandes/pequeños.
-   Definir APIs claras.
-   Mantener bases de datos separadas.
-   Evitar sobre-descomposición.

## 11. Domain Driven Design (DDD)

-   **Bounded Contexts:** límites conceptuales de dominios.
-   **Lenguaje Ubicuo:** comunicación clara entre técnicos y negocio.
-   **Context Maps:** relaciones entre contextos.

## 12. Consistencia de Datos

-   Eventos de dominio.
-   Patrón Sagas para transacciones distribuidas.
-   CQRS (separación de lectura/escritura).
-   Consistencia eventual.
-   Idempotencia.

## 13. Seguridad en Microservicios

-   Autenticación/autorización centralizada (OAuth2, JWT).
-   Comunicación segura (TLS).
-   Gestión de secretos (HashiCorp Vault).
-   Principio de privilegios mínimos.
-   Monitoreo y auditoría.

## 14. Cierre

La arquitectura de microservicios permite agilidad, escalabilidad y
resiliencia, pero introduce complejidad operativa y de coordinación. Es
clave aplicarla en escenarios adecuados, con buenas prácticas de diseño,
seguridad y gestión de datos.

------------------------------------------------------------------------

📚 **Referencias** - Evans, E. *Domain-driven design* (2003). - Fowler,
M. *Microservices* (2014). - Newman, S. *Building microservices*
(2015). - Richardson, C. *Microservices patterns* (2018).
