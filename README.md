# Cloud Architecture
# 🚀 Guía Esencial del Arquitecto Cloud (AWS Focus)

## 1. Fundamentos Clave de Arquitectura Cloud

La arquitectura cloud es el **diseño estructural de sistemas construidos, desplegados, escalados y gestionados en entornos de nube**. Busca optimizar recursos, mejorar el rendimiento y asegurar la mantenibilidad a largo plazo.

### 1.1 Principios de Diseño Esenciales
Un buen diseño arquitectónico considera:
* **Modularidad:** Componentes independientes y cohesivos (ej. Microservicios).
* **Resiliencia:** Capacidad de adaptarse y recuperarse de fallos sin interrupciones críticas.
* **Escalabilidad:** Habilidad para manejar cargas de trabajo crecientes o decrecientes.
* **Automatización:** Reducir la intervención humana.
* **Alta Disponibilidad:** Operatividad y accesibilidad constante.
* **Seguridad por Diseño:** Integrar la seguridad desde el inicio.
* **Optimización de Costos:** Maximizar valor y minimizar gastos.
* **Eficiencia de Rendimiento:** Uso eficiente de recursos.
* **Sostenibilidad:** Considerar el impacto ambiental de los recursos.

### 1.2 Modelos de Servicio: ¿Quién Gestiona Qué?
Definen el nivel de abstracción y responsabilidad compartida entre el proveedor y el usuario.

| Modelo | ¿Qué te ofrece?                                        | ¿Qué gestionas tú?                                    | Ejemplos AWS / GCP / Azure                             |
| :----- | :----------------------------------------------------- | :---------------------------------------------------- | :----------------------------------------------------- |
| **IaaS** | Infraestructura virtual (servidores, almacenamiento, redes). | SO, middleware, runtime, aplicación, datos. | **AWS EC2**, Google Compute Engine, Azure VMs. |
| **PaaS** | Plataforma para desarrollo/despliegue (SO, runtime, middleware gestionado). | Código de tu aplicación y sus datos.       | **AWS Elastic Beanstalk**, Google App Engine, Azure App Services. |
| **FaaS** | Funciones como Servicio (Serverless Compute). | Código de tus funciones y lógica de eventos. | **AWS Lambda**, Google Cloud Functions, Azure Functions. |
| **SaaS** | Aplicaciones completas listas para usar vía web. | Solo tus datos y configuración de uso.     | **AWS WorkMail**, Google Workspace, Salesforce, Zoom. |

---

## 2. Modelos de Implementación: ¿Dónde Residen los Servicios?
Definen la ubicación y gestión de la infraestructura.

| Modelo            | Descripción                                                                                                 | Ventajas Clave                                                                        | Desventajas Clave                                                              | Ejemplos (Casos de Uso)                               |
| :---------------- | :---------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------- | :---------------------------------------------------- |
| **On-Premise** | Toda la infraestructura y software gestionados **internamente**.                                 | Control total, seguridad máxima para datos sensibles.                      | Altos costos, baja flexibilidad y escalabilidad.                     | Bancos tradicionales (datos sensibles).     |
| **Cloud Pública** | Infraestructura gestionada por un **proveedor externo** (AWS, Azure, GCP) y compartida por múltiples clientes. | Bajos costos iniciales, alta flexibilidad y escalabilidad, menor administración. | Menor control, dependencia del proveedor, posibles costos elevados a largo plazo sin optimización. | **Netflix (AWS)**, Airbnb (Google Cloud). |
| **Cloud Privada** | Infraestructura dedicada **exclusivamente a una única organización**.                              | Mayor seguridad y privacidad, personalización total, cumplimiento normativo estricto. | Altos costos de implementación/mantenimiento, requiere personal especializado, menor flexibilidad. | Banco Santander (datos financieros).        |
| **Cloud Híbrida** | Combina elementos de **nube pública y privada**.                                                | Equilibrio entre seguridad y escalabilidad, reducción de costos operativos, flexibilidad. | Complejidad de integración y administración, mayor supervisión de seguridad. | General Electric, NASA.                     |
| **Multi-Cloud** | Uso de **varios proveedores de nube pública diferentes** simultáneamente.                               | Evita el *vendor lock-in*, optimiza servicios por proveedor.                          | Mayor complejidad de gestión, integración, y monitoreo.                        | Empresas que usan AWS para cómputo y Azure para servicios de datos específicos. |

