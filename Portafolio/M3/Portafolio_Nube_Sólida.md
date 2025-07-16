# ☁️ Proyecto Nube Sólida - Solución

## 📘 Resumen General

La siguiente propuesta responde al desafío planteado por el área de Infraestructura y Seguridad de una empresa de tecnología, que busca modernizar sus servicios mediante una arquitectura cloud robusta, escalable, segura y resiliente.

---

## 📚 Lección 1: Introducción a la Computación en la Nube

### ✅ Objetivo:
Comprender los conceptos fundamentales de la computación en la nube y sus beneficios.

### 📄 Informe resumen:
- **Fundamentos**:  
  - Definición de cloud computing  
  - Modelos de servicio  
  - Modelos de implementación

- **Beneficios**:  
  - Elasticidad  
  - Reducción de costos  
  - Accesibilidad y disponibilidad global  
  - Escalabilidad automática

- **Proveedores principales**:
  - AWS
  - Microsoft Azure
  - Google Cloud Platform (GCP)

- **Modelos de despliegue**:
  - Nube pública
  - Nube privada
  - Nube híbrida

---

## 🧩 Lección 2: Modelos de Servicio en la Nube

### ✅ Objetivo:
Seleccionar y justificar los modelos de servicio (IaaS, PaaS, SaaS, FaaS) adecuados.

### 📄 Informe técnico:

| Componente             | Modelo de Servicio | Justificación                                 |
|------------------------|--------------------|-----------------------------------------------|
| Servidor de Aplicación | PaaS               | Permite centrarse en el desarrollo sin gestionar infra. |
| Base de Datos          | DBaaS (PaaS)       | Gestión automática, backups, alta disponibilidad. |
| Autenticación          | SaaS               | Uso de servicios como Auth0, Firebase, etc.   |
| Backend Serverless     | FaaS               | Escalabilidad automática, pago por ejecución. |
| Red / Infraestructura  | IaaS               | Control total de redes virtuales y firewalls. |

---

## 🏗️ Lección 3: Modelos de Implementación en la Nube

### ✅ Objetivo:
Determinar y justificar el modelo de implementación más adecuado.

### 📄 Análisis:

- **Modelo seleccionado**: Nube híbrida  
- **Justificación**:
  - Permite aprovechar la nube pública para aplicaciones no críticas.
  - La nube privada se usa para servicios que requieren mayor control y seguridad.
  - Se mantiene flexibilidad y cumplimiento normativo.

| Modelo      | Ventajas                          | Desventajas                       |
|-------------|-----------------------------------|-----------------------------------|
| Pública     | Escalable, económica, accesible   | Menor control sobre la seguridad |
| Privada     | Control total, mayor seguridad    | Costosa y compleja de mantener   |
| Híbrida ✅  | Equilibrio entre control y agilidad| Complejidad en integración        |

---

## 🧱 Lección 4: Principios de Diseño Arquitectónico

### ✅ Objetivo:
Aplicar principios fundamentales de diseño para una arquitectura modular, resiliente y segura.

### 📄 Aplicación de principios:
- **Modularidad**: Separación de componentes en microservicios.
- **Desacoplamiento**: Uso de colas y eventos (ej. SQS, Pub/Sub).
- **Resiliencia**: Balanceadores de carga, backups automáticos, tolerancia a fallos.
- **Seguridad**: IAM, cifrado en tránsito y en reposo, políticas de red.

### 🖼️ Esquema conceptual (describir o insertar imagen):

```
[ Usuario ]
    ↓
[ Frontend Web / Móvil ]
    ↓
[ API Gateway ]
    ↓
[ Microservicios o Lambdas ]
    ↓
[ Base de Datos / Almacenamiento ]
```

---

## 🔐 Lección 5: Atributos de Calidad en la Arquitectura Cloud
### ✅ Objetivo:
Integrar atributos clave: resiliencia, seguridad y escalabilidad.

### 📄 Estrategias:
- Resiliencia:
  - Auto-healing groups
  - Zonas de disponibilidad redundantes
  - Replicación geográfica
- Seguridad:
  - Gestión de accesos con IAM
  - Logs de auditoría (CloudTrail / Monitor)
  - Cifrado en tránsito y en reposo
- Escalabilidad:
  - Auto Scaling Groups para instancias
  - Uso de FaaS que escala automáticamente
  - CDN para distribución eficiente de contenido

---

## 📦 Entregables
### ✅ Documento integrador:
- Informe Lección 1: Fundamentos y beneficios del cloud
- Informe Lección 2: Modelos de servicio asignados
- Informe Lección 3: Modelo de implementación seleccionado
- Diagrama conceptual cliente-servidor
- Documento técnico con principios de diseño y atributos de calidad

### 💼 Portafolio Profesional
Puedes incluir los siguientes elementos:

- Diseño conceptual de la arquitectura
- Diagramas técnicos
- Justificación técnica de cada decisión
- Estrategias implementadas para cumplir con requisitos de negocio

---