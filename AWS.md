---
# 📚 Guía Completa de Arquitectura Cloud con AWS y Conceptos Esenciales

---

## 1. Fundamentos Clave de Arquitectura Cloud

### 1.1 ¿Qué es Arquitectura Cloud?
Es el **diseño estructural de sistemas que se construyen, despliegan, escalan y gestionan en entornos de computación en la nube**. Se basa en principios fundamentales para asegurar que las aplicaciones sean robustas y eficientes.

**Principios clave:**
* **Resiliencia:** Capacidad de recuperarse de fallos y mantener la funcionalidad.
* **Escalabilidad:** Habilidad para manejar cargas de trabajo crecientes o decrecientes.
* **Automatización:** Reducir la intervención humana en despliegue, gestión y operación.
* **Alta Disponibilidad:** Asegurar que el sistema esté operativo y accesible la mayor parte del tiempo.
* **Seguridad por Diseño:** Integrar la seguridad en cada etapa del desarrollo y despliegue.

### 1.2 Los Pilares de Toda Arquitectura Cloud

| Pilar                 | Qué incluye                                     | Importancia                                             |
| :-------------------- | :---------------------------------------------- | :------------------------------------------------------ |
| **Modelos de Despliegue** | Público, Privado, Híbrido, Multi-Cloud          | Define **dónde** residen y se gestionan los servicios.  |
| **Modelos de Servicio** | IaaS, PaaS, SaaS, FaaS                          | Define **quién gestiona qué** en el stack tecnológico.  |
| **Diseño Técnico** | Microservicios, API REST, Autenticación, DevOps, Monitoreo, Bases de Datos | Define **cómo** interactúan los componentes del sistema. |

> ⚠️ **Pregunta fundamental de un Arquitecto:** ¿Quién gestiona qué? ¿Dónde está el código? ¿Cómo se asegura, monitorea y escala?

---

## 2. Modelos de Despliegue en la Nube

Estos modelos definen la ubicación y la gestión de la infraestructura de tu aplicación.

| Modelo          | Descripción                                                                                                  | Ejemplo                                                                                                     |
| :-------------- | :----------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| **On-Premise** | Toda la infraestructura y el software están instalados y gestionados **dentro de la propia empresa**.       | Servidor físico en la oficina con base de datos local y aplicaciones propias.                               |
| **Cloud Pública** | Recursos de computación compartidos, alojados y gestionados por un proveedor externo de la nube (AWS, Azure, GCP). | **AWS EC2, S3, Lambda**; Azure VMs, Azure Blob Storage; Gmail, Google Drive.                           |
| **Cloud Privada** | Infraestructura de nube dedicada **exclusivamente a una única organización**. Puede ser on-premise o alojada por un tercero. | Una empresa que usa OpenStack para gestionar sus propios servidores en su centro de datos.                  |
| **Cloud Híbrida** | Una combinación de infraestructura **on-premise** con recursos de **nube pública**. Permite compartir datos y aplicaciones entre ambos entornos. | Base de datos local para datos sensibles + backups automáticos en **AWS S3** o **Azure Blob Storage**.      |
| **Multi-Cloud** | El uso de **varios proveedores de nube pública diferentes** simultáneamente para distintas aplicaciones o componentes. | Aplicación principal en **AWS** + CDN en GCP + base de datos específica en **Azure**.                      |

---

## 3. Modelos de Servicio en la Nube (La clave de la responsabilidad)

Estos modelos definen el nivel de abstracción y, por lo tanto, tu nivel de responsabilidad sobre la infraestructura.

