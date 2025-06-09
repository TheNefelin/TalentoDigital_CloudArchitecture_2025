
# 🧭 Guía Fundamental para Aprender Arquitectura Cloud con AWS

---

## 🧱 1. Fundamentos Sagrados de Arquitectura Cloud

### 🔹 ¿Qué es arquitectura cloud?
- Diseño estructural de sistemas que se ejecutan, escalan y se gestionan en la nube.
- Basado en principios: **resiliencia, escalabilidad, automatización, alta disponibilidad, seguridad por diseño**.

### 🔹 Los 3 pilares de toda arquitectura cloud
| Pilar              | Qué incluye                                                  | Por qué es sagrado |
|--------------------|---------------------------------------------------------------|---------------------|
| **Despliegue**     | Público, Privado, Híbrido, Multi-Cloud                        | Define dónde viven los servicios |
| **Modelo de servicio** | IaaS, PaaS, SaaS                                            | Define qué gestionas tú y qué gestiona AWS |
| **Diseño técnico** | Microservicios, API REST, Autenticación, DevOps, Monitoreo   | Define cómo interactúan los componentes |

> ⚠️ **Siempre pregúntate**: ¿Quién gestiona qué? ¿Dónde está el código? ¿Cómo se asegura, monitorea y escala?

---

## 🧰 2. Servicios y tecnologías AWS esenciales

| Servicio AWS           | Tipo       | ¿Para qué sirve?                                           | Similar a...                     |
|------------------------|------------|------------------------------------------------------------|----------------------------------|
| **EC2**                | IaaS       | VMs para ejecutar cualquier sistema operativo              | Azure VMs                        |
| **S3**                 | Almacenamiento | Almacén de objetos (imágenes, backups, logs, etc.)    | Azure Blob Storage               |
| **RDS / DynamoDB**     | BBDD       | RDS = SQL; DynamoDB = NoSQL escalable                     | Azure SQL, Cosmos DB             |
| **Lambda**             | Serverless | Ejecuta funciones sin servidor, bajo demanda              | Azure Functions                  |
| **API Gateway**        | PaaS/API   | Puerta de entrada a tus APIs REST                         | Azure API Management             |
| **Cognito / IAM**      | Seguridad  | Autenticación y autorización                              | Azure AD B2C, RBAC               |
| **CloudWatch / X-Ray** | Monitoreo  | Logs, métricas, trazabilidad                              | Azure Monitor                    |
| **CloudFormation / CDK / Terraform** | Infraestructura como código | Automatización del despliegue | Azure Resource Manager           |
| **ECS / EKS**          | Contenedores | Orquestación de contenedores con Docker / Kubernetes     | Azure AKS                        |

> 🎯 **Memoriza**:
> - S3 = almacenamiento barato y escalable.
> - Lambda + API Gateway = arquitectura serverless sin backend fijo.
> - RDS = base de datos SQL administrada.
> - Cognito = autenticación federada (login con Google, Facebook, etc).

---

## 🎯 3. Diseño de Arquitectura Cloud para Casos Reales

| Componente              | Buenas Prácticas                                                               |
|-------------------------|---------------------------------------------------------------------------------|
| **Frontend Web**        | Sube a S3 (estático) + usa CloudFront para distribuir                          |
| **Backend Java/Spring** | Ejecuta en EC2, ECS o Lambda (si es microservicio)                            |
| **Seguridad**           | Usa IAM para roles de acceso, Cognito para usuarios finales                   |
| **Base de Datos**       | RDS para relacional; DynamoDB para NoSQL escalable                            |
| **APIs REST**           | Usa API Gateway con control de acceso + throttling                            |
| **Monitoreo**           | Activa CloudWatch Logs, métricas y alertas                                    |
| **Infraestructura**     | Usa Terraform o CloudFormation para reproducibilidad                          |
| **Escalabilidad**       | Autoscaling en EC2 / Fargate; Serverless escala automáticamente                |

---

## 🧠 4. Qué debes memorizar como arquitecto cloud en AWS

### ✅ Conceptos
- Qué es IaaS / PaaS / SaaS
- Qué es un VPC, Subnet, Security Group, IAM Role, S3 bucket policy
- Arquitectura de microservicios vs monolítica

### ✅ Flujos
- Cómo entra un request (desde API Gateway → Lambda/EC2 → DB)
- Cómo proteger un endpoint con Cognito / IAM
- Cómo desplegar una app vía ECS o Lambda

### ✅ Comandos y herramientas
- Terraform (infraestructura como código)
- AWS CLI (manejo de servicios desde terminal)
- Spring Boot + AWS SDK (para integración directa)

---

## ⚔️ 5. Errores comunes que debes evitar

| Error | Solución recomendada |
|-------|-----------------------|
| Acceso directo a la DB desde frontend | Siempre pasa por backend o API Gateway |
| Guardar secretos en código fuente | Usa AWS Secrets Manager |
| No habilitar logs ni métricas | Usa CloudWatch siempre |
| Exponer S3 públicamente por defecto | Usa políticas y roles con permisos mínimos |
| Usar EC2 cuando puedes usar Lambda | Evalúa si puedes serverless antes de usar IaaS |

---

## 🧩 6. Checklist Mental para resolver cualquier caso como arquitecto Cloud

```
✅ ¿Qué tipo de app es? (Web, API, batch, streaming, etc.)
✅ ¿Cómo se va a desplegar? (EC2, Lambda, ECS)
✅ ¿Dónde están los datos? (RDS, S3, DynamoDB)
✅ ¿Cómo se autentica el usuario? (Cognito, IAM)
✅ ¿Quién puede acceder a qué recurso? (Roles, políticas, grupos)
✅ ¿Qué necesita escalar y cómo? (Auto Scaling, Serverless)
✅ ¿Qué se va a monitorear y cómo? (CloudWatch, X-Ray)
✅ ¿Se puede reproducir el entorno? (Infraestructura como código)
```

---

## 📚 Recomendaciones finales de aprendizaje

- ✅ **Practica en AWS Free Tier**: crea una API con Lambda + API Gateway + DynamoDB.
- ✅ **Haz laboratorios en**: [AWS Skill Builder](https://skillbuilder.aws), [Qwiklabs](https://www.qwiklabs.com/)
- ✅ **Preguntas clave en cada proyecto**:
  - ¿Qué parte es infraestructura?
  - ¿Qué parte puedo automatizar?
  - ¿Dónde está el riesgo de seguridad?
  - ¿Se puede escalar esto sin rediseñar todo?
