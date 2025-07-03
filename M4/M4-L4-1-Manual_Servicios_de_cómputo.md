# Servicios de Cómputo en la Nube

**Módulo:** Fundamentos de Tecnología Cloud  
**Aprendizaje Esperado:** Diferenciar las características fundamentales de los servicios de cómputo en la nube para satisfacer una necesidad de la organización.

## Introducción

Los servicios de cómputo en la nube permiten ejecutar aplicaciones y procesar datos sin gestionar infraestructura física. Aportan flexibilidad, escalabilidad y costos competitivos frente a entornos tradicionales.  
En esta lección se abordan los tipos de servicios (máquinas virtuales, contenedores y sin servidor), sus beneficios, limitaciones y factores clave para elegir el servicio más adecuado.

---

## 1. ¿Qué es un servicio de cómputo?

Un servicio de cómputo es una plataforma proporcionada por un proveedor (como AWS, Azure, GCP) que permite ejecutar aplicaciones sin administrar directamente el hardware.

**Ejemplos:**
- EC2 (máquinas virtuales)
- AWS Lambda (serverless)
- ECS/EKS (contenedores)

**Características clave:**
- Procesamiento según demanda
- Modelo de pago por uso
- Escalabilidad y resiliencia

---

## 2. Características de los servicios de cómputo en la nube

1. **Elasticidad y escalabilidad**
2. **Pago por uso**
3. **Automatización** (actualizaciones, balanceo, etc.)
4. **Alta disponibilidad** (SLA garantizados)
5. **Multizona y redundancia**

---

## 3. Beneficios

- Reducción de costos iniciales
- Rápido despliegue
- Escalabilidad bajo demanda
- Enfoque en la aplicación
- Acceso global y cumplimiento normativo

---

## 4. Limitaciones

- Requiere conexión a internet
- Costos elevados a gran escala
- Requiere baja latencia en algunos casos
- Restricciones legales o regulatorias

---

## 5. Tipos de servicios de cómputo

### 5.1 Máquinas Virtuales (VM)

**Ventajas:**
- Control total del entorno
- Aislamiento fuerte
- Facilidad de backup/restauración

**Ejemplos:**
- Amazon EC2, Azure VMs, Google Compute Engine

**Casos de uso:**
- Migración de apps monolíticas
- Entornos de desarrollo/pruebas
- Requisitos de SO específico

---

### 5.2 Contenedores

**¿Qué es un contenedor?**
Un paquete con aplicación + dependencias. Usa Docker para portabilidad y eficiencia.

**Ventajas:**
- Ligereza y velocidad
- Portabilidad
- Escalado rápido

**Comparación:**

| Aspecto           | Máquinas Virtuales         | Contenedores                     |
|-------------------|----------------------------|----------------------------------|
| Aislamiento       | SO propio (hipervisor)     | SO compartido                    |
| Uso de recursos   | Alto                        | Bajo                             |
| Portabilidad      | Limitada                   | Alta                             |
| Escalabilidad     | Lenta                      | Rápida                           |
| Casos de uso      | Apps monolíticas, control total | Microservicios, despliegues continuos |

**Orquestadores:** Kubernetes, ECS, EKS, Docker Swarm

---

### 5.3 Servicios Serverless

**¿Qué es?**
Modelo donde el usuario solo provee código; la infraestructura es gestionada automáticamente por el proveedor.

**Ventajas:**
- Escalado automático
- Pago por ejecución
- Menor complejidad operativa

**Ejemplos:**
- AWS Lambda, Azure Functions, Google Cloud Functions

**Casos de uso:**
- Tareas en segundo plano
- API REST y microservicios
- Automatización basada en eventos (IoT, BDD, almacenamiento)

---

## 6. Factores a considerar al elegir un servicio

1. **Tipo de aplicación:** ¿Monolítica, batch, real-time, microservicios?
2. **Escalabilidad y disponibilidad:** ¿Uso predecible o variable?
3. **Costo total (TCO):** ¿Cuál es el gasto a largo plazo?
4. **Flexibilidad/portabilidad:** ¿Evitar dependencia del proveedor?
5. **Experiencia del equipo:** ¿VMs, Docker, Kubernetes?
6. **Cumplimiento y seguridad:** ¿Cifrado, ubicación de datos, aislamiento?

---

## 7. Costos asociados

**Basados en:**
- Recursos utilizados (CPU, RAM, almacenamiento, etc.)
- Tipo de servicio:
  - **VM (EC2):** Por tiempo activo, EBS, transferencia de datos
  - **Contenedores:** Por capacidad reservada o instancias
  - **Serverless:** Por ejecución y solicitudes

**Ejemplo AWS:**
- EC2 `t4g.small`: costo por hora
- Lambda: cobra solo en ejecución → útil para cargas intermitentes
- Cargas constantes → EC2 reservado es más rentable

---

## Conclusión

Seleccionar el servicio de cómputo adecuado depende del tipo de aplicación, costo, experiencia del equipo y requerimientos normativos:

- **Máquinas virtuales:** mayor control, ideal para migraciones.
- **Contenedores:** portabilidad y eficiencia para microservicios.
- **Serverless:** óptimo para cargas intermitentes y eventos.

La computación en la nube se vuelve un aliado estratégico si se alinea correctamente con los objetivos de negocio.

---

## Referencias

- [Amazon EC2 – Descripción general](https://aws.amazon.com/es/ec2/)
- [Amazon ECS – ¿Qué es ECS?](https://aws.amazon.com/es/ecs/)
- [Amazon EKS – Descripción general](https://aws.amazon.com/es/eks/)
- [AWS Lambda – ¿Qué es AWS Lambda?](https://aws.amazon.com/es/lambda/)
- [Cómo elegir el servicio de cómputo en AWS](https://aws.amazon.com/es/compute/)

---

# Desarrollo


