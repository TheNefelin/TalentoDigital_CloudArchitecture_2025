# 📘 Resumen de Arquitectura Cloud en AWS

## 🌐 Modelos de Despliegue (Dónde se ejecuta el software)

| Modelo           | Descripción                                                                 | Ejemplo                                  |
|------------------|------------------------------------------------------------------------------|------------------------------------------|
| **On-Premise**   | Todo está instalado y gestionado dentro de la empresa.                      | Servidor físico en oficina con base de datos local |
| **Cloud Pública**| Recursos compartidos alojados en la nube de un proveedor (AWS).            | AWS EC2, S3, Lambda                      |
| **Cloud Privada**| Infraestructura dedicada exclusivamente a una organización.                | AWS VPC con configuración privada       |
| **Cloud Híbrida**| Combinación de on-premise y servicios en AWS.                              | Base de datos local + backups en S3     |
| **Multi-Cloud**  | Uso de varios proveedores (AWS, Azure, GCP).                               | App en AWS + backups en Azure           |

---

## 🛠️ Modelos de Servicio (Qué parte del stack consumes)

| Modelo   | ¿Qué te ofrece?                                 | ¿Qué gestionas tú?          | Ejemplo                        |
|----------|--------------------------------------------------|------------------------------|--------------------------------|
| **IaaS** | Infraestructura virtual: servidores, redes, etc. | Sistema operativo y apps     | Amazon EC2, EBS, VPC           |
| **PaaS** | Plataforma para desplegar apps sin gestionar infra | Solo el código de tu app     | AWS Elastic Beanstalk, Fargate |
| **SaaS** | Aplicaciones completas listas para usar          | Solo los datos y configuración | AWS WorkMail, Amazon Chime     |

---

## 🧱 Comparación: ¿Quién gestiona qué?

| Parte del sistema                | On-Premise | IaaS      | PaaS      | SaaS                                |
|----------------------------------|------------|-----------|-----------|-------------------------------------|
| Infraestructura física           | Tú         | AWS       | AWS       | AWS                                 |
| Red y servidores                 | Tú         | AWS       | AWS       | AWS                                 |
| Sistema operativo                | Tú         | Tú        | AWS       | AWS                                 |
| Plataforma (runtime, middleware) | Tú         | Tú        | AWS       | AWS                                 |
| Aplicación                       | Tú         | Tú        | Tú        | AWS                                 |
| **Datos y uso**                  | Tú         | Tú        | Tú        | **Tú (almacenados por AWS)**        |

> **Nota:** En SaaS tú controlas los datos y configuración, pero AWS los aloja y mantiene. Es esencial conocer las políticas de cifrado, respaldo y cumplimiento (ej. GDPR, HIPAA).

---

## 🧠 Conceptos Clave de Arquitectura Cloud en AWS

- **Cloud Computing:** Entrega de recursos como servidores, bases de datos o almacenamiento bajo demanda y por uso.
- **Arquitectura:** Combinación de modelo de despliegue, servicio, diseño de sistema, y gestión de datos.
- **Microservicios:** Descomposición en servicios pequeños; se facilita con AWS Lambda, API Gateway, ECS/Fargate.
- **Monolito:** Toda la lógica en una sola app, más simple pero menos flexible.
- **Escalabilidad:** AWS Auto Scaling permite crecer vertical y horizontalmente según demanda.
- **Disponibilidad:** AWS ofrece zonas de disponibilidad (AZ) y regiones para alta disponibilidad.
- **Seguridad:** IAM, KMS, WAF, y CloudTrail garantizan control de acceso, cifrado y auditoría.
- **Monitoreo:** AWS CloudWatch permite visualizar logs, métricas y alarmas en tiempo real.

---

## ⚙️ Servicios y Tecnologías de AWS

| Servicio / Tecnología           | Tipo              | Función Principal                                     | Relación con Arquitectura/Modelo     |
|--------------------------------|-------------------|------------------------------------------------------|--------------------------------------|
| **Amazon EC2**                 | IaaS              | Instancias virtuales configurables                   | Infraestructura como servicio (IaaS) |
| **AWS Lambda**                | PaaS/FaaS         | Ejecuta código sin administrar servidores            | Microservicios, arquitectura serverless |
| **Amazon S3**                 | IaaS              | Almacenamiento de objetos                           | Almacenamiento escalable y seguro    |
| **Elastic Beanstalk**        | PaaS              | Despliegue automático de apps con infraestructura   | Simplifica despliegue de aplicaciones web |
| **Amazon RDS**               | PaaS/DBaaS        | Base de datos relacional gestionada                 | Almacén de datos en la nube          |
| **Amazon VPC**               | IaaS              | Red privada virtual dentro de AWS                   | Seguridad y segmentación de red      |
| **Amazon CloudFront**        | CDN               | Distribución global de contenido estático y dinámico| Mejora rendimiento y latencia        |
| **AWS IAM**                  | Seguridad         | Gestión de identidades y accesos                    | Control de acceso y permisos         |
| **AWS CloudWatch**           | Monitoreo         | Métricas, logs y alarmas                            | Observabilidad y rendimiento         |
| **AWS CloudFormation**       | IaC               | Infraestructura como código declarativa             | Automatiza recursos IaaS/PaaS        |
| **AWS WAF**                  | Seguridad         | Firewall para aplicaciones web                      | Protección frente a ataques web      |

---

## 🧩 Resumen Final

- En **AWS**, la arquitectura cloud se compone de modelos de despliegue (pública, híbrida, etc.), modelos de servicio (IaaS, PaaS, SaaS) y diseño arquitectónico (monolito vs. microservicios).
- AWS provee servicios específicos para cada necesidad del sistema: cómputo, almacenamiento, seguridad, monitoreo y automatización.
- Entender qué parte gestionas tú y qué parte gestiona AWS es clave para diseñar soluciones escalables, seguras y eficientes.
- Con herramientas como **CloudFormation**, **IAM** y **CloudWatch**, puedes construir arquitecturas robustas, auditables y mantenibles en el tiempo.

---