---

## 3. Atributos de Calidad en Arquitectura Cloud

Son fundamentales para diseñar soluciones que maximicen disponibilidad, seguridad y capacidad de respuesta.

### 3.1 Resiliencia y Alta Disponibilidad
La **resiliencia** es la capacidad de un sistema para **adaptarse y recuperarse de fallos o interrupciones** sin afectar la disponibilidad y el rendimiento. La **disponibilidad** es la capacidad de estar **operativo y accesible constantemente**.
* **Mecanismos Clave:**
    * **Redundancia:** Duplicación de componentes críticos (datos, geográfica, servidores, redes).
    * **Recuperación ante Fallos:** Estrategias automáticas como reinicio de instancias, *failover*.
    * **Aislamiento de Componentes:** Limita el impacto de fallos (microservicios, contenedores, *circuit breakers*).
    * **Distribución Geográfica:** Uso de **Múltiples Zonas de Disponibilidad (AZs)** y Regiones.
    * **Pruebas de Resiliencia (Chaos Engineering):** Simulan fallos controlados (ej. Netflix con Chaos Monkey).
    * **Planes de Recuperación ante Desastres (DR):** Incluyen respaldos y conmutación automática.

### 3.2 Escalabilidad
Capacidad de un sistema para **manejar un aumento o disminución en la carga de trabajo** sin comprometer rendimiento ni disponibilidad.
* **Escalabilidad Horizontal (Scale Out):** Agrega **más instancias** para distribuir la carga. Común en microservicios y contenedores. (Ej. **AWS Auto Scaling Groups**).
* **Escalabilidad Vertical (Scale Up):** Mejora la **capacidad de servidores existentes** (CPU, RAM).
* **Autoescalado y Elasticidad:** Ajusta automáticamente los recursos según la demanda, incluso a cambios inesperados, **sin intervención humana**. (Ej. **AWS Lambda**).
* **Escalabilidad Global:** Distribuye cargas de trabajo en múltiples regiones geográficas para mejorar rendimiento y disponibilidad (ej. **AWS CloudFront** para CDN).

### 3.3 Seguridad
Crítica en entornos globalmente accesibles. Se basa en el **Modelo de Responsabilidad Compartida**.
* **Autenticación y Autorización:** Control de acceso, **MFA**, **OAuth**, **OpenID Connect**. **AWS IAM** para gestión de identidades y accesos, aplicando el **Principio de Mínimo Privilegio (PoLP)**.
* **Cifrado de Datos:**
    * **En Reposo:** Protege datos almacenados (discos, BDs). (Ej. **AWS KMS**, S3 encryption).
    * **En Tránsito:** Protege datos durante la transmisión (TLS 1.3, certificados SSL/TLS).
* **Red y Firewall:** **AWS VPC** (red privada aislada), **Security Groups** (firewall a nivel de instancia), **AWS WAF** (protección contra ataques web).
* **Monitoreo y Auditoría:** **AWS CloudTrail** (registra actividad de la cuenta), **AWS CloudWatch** (métricas, logs, alarmas).

### 3.4 Rendimiento
Eficiencia en la entrega de servicios y tiempo de respuesta.
* **Métricas:** Tiempo de respuesta (<2s para 90% del tráfico).
* **Optimización:** Caching (ej. **Amazon ElastiCache**), CDN (**AWS CloudFront**).

### 3.5 Mantenibilidad
Facilidad para actualizar, corregir y evolucionar el sistema.
* **Código Limpio y Documentación**.
* **Automatización de Despliegues (CI/CD):** **AWS CodePipeline, CodeBuild, CodeDeploy**.
* **Infraestructura como Código (IaC):** **AWS CloudFormation, AWS CDK, Terraform**.

---

## 4. Patrones Arquitectónicos Clave

Enfoques estandarizados para el diseño de software.