| Modelo | ¿Qué te ofrece?                                                 | ¿Qué gestionas tú?                                    | Ejemplos AWS/Azure                                                                                                                  |
| :----- | :-------------------------------------------------------------- | :---------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| **IaaS** | **Infraestructura virtual**: Servidores (VMs), redes, almacenamiento, balanceadores de carga. Es como tener un centro de datos virtual. | Sistema operativo, middleware, runtime, aplicación, datos. | **AWS EC2, EBS, VPC**; Azure VMs, Azure Virtual Network.                                                                             |
| **PaaS** | **Plataforma lista** para desplegar aplicaciones. Incluye el SO, runtime, middleware y servicios de base de datos gestionados. | Solo el **código de tu aplicación** y sus datos. | **AWS Elastic Beanstalk, Amazon Fargate (ECS/EKS)**; Azure App Services, Azure Kubernetes Service (AKS), Google App Engine.          |
| **FaaS** | **Función como Servicio** (Serverless Compute). Ejecuta código en respuesta a eventos sin gestionar ningún servidor subyacente. | Solo el **código de tus funciones** y la lógica de los eventos. | **AWS Lambda**; Azure Functions, Google Cloud Functions.                                                                           |
| **SaaS** | **Aplicaciones completas listas para usar**, accesibles directamente desde un navegador web o una aplicación cliente. | Solo tus **datos** y la configuración de la aplicación (usuarios, permisos específicos, etc.). | **AWS WorkMail, Amazon Chime, Amazon Connect, Amazon QuickSight**; Microsoft 365, Salesforce, Gmail. Tú eres el consumidor. |

---

### 3.1 Comparación de Responsabilidades: ¿Quién Gestiona Qué?

Esta tabla es crucial para entender la diferencia entre los modelos de servicio desde la perspectiva de tu responsabilidad como usuario/desarrollador.

| Parte del Sistema                   | On-Premise (Tú) | IaaS (Tú)    | PaaS (Tú)    | FaaS (Tú)      | SaaS (Tú)                               |
| :---------------------------------- | :-------------- | :----------- | :----------- | :------------- | :-------------------------------------- |
| Infraestructura Física              | **Tú** | Proveedor    | Proveedor    | Proveedor      | Proveedor                               |
| Red y Servidores Físicos            | **Tú** | Proveedor    | Proveedor    | Proveedor      | Proveedor                               |
| Virtualización                      | **Tú** | Proveedor    | Proveedor    | Proveedor      | Proveedor                               |
| Sistema Operativo                   | **Tú** | **Tú** | Proveedor    | Proveedor      | Proveedor                               |
| Plataforma (Runtime, Middleware)    | **Tú** | **Tú** | Proveedor    | Proveedor      | Proveedor                               |
| **Aplicación** | **Tú** | **Tú** | **Tú** | Proveedor      | Proveedor                               |
| **Código de Funciones/Microservicios** | N/A             | N/A          | N/A          | **Tú** | N/A                                     |
| **Datos y Configuración de Uso** | **Tú** | **Tú** | **Tú** | **Tú** | **Tú (almacenados y gestionados por el proveedor)** |

> **Nota:** En **SaaS**, eres dueño de tus datos (los subes, los creas, los controlas), pero el proveedor es responsable de la infraestructura y el software que los aloja, cifra, y te permite acceder. Es vital revisar sus políticas de seguridad y privacidad.

---

## 4. Servicios y Tecnologías Clave de AWS (con equivalentes en Azure)

Como arquitecto, debes conocer los servicios específicos que usarás para implementar tus diseños.

| Servicio / Tecnología | Tipo                                | Función Principal                                                         | Relación con Arquitectura/Modelo       | Similar a... (Azure)         |
| :-------------------- | :---------------------------------- | :-------------------------------------------------------------------------- | :------------------------------------- | :--------------------------- |
| **Amazon EC2** | **IaaS** | Instancias virtuales configurables para ejecutar cualquier SO o aplicación. | Computo fundamental (VMs).             | Azure VMs                    |
| **Amazon S3** | **IaaS** (Almacenamiento de objetos) | Almacén de objetos escalable y duradero (imágenes, backups, logs, documentos). | Almacenamiento primario en la nube.    | Azure Blob Storage           |
| **Amazon RDS** | **PaaS** (DBaaS)                    | Base de datos relacional gestionada (MySQL, PostgreSQL, SQL Server, Oracle). | Base de datos relacional.              | Azure SQL Database, Azure Database for PostgreSQL/MySQL |
| **Amazon DynamoDB** | **PaaS** (DBaaS)                    | Base de datos NoSQL de alto rendimiento y escalabilidad.                     | Base de datos NoSQL.                   | Azure Cosmos DB              |
| **AWS Lambda** | **FaaS** | Ejecuta código (funciones) en respuesta a eventos sin gestionar servidores. | Serverless, microservicios.            | Azure Functions              |
| **API Gateway** | **PaaS / API** | Puerta de entrada para APIs REST y WebSocket, con control de acceso y throttling. | Exposición de APIs, serverless.        | Azure API Management         |
| **AWS Elastic Beanstalk** | **PaaS** | Despliegue automático y gestión de aplicaciones web y servicios.             | Simplifica despliegue de apps.         | Azure App Services           |
| **Amazon ECS / EKS** | **PaaS / Contenedores** | Orquestación de contenedores (Docker/Kubernetes) para microservicios.      | Contenerización, microservicios.       | Azure Kubernetes Service (AKS) |
| **Amazon VPC** | **IaaS** (Redes)                    | Red privada virtual aislada dentro de AWS para tus recursos.                 | Base de la red y seguridad.            | Azure Virtual Network        |
| **AWS IAM** | **Seguridad** | Gestión de identidades y accesos; controla quién puede hacer qué en AWS.     | Autenticación, autorización.           | Azure Active Directory (AD)  |
| **AWS Cognito** | **Seguridad** | Autenticación, autorización y gestión de usuarios para aplicaciones web y móviles. | Autenticación de usuarios finales.     | Azure AD B2C                 |
| **AWS CloudWatch** | **Monitoreo** | Recopila logs, métricas y permite configurar alarmas y paneles de control.   | Observabilidad, rendimiento.           | Azure Monitor                |
| **AWS CloudFormation**| **Infraestructura como Código (IaC)** | Permite definir y aprovisionar recursos de AWS mediante código declarativo. | Automatización, reproducibilidad.      | Azure Resource Manager (ARM) Templates, Terraform |
| **AWS WAF** | **Seguridad** | Firewall de aplicaciones web que protege contra ataques web comunes.          | Protección de aplicaciones web.        | Azure Application Gateway WAF |
| **AWS CloudFront** | **CDN** | Distribución global de contenido estático y dinámico para mejorar la latencia y rendimiento. | Mejora de rendimiento y latencia.      | Azure CDN                    |
| **AWS CloudTrail** | **Auditoría / Seguridad** | Registra toda la actividad de la cuenta AWS para auditoría y cumplimiento.   | Trazabilidad, seguridad, auditoría.    | Azure Activity Log           |

---

## 5. Diseño de Arquitectura Cloud: Consideraciones y Buenas Prácticas

Aquí es donde los conceptos y servicios se unen para construir soluciones robustas.

