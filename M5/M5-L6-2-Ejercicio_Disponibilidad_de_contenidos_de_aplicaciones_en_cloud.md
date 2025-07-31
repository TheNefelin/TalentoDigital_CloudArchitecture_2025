# 💼 Ejercicio: Disponibilidad de Contenidos de Aplicaciones en Cloud

## 🎯 Desafío
Diseñar una arquitectura cloud que garantice **alta disponibilidad** y **distribución eficiente de contenidos** (videos y archivos multimedia) para usuarios de distintas regiones, cumpliendo con los siguientes requerimientos:

### Requisitos
- ✅ Instancias EC2 con Auto Scaling y ELB.
- ✅ CloudFront como CDN.
- ✅ Route 53 para gestión DNS.
- ✅ Direct Connect (opcional).
- ✅ Protección de contenidos sensibles (HTTPS, autenticación, políticas).

---

## 🧩 Arquitectura Principal

### 🖧 EC2 + Auto Scaling + ELB
- EC2 en múltiples zonas de disponibilidad.
- Auto Scaling para ajustar capacidad ante carga variable.
- Application Load Balancer (ALB) distribuye el tráfico.

### 🌍 CloudFront
- Distribuye contenido estático y multimedia globalmente.
- Mejora velocidad y reduce carga al backend.
- Habilita HTTPS y signed URLs para protección.

### 🌐 Route 53
- DNS global y redundante.
- Soporta routing geográfico y failover.
- Asocia el dominio (ej. `media.empresa.com`) a CloudFront o al Load Balancer.

### 🔒 Seguridad y protección de contenidos
- HTTPS en todos los servicios (ALB, CloudFront, S3).
- Autenticación en backend (OAuth, Cognito, etc).
- CloudFront con signed cookies o signed URLs.
- IAM y políticas de bucket restringidas por origen.

---

## ➕ Variantes

### ☁️ Variante 1: Solo Cloud
- Igual a la arquitectura principal.
- No incluye integración on-premise.
- Beneficios: simple, escalable, rápida implementación.
- Limitación: no conecta con infraestructura local.

### 🌐 Variante 2: Híbrida con Direct Connect
- Agrega AWS Direct Connect entre VPC y centro de datos local.
- Aplica si parte del procesamiento o almacenamiento es on-premise.
- Beneficios: baja latencia, seguridad, integración de sistemas legacy.
- Limitaciones: mayor complejidad y costo.

---

## 🧠 Reflexión
- El uso de servicios administrados (CloudFront, Route 53, ELB) reduce complejidad operativa.
- CloudFront es clave para acelerar distribución de contenido multimedia globalmente.
- La opción híbrida es útil si ya existen inversiones en infraestructura local.
- La protección de contenidos debe ser una prioridad en cada capa: red, app y almacenamiento.

---

## 📚 Recursos útiles
- [Amazon CloudFront Docs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
- [EC2 Auto Scaling Docs](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
- [Elastic Load Balancing Docs](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)