* **Monolítica:** Toda la aplicación en un solo bloque. Simplicidad inicial, pero escalado y mantenimiento complejos. (Ej. Aplicaciones bancarias tradicionales).
* **Microservicios:** Aplicación dividida en múltiples servicios independientes y pequeños. Alta escalabilidad granular, mayor resiliencia y flexibilidad.
    * **Orquestación:** **Amazon ECS/EKS** (Kubernetes), **Amazon Fargate**. (Ej. Netflix, Amazon).
* **Serverless (FaaS):** Ejecución de funciones en la nube sin gestionar servidores directamente. Bajo costo operativo (pago por uso), escalabilidad automática. (Ej. **AWS Lambda** para procesamiento de eventos en tiempo real).
* **Contenedores:** Encapsulan aplicaciones y sus dependencias en entornos portátiles (Docker). Despliegue y escalabilidad eficiente, alta portabilidad. (Ej. CI/CD en DevOps).

---

## 5. Diseño Práctico de Arquitectura Cloud: Checklist y Errores a Evitar

### 5.1 Checklist de Validación
* ¿Los SLOs (Service Level Objectives) cubren necesidades de negocio?
* ¿Existe redundancia multi-Zona?
* ¿Se automatizaron despliegues?
* ¿Se definieron RTO (Recovery Time Objective) y RPO (Recovery Point Objective) para DR?
* ¿Se aplican el Principio de Mínimo Privilegio?

### 5.2 Errores Comunes a Evitar
* **Acceso directo a DB desde Frontend:** Siempre a través de un backend (API).
* **Guardar secretos en código:** Usar **AWS Secrets Manager** o **Parameter Store**.
* **No habilitar logs/métricas/alarmas:** Monitorear desde el inicio con **AWS CloudWatch**.
* **Exponer recursos públicamente por defecto:** Aplicar PoLP con IAM y Security Groups restrictivos.
* **Usar IaaS cuando PaaS/FaaS son mejores:** Priorizar Serverless o PaaS para reducir la carga operativa.
* **No automatizar infraestructura:** Adoptar **IaC** para reproducibilidad y consistencia.

---

## 6. Proveedores Clave y Modelos de Costo

### 6.1 Proveedores Principales
1.  **AWS:** Líder del mercado.
2.  **Microsoft Azure:** Fuerte integración con Office 365.
3.  **Google Cloud:** Enfoque en IA y Big Data.
4.  IBM/Oracle Cloud: Soluciones empresariales.

### 6.2 Modelos de Costo
* **Pago por Uso:** Pagas solo por lo que consumes.
* Suscripciones, Instancias Reservadas (descuentos).

---

# 📊 Servicios AWS por Capa y Modelo (Guía Esencial para Arquitectos)

Esta guía segmenta los servicios de AWS en capas fundamentales y modelos de servicio, destacando su rol y necesidad en cualquier arquitectura cloud.

---

## 1. ⚙️ Capa de Infraestructura Fundamental y Habilitadores (Base para TODO)

Estos servicios son la columna vertebral de cualquier arquitectura en AWS. Son **absolutamente necesarios** o **altamente recomendados** para la operación, seguridad, monitoreo y conectividad de cualquier aplicación, sin importar el modelo de servicio que utilices (IaaS, PaaS, FaaS).

