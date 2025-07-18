# 🧱 ARQUITECTURA AWS PARA SISTEMA DE RESERVAS

## 🔍 Resumen del sistema
- **Tipo de arquitectura**: Microservicios
- **Backend**: Node.js
- **Base de datos**: Amazon RDS (PostgreSQL o MySQL)
- **Comunicación**: REST (API Gateway)
- **Despliegue**: Contenedores Docker en Amazon ECS (Fargate)
- **Seguridad**: Amazon Cognito, IAM, HTTPS, Secrets Manager
- **Escalabilidad**: Auto Scaling + Load Balancer
- **Observabilidad**: CloudWatch (Logs + Métricas)

## 🌐 DIAGRAMA CONCEPTUAL DE LA ARQUITECTURA
```
                            ┌───────────────┐
                            │   Usuario     │
                            └──────┬────────┘
                                   │ HTTPS
                        ┌──────────▼──────────┐
                        │   Amazon API Gateway│
                        └──────────┬──────────┘
                                   │
            ┌──────────────────────┼────────────────────────┐
            │                      │                        │
┌───────────▼────────────┐ ┌───────▼────────────┐ ┌────────▼─────────────┐
│ Authentication Service │ │ Reservation Service│ │ Notification Service │
│   (Amazon Cognito +     │ │  (ECS + Node.js)   │ │   (ECS + Node.js)    │
│ Lambda Pre-token hook) │ └────────┬───────────┘ └────────┬────────────┘
└──────────┬─────────────┘          │                        │
           │                        │                        │
┌──────────▼─────────────┐ ┌────────▼────────────┐ ┌────────▼────────────┐
│ Amazon RDS (Usuarios)  │ │ Amazon RDS ()│ │ Amazon SNS/SQS      │
└────────────────────────┘ └──────────────────────┘ └────────────────────┘
             │                         │
             ▼                         ▼
       AWS Secrets Manager      Amazon CloudWatch
       (Credenciales DB)       (Logs, Alarms, Metrics)
```

## 🧱 Paso a Paso

### 1. 🛠 Crear la VPC y Subnets
- Crea una nueva VPC (ej. VPC-Reservas)
- Dentro de esa VPC:
  - Crea una subred pública (ej. Subnet-Public)
  - Crea una subred privada (ej. Subnet-Private)
- Asocia una tabla de ruteo a la subred pública que permita acceso a Internet
- Agrega una Internet Gateway para la VPC

### 2. 🌐 Configurar Security Groups

| Nombre   | Descripción                  | Regla de entrada                       |
| -------- | ---------------------------- | -------------------------------------- |
| `SG-ELB` | Para el Load Balancer        | HTTP (80), HTTPS (443) desde 0.0.0.0/0 |
| `SG-EC2` | Para Elastic Beanstalk / EC2 | Puerto 3000 o 80 desde `SG-ELB`        |
| `SG-RDS` | Para PostgreSQL              | Puerto 5432 desde `SG-EC2`             |

---

### 3. 🚀 Desplegar Elastic Beanstalk
- Crear una nueva aplicación Node.js usando Beanstalk
- Elegir entorno EC2
- Usar instancia pequeña (t2.micro)
- Seleccionar tu VPC y subred pública
- Asociar el SG-EC2 creado previamente
- Activar logs en CloudWatch

### 4. 🗄 Crear una instancia RDS PostgreSQL
- Seleccionar PostgreSQL o MySQL
- Ubicarla en la subred privada
- Asociar el SG-RDS
- Habilitar acceso solo desde el SG-EC2

### 5. 🔐 Configurar Secrets Manager
- Crear secreto con:
  - Usuario/clave de RDS
  - JWT secret (opcional)
- Permitir acceso desde Beanstalk usando el rol LabRole

### 6. 📊 Activar logs con CloudWatch
- En Elastic Beanstalk > Configuración > Software
- Activa la opción de enviar logs a CloudWatch
- Puedes visualizar métricas de CPU y RAM también

### 7. Diagrama

<img src=".\img\P2.png">

### 8. Componentes

| Elemento                  | Estado     | Comentario                                                                                                           |
| ------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------- |
| **VPC**                   | ✅ Correcto | Bien definido como contenedor de red.                                                                                |
| **Subnets**               | ✅ Correcto | Pública y privada bien diferenciadas.                                                                                |
| **ELB en Subred Pública** | ✅ Correcto | Lugar adecuado para balancear tráfico entrante.                                                                      |
| **Elastic Beanstalk**     | ✅ Correcto | Supone una app en Node.js desplegada.                                                                                |
| **Amazon RDS (Privado)**  | ✅ Correcto | Buena práctica: mantener la base de datos en subred privada.                                                         |
| **Security Groups**       | ✅ Correcto | Bien separados por componente.                                                                                       |
| **CloudWatch**            | ✅ Correcto | Para logs y monitoreo, está bien conectado a RDS. Podrías también vincularlo a EC2 o ELB si quieres mayor cobertura. |
| **Secrets Manager**       | ✅ Correcto | Buena práctica para manejar credenciales de RDS.                                                                     |
| **SNS**                   | ✅ Correcto | Aparentemente para alertas o eventos desde RDS. Asegúrate de configurar triggers específicos.                        |

---