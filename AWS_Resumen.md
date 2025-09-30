# Guía de Estudio AWS - Servicios Fundamentales

## Tabla de Contenidos
1. [Amazon EC2](#amazon-ec2)
2. [Grupos de Seguridad](#grupos-de-seguridad)
3. [Elastic Load Balancing (ELB)](#elastic-load-balancing-elb)
4. [Amazon EBS](#amazon-ebs)
5. [Amazon EFS](#amazon-efs)
6. [Amazon S3](#amazon-s3)
7. [Amazon SNS](#amazon-sns)
8. [Amazon SQS](#amazon-sqs)
9. [Amazon ECR](#amazon-ecr)
10. [Amazon ECS](#amazon-ecs)
11. [Amazon EKS](#amazon-eks)
12. [Diagramas Conceptuales](#diagramas-conceptuales)

---

## Amazon EC2

### Descripción
Amazon EC2 (Elastic Compute Cloud) es un servicio de computación en la nube que permite ejecutar servidores virtuales (instancias) en la infraestructura de AWS con capacidad escalable bajo demanda.

### Características Principales
- **Escalabilidad**: Aumentar o disminuir capacidad fácilmente
- **Elasticidad**: Iniciar y detener instancias según demanda
- **Diversidad de instancias**: Tipos para diferentes usos (general, cómputo intensivo, memoria, GPU)
- **Almacenamiento flexible**: EBS, Instance Store, EFS, S3
- **Seguridad**: Security Groups, pares de claves, IAM roles, VPC
- **Opciones de compra**: On-Demand, Reserved, Spot, Savings Plans
- **Automatización**: Auto Scaling, ELB, CloudWatch, CloudFormation

### Componentes

| Componente | Descripción |
|------------|-------------|
| **Instancia** | Servidor virtual ejecutándose en la nube |
| **AMI** | Imagen con SO y configuraciones preinstaladas |
| **Tipo de instancia** | Combinación de CPU, memoria, almacenamiento (ej: t2.micro, m5.large) |
| **EBS** | Almacenamiento persistente adjuntable |
| **Key Pairs** | Acceso seguro vía SSH |
| **Security Groups** | Firewall virtual para tráfico |
| **Elastic IP** | Dirección IP fija |
| **VPC** | Red virtual donde operan las instancias |

### Configuraciones Habituales
1. **AMI**: Seleccionar imagen (Amazon Linux, Ubuntu, Windows Server)
2. **Tipo de instancia**: Elegir tamaño (t2.micro para pruebas, m5.large para producción)
3. **Par de claves**: Generar o seleccionar para SSH
4. **Red y Subred**: Seleccionar VPC y subnet
5. **Security Group**: Configurar reglas de tráfico (puerto 22 para SSH)
6. **Almacenamiento**: Seleccionar volúmenes EBS, tamaño y tipo
7. **User Data**: Script de inicio para instalar software
8. **Etiquetas**: Organización (Name = ServidorWeb)

### Casos de Uso
- Hospedaje de aplicaciones web y APIs
- Servidores de base de datos
- Entornos de desarrollo y pruebas
- Machine Learning e IA
- Procesamiento intensivo

---

## Grupos de Seguridad

### Descripción
Firewall virtual a nivel de instancia que controla el tráfico entrante y saliente. Son de estado (stateful), permitiendo automáticamente respuestas sin reglas adicionales.

### Características Principales
- **Firewall de estado**: Respuestas automáticas autorizadas
- **Nivel de instancia**: Se aplican a instancias individuales, no a subredes
- **Reglas permisivas**: Solo permiten tráfico definido; todo lo demás se bloquea
- **Actualizaciones en tiempo real**: Cambios se aplican inmediatamente
- **Compatibilidad con protocolos**: TCP, UDP, ICMP
- **Referencias entre grupos**: Permitir tráfico desde otros Security Groups

### Componentes
- **Reglas de entrada (Inbound)**: Tráfico que puede ingresar
- **Reglas de salida (Outbound)**: Tráfico que puede salir (por defecto todo permitido)
- **Protocolos y Puertos**: TCP, UDP, ICMP con rangos de puertos
- **Fuentes y Destinos**: IPs, rangos CIDR, otros Security Groups
- **Asociación con ENI**: Aplicados a interfaces de red

### Configuraciones Habituales

#### Servidor Web Público
```
Entrada:
- HTTP (80) desde 0.0.0.0/0
- HTTPS (443) desde 0.0.0.0/0
Salida:
- Todo el tráfico permitido
```

#### Servidor de Base de Datos Privado
```
Entrada:
- MySQL (3306) desde SG-App-Web solamente
Salida:
- Restringido a VPC interna
```

#### Servidor de Administración
```
Entrada:
- SSH (22) desde IP corporativa (200.45.x.x/32)
Salida:
- Todo permitido para actualizaciones
```

### Buenas Prácticas
1. Principio de privilegios mínimos
2. Usar nombres descriptivos (SG-WebServer-Prod)
3. Monitorear con CloudTrail y CloudWatch
4. Revisión periódica de reglas
5. Documentar cambios

---

## Elastic Load Balancing (ELB)

### Descripción
Servicio administrado que distribuye automáticamente el tráfico entrante entre múltiples destinos (instancias EC2, contenedores, IPs) para garantizar alta disponibilidad y escalabilidad.

### Características Principales
- **Automatización**: Sin gestión de hardware
- **Alta disponibilidad**: Redundancia entre múltiples AZs
- **Seguridad**: Integración con ACM para SSL/TLS y AWS WAF
- **Escalabilidad automática**: Ajuste según tráfico
- **Compatibilidad multicapas**: Capa 4 (transporte) y Capa 7 (aplicación)
- **Monitoreo**: CloudWatch para métricas
- **Health Checks**: Verifica estado de destinos

### Tipos de Load Balancers

| Tipo | Capa OSI | Uso Principal | Características |
|------|----------|---------------|-----------------|
| **ALB** | 7 | Aplicaciones web, microservicios | Enrutamiento basado en contenido, Lambda |
| **NLB** | 4 | Alto tráfico, baja latencia | Millones de req/seg, IPs estáticas |
| **CLB** | 4 y 7 | Legacy | Migrar a ALB/NLB |

### Componentes
- **Load Balancer**: Punto de entrada con DNS público
- **Listeners**: Escuchan solicitudes en puerto/protocolo específico
- **Target Groups**: Conjuntos de destinos (instancias, IPs)
- **Rules**: Enrutamiento basado en rutas, headers, dominios
- **Health Checks**: Validación de disponibilidad

### Configuraciones Habituales
1. Seleccionar tipo (ALB, NLB, CLB)
2. Definir Availability Zones para redundancia
3. Configurar listeners (HTTP 80, HTTPS 443)
4. Crear y asociar target groups
5. Configurar health checks
6. Aplicar certificados SSL con ACM
7. Configurar Security Groups
8. Integrar con Auto Scaling Groups

### Buenas Prácticas
- Usar ALB o NLB en arquitecturas nuevas
- Definir health checks estrictos
- Aplicar certificados SSL y WAF
- Activar cross-zone load balancing
- Integrar con Auto Scaling

---

## Amazon EBS

### Descripción
Servicio de almacenamiento en bloque persistente que se integra con instancias EC2, actuando como discos duros virtuales con elasticidad, redundancia y alto rendimiento.

### Características Principales
- **Persistencia**: Datos permanecen aunque se detenga la instancia
- **Alto rendimiento**: Hasta millones de IOPS
- **Elasticidad**: Redimensionamiento sin interrupciones
- **Redundancia**: Replicación automática dentro de la AZ
- **Seguridad**: Cifrado en tránsito y reposo con KMS
- **Snapshots**: Respaldo incremental en S3
- **Durabilidad**: 99.999% de disponibilidad

### Tipos de Volúmenes

| Tipo | Uso | Características |
|------|-----|-----------------|
| **gp2/gp3** | Uso general | Balance rendimiento/costo, hasta 16,000 IOPS |
| **io1/io2** | Bases de datos críticas | IOPS dedicadas, mayor durabilidad |
| **st1** | Big data, logs | Optimizado para lectura/escritura secuencial |
| **sc1** | Acceso infrecuente | Bajo costo |

### Componentes
- **Volúmenes EBS**: Unidades de almacenamiento
- **Snapshots**: Copias de seguridad en S3
- **Encryption**: Cifrado con KMS
- **Availability Zone**: Debe estar en la misma AZ que EC2

### Configuraciones Habituales
1. **Creación**: Seleccionar AZ y tipo de volumen
2. **Asociación**: Adjuntar a instancia EC2
3. **Cifrado**: Habilitar con KMS
4. **Redimensionamiento**: Expandir capacidad dinámicamente
5. **Snapshots**: Crear copias automáticas con AWS Backup
6. **Optimización**: Usar instancias EBS-Optimized

### Casos de Uso
- Bases de datos transaccionales (MySQL, Oracle, PostgreSQL)
- Aplicaciones de baja latencia
- Big Data y Analytics
- Entornos de desarrollo
- Respaldo y recuperación

---

## Amazon EFS

### Descripción
Sistema de almacenamiento de archivos basado en NFS que permite acceso concurrente desde múltiples instancias EC2, contenedores y servidores on-premises, con escalabilidad automática.

### Características Principales
- **Elasticidad automática**: Crecimiento/decrecimiento automático
- **Acceso concurrente**: Miles de instancias simultáneamente
- **Alto rendimiento**: Cargas intensivas de lectura/escritura
- **Alta disponibilidad**: Replicación entre múltiples AZs
- **Seguridad**: Cifrado en reposo y tránsito
- **Compatibilidad NFSv4**: Facilita migraciones
- **Modos de rendimiento**: General Purpose y Max I/O

### Componentes
- **Sistema de Archivos EFS**: Unidad lógica principal
- **Mount Targets**: Puntos de conexión en subnets de VPC
- **Security Groups**: Control de tráfico a mount targets
- **Access Points**: Configuraciones de acceso específicas con UID/GID
- **Performance Modes**: General Purpose (baja latencia) o Max I/O (alta concurrencia)

### Configuraciones Habituales
1. **Creación**: Definir región y VPC
2. **Modo de rendimiento**: General Purpose o Max I/O
3. **Mount targets**: En cada subnet de AZs necesarias
4. **Seguridad**: Security Groups permitiendo NFS (puerto 2049)
5. **Access Points**: Control granular de permisos
6. **Cifrado**: Habilitar en reposo y tránsito
7. **Integración**: Montar en EC2 con NFSv4, usar en ECS/EKS
8. **Backup**: Configurar AWS Backup

### Casos de Uso
- Almacenamiento compartido para aplicaciones web
- Big Data y análisis
- Machine Learning
- Content Management Systems
- DevOps y entornos de prueba

---

## Amazon S3

### Descripción
Servicio de almacenamiento de objetos escalable y duradero para cualquier cantidad de datos. Los objetos se almacenan en buckets con metadatos y un identificador único (key).

### Características Principales
- **Durabilidad**: 99.999999999% (11 nueves)
- **Disponibilidad**: 99.99% dentro de la región
- **Escalabilidad**: Sin límites de almacenamiento
- **Seguridad**: Cifrado SSE-S3, SSE-KMS, SSE-C
- **Versionado**: Conserva versiones anteriores
- **Gestión de ciclo de vida**: Migración automática a almacenamiento económico
- **Eventos**: Integración con Lambda, SNS, SQS

### Clases de Almacenamiento

| Clase | Uso | Características |
|-------|-----|-----------------|
| **Standard** | Alta frecuencia | Acceso inmediato, costo más alto |
| **Intelligent-Tiering** | Patrones variables | Ajuste automático |
| **Infrequent Access (IA)** | Acceso poco frecuente | Menor costo |
| **Glacier** | Archivado | Bajo costo, recuperación en minutos/horas |
| **Glacier Deep Archive** | Archivado largo plazo | Costo mínimo, recuperación en 12 horas |

### Componentes
- **Buckets**: Contenedores lógicos
- **Objetos**: Datos con identificador único (key)
- **Keys**: Identificadores únicos
- **Versiones**: Registro de versiones de objetos
- **Policies y ACLs**: Control de acceso
- **Eventos**: Notificaciones automáticas
- **Replication Rules**: Replicación entre regiones

### Configuraciones Habituales
1. **Creación de Buckets**: Nombre único global, región
2. **Versionado**: Protección contra borrados
3. **Cifrado**: SSE o KMS
4. **Control de Acceso**: Policies, ACLs, IAM roles
5. **Ciclo de Vida**: Migración automática según antigüedad
6. **Eventos**: Activar Lambda, SNS, SQS
7. **Replicación**: CRR para recuperación de desastres

### Casos de Uso
- Archivos web y multimedia
- Backups y recuperación
- Big Data y Analytics
- Entornos serverless
- Content Distribution con CloudFront
- Archivado y cumplimiento normativo

---

## Amazon SNS

### Descripción
Servicio de mensajería pub/sub totalmente administrado que permite comunicación entre aplicaciones, microservicios y usuarios mediante múltiples protocolos.

### Características Principales
- **Alta escalabilidad**: Millones de mensajes por segundo
- **Multicanalidad**: HTTP/HTTPS, Lambda, SQS, SMS, Email, Push móvil
- **Integración con AWS**: CloudWatch, S3, EC2, RDS, DynamoDB
- **Entrega garantizada**: Reintentos automáticos
- **Seguridad**: IAM Policies, cifrado TLS y KMS
- **Modelo de precios**: Pago por uso

### Componentes
- **Tópicos**: Canales de comunicación lógicos
- **Publicadores**: Envían mensajes al tópico
- **Suscriptores**: Reciben mensajes (HTTP, SQS, Lambda, SMS, Email)
- **Políticas de Acceso**: Control con IAM
- **Filtros de Mensajes**: Suscriptores reciben solo mensajes relevantes

### Configuraciones Habituales
1. **Crear Tópico**: Nombre único, región, permisos IAM
2. **Gestionar Suscripciones**: Configurar endpoints, validar con token
3. **Filtros**: Definir atributos para distribución selectiva
4. **Seguridad**: Políticas IAM, cifrado KMS
5. **Reintentos y DLQ**: Política de reintentos, asignar SQS como DLQ
6. **Monitoreo**: CloudWatch para métricas

### Ejemplo de Uso
**Aplicación bancaria:**
- Tópico: "TransaccionesSeguras"
- Publicador: Sistema de transacciones
- Suscriptores:
  - Lambda: verificación antifraude
  - SQS: auditoría
  - Email: confirmación cliente
  - SMS: alertas

---

## Amazon SQS

### Descripción
Servicio de colas de mensajes administrado que permite comunicación asíncrona y desacoplada entre sistemas mediante almacenamiento temporal de mensajes.

### Características Principales
- **Desacoplamiento**: Productores y consumidores independientes
- **Escalabilidad**: Millones de mensajes por segundo
- **Entrega confiable**: Replicación en múltiples servidores
- **Dos tipos de colas**: Standard y FIFO
- **Visibility Timeout**: Invisibilidad temporal tras lectura
- **Seguridad**: IAM, cifrado TLS y KMS
- **Dead-Letter Queues**: Para mensajes no procesables

### Tipos de Colas

| Tipo | Orden | Entrega | Uso |
|------|-------|---------|-----|
| **Standard** | No garantizado | At-least-once | Máxima velocidad |
| **FIFO** | Estricto | Exactly-once | Orden crítico |

### Componentes
- **Colas**: Almacenamiento temporal
- **Mensajes**: Hasta 256 KB, retención hasta 14 días
- **Productores**: Envían mensajes
- **Consumidores**: Procesan mensajes (EC2, ECS, Lambda)
- **DLQ**: Cola secundaria para mensajes fallidos
- **Políticas de Acceso**: IAM o SQS Queue Policies

### Configuraciones Habituales
1. **Crear Cola**: Standard o FIFO (.fifo)
2. **Retención**: 1 minuto a 14 días
3. **Visibility Timeout**: Ajustar según tiempo de procesamiento (default 30s)
4. **Reintentos y DLQ**: Máximo de intentos antes de DLQ
5. **Long Polling**: Esperar hasta 20s por mensajes nuevos
6. **Integración**: Conectar con SNS, activar Lambda
7. **Seguridad**: Permisos IAM, cifrado KMS
8. **Monitoreo**: CloudWatch para métricas

### Ejemplo de Uso
**E-commerce:**
- Productores: Carrito de compras envía órdenes
- Cola SQS: Almacena pedidos temporalmente
- Consumidores:
  - Lambda: valida pagos
  - EC2/ECS: gestiona inventario
  - DLQ: pedidos fallidos

---

## Amazon ECR

### Descripción
Servicio administrado de registro de imágenes de contenedores, integrado con Docker y OCI, que permite almacenar, administrar y desplegar imágenes de forma segura.

### Características Principales
- **Administrado**: Sin gestión de infraestructura
- **Repositorios privados y públicos**: Para proyectos internos o comunitarios
- **Integración con IAM**: Control granular de accesos
- **Escaneo de vulnerabilidades**: Con Amazon Inspector
- **Almacenamiento escalable**: Millones de imágenes
- **Replicación**: Entre regiones
- **Compatibilidad**: Docker y OCI

### Componentes
- **Repositorios**: Contenedores lógicos de imágenes
- **Imágenes**: Archivos empaquetados con código y dependencias
- **Autenticación**: IAM Roles y políticas
- **Escaneo**: Análisis de vulnerabilidades
- **Replicación**: Políticas multi-región
- **Integración**: ECS, EKS, Lambda

### Configuraciones Habituales
1. **Crear Repositorio**: Privado o público, políticas IAM
2. **Autenticación**: `aws ecr get-login-password`
3. **Lifecycle Policies**: Eliminar imágenes antiguas
4. **Escaneo**: Activar análisis de vulnerabilidades
5. **Replicación**: Configurar reglas multi-región
6. **CI/CD**: Integrar con CodePipeline, CodeBuild
7. **Monitoreo**: CloudWatch y CloudTrail

---

## Amazon ECS

### Descripción
Servicio de orquestación de contenedores administrado que permite ejecutar aplicaciones Docker en clústeres EC2 o mediante Fargate (serverless).

### Características Principales
- **Modelos flexibles**: EC2 (administrado) o Fargate (serverless)
- **Escalabilidad automática**: Ajuste dinámico de contenedores
- **Alta disponibilidad**: Distribución multi-AZ
- **Integración con AWS**: VPC, IAM, CloudWatch, ECR
- **Monitoreo**: CloudWatch, X-Ray
- **Soporte para microservicios**: Arquitecturas desacopladas
- **CI/CD**: CodePipeline, CodeBuild, CodeDeploy

### Componentes
- **Clústeres**: Conjunto lógico de recursos
- **Tareas**: Unidades de ejecución definidas por Task Definition
- **Task Definitions**: Plantillas (imágenes, recursos, configuraciones)
- **Servicios**: Mantienen número deseado de tareas
- **Launch Types**: EC2 (gestionado) o Fargate (serverless)
- **ECS Agent**: Administra tareas en instancias EC2

### Configuraciones Habituales
1. **Crear Clúster**: EC2 o Fargate, configurar VPC
2. **Task Definitions**: Imagen ECR, CPU, memoria, puertos
3. **Servicios**: Réplicas, ELB, autoscaling
4. **Seguridad**: IAM Roles, Security Groups
5. **Monitoreo**: CloudWatch Logs y Metrics, X-Ray
6. **Optimización**: Spot Instances en EC2, políticas adaptativas en Fargate

---

## Amazon EKS

### Descripción
Servicio administrado de Kubernetes que facilita implementación, gestión y escalado de contenedores con compatibilidad total con el estándar Kubernetes.

### Características Principales
- **Kubernetes estándar**: 100% compatible
- **Alta disponibilidad**: Plano de control multi-AZ
- **Ejecución flexible**: EC2, Fargate, EKS Anywhere
- **Seguridad**: IAM, KMS, CNI plugin
- **Escalabilidad**: Cluster Autoscaler, HPA
- **Integración AWS**: EBS, EFS, VPC, ELB, CloudWatch
- **Actualizaciones**: Gestionadas por AWS

### Componentes
- **Control Plane**: API server, etcd, controladores (administrado por AWS)
- **Worker Nodes**: EC2 o Fargate para ejecutar pods
- **Pods y Deployments**: Unidades de ejecución
- **Kubernetes API**: Interacción con kubectl
- **CNI Plugin**: IPs nativas de VPC
- **Almacenamiento**: EBS, EFS, FSx
- **IRSA**: IAM Roles for Service Accounts

### Configuraciones Habituales
1. **Crear Clúster**: Región, VPC, subnets, versión K8s
2. **Nodos**: Grupos con Auto Scaling, Fargate Profiles
3. **Autenticación**: IAM, kubeconfig para kubectl
4. **Despliegue**: Manifiestos YAML, Helm charts
5. **Red**: LoadBalancer con ELB, Ingress Controllers
6. **Observabilidad**: CloudWatch, Prometheus, Grafana
7. **Seguridad**: Políticas de red, IRSA
8. **Escalabilidad**: Cluster Autoscaler, HPA

---

## Diagramas Conceptuales

### 1. EC2 con Almacenamiento y Seguridad
```
[Usuario/Cliente]
       ↓
[Internet/VPC Pública]
       ↓
┌─────────────────┐
│  Instancia EC2  │
│  - SO           │
│  - Aplicaciones │
└─────────────────┘
       ↓
┌─────────────────┐
│  Volumen EBS    │
│  (Persistente)  │
└─────────────────┘
       ↓
[Security Groups] → SSH/HTTP/HTTPS
```

### 2. EBS con Snapshots
```
┌─────────────────┐
│  Instancia EC2  │
└─────────────────┘
       ↓
┌─────────────────┐
│  Volumen EBS    │
│  - Tipo: gp3    │
│  - 100 GB       │
│  - 3000 IOPS    │
└─────────────────┘
       ↓
┌─────────────────┐
│   Snapshots     │
│ (en S3)         │
└─────────────────┘
```

### 3. EFS Acceso Concurrente
```
┌──────────┐     ┌──────────┐
│ EC2 App1 │     │ EC2 App2 │
└──────────┘     └──────────┘
      \               /
       \             /
        ┌───────────┐
        │   EFS FS  │
        │ Multi-AZ  │
        │Mount Tgts │
        └───────────┘
             ↓
     [Security Groups]
```

### 4. S3 con Integración
```
[Usuarios/Aplicaciones]
          ↓
    ┌─────────┐
    │ Bucket  │
    │ Objetos │
    └─────────┘
         ↓
┌────────┴────────┐
│                 │
[Versionado]  [Cifrado]
│                 │
[Replicación] [Eventos]
    ↓             ↓
[Otra Región] [Lambda/SNS/SQS]
```

### 5. ELB Distribución de Tráfico
```
   [Usuarios/Internet]
          ↓
    ┌─────────┐
    │   ELB   │
    │Listeners│
    │HealthCk │
    └─────────┘
    /    |    \
   ↓     ↓     ↓
[EC2-1][EC2-2][EC2-3]
```

---

## Tips de Estudio

### Priorización de Servicios
1. **Fundamentales**: EC2, S3, IAM, VPC
2. **Almacenamiento**: EBS, EFS, S3
3. **Red y Seguridad**: ELB, Security Groups, VPC
4. **Contenedores**: ECR, ECS, EKS
5. **Mensajería**: SNS, SQS

### Conceptos Clave por Servicio
- **EC2**: Tipos de instancias, AMIs, Security Groups
- **EBS**: Tipos de volúmenes, snapshots, IOPS
- **EFS**: NFS, mount targets, modos de rendimiento
- **S3**: Clases de almacenamiento, versionado, lifecycle
- **ELB**: ALB vs NLB, health checks, target groups
- **SNS/SQS**: Pub/Sub vs Queues, FIFO vs Standard

### Comparaciones Importantes

| Aspecto | EBS | EFS | S3 |
|---------|-----|-----|----|
| **Tipo** | Bloque | Archivo | Objeto |
| **Acceso** | Una instancia | Múltiples instancias | API/HTTP |
| **Uso** | Discos EC2 | Compartido | Archivos estáticos |
| **Persistencia** | Sí | Sí | Sí |

---

**Última actualización**: Guía generada para estudio de servicios AWS fundamentales