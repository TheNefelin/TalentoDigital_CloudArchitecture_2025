# 📘 Diccionario de Servicios AWS (Arquitectura Microservicios)

Este documento contiene un resumen de los principales servicios de AWS usados en la arquitectura de microservicios.

---

## 🚪 Entrada (API & Frontend)

### **Amazon API Gateway**
- Expone endpoints REST/HTTP o WebSocket.
- Maneja **throttling, versionado, validación de requests**.
- Puede integrarse con **Cognito** para autenticación.
- Ideal para centralizar el acceso a microservicios.

### **Amazon Cognito**
- Autenticación y autorización de usuarios.
- Emite **JWT tokens** para validar identidad.
- Soporta **login social** (Google, Facebook, etc.) y **MFA**.
- Puede trabajar solo o en conjunto con un servicio de Auth propio.

### **AWS WAF (Web Application Firewall)**
- Protege aplicaciones de ataques comunes (SQL Injection, XSS, etc.).
- Se integra con **API Gateway, ALB o CloudFront**.

---

## ⚖️ Balanceo de Carga

### **Application Load Balancer (ALB)**
- Load balancer a nivel de **capa 7 (HTTP/HTTPS)**.
- Permite **routing basado en path** (ej: `/auth`, `/orders`, `/catalog`).
- Hace **health checks** para asegurar disponibilidad.
- Distribuye tráfico a los contenedores de ECS.

---

## 🛠️ Microservicios y Contenedores

### **Amazon ECS (Elastic Container Service)**
- Orquestador de contenedores Docker.
- Dos modos de ejecución:
  - **EC2** → sobre instancias administradas.
  - **Fargate** → serverless, no necesitas manejar instancias.

### **AWS Fargate**
- Motor **serverless** para correr contenedores en ECS.
- Escala automáticamente.
- No requiere administrar servidores.

### **Amazon ECR (Elastic Container Registry)**
- Repositorio privado de imágenes Docker.
- Se integra con ECS/EKS/Fargate.

---

## 🗄️ Persistencia de Datos

### **Amazon Aurora (RDS)**
- Base de datos relacional compatible con **MySQL** o **PostgreSQL**.
- Alta disponibilidad, replicación automática.
- Escalabilidad horizontal en lecturas.

### **Amazon DynamoDB**
- Base de datos **NoSQL serverless**.
- Ideal para catálogos, sesiones o datos con acceso de baja latencia.
- Soporta **escalado automático**.

### **Amazon S3 (Simple Storage Service)**
- Almacenamiento de objetos.
- Ideal para **assets estáticos** (imágenes, documentos, frontend).
- Integra con CloudFront para distribución global.

---

## 🌍 Entrega de Contenido

### **Amazon CloudFront**
- CDN (Content Delivery Network).
- Distribuye contenido desde S3 o aplicaciones globalmente.
- Reduce latencia y mejora seguridad.

---

## 🔒 Seguridad y Gestión

### **Amazon VPC (Virtual Private Cloud)**
- Red privada para aislar recursos en AWS.
- Subnets públicas y privadas.
- Controla el tráfico entre capas.

### **Security Groups**
- Firewalls virtuales a nivel de instancia/servicio.
- Definen qué tráfico entra/sale.

### **AWS Secrets Manager**
- Almacena credenciales de forma segura (DB, API keys).
- Rotación automática de secretos.

### **AWS KMS (Key Management Service)**
- Manejo de llaves de cifrado.
- Se usa para **S3, RDS, DynamoDB** y otros.

---

## 📊 Observabilidad y Monitoreo

### **Amazon CloudWatch**
- Métricas, logs y alarmas.
- Integración con ECS, RDS, DynamoDB, etc.

### **AWS X-Ray**
- Rastreo de peticiones en microservicios.
- Ayuda a identificar cuellos de botella.

### **AWS CloudTrail**
- Auditoría de llamadas a la API de AWS.
- Registro de actividades para seguridad/compliance.

---

## ⚡ Opcionales

### **AWS Lambda**
- Funciones serverless para ejecutar código bajo demanda.
- Útil para eventos (S3 uploads, triggers de DynamoDB).

### **Amazon SQS (Simple Queue Service)**
- Cola de mensajes.
- Desacopla microservicios.

### **Amazon SNS (Simple Notification Service)**
- Publicación/suscripción de mensajes (pub/sub).
- Notificaciones push, integraciones entre servicios.

### **Amazon EventBridge**
- Bus de eventos para integrar aplicaciones.
- Útil para arquitecturas event-driven.

---
