# 🌐 Proyecto: Infraestructura Viva - Portafolio Cloud

## 🏢 Situación Inicial

**Unidad solicitante:** Equipo de Innovación Tecnológica de la empresa _“Soluciones Digitales ACME”_

El área de Innovación Tecnológica ha identificado la necesidad de modernizar la infraestructura para responder a crecientes requerimientos de procesamiento, almacenamiento y disponibilidad de datos.

Actualmente, los departamentos de **ventas**, **soporte** y **finanzas** utilizan un entorno **on-premise**, que genera altos costos de mantenimiento y limita la rápida implementación de nuevas funcionalidades.

### 🔍 Problemáticas a resolver

1. Disponer de un entorno de **cómputo escalable y seguro** para desplegar aplicaciones.
2. Integrar de forma unificada **bases de datos relacionales y NoSQL** sin depender de hardware físico.
3. Implementar un **sistema de almacenamiento confiable**, diferenciando datos de uso frecuente y de archivado.
4. Configurar una **red virtual** que permita aislar servicios internos y exponer aplicaciones públicas de forma segura.
5. Establecer un **plan de monitoreo y notificaciones** que detecte y corrija incidentes de forma proactiva.
6. Diseñar una **solución que pueda implementarse** utilizando los contenidos y conceptos vistos en los manuales del curso.

---

## 📘 Presentación del Caso

Este proyecto tiene como objetivo migrar una infraestructura on-premise hacia la nube, implementando una solución denominada **“Infraestructura Viva”**, utilizando recursos gratuitos de AWS (AWS Free Tier y AWS Academy).

Se busca poner en práctica los conceptos del módulo 4: _Fundamentos de Tecnología Cloud_, mediante el uso de servicios gestionados de cómputo, bases de datos, almacenamiento, redes, monitoreo y notificaciones, con énfasis en el diseño escalable, seguro y viable dentro de un entorno educativo.

---

## ⚙️ Alcance y Restricciones Técnicas

Dado que el entorno de laboratorio en AWS Academy (Alchemy Lab) **no permite el acceso completo a todos los servicios**, se tomaron decisiones técnicas basadas en disponibilidad real. Las siguientes limitaciones fueron detectadas:

| Servicio | Restricción en Alchemy | Solución Alternativa |
|----------|------------------------|------------------------|
| CloudFront | No disponible | Se omite CDN; se trabaja solo con S3 público |
| Lightsail | No disponible | Se utiliza EC2 t2.micro desde Free Tier |
| ACM / dominios personalizados | No disponible | Uso de dominios internos o IP públicas |
| CLI o SDK limitado | No disponible | Se utiliza únicamente la consola web (GUI) de AWS Academy |

Estas decisiones permiten mantener la **viabilidad técnica del proyecto**, ajustándose al entorno educativo, sin perder los objetivos de aprendizaje.

---

## 🧱 Componentes de la Arquitectura

```mermaid
graph TD
  Usuario([Usuario]) --> S3[Sitio Web (S3 Público)]
  S3 --> EC2[App Backend (EC2 o Lambda)]
  EC2 --> RDS[Base de datos relacional (RDS)]
  EC2 --> DynamoDB[Base NoSQL (DynamoDB)]
  RDS -->|Backups| Glacier[Almacenamiento Archivado (Glacier)]
  DynamoDB -->|Respaldo NoSQL| Glacier
  EC2 --> CloudWatch
  RDS --> CloudWatch
  DynamoDB --> CloudWatch
  CloudWatch --> SNS[Notificación (SNS)]
  SNS --> SQS[Cola de Mensajes (SQS)]
```