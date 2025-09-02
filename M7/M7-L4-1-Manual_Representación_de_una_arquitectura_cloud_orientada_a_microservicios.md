# 📘 Resumen: Representación de una Arquitectura Cloud Orientada a Microservicios

## 1. Introducción
- Los microservicios son clave para aplicaciones escalables, modulares y mantenibles en la nube.
- **Herramientas de diseño:**
  - **Cloudcraft:** diagramas interactivos AWS, cálculo de costos, drag-and-drop.
  - **AWS Perspective:** genera diagramas desde la infraestructura real (open source).
  - **AWS Icons + Draw.io/Lucidchart:** documentación con íconos oficiales.
  - **Azure Architecture Center:** plantillas y diagramación integrada.
  - **GCP Diagramming Tool:** creación de diagramas en consola nativa.

| Herramienta              | Tipo        | Integración | Costos | Visual | Licencia   |
|---------------------------|-------------|-------------|--------|--------|------------|
| Cloudcraft               | Externa     | Parcial AWS | Sí     | Intuitiva | Freemium |
| AWS Perspective          | Nativa AWS  | Total       | No     | Automática | Gratuita |
| Azure Architecture Center| Nativa Azure| Total       | No     | Profesional | Gratuita |
| GCP Diagramming Tool     | Nativa GCP  | Total       | No     | Integrada | Gratuita |
| AWS Icons + Draw.io      | Manual      | No          | No     | Flexible | Gratuita |

---

## 2. Representación con Contenedores
- **Ventajas:**
  - Portabilidad entre entornos.
  - Cohesión y aislamiento de microservicios.
  - Despliegue rápido.
- **Cloudcraft:** permite visualizar contenedores (ECS, EKS, EC2), etiquetar servicios y reflejar redes (VPC, Subnets).

---

## 3. Ejemplos de Arquitecturas

### 3.1 Aplicaciones Web
- **Componentes:** S3 + CloudFront (frontend), API Gateway, microservicios en ECS/EKS, bases de datos RDS/DynamoDB.
- **Seguridad con SG (Security Groups):**
  - ALB: puertos 80/443 abiertos al público.
  - Backend: tráfico solo desde el ALB.
  - BD: solo accesible desde backend.
  - SSH: restringido a IP fija/VPN.

### 3.2 Aplicaciones IoT
- Entrada: AWS IoT Core.
- Procesamiento en contenedores.
- Almacenamiento: S3 o BD.
- Posible uso de Kinesis o Lambda como capa intermedia.

### 3.3 Aplicaciones Mobile con JWT
- Cognito para autenticación (User Pools).
- API Gateway valida tokens.
- Microservicios backend para perfiles, notificaciones, sincronización.

### 3.4 Aplicaciones con Alta Disponibilidad de Archivos
- S3 como repositorio.
- Microservicios de análisis/procesamiento.
- CloudFront para distribución global.

### 3.5 Otros Casos
- **ML/IA:** cada microservicio encapsula un modelo.
- **DevOps:** microservicios para CI/CD.
- **Back-office:** microservicios por área (finanzas, RRHH, etc.).

---

## 4. Estimación de Costos
- **Factores:**
  - Número de contenedores y tiempo de ejecución.
  - Tipo de instancia (EC2/Fargate).
  - Servicios extra (RDS, DynamoDB, S3, API Gateway).
  - Región.
- **Cloudcraft:** permite estimar costos en tiempo real configurando cada recurso.
- **Buenas prácticas:**
  - Autoscaling → pagar solo por lo usado.
  - Reserved Instances o Savings Plans en cargas estables.
  - Usar serverless en partes específicas.

---

## 5. Cierre
- Cloudcraft y herramientas nativas permiten **visualizar arquitecturas, calcular costos y documentar soluciones** en entornos cloud.
- Ejemplos (web, IoT, mobile, archivos) muestran la **versatilidad de los microservicios**.
- Con **etiquetado, segmentación y control de costos**, es posible crear diagramas fieles a producción.

---

📚 **Referencias**
- [AWS Microservices on AWS](https://aws.amazon.com/microservices/)
- [Amazon ECS Documentation](https://docs.aws.amazon.com/ecs/index.html)
- [Cloudcraft Help Center](https://help.cloudcraft.co/)
