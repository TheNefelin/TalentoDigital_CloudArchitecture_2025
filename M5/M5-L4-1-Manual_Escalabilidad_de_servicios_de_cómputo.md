# 📘 Manual: Escalabilidad de Servicios de Cómputo

## 🧑‍💻 Objetivo del Manual

Explorar cómo diseñar arquitecturas escalables en la nube, considerando costos, alta disponibilidad y herramientas como:

- EC2 AutoScaling
- Elastic Load Balancer
- Elastic Beanstalk
- ECS (Elastic Container Service)
- EKS (Elastic Kubernetes Service)

---

## 🎯 Aprendizajes Esperados

- Identificar las características clave de una arquitectura escalable.
- Incorporar consideraciones de costo en soluciones escalables.
- Analizar casos de alta disponibilidad en entornos web y basados en contenedores.

---

## 1️⃣ Conceptos Fundamentales de Escalabilidad

### 🔍 Definición

Capacidad de un sistema para adaptarse al aumento de carga sin pérdida de rendimiento. Se puede escalar:

- **Verticalmente**: aumentando recursos en una instancia.
- **Horizontalmente**: agregando más instancias.

### ⭐ Características Clave

- **Elasticidad**: ajuste automático de recursos.
- **Distribución de cargas**
- **Resiliencia**
- **Automatización**

---

## 2️⃣ Ventajas, Desventajas y Análisis de Costos

### ✅ Ventajas

- Pago por uso.
- Alta disponibilidad.
- Flexibilidad y adaptación.

### ❌ Desventajas

- Complejidad en gestión.
- Costos variables.
- Dependencia del proveedor de nube.

### 💲 Factores de Costo

- Recursos computacionales (instancias, redes, almacenamiento)
- Licencias y soporte
- Integración con sistemas locales (VPN, Direct Connect)

---

## 3️⃣ Alta Disponibilidad con EC2 AutoScaling + ELB

### ⚙️ Implementación

- AutoScaling + Load Balancer distribuyen el tráfico y escalan instancias automáticamente.

### 🛒 Caso de Uso

Sitio e-commerce durante eventos de alta demanda (ej. Black Friday).

### 📊 Comparativa

| Aspecto         | EC2 + ELB                      | Solución Tradicional           |
|-----------------|--------------------------------|--------------------------------|
| Flexibilidad    | Escalado automático            | Escalado manual y limitado     |
| Costos          | Pago por demanda               | Costos fijos y sobreaprovisionamiento |
| Manejo de fallos| Redundancia integrada          | Dependencia de instancias únicas |

---

## 4️⃣ Escalabilidad con Contenedores y Microservicios

### 📦 Ventajas

- Portabilidad
- Aislamiento
- Escalado independiente por microservicio

### ⚠️ Desventajas

- Mayor complejidad en la orquestación (requiere ECS o EKS)
- Costos de gestión y monitoreo

### 💰 Análisis de Costos

- Uso de instancias eficientes
- Herramientas de orquestación
- Optimización de hardware compartido

---

## 5️⃣ Alta Disponibilidad en Servicios con Contenedores

### 🧩 Herramientas

- **API Gateway**: facilita el enrutamiento y la resiliencia.
- **ECS**: gestión nativa y sencilla en AWS.
- **EKS**: solución flexible basada en Kubernetes.

### 🧪 Caso de Uso

Procesamiento de datos en tiempo real usando contenedores y API Gateway para redirigir peticiones si falla un nodo.

### 📊 Comparativa ECS vs. EKS

| Aspecto          | ECS                            | EKS                              |
|------------------|---------------------------------|----------------------------------|
| Gestión          | Servicio gestionado nativamente| Basado en Kubernetes             |
| Curva de Aprendizaje | Baja                        | Alta                             |
| Casos de Uso     | Aplicaciones AWS integradas    | Necesidades multiplataforma     |

---

## ✅ Conclusión

Este manual cubre:

- Fundamentos de la escalabilidad.
- Comparativas entre tipos de escalado.
- Costos asociados.
- Casos de alta disponibilidad con EC2 y contenedores.

El conocimiento permite diseñar soluciones en la nube escalables, resilientes y adaptables a diferentes demandas y contextos empresariales.

---

## 📚 Referencias

- [AWS Architecture](https://aws.amazon.com/architecture/)
- [Google Cloud Products](https://cloud.google.com/products)
- [IBM Cloud Computing](https://www.ibm.com/cloud/learn/what-is-cloud-computing)
- [Microsoft Azure Architecture](https://learn.microsoft.com/en-us/azure/architecture/)
- [VMware Cloud Topics](https://www.vmware.com/topics/cloud.html)