| Componente           | Buenas Prácticas                                                                                                                                                                                                                                                        |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Frontend Web** | **Hosting estático en S3** (para HTML/CSS/JS) con **CloudFront** (CDN) para distribución global, baja latencia y caching.                                                                                                                                               |
| **Backend** | Generalmente implementado como **API REST**. Puede correr en **EC2** (IaaS, control total), **Elastic Beanstalk** (PaaS, enfoque en código), **ECS/EKS** (PaaS, contenedores) o **Lambda** (FaaS, serverless para microservicios o funciones específicas).                 |
| **Seguridad** | **IAM Roles y Políticas** para permisos de servicio a servicio y de usuario a recurso. **Cognito** para autenticación de usuarios finales. **Grupos de Seguridad (Security Groups)** como firewalls a nivel de instancia. **WAF** para protección de aplicaciones web. Siempre usar **principio de menor privilegio**. |
| **Base de Datos** | **RDS** para datos relacionales (ej. transacciones, usuarios). **DynamoDB** para datos NoSQL que requieren alta escalabilidad y flexibilidad (ej. perfiles de usuario, eventos, logs). Elige según el patrón de acceso a los datos.                                    |
| **APIs REST** | Usar **API Gateway** como "fachada" para tus backends (Lambda, EC2, ECS). Provee control de acceso, throttling (límites de llamadas), caching y monitoreo centralizado.                                                                                                |
| **Monitoreo y Logs** | Activar **CloudWatch** para métricas, logs (CloudWatch Logs) y alarmas. **X-Ray** para trazabilidad de solicitudes en sistemas distribuidos (microservicios). **CloudTrail** para auditoría de acciones en tu cuenta.                                                   |
| **Infraestructura como Código (IaC)** | Usar **CloudFormation, AWS CDK o Terraform** para definir y aprovisionar toda tu infraestructura como código. Esto asegura reproducibilidad, automatización y consistencia en los despliegues.                                                              |
| **Escalabilidad** | **Auto Scaling** para EC2 o Fargate para escalar horizontalmente los recursos de cómputo según la demanda. Los servicios **Serverless (Lambda, DynamoDB)** escalan automáticamente.                                                                                   |
| **Alta Disponibilidad** | Desplegar componentes clave en **múltiples Zonas de Disponibilidad (AZs)** dentro de una región. Usar **Balanceadores de Carga (ELB)** para distribuir el tráfico entre instancias. Configurar **replicas de lectura en RDS** y **tablas globales en DynamoDB**.     |
| **Gestión de Secretos** | Nunca guardar credenciales o secretos en el código. Usar **AWS Secrets Manager** o **AWS Systems Manager Parameter Store** para gestionar y rotar secretos de forma segura.                                                                                               |
| **Despliegue (CI/CD)** | Implementar pipelines de Integración Continua / Despliegue Continuo (CI/CD) usando servicios como **AWS CodePipeline, CodeBuild, CodeDeploy** o herramientas de terceros como GitLab CI/CD, Jenkins.                                                                 |

---

## 6. Errores Comunes que Debes Evitar como Arquitecto Cloud

| Error Común                             | Solución Recomendada                                                               |
| :-------------------------------------- | :--------------------------------------------------------------------------------- |
| Acceso directo a la Base de Datos desde el Frontend. | Siempre pasa por un **Backend (API)** o un servicio de API Gateway.              |
| Guardar secretos (claves API, credenciales DB) en el código fuente. | Usa **AWS Secrets Manager** o **AWS Systems Manager Parameter Store**.           |
| No habilitar logs, métricas y alarmas.  | Activa **CloudWatch Logs**, métricas y configura **alarmas** desde el inicio.        |
| Exponer recursos (ej. S3 Buckets, EC2) públicamente por defecto. | Aplica el **Principio de Menor Privilegio (PoLP)** con IAM. Usa **políticas de bucket** y **Security Groups** restrictivos. |
| Usar **IaaS (EC2)** cuando una solución **PaaS o FaaS** es más adecuada. | Siempre evalúa si puedes usar **Serverless (Lambda)** o **PaaS (Elastic Beanstalk, ECS Fargate)** antes de optar por IaaS para reducir la carga operativa. |
| No planificar la **recuperación ante desastres (DR)**. | Define una estrategia de RTO (Recovery Time Objective) y RPO (Recovery Point Objective) y haz backups regulares. |
| Olvidar la **automatización de la infraestructura**. | Adopta **Infraestructura como Código (IaC)** con CloudFormation o Terraform para todos los despliegues. |

---

## 7. Checklist Mental para Resolver Cualquier Caso como Arquitecto Cloud

Usa esta lista de preguntas para guiar tus decisiones de diseño:

* ✅ **Propósito de la Aplicación:** ¿Qué tipo de aplicación es (web, API, batch, streaming, móvil, IoT)?
* ✅ **Modelo de Despliegue:** ¿Necesita ser pública, privada, híbrida, multi-cloud?
* ✅ **Modelo de Servicio:** ¿Cuál es el nivel de gestión deseado (IaaS, PaaS, FaaS) para cada componente? ¿Se puede usar un SaaS ya existente?
* ✅ **Componentes de Cómputo:** ¿Dónde vivirá el código (EC2, Lambda, ECS/EKS, Elastic Beanstalk)?
* ✅ **Almacenamiento de Datos:** ¿Dónde se guardarán los datos (RDS, S3, DynamoDB, ElastiCache, EBS)? ¿Qué tipo de base de datos se adapta mejor?
* ✅ **Autenticación y Autorización:** ¿Cómo se autenticarán los usuarios y cómo se controlará el acceso a los recursos (Cognito, IAM)?
* ✅ **Redes:** ¿Cómo se aislará la red (VPC), qué puertos se abrirán (Security Groups), cómo se enrutará el tráfico (Route 53, ALB/NLB)?
* ✅ **Escalabilidad y Alta Disponibilidad:** ¿Cómo escalará el sistema bajo demanda (Auto Scaling, Serverless)? ¿Cómo se asegurará la continuidad del servicio ante fallos (múltiples AZs, ELB)?
* ✅ **Monitoreo y Observabilidad:** ¿Cómo se monitoreará el rendimiento, se recolectarán logs y se configurarán alarmas (CloudWatch, X-Ray, CloudTrail)?
* ✅ **Automatización y Despliegue:** ¿Se puede automatizar el despliegue de la infraestructura y la aplicación (IaC, CI/CD)?
* ✅ **Seguridad:** ¿Cómo se protegerán los datos (cifrado en reposo/tránsito), se gestionarán los secretos (Secrets Manager) y se protegerá contra ataques (WAF)?
* ✅ **Costos:** ¿Cuál es el costo estimado de la solución y cómo se optimizará?
* ✅ **Riesgos:** ¿Cuáles son los riesgos identificados y cómo se mitigarán?

---

## 8. Plantilla: Diseño Inicial de Arquitectura Cloud (Proyecto Real)

Usa esta plantilla para estructurar tus propuestas de arquitectura para cualquier proyecto.

---

### # 📘 Diseño Inicial de Arquitectura – Proyecto [Nombre del Proyecto]

## 1. Resumen del Proyecto
Breve descripción del objetivo del sistema, los usuarios clave y el problema que resuelve.
*Ejemplo: "BarCraft" es una aplicación web que permite a los clientes del bar realizar pedidos de cerveza artesanal desde sus teléfonos móviles. Al mismo tiempo, el personal del bar (cajeros o garzones) puede gestionar los pedidos desde una interfaz interna.*

## 2. Alcance
-   **Funcionalidades Incluidas en esta Fase:**
    -   [ ] Listar funcionalidades clave del sistema (ej. Módulo de cliente: visualización de menú, selección de productos, añadir al carrito, pago online. Módulo de personal: visualización de pedidos entrantes, cambio de estado de pedidos).
-   **Exclusiones:**
    -   [ ] Funcionalidades fuera del alcance (ej. Gestión de inventario, integración con sistemas POS existentes, etc.).
-   **Límites Técnicos:**
    -   [ ] Restricciones específicas (ej. solo compatible con navegadores modernos, no soporta pagos en efectivo vía app).

## 3. Requisitos
### 3.1 Requisitos Funcionales
-   [ ] Los clientes deben poder ver el menú actualizado en tiempo real.
-   [ ] Los clientes deben poder añadir productos al carrito y ajustar cantidades.
-   [ ] Los clientes deben poder realizar pagos seguros online (ej. con tarjeta de crédito).
-   [ ] El personal del bar debe poder ver una lista de pedidos entrantes.
-   [ ] El personal debe poder cambiar el estado de un pedido (ej. "En preparación", "Listo para recoger", "Entregado").

### 3.2 Requisitos No Funcionales
-   **Alta Disponibilidad:** [99.9% uptime esperado]
-   **Escalabilidad:** [Automática / Horizontal para manejar picos de demanda durante fines de semana y eventos especiales]
-   **Seguridad:** [Cifrado de datos en tránsito y en reposo, autenticación de usuarios robusta, cumplimiento con PCI DSS para pagos].
-   **Tiempo de Respuesta Esperado:** [Menos de 300 ms para interacciones críticas con la aplicación].
-   **Rendimiento:** [Soportar hasta 1000 usuarios concurrentes sin degradación del servicio].
-   **Mantenibilidad:** [Fácil de actualizar y mantener con pipelines CI/CD].

