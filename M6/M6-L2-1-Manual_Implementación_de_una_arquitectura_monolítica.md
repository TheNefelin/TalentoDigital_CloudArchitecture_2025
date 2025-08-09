# 🏗 Implementación de una Arquitectura Monolítica en AWS

## 🧑‍💻 Introducción
Guía para implementar una arquitectura monolítica básica en **AWS Cloud**, cubriendo desde la preparación del entorno hasta la configuración de redes, seguridad y despliegue de la aplicación, siguiendo **buenas prácticas de la industria**.

## 🎯 Aprendizaje esperado
Implementar una arquitectura monolítica básica en AWS conforme a estándares y buenas prácticas para resolver necesidades organizacionales.

---

## 1️⃣ Preparación del entorno AWS
- **Cuenta AWS**: Registro con datos y método de pago → credenciales iniciales.
- **Organización de recursos**: Uso de *tags* y convenciones de nombres.
- **Permisos (IAM)**: Asignar el **menor privilegio necesario**, revisando políticas periódicamente.

| Rol/Grupo     | Permisos recomendados             | Comentarios                        |
|---------------|-----------------------------------|-------------------------------------|
| Administrador | Acceso total                      | Uso restringido a personal clave    |
| Desarrollador | Acceso limitado a recursos        | Gestión del entorno de desarrollo  |
| Operaciones   | Monitorización y despliegue       | Control de infraestructura operativa|

---

## 2️⃣ Región y cumplimiento normativo
- **Criterios de selección**: cercanía a usuarios, disponibilidad de servicios, costos.
- **Normativas**: GDPR, HIPAA, entre otras.
- **Recomendación**: Usar servicios certificados y revisar guías de AWS Compliance.

---

## 3️⃣ Servicios de cómputo (EC2)
- Selección según carga, rendimiento y presupuesto.
- Ejemplos:
  - `t2.micro`: pruebas, bajo costo.
  - `m5.large`: producción media.
  - `c5.xlarge`: cómputo intensivo.

**Buenas prácticas**: pruebas de rendimiento y escalamiento vertical ante mayor carga.

---

## 4️⃣ Creación de AMI personalizada
- **AMI**: plantilla con SO, apps y configuraciones.
- **Ventajas**: replicación rápida, entornos consistentes.
- **Proceso**: configurar → probar → crear AMI.

---

## 5️⃣ Despliegue de la aplicación
- **AWS Elastic Beanstalk**:
  - Alta automatización (despliegue, escalado, monitoreo).
  - Fácil para desarrolladores.
- **AWS OpsWorks**:
  - Más personalización con Chef/Puppet.
  - Mayor complejidad, más control.

| Característica | Elastic Beanstalk                 | OpsWorks                          |
|----------------|-----------------------------------|------------------------------------|
| Automatización | Alta                              | Configuración manual adicional     |
| Facilidad uso  | Muy amigable                      | Más complejo                       |
| Personalización| Limitada                          | Muy alta                           |

---

## 6️⃣ Bases de datos en AWS
- **Amazon RDS**: SQL, integridad y relaciones complejas.
- **Amazon DynamoDB**: NoSQL, alta escalabilidad y baja latencia.

**Elección**: según tipo de datos, volumen y frecuencia de acceso.

---

## 7️⃣ Despliegue e integración de la base de datos
- Configuración segura (encriptación, acceso restringido).
- Pruebas de rendimiento y conectividad.
- **Buenas prácticas**: backups, monitoreo y alarmas.

---

## 8️⃣ Configuración de redes
- **VPC**: aislamiento y control de red.
- **Subredes**:
  - Públicas: recursos con acceso a Internet.
  - Privadas: bases de datos y servidores internos.
- **Elastic IP**: IP fija para recursos críticos.
- **Rutas de red**: definir flujo entre subredes e Internet.
- **Route 53**: gestión DNS y enrutamiento.
- **ACM (SSL/TLS)**: cifrado de comunicaciones.

| Elemento          | Función                                   | Claves                       |
|-------------------|-------------------------------------------|------------------------------|
| VPC               | Aislar/controlar red                      | Definir rangos IP adecuados  |
| Subredes           | Segmentar recursos                       | Seguridad y accesibilidad    |
| Elastic IP        | IP fija                                   | Configuración manual posible |
| Rutas de red      | Flujo tráfico                             | Redundancia recomendada      |
| Route 53          | DNS                                       | Registros A, CNAME, etc.     |
| ACM               | Certificados SSL/TLS                      | Renovación automática        |

---

## ✍️ Cierre
Este manual ofrece una ruta completa para desplegar una **arquitectura monolítica en AWS**: desde la creación de cuenta y permisos, elección de región, configuración de cómputo y base de datos, hasta redes y seguridad, aplicando **buenas prácticas** para asegurar rendimiento, disponibilidad y seguridad.

---

## 📚 Referencias
- [AWS DynamoDB Docs](https://docs.aws.amazon.com/dynamodb/)
- [AWS RDS Docs](https://docs.aws.amazon.com/rds/)
- [AWS ACM Docs](https://docs.aws.amazon.com/acm/)
- [AWS Getting Started](https://docs.aws.amazon.com/gettingstarted/)
- [AWS EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)
- [Elastic Beanstalk vs OpsWorks](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.config.html)
- [AWS IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [AWS Route 53 Docs](https://docs.aws.amazon.com/route53/)
- [AWS VPC Docs](https://docs.aws.amazon.com/vpc/)
