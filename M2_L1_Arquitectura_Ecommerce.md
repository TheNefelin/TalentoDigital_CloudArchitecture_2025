
# Arquitectura para un Sistema de E-commerce Adaptable

## 🎯 Desafío
Diseñar una arquitectura adaptable a cambios frecuentes, priorizando **rendimiento**, **seguridad** y **escalabilidad**.

---

## 📌 Paso 1: Atributos de Calidad Clave

### 1. Rendimiento
- **Justificación**: Mejora la experiencia del usuario y la retención.
- **Escenarios**:
  - Bajo carga normal: respuestas < 2 segundos.
  - En picos de tráfico: respuestas < 5 segundos.
  - Consultas masivas: mantener eficiencia con balanceo de carga y caché.

### 2. Seguridad
- **Justificación**: Protege los datos del usuario y mantiene la confianza.
- **Escenarios**:
  - Encriptación de transacciones y datos sensibles.
  - Bloqueo de IP ante accesos no autorizados.
  - Auditorías periódicas y corrección de vulnerabilidades.

### 3. Escalabilidad
- **Justificación**: Soporta crecimiento sin degradar el servicio.
- **Escenarios**:
  - Auto-escalado al superar el 75% de capacidad.
  - Activación automática de instancias en alta demanda.
  - Escalado de base de datos ante más productos o usuarios.

---

## 📌 Paso 2: Escenarios de Calidad (Resumen)

| Atributo     | Escenario 1                                  | Escenario 2                                     | Escenario 3                                     |
|--------------|----------------------------------------------|-------------------------------------------------|-------------------------------------------------|
| Rendimiento  | < 2s bajo carga normal                       | < 5s en eventos especiales                      | Balanceo automático y uso de caché              |
| Seguridad    | Encriptación completa                        | Detección y bloqueo de accesos ilegales        | Auditorías y correcciones periódicas            |
| Escalabilidad| Auto-escalado si carga > 75%                 | Instancias nuevas en picos                      | Escalado automático de base de datos            |

---

## 📌 Paso 3: Diagrama de Arquitectura Básica

```
[Usuario]
   |
   v
[CDN] -- [Frontend SPA: React/Angular]
   |
   v
[API Gateway]
   |
   +--> [Auth Service]
   |
   +--> [User Service] --> [DB: SQL]
   +--> [Product Service] --> [DB: SQL]
   +--> [Cart Service] --> [DB: NoSQL]
   +--> [Payment Service] --> [Pasarela externa]
   |
   v
[Redis / Memcached] - Caché
   |
   v
[Logging & Monitoring: CloudWatch / Prometheus]
```

---

## 📌 Paso 4: Adaptación a Metodología Ágil

- Arquitectura modular basada en microservicios.
- Contenedores Docker orquestados con Kubernetes.
- Arquitecto participa en todos los sprints:
  - Evalúa implicancias técnicas de nuevas historias.
  - Asegura integridad y consistencia de calidad.
- Refactorización continua sin comprometer la estabilidad.
- Integración de CI/CD para despliegues constantes.

---

## ➕ Plus: Integración de Buenas Prácticas

### AWS Well-Architected Framework
- **Fiabilidad**: Auto-scaling, balanceo de carga, alta disponibilidad.
- **Eficiencia operativa**: CI/CD, monitoreo, alertas.
- **Optimización de costos**: Instancias on-demand y reservadas.

### Google SRE
- **SLIs/SLOs** para definir métricas de rendimiento.
- **Error budgets** para mantener estabilidad.
- **Automatización** de despliegues, monitoreo y manejo de incidentes.

---

## ✅ Conclusión
Este diseño garantiza que el sistema:
- Se adapta rápidamente a los cambios del cliente.
- Mantiene un alto rendimiento y seguridad.
- Escala eficientemente con el crecimiento del negocio.

---

## ✅ Decisiones de Despliegue en la Nube y Tecnologías

### Modelo de Servicio
Se opta por un enfoque mixto, combinando varios modelos según el componente:

- **SaaS**: Uso de servicios como pasarela de pagos (ej. Stripe, PayPal) y monitoreo externo (New Relic, Datadog).
- **PaaS**: Implementación de microservicios en plataformas como **Azure App Service** o **Google App Engine**, lo que simplifica el despliegue y escalado automático.
- **IaaS**: Uso de máquinas virtuales o contenedores en Kubernetes (AKS o GKE), lo que permite mayor control sobre la infraestructura y configuración.

### Modelo de Despliegue
- **Primera elección**: **Cloud Privada**  
  Útil para mantener control total sobre la seguridad, cumplimiento de normativas y datos sensibles.
- **Segunda elección**: **Multi-Cloud**  
  Permite alta disponibilidad y redundancia usando múltiples proveedores (ej. Azure + AWS), mitigando dependencia de un único proveedor.

### Tecnologías Seleccionadas

| Capa                   | Tecnología Elegida                        | Motivo                                                                 |
|------------------------|-------------------------------------------|------------------------------------------------------------------------|
| Frontend               | React + CDN (Cloudflare, AWS CloudFront)  | Alta performance y distribución global de contenido estático          |
| Backend (Microservicios) | Azure App Service + Kubernetes (AKS)      | Escalabilidad automática y despliegue ágil de contenedores            |
| Autenticación          | Azure Active Directory B2C                | Gestión de identidad y acceso seguro                                  |
| Bases de datos         | Azure SQL + Cosmos DB (NoSQL)             | Soporte para datos estructurados y no estructurados                   |
| Cache                  | Azure Redis Cache                         | Reducción de latencia y aceleración de respuestas frecuentes           |
| Almacenamiento         | Azure Blob Storage                        | Almacenamiento de imágenes y archivos adjuntos                        |
| Monitoreo              | Azure Monitor + Application Insights      | Observabilidad, métricas, logs y alertas                              |
| Seguridad              | Azure Firewall + DDoS Protection + SSL    | Protección frente a amenazas externas                                 |



---

© Proyecto de Arquitectura de Software - E-commerce