## 4. Arquitectura Propuesta
### 4.1 Descripción General
La aplicación se construirá con una arquitectura de microservicios. El frontend será una Single Page Application (SPA) estática. El backend se compondrá de APIs Serverless para el procesamiento de pedidos y gestión de menú, y un PaaS para la interfaz de administración del personal. Se utilizará una base de datos gestionada para los datos transaccionales.

### 4.2 Diagrama de Arquitectura
```mermaid
graph TD
    subgraph Cliente - Web/Móvil
        A[Navegador/App Móvil]
    end

    subgraph CDN
        B[CloudFront - Distribución Global]
    end

    subgraph Hosting Frontend
        C[Amazon S3 - Hosting Estático]
    end

    subgraph API Gateway
        D[API Gateway - Puntos de Acceso para Clientes]
    end

    subgraph Lógica de Negocio - Serverless
        E[AWS Lambda - Microservicio Pedidos]
        F[AWS Lambda - Microservicio Menu]
        G[AWS Lambda - Microservicio Pagos]
    end

    subgraph Base de Datos
        H[Amazon RDS - MySQL para Transacciones]
    end

    subgraph Personal del Bar - Interfaz Admin
        I[Backend Admin - AWS Elastic Beanstalk]
        J[Frontend Admin - S3 + CloudFront]
    end

    subgraph Autenticación y Autorización
        K[Amazon Cognito - Gestión de Usuarios Clientes]
        L[AWS IAM - Roles para Servicios]
    end

    subgraph Almacenamiento de Contenido
        M[Amazon S3 - Imágenes de Productos]
    end

    subgraph Redes y Seguridad
        N[Amazon VPC - Red Aislada]
        O[Security Groups - Firewall]
    end

    subgraph Monitoreo y Auditoría
        P[AWS CloudWatch - Logs y Métricas]
        Q[AWS CloudTrail - Auditoría de Acciones]
    end

    A -- "Accede" --> B
    B -- "Contenido Estático" --> C
    A -- "Llama APIs" --> D
    D -- "Invoca" --> E
    D -- "Invoca" --> F
    D -- "Invoca" --> G
    E -- "Accede" --> H
    F -- "Accede" --> H
    G -- "Accede" --> H
    G -- "Procesa" --> Z[Servicio de Pago Externo]

    I -- "Accede" --> H
    I -- "Accede" --> M
    I -- "Accede" --> L
    J -- "Accede" --> B
    J -- "Accede" --> I

    L -- "Autoriza" --> E, F, G, I
    K -- "Autentica Clientes" --> A, D
    O -- "Controla Tráfico" --> E, F, G, H, I
    N -- "Contiene" --> E, F, G, H, I, O
    P -- "Monitorea" --> E, F, G, H, I
    Q -- "Audita" --> L
```

*Incluir servicios como EC2, Lambda, RDS, S3, VPC, etc.*