| Categoría Principal          | Servicio AWS                 | Necesidad   | Descripción                                                                                                                                                                                                            |
| :--------------------------- | :--------------------------- | :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Redes Virtuales** | **Amazon VPC** | Absoluta    | **Red privada virtual aislada** en la nube. Fundamental para lanzar recursos de forma segura y personalizada, definiendo subredes, tablas de ruteo, etc.                                                       |
|                              | **Amazon Route 53** | Absoluta    | **Servicio de DNS** escalable y de alta disponibilidad. Permite que tus aplicaciones sean accesibles mediante nombres de dominio amigables (ej. `miempresa.com`).                                           |
|                              | **AWS Direct Connect** | Opcional    | Establece una conexión de red privada dedicada de alta velocidad entre tu centro de datos on-premise y AWS. Ideal para híbridos y grandes volúmenes de datos.                                             |
| **Seguridad y Acceso** | **AWS IAM** | Absoluta    | **Gestión de identidades y accesos**. Controla quién (usuarios, grupos, roles) puede autenticarse y qué acciones pueden realizar en tu cuenta de AWS. Imprescindible para el **Principio de Mínimo Privilegio**. |
|                              | **AWS KMS** | Absoluta    | **Servicio de gestión de claves de cifrado**. Esencial para proteger tus datos en reposo (en S3, EBS, RDS, etc.) y en tránsito.                                                                        |
|                              | **AWS Secrets Manager** | Recomendado | Almacena, recupera y rota de forma segura credenciales de bases de datos, claves de API y otros secretos. Ayuda a evitar guardar secretos directamente en el código.                                    |
|                              | **AWS WAF** | Recomendado | **Firewall de aplicaciones web**. Protege tus aplicaciones web (detrás de CloudFront, API Gateway, ALB) de ataques web comunes (ej. inyección SQL, XSS).                                                 |
|                              | **AWS Shield** | Recomendado | Protección contra ataques DDoS (Denegación de Servicio Distribuida). (Shield Standard es automático y gratuito; Shield Advanced es de pago para mayor protección).                                         |
| **Monitoreo y Gestión** | **Amazon CloudWatch** | Absoluta    | **Monitoreo y observabilidad**. Recopila métricas (CPU, red), logs (aplicaciones, sistemas) y permite configurar alarmas y dashboards. Esencial para la visibilidad operativa.                                |
|                              | **AWS CloudTrail** | Absoluta    | **Auditoría y gobernanza**. Registra la actividad de la cuenta de AWS y las llamadas a la API, facilitando el cumplimiento normativo y la investigación de seguridad.                                        |
|                              | **AWS Config** | Opcional    | Evalúa, audita y valora las configuraciones de tus recursos de AWS para identificar desviaciones y cumplimiento, ayudando a mantener la seguridad y conformidad.                                        |
| **Almacenamiento Base** | **Amazon S3** | Absoluta    | **Almacenamiento de objetos escalable, duradero y disponible**. Utilizado para almacenar todo tipo de datos: backups, logs, contenido web estático, data lakes. Es la base de muchos servicios.                 |
| **Entrega de Contenido (CDN)** | **Amazon CloudFront** | Recomendado | **Red de entrega de contenido (CDN)**. Acelera la entrega de contenido web estático y dinámico a los usuarios finales mediante una caché en Edge Locations, mejorando el rendimiento y reduciendo la latencia. |
| **Infraestructura como Código (IaC)** | **AWS CloudFormation** | Absoluta    | Define y provisiona recursos de AWS mediante código declarativo (plantillas JSON/YAML). **Esencial para la automatización, reproducibilidad y consistencia** de tus infraestructuras.                       |
|                              | **AWS CDK** | Recomendado | Framework que permite definir tus recursos de nube usando lenguajes de programación populares (Python, TypeScript, Java, C#). Genera plantillas de CloudFormation.                                         |

---

## 2. ☁️ Servicios AWS por Modelo de Abstracción

Estos servicios se agrupan según el nivel de gestión y responsabilidad que AWS asume, permitiéndote concentrarte más o menos en el desarrollo de tu aplicación.

### 2.1. IaaS (Infraestructura como Servicio): Tú gestionas el sistema operativo y el software.

| Categoría Principal | Servicio AWS           | Descripción                                                                                               |
| :------------------ | :--------------------- | :-------------------------------------------------------------------------------------------------------- |
| **Cómputo** | **Amazon EC2** | Proporciona capacidad computacional redimensionable en la nube (máquinas virtuales).                        |
|                     | **Amazon EBS** | Almacenamiento persistente a nivel de bloque para instancias EC2 (discos virtuales que se adjuntan a VMs). |
| **Almacenamiento** | **Amazon EFS** | Sistema de archivos de red (NFS) escalable y compartido para instancias EC2, usable por múltiples instancias simultáneamente. |
|                     | **Amazon S3 Glacier** | Almacenamiento de archivo de bajo costo para datos a largo plazo (décadas), con tiempos de recuperación flexibles (minutos a horas). |

### 2.2. PaaS (Plataforma como Servicio): AWS gestiona el SO, el middleware y el runtime. Tú te enfocas en tu código.

| Categoría Principal   | Servicio AWS              | Descripción                                                                                               |
| :-------------------- | :------------------------ | :-------------------------------------------------------------------------------------------------------- |
| **Cómputo/Aplicaciones** | **AWS Elastic Beanstalk** | Facilita el despliegue y escalado de aplicaciones web y servicios con diversos lenguajes de programación (Java, .NET, PHP, Node.js, Python, Ruby, Go, y Docker). |
|                       | **Amazon ECS / EKS** | Servicios de orquestación de contenedores gestionados (ECS para Docker nativo de AWS, EKS para Kubernetes). |
|                       | **Amazon App Runner** | Despliegue de aplicaciones web en contenedores de forma más sencilla, sin gestionar la infraestructura subyacente. |
| **Bases de Datos** | **Amazon RDS** | Bases de datos relacionales gestionadas (MySQL, PostgreSQL, Oracle, SQL Server, MariaDB, Aurora). AWS se encarga de parches, backups y escalado. |
|                       | **Amazon DynamoDB** | Base de datos NoSQL clave-valor y de documentos de alto rendimiento, escalable y totalmente gestionada.  |
|                       | **Amazon ElastiCache** | Servicio de caché en memoria gestionado (Redis, Memcached) para acelerar las respuestas de la base de datos y la aplicación. |
| **APIs** | **Amazon API Gateway** | Crea, publica, mantiene, monitorea y asegura APIs RESTful y WebSocket. Actúa como el "front door" para el acceso a servicios backend. |
| **Integración** | **Amazon SQS** | Servicio de colas de mensajes desacopladas. Permite que los componentes de una aplicación envíen y reciban mensajes de forma asíncrona. |
|                       | **Amazon SNS** | Servicio de notificaciones push y publicación/suscripción. Envía mensajes a múltiples suscriptores o endpoints. |
|                       | **Amazon EventBridge** | Bus de eventos sin servidor para conectar aplicaciones con datos de tus propias aplicaciones, servicios SaaS y servicios de AWS. |

### 2.3. FaaS (Funciones como Servicio) / Serverless: Ejecutas código sin gestionar servidores.

| Categoría Principal    | Servicio AWS           | Descripción                                                                                               |
| :--------------------- | :--------------------- | :-------------------------------------------------------------------------------------------------------- |
| **Cómputo Serverless** | **AWS Lambda** | Ejecuta tu código en respuesta a eventos sin aprovisionar o administrar servidores. Pagas solo por el tiempo de cómputo consumido. |

### 2.4. SaaS (Software como Servicio): Aplicaciones completas listas para usar.

| Categoría Principal | Servicio AWS              | Descripción                                                                                               |
| :------------------ | :------------------------ | :-------------------------------------------------------------------------------------------------------- |
| **Productividad** | **Amazon WorkSpaces** | Escritorios virtuales en la nube a los que los usuarios pueden acceder desde cualquier dispositivo.         |
|                     | **Amazon Chime** | Servicio de comunicación unificada para reuniones, chat y llamadas.                                      |
| **Contact Center** | **Amazon Connect** | Servicio de centro de contacto omnicanal basado en la nube que permite configurar y administrar un centro de llamadas. |
| **Análisis de Datos** | **Amazon QuickSight** | Servicio de inteligencia de negocios escalable sin servidor que facilita la creación de visualizaciones y dashboards interactivos. |

---

# 🛠️ Desglose de Servicios AWS: Componentes Fundamentales

Esta tabla profundiza en los servicios principales de AWS, detallando sus componentes esenciales o más comúnmente utilizados. Comprender estos componentes es clave para diseñar, implementar y operar arquitecturas robustas en la nube.

---

| Servicio Principal | Componente Fundamental         | Tipo de Componente | Descripción                                                                                                                                                                                                                                                                                                         |
| :----------------- | :----------------------------- | :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Amazon S3** | **Buckets** | Absoluto           | Los contenedores lógicos donde se almacenan los objetos (archivos). Es el punto de partida para cualquier dato en S3. Cada objeto debe residir en un bucket.                                                                                                                                                            |
|                    | **Objetos** | Absoluto           | Los archivos reales (datos y metadatos) que se almacenan dentro de un bucket. Son la unidad de almacenamiento más pequeña en S3.                                                                                                                                                                                      |
|                    | **Clases de Almacenamiento** | Absoluto           | Tipos de almacenamiento que definen la durabilidad, disponibilidad, rendimiento y costo de los objetos (ej. S3 Standard, S3 Standard-IA, S3 Glacier, S3 Deep Archive). Se elige una clase por objeto.                                                                                                                   |
|                    | **Políticas de Bucket** | Recomendado        | Documentos JSON que definen permisos a nivel de bucket para controlar el acceso a sus objetos. Esencial para la seguridad y el control de acceso fino.                                                                                                                                                                  |
|                    | **Políticas de Ciclo de Vida** | Recomendado        | Reglas que automatizan la transición de objetos entre clases de almacenamiento (para optimizar costos) o su eliminación después de un tiempo específico.                                                                                                                                                               |
|                    | **Versionamiento** | Opcional           | Característica a nivel de bucket que permite mantener múltiples versiones de un objeto, protegiendo contra eliminaciones accidentales y permitiendo la recuperación de versiones anteriores.                                                                                                                             |
| **Amazon EC2** | **Instancias EC2** | Absoluto           | Las máquinas virtuales redimensionables que proporcionan la capacidad de cómputo. Se elige un tipo de instancia (CPU, RAM) al lanzar.                                                                                                                                                                                |
|                    | **Amazon Machine Images (AMI)**| Absoluto           | Plantillas preconfiguradas que contienen el sistema operativo, software y configuraciones necesarias para lanzar una instancia EC2. Pueden ser proporcionadas por AWS, la comunidad o personalizadas por el usuario.                                                                                                   |
|                    | **Tipos de Instancia** | Absoluto           | Define la capacidad de cómputo (CPU, memoria, almacenamiento, red) de una instancia. Se elige al lanzar la instancia (ej. `t3.micro`, `m6g.large`).                                                                                                                                                                       |
|                    | **Pares de Claves** | Absoluto           | Se utilizan para conectarse de forma segura a las instancias EC2 mediante SSH (Linux) o para cifrar contraseñas de RDP (Windows). Consta de una clave pública (en AWS) y una clave privada (en tu poder).                                                                                                                     |
|                    | **Grupos de Seguridad** | Absoluto           | Actúan como firewalls virtuales para tus instancias EC2, controlando el tráfico de red de entrada y salida a nivel de instancia. Son fundamentales para la seguridad de la red.                                                                                                                                        |
|                    | **Volúmenes EBS** | Absoluto           | Almacenamiento persistente a nivel de bloque que se adjunta a las instancias EC2, funcionando como discos duros virtuales.                                                                                                                                                                                            |
| **Amazon VPC** | **VPC (Virtual Private Cloud)**| Absoluto           | Tu red virtual aislada en la nube de AWS. Cada recurso que lanzas en AWS reside en una VPC.                                                                                                                                                                                                                         |
|                    | **Subredes** | Absoluto           | Divisiones lógicas de tu VPC (rangos de direcciones IP) que permiten organizar y aislar recursos, y pueden ser públicas (con acceso a internet) o privadas.                                                                                                                                                              |
|                    | **Tablas de Rutas** | Absoluto           | Conjunto de reglas que controlan el enrutamiento del tráfico de red dentro de tu VPC y hacia fuera de ella. Cada subred debe estar asociada a una tabla de rutas.                                                                                                                                                         |
|                    | **Internet Gateway (IGW)** | Recomendado        | Permite la comunicación entre las instancias de tu VPC (en subredes públicas) e Internet. Es necesario para que tus recursos en la nube sean accesibles desde fuera de AWS.                                                                                                                                                |
|                    | **Grupos de Seguridad** | Absoluto           | (Ya mencionado con EC2, pero aplicable a la capa de red general). Controlan el tráfico a nivel de instancia.                                                                                                                                                                                                           |
|                    | **Listas de Control de Acceso de Red (NACLs)** | Recomendado        | Firewalls a nivel de subred. Operan de forma stateless (sin estado) y permiten tanto reglas de entrada como de salida, ofreciendo una capa de seguridad adicional a los Grupos de Seguridad.                                                                                                                          |
| **Amazon RDS** | **Instancias de Base de Datos**| Absoluto           | La unidad fundamental de un motor de base de datos relacional gestionado por RDS (MySQL, PostgreSQL, etc.).                                                                                                                                                                                                       |
|                    | **Grupos de Parámetros de DB** | Recomendado        | Conjunto de configuraciones que se aplican a las instancias de base de datos. Permiten ajustar el comportamiento del motor de la base de datos (ej. tamaño de caché, logs).                                                                                                                                       |
|                    | **Grupos de Opciones de DB** | Recomendado        | Permiten habilitar funciones o características adicionales para tu base de datos (ej. soporte para Memcached, Transparent Data Encryption en SQL Server).                                                                                                                                                            |
|                    | **Grupos de Seguridad (VPC)** | Absoluto           | Controlan qué tráfico de red puede alcanzar tu instancia de base de datos RDS. Esencial para asegurar el acceso.                                                                                                                                                                                                    |
|                    | **Snapshots de DB** | Absoluto           | Copias de seguridad completas de tu instancia de base de datos en un punto en el tiempo, almacenadas en S3. Son esenciales para la recuperación ante desastres.                                                                                                                                                         |
|                    | **Read Replicas** | Opcional           | Copias asíncronas de tu instancia de base de datos que permiten escalar el rendimiento de lectura de tu aplicación.                                                                                                                                                                                                    |
| **AWS Lambda** | **Funciones Lambda** | Absoluto           | La unidad de código que se ejecuta en respuesta a eventos. Es el corazón del servicio Lambda.                                                                                                                                                                                                                       |
|                    | **Disparadores (Triggers)** | Absoluto           | El evento o servicio de AWS que invoca tu función Lambda (ej. una subida a S3, un mensaje de SQS, una llamada de API Gateway, una tabla de DynamoDB). Una función requiere al menos un disparador para ejecutarse.                                                                                                   |
|                    | **Entorno de Ejecución (Runtime)** | Absoluto           | El lenguaje de programación y la versión en la que se ejecuta tu código Lambda (ej. Node.js 18, Python 3.9, Java 17).                                                                                                                                                                                              |
|                    | **Capas (Layers)** | Opcional           | Permiten empaquetar librerías, runtimes personalizados o código común que puede ser compartido por múltiples funciones Lambda, reduciendo el tamaño de los paquetes de despliegue.                                                                                                                                  |
|                    | **Variables de Entorno** | Recomendado        | Pares clave-valor que puedes definir para tu función Lambda para almacenar configuraciones que no quieres codificar directamente (ej. cadenas de conexión a bases de datos, claves de API).                                                                                                                            |
| **AWS IAM** | **Usuarios (Users)** | Absoluto           | Representan personas o aplicaciones que interactúan con AWS. Cada usuario tiene sus propias credenciales (nombre de usuario/contraseña, claves de acceso).                                                                                                                                                           |
|                    | **Grupos (Groups)** | Recomendado        | Colecciones de usuarios a las que se adjuntan políticas. Simplifica la gestión de permisos al aplicarlos a múltiples usuarios a la vez.                                                                                                                                                                               |
|                    | **Roles (Roles)** | Recomendado        | Identidades de IAM con permisos específicos que puedes asumir temporalmente. Muy utilizados por servicios de AWS para interactuar entre sí, o para dar acceso temporal a usuarios federados. Promueven el Principio de Mínimo Privilegio.                                                                                |
|                    | **Políticas (Policies)** | Absoluto           | Documentos JSON que definen los permisos (acciones permitidas o denegadas) sobre los recursos de AWS. Se adjuntan a usuarios, grupos o roles. Son el corazón del control de acceso en AWS.                                                                                                                             |
|                    | **MFA (Multi-Factor Authentication)** | Recomendado        | Una capa adicional de seguridad que requiere una segunda forma de verificación (ej. código de un dispositivo, huella dactilar) además de la contraseña. Altamente recomendado para usuarios raíz y usuarios IAM privilegiados.                                                                                     |

---

Esta tabla es un buen punto de partida para ver cómo los servicios de alto nivel se componen de bloques más pequeños que controlas. ¡Espero que te sea de gran utilidad!