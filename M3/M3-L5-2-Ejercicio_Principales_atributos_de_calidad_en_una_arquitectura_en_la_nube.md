# Diseño de Arquitectura en la Nube para Plataforma de Streaming

## 🎯 Desafío

Diseñar una estrategia arquitectónica en la nube para una empresa de **streaming de video** en expansión, asegurando **resiliencia**, **escalabilidad** y **seguridad**, frente a altos niveles de tráfico y demanda.

---

## 1. 🔄 Resiliencia

### Estrategias:
- **Implementación de zonas de disponibilidad (AZs)** para distribuir instancias críticas.
- **Balanceadores de carga (ALB/NLB)** para distribuir tráfico entre instancias activas.
- **Base de datos multi-AZ** (ej. Amazon RDS) con failover automático.
- **Uso de colas (ej. SQS/Kafka)** para desacoplar procesos críticos como transcodificación.
- **Monitoreo con AWS CloudWatch** para detección proactiva de errores y auto-recuperación.

---

## 2. 📈 Escalabilidad

### Estrategias:
- **Auto Scaling Groups** para servicios en contenedores (ECS/EKS) o instancias EC2.
- **CDN (CloudFront)** para distribución global de contenido multimedia, reduciendo la latencia.
- **Event-driven architecture (AWS Lambda)** para tareas bajo demanda.
- **Separación por capas**: API, procesamiento, base de datos, almacenamiento.

---

## 3. 🔐 Seguridad

### Medidas:
- **IAM con principio de mínimo privilegio** para acceso a recursos.
- **WAF (Web Application Firewall)** y **AWS Shield** para protección contra DDoS y ataques comunes.
- **Validación de entrada y protección XSS/CSRF** en el frontend.
- **Certificados TLS/SSL** en todas las comunicaciones públicas.
- **Auditorías y logs con CloudTrail** para trazabilidad.

---

## 4. 🧬 Redundancia y Recuperación ante Fallos

### Propuesta:
- **Base de datos replicada en múltiples zonas** con backups automáticos y snapshots regulares.
- **Infraestructura como código (IaC)** para recuperación rápida (Terraform/CDK).
- **Multi-región activa/pasiva** para recuperación ante desastres regionales.
- **Almacenamiento en S3 con versionado y replicación cruzada (CRR)**.

---

## 5. 📊 Autoescalado y Elasticidad

### Plan:
- **Auto Scaling Policies** basadas en métricas (CPU, tráfico, solicitudes).
- **Lambda Functions** para microtareas altamente concurrentes sin mantener servidores.
- **EC2 Spot Instances** para cargas temporales de bajo costo.
- **Programación de apagado de entornos no productivos fuera de horario laboral.**

---

## 6. 🔏 Cifrado de Datos y Gestión de Accesos

### Soluciones:
- **Cifrado en tránsito (TLS)** y **en reposo (KMS, SSE-S3, RDS encryption)**.
- **Amazon Cognito o Auth0** para autenticación federada y gestión de sesiones.
- **Seguridad por capas**: IAM → Seguridad a nivel de red → Seguridad en la aplicación.
- **Rotación automática de claves y contraseñas** con AWS Secrets Manager.

---

## 7. 🏆 Caso de Éxito: Netflix

Netflix es uno de los principales ejemplos de éxito en resiliencia, escalabilidad y seguridad en la nube:

- **Arquitectura 100% basada en AWS.**
- Microservicios desplegados globalmente en múltiples regiones.
- Uso intensivo de autoescalado, CDN, y bases de datos distribuidas.
- Instrumentación completa de métricas y logs para resiliencia operacional.

📚 Referencia: [Netflix AWS Case Study](https://aws.amazon.com/solutions/case-studies/netflix/)

---

## 🧰 Recursos

- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [Google Cloud Architecture Center](https://cloud.google.com/architecture)
- [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/)

---

## ➕ Plus: Tabla Comparativa

| Empresa     | Estrategia de Resiliencia           | Estrategia de Seguridad             |
|-------------|-------------------------------------|-------------------------------------|
| Netflix     | Multi-region, autoescalado          | IAM personalizado, TLS en todo      |
| Spotify     | Contenedores + CDN global           | OAuth2, rotación de secretos        |
| Amazon      | Desacoplamiento con SQS + Lambda    | Red team interno, auditoría continua|

---
