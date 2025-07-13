# 📊 Servicios de Monitoreo y Correlación de Incidentes en la Nube

## 🎯 Objetivo
Comparar y aplicar servicios de monitoreo en un entorno cloud, para mejorar disponibilidad, rendimiento y control de costos.

---

## 1. ¿Qué es un servicio de monitoreo?

Un servicio de monitoreo en la nube permite observar el comportamiento de los recursos e identificar problemas de forma proactiva.

### 🧱 Componentes clave:
- **Métricas**: CPU, memoria, red, etc.
- **Registros (Logs)**: Eventos del sistema y aplicaciones.
- **Alertas / Alarmas**: Basadas en umbrales definidos.
- **Dashboards**: Visualización de métricas.

### ✅ Beneficios:
- Detección temprana de fallas.
- Optimización de costos.
- Aumento de disponibilidad.
- Visibilidad completa del entorno cloud.

### 💸 Costos asociados:
- Número y frecuencia de métricas recolectadas.
- Cantidad de logs almacenados.
- Cantidad de alarmas configuradas y notificaciones enviadas.

---

## 2. Amazon CloudWatch (Servicio nativo de AWS)

### 🔧 Funcionalidades principales:

#### 📈 Métricas:
- CPU, red, disco, memoria (requiere agente).
- Soporte para métricas personalizadas.
- Dashboards centralizados.

#### 📋 Registros (CloudWatch Logs):
- Logs de apps, sistemas y servicios (ej. VPC Flow Logs).
- Búsqueda y retención por periodos configurables.

#### 🧭 Eventos (CloudWatch Events / EventBridge):
- Responde a cambios de estado en recursos.
- Puede invocar funciones Lambda o notificar vía SNS (Simple Notification Service).

#### 🚨 Alarmas:
- Umbrales definidos en métricas (ej. CPU > 80%).
- Notificaciones por SNS, Slack o acciones automáticas.
- Alarmas de presupuesto (Billing) para evitar gastos inesperados.

---

## 3. Alertas y Alarmas en la Nube

### 💰 Asociadas a Billing:
- Detectan gastos anómalos o fugas de recursos.
- Ej: Enviar alerta si el gasto mensual supera los $300 USD.

### 🖥️ Asociadas al uso:
- Monitorizan uso de CPU, memoria, conexiones, etc.
- Permiten escalar o detener recursos según necesidad.

---

## 4. Casos de uso

### 🏗️ Infraestructura (EC2 + RDS):
- Monitorear CPU, red y memoria.
- Alarmas para activar Auto Scaling ante alto uso.

### 🎵 Plataforma de streaming:
- Escalar servidores automáticamente según tráfico.
- Analizar logs para prever demanda futura.

### 🛒 E-commerce:
- Detectar errores 5xx y correlacionarlos con IPs sospechosas.
- Alerta si hay más de 10 errores en 1 min.

---

## 5. Comparativa de Servicios de Monitoreo

| Servicio       | Características principales                                     | Ventajas                                    | Desventajas                             |
|----------------|---------------------------------------------------------------|---------------------------------------------|------------------------------------------|
| **CloudWatch** | Métricas, logs, eventos, dashboards integrados                | Integración total con AWS                   | Costos pueden escalar con mucho tráfico  |
| **Datadog**    | Monitoreo multicloud, dashboards y APM (Application Performance Monitoring) | Observabilidad completa                     | Costo adicional, curva de aprendizaje     |
| **New Relic**  | APM y monitoreo en tiempo real                                | Fuerte en rastreo distribuido               | Requiere agentes, licencias               |
| **Splunk**     | Análisis avanzado de logs, ML, Big Data                       | Ideal para análisis forense                 | Costoso y complejo                        |

---

## ✅ Conclusión

- **Amazon CloudWatch** es la mejor opción integrada para quienes trabajan exclusivamente en AWS.
- Herramientas de terceros ofrecen más personalización y trazabilidad, pero a mayor costo y complejidad.
- La decisión depende del entorno, presupuesto y necesidades de observabilidad.

