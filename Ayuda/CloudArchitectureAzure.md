# 📘 Resumen de Arquitectura Cloud y Modelos de Servicio

## 🌐 Modelos de Despliegue (Dónde se ejecuta el software)

| Modelo           | Descripción                                                                 | Ejemplo                                  |
|------------------|------------------------------------------------------------------------------|------------------------------------------|
| **On-Premise**   | Todo está instalado y gestionado dentro de la empresa.                      | ERP en servidores propios                |
| **Cloud Pública**| Recursos compartidos alojados en la nube de un proveedor.                   | Gmail, Google Drive, AWS EC2             |
| **Cloud Privada**| Infraestructura dedicada solo para una organización.                        | Nube privada con OpenStack               |
| **Cloud Híbrida**| Combina on-premise con servicios en la nube.                                | Backups en AWS + ERP local               |
| **Multi-Cloud**  | Uso de múltiples proveedores de nube.                                       | App en AWS + CDN en GCP + DB en Azure    |

---

## 🛠️ Modelos de Servicio (Qué parte del stack consumes)

| Modelo   | ¿Qué te ofrece?                                 | ¿Qué gestionas tú?          | Ejemplo                        |
|----------|--------------------------------------------------|------------------------------|--------------------------------|
| **IaaS** | Infraestructura virtual (VMs, redes, almacenamiento) | Sistema operativo y apps     | Amazon EC2, Azure VMs          |
| **PaaS** | Plataforma lista para desplegar apps             | Solo el código de tu app     | Heroku, Google App Engine      |
| **SaaS** | Aplicaciones listas para usar desde el navegador | Solo los datos y configuración | Gmail, Office 365, Salesforce  |

---

## 🧱 Comparación: ¿Quién gestiona qué?

| Parte del sistema                | On-Premise | IaaS      | PaaS      | SaaS                                |
|----------------------------------|------------|-----------|-----------|-------------------------------------|
| Infraestructura física           | Tú         | Proveedor | Proveedor | Proveedor                           |
| Red y servidores                 | Tú         | Proveedor | Proveedor | Proveedor                           |
| Sistema operativo                | Tú         | Tú        | Proveedor | Proveedor                           |
| Plataforma (runtime, middleware) | Tú         | Tú        | Proveedor | Proveedor                           |
| Aplicación                       | Tú         | Tú        | Tú        | Proveedor                           |
| **Datos y uso**                  | Tú         | Tú        | Tú        | **Tú (almacenados por proveedor)**  |

> **Nota:** En SaaS, tú eres dueño de los datos, pero el proveedor los gestiona técnicamente. Es importante revisar sus políticas de privacidad, cifrado y exportación de datos.

---

## 🧠 Conceptos Clave de Arquitectura Cloud

- **Cloud Computing:** Modelo que ofrece recursos computacionales por internet sin necesidad de tener infraestructura física propia.
- **Arquitectura:** La combinación de modelo de despliegue + modelo de servicio + composición del sistema + propiedad y gestión de datos.
- **Microservicios:** Arquitectura donde la aplicación se divide en servicios pequeños e independientes, ideales para escalabilidad y despliegue flexible.
- **Monolito:** Arquitectura tradicional donde toda la aplicación es un bloque único, más sencilla pero menos flexible para escalar.
- **Escalabilidad:** Capacidad del sistema para crecer (horizontal o verticalmente) según demanda.
- **Disponibilidad:** Medida en que el sistema está operativo y accesible.
- **Seguridad:** Protección contra accesos no autorizados, incluyendo autenticación, autorización, cifrado y cumplimiento normativo.
- **Monitoreo:** Seguimiento y alertas en tiempo real sobre el estado y rendimiento del sistema.

---

## ⚙️ Tecnologías y Servicios Cloud Ejemplares

| Servicio / Tecnología           | Tipo                | Función Principal                                     | Relación con Arquitectura/Modelo     |
|--------------------------------|---------------------|------------------------------------------------------|-------------------------------------|
| **Azure Blob Storage**          | Almacenamiento IaaS | Almacenamiento de objetos (videos, backups, etc.)    | Parte de Infraestructura y Almacenamiento en Cloud (IaaS) |
| **Azure App Services**          | PaaS                | Plataforma para desplegar aplicaciones web y APIs    | Implementa modelo PaaS para despliegue de apps           |
| **Azure Kubernetes Service (AKS)** | PaaS/IaaS        | Orquestación de contenedores para microservicios     | Facilita arquitectura de microservicios, escalabilidad   |
| **Azure Cosmos DB**             | PaaS/DBaaS          | Base de datos NoSQL distribuida globalmente          | Parte del almacenamiento y base de datos en la nube      |
| **Azure Active Directory**      | SaaS                | Gestión de identidades y control de acceso            | Seguridad: autenticación y autorización                   |
| **Azure Monitor**               | SaaS                | Monitoreo y alertas para aplicaciones y recursos     | Soporte para monitoreo y disponibilidad                   |
| **Terraform**                  | Infraestructura como código | Automatización y gestión declarativa de infraestructura | Permite gestionar IaaS/PaaS como código                    |
| **CDN (Content Delivery Network)** | Servicio Cloud    | Distribución rápida y global de contenido estático    | Mejora rendimiento y disponibilidad de videos            |

---

## 🧩 Resumen Final

- La arquitectura Cloud no solo define dónde corre la app (modelo de despliegue) y qué parte gestionas (modelo de servicio), sino también cómo está diseñada la app (microservicios o monolito), cómo se protege, se escala y se monitorea.
- Las tecnologías y servicios en la nube son herramientas concretas para implementar esa arquitectura, y cada uno encaja en un nivel diferente.
- Entender la relación entre conceptos generales y herramientas específicas te ayudará a diseñar sistemas robustos y escalables.

---