### 4.3 Componentes Principales
| Componente             | Servicio AWS / Modelo           | Descripción                                                                                                                                                                                                                                                                     |
| :--------------------- | :------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Frontend Clientes** | **Amazon S3 + CloudFront** (IaaS/CDN) | SPA estática para la interfaz del cliente. Hosting de bajo costo y alta velocidad de entrega global.                                                                                                                                                                  |
| **Backend API Clientes** | **API Gateway + AWS Lambda** (PaaS/FaaS) | Microservicios Serverless para lógica de negocio de pedidos, menú y pagos. Escalabilidad automática y pago por uso, ideal para picos de demanda.                                                                                                                             |
| **Base de Datos** | **Amazon RDS (MySQL)** (PaaS/DBaaS) | Base de datos relacional gestionada para almacenar usuarios, pedidos, detalles de menú, etc. Provee backups automáticos, alta disponibilidad y escalado sin gestión de infraestructura de DB.                                                                             |
| **Autenticación** | **Amazon Cognito** (SaaS/Security) | Gestión de usuarios y autenticación para los clientes de la aplicación. Permite login con email/contraseña o redes sociales.                                                                                                                                             |
| **Backend Administración** | **AWS Elastic Beanstalk** (PaaS) | Interfaz web para el personal del bar. Ideal para aplicaciones web tradicionales que requieren un entorno de ejecución gestionado sin la complejidad de IaaS, pero con más control que FaaS para una aplicación con más estado.                                                    |
| **Almacenamiento de Medios** | **Amazon S3** (IaaS)          | Almacenamiento de imágenes de productos y otros recursos estáticos.                                                                                                                                                                                                  |
| **Redes** | **Amazon VPC** (IaaS)           | Red virtual aislada para todos los recursos, con subredes privadas para bases de datos y backends, y subredes públicas para balanceadores de carga.                                                                                                                           |
| **Control de Acceso** | **AWS IAM** (Security)          | Define roles y políticas para que los servicios de AWS interactúen de forma segura entre sí (ej. Lambda accede a RDS, Elastic Beanstalk accede a S3).                                                                                                                     |

## 5. Seguridad
-   **Autenticación y Autorización:**
    -   **Cognito** para autenticación de usuarios finales (clientes).
    -   **IAM Roles** con el **Principio de Menor Privilegio (PoLP)** para la comunicación entre servicios de AWS (ej. Lambda solo puede leer/escribir en tablas específicas de DynamoDB).
-   **Red y Firewall:**
    -   **Grupos de Seguridad (Security Groups)** para controlar el tráfico de red permitido a nivel de instancia/recurso.
    -   **VPC** para aislamiento de red.
    -   Posible uso de **AWS WAF** para protección de la API de clientes contra ataques web comunes.
-   **Cifrado:**
    -   **Cifrado en tránsito (HTTPS/SSL)** para todas las comunicaciones (CloudFront, API Gateway, Elastic Beanstalk).
    -   **Cifrado en reposo** para datos en S3 y RDS.
-   **Auditoría:**
    -   **AWS CloudTrail** para registrar todas las acciones de la API en la cuenta AWS.
    -   **AWS CloudWatch Logs** para recolectar logs de aplicaciones y servicios.

## 6. Networking
-   **Amazon VPC:** Se creará una VPC con subredes públicas y privadas distribuidas en múltiples Zonas de Disponibilidad para alta disponibilidad.
-   **Subredes Privadas:** Para RDS, Lambdas (si se necesitan dentro de la VPC), y el backend de Elastic Beanstalk.
-   **Subredes Públicas:** Para Application Load Balancers (ALB) y NAT Gateways.
-   **API Gateway:** Servirá como endpoint público para la API de clientes.
-   **CloudFront:** Actuará como CDN y punto de entrada para el frontend estático.
-   **Route 53:** Gestionará los registros DNS para los dominios de la aplicación.

## 7. Escalabilidad y Alta Disponibilidad
-   **Escalabilidad:**
    -   **AWS Lambda:** Escala automáticamente según la carga de invocaciones.
    -   **Amazon RDS:** Permite escalar verticalmente (cambiar tipo de instancia) y escalar con réplicas de lectura.
    -   **Elastic Beanstalk:** Configurará Auto Scaling Groups para escalar las instancias EC2 subyacentes según la demanda.
    -   **Amazon S3 y DynamoDB:** Servicios que escalan automáticamente por diseño.
-   **Alta Disponibilidad:**
    -   **Múltiples Zonas de Disponibilidad (AZs):** Todos los componentes críticos (RDS, Elastic Beanstalk, Lambda si es necesario) se desplegarán en al menos dos AZs para tolerancia a fallos.
    -   **Application Load Balancer (ALB):** Distribuirá el tráfico entre las instancias de Elastic Beanstalk y los endpoints de Lambda/API Gateway.
    -   **RDS Multi-AZ:** Para la base de datos relacional, se habilitará la opción Multi-AZ para una réplica síncrona en otra AZ.

## 8. Backup y Recuperación
-   **Backup:**
    -   **RDS Snapshots:** Backups automáticos y manuales de la base de datos.
    -   **S3 Versioning:** Protección contra eliminación accidental de archivos en S3.
    -   **Lambda/APIs:** El código fuente se gestionará en un repositorio Git y se desplegará a través de CI/CD.
-   **Recuperación ante Desastres (DR):**
    -   **RTO (Recovery Time Objective):** [Ej: < 4 horas para servicios críticos].
    -   **RPO (Recovery Point Objective):** [Ej: < 15 minutos de pérdida de datos].
    -   Se establecerán procedimientos de restauración a partir de backups en caso de desastre.

## 9. Costeo Estimado
*Se realizaría un análisis detallado aquí con la calculadora de costos de AWS, considerando el dimensionamiento inicial y las proyecciones de uso.*

| Componente           | Servicio AWS              | Estimado Mensual (USD) | Notas                                     |
| :------------------- | :------------------------ | :--------------------- | :---------------------------------------- |
| Cómputo API Clientes | API Gateway + Lambda      | $X.XX                   | Por invocación y GB-segundo.              |
| Base de Datos        | RDS (MySQL)               | $X.XX                   | Tipo de instancia, almacenamiento, I/O.   |
| Almacenamiento       | S3                        | $X.XX                   | Por GB almacenado, solicitudes, transferencia. |
| Hosting Frontend     | S3 + CloudFront           | $X.XX                   | Transferencia de datos, solicitudes.      |
| Backend Admin        | Elastic Beanstalk         | $X.XX                   | Horas de EC2, ELB, almacenamiento.        |
| Autenticación        | Cognito                   | $X.XX                   | Por usuarios activos mensuales.           |
| Monitoreo            | CloudWatch                | $X.XX                   | Logs, métricas, alarmas.                  |
| **TOTAL ESTIMADO** | **$X.XX - $Y.YY** |                        | **Rango inicial.** |

## 10. Riesgos Identificados
| Riesgo                                 | Impacto  | Mitigación                                                         |
| :------------------------------------- | :------- | :----------------------------------------------------------------- |
| Falta de experiencia del equipo con Serverless. | Medio    | Capacitación en AWS Lambda y API Gateway; iniciar con prototipos pequeños. |
| Aumento inesperado de tráfico durante eventos especiales. | Alto     | Configurar límites de concurrencia en Lambda; provisionar suficiente capacidad en Elastic Beanstalk y RDS. |
| Complejidad en la integración de pagos. | Medio    | Usar SDKs y frameworks bien documentados; pruebas exhaustivas.    |
| Costos iniciales más altos de lo esperado si no se optimiza. | Medio    | Monitoreo constante de costos con AWS Cost Explorer; usar Free Tier al inicio. |

## 11. Anexos
-   Enlaces a la documentación oficial de cada servicio de AWS.
-   Referencias a patrones de arquitectura serverless o de microservicios.
-   Diagramas de flujo de proceso más detallados para pedidos y administración.

---

## 📚 Recomendaciones Finales de Aprendizaje

-   ✅ **Practica en AWS Free Tier**: La mejor manera de aprender es haciendo. Crea una API con Lambda + API Gateway + DynamoDB.
-   ✅ **Realiza laboratorios en:** [AWS Skill Builder](https://skillbuilder.aws), [Qwiklabs](https://www.qwiklabs.com/) y los laboratorios de Azure.
-   ✅ **Preguntas clave en cada proyecto**:
    -   ¿Qué parte es infraestructura y cuál es aplicación?
    -   ¿Qué parte puedo automatizar (IaC, CI/CD)?
    -   ¿Dónde están los riesgos de seguridad y cómo se mitigan?
    -   ¿Se puede escalar esto sin rediseñar todo?
    -   ¿Cómo se monitoreará el sistema para asegurar su operación?

---