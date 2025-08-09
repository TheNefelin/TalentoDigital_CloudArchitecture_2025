# ⚙️ Implementación de Escalabilidad y Alta Disponibilidad en Arquitecturas Monolíticas en la Nube

## 🧑‍💻 Introducción
Guía para aplicar **mecanismos de escalabilidad y alta disponibilidad** en arquitecturas monolíticas implementadas en la nube (AWS).  
Incluye conceptos de **escalado vertical y horizontal**, autoescalamiento, balanceo de carga y uso de **zonas de disponibilidad**.

## 🎯 Aprendizaje esperado
Implementar mecanismos de escalabilidad y alta disponibilidad en arquitecturas monolíticas en la nube usando servicios de cómputo para resolver necesidades específicas.

---

## 1️⃣ Autoescalamiento y Escalabilidad Vertical
- **Definición**: Incrementar recursos de una sola instancia (CPU, RAM, almacenamiento).
- **Aplicación**: Ideal en sistemas con fuerte acoplamiento o estado centralizado.
- **Monitoreo**: AWS CloudWatch para métricas (CPU, memoria, tráfico de red) y activar políticas de escalado.
- **Procedimiento Auto Scaling EC2**:
  1. Definir métricas y umbrales.
  2. Configurar políticas de escalado (agregar/eliminar instancias).
  3. Probar y ajustar parámetros.
- **Tipos de escalado**:
  - **Predictivo**: basado en tendencias históricas.
  - **Dinámico**: reacción en tiempo real.
- **Reemplazo de instancias**:
  - Sustituir instancias defectuosas o antiguas.
  - Uso de AMI personalizada para despliegue rápido.

---

## 2️⃣ Balanceo de Carga y Escalabilidad Horizontal
- **Definición**: Añadir más instancias para distribuir la carga.
- **Ventajas**:
  - Mayor tolerancia a fallos.
  - Escalabilidad casi ilimitada.
- **Desventajas**:
  - Mayor complejidad en gestión y sincronización.
- **Tipos de ELB**:
  - **ALB (Application Load Balancer)**: optimizado para HTTP/HTTPS.
  - **NLB (Network Load Balancer)**: baja latencia, nivel de red.
- **Procedimiento ELB**:
  - Crear ELB en AWS.
  - Configurar reglas de enrutamiento y chequeos de salud.
  - Asignar grupos de instancias EC2.

| Característica   | Escalabilidad Vertical            | Escalabilidad Horizontal          |
|------------------|-----------------------------------|------------------------------------|
| Estrategia       | Aumentar recursos en un servidor  | Añadir múltiples instancias        |
| Complejidad      | Menor, pero con límites físicos   | Mayor, requiere coordinación       |
| Costo            | Alto a gran escala                | Escalable agregando nodos          |
| Resiliencia      | Punto único de fallo              | Alta disponibilidad                |

---

## 3️⃣ Zonas de Disponibilidad (AZ)
- **Definición**: Centros de datos independientes en una región.
- **Beneficios**:
  - Alta disponibilidad y redundancia.
  - Menor riesgo ante fallos físicos o de red.
- **Procedimiento**:
  - Seleccionar múltiples AZ al desplegar EC2.
  - Configurar ELB para distribuir tráfico entre AZs.
  - Implementar replicación de datos entre zonas.
- **Casos de uso**:
  - Aplicaciones críticas con 99.99% de uptime.
  - Servicios financieros y de salud.
- **Integración**: combinadas con autoescalamiento y ELB para máxima resiliencia.

---

## ✍️ Cierre
Este manual describe cómo implementar **autoescalamiento**, **escalado vertical/horizontal**, **balanceo de carga** y **zonas de disponibilidad** en AWS para arquitecturas monolíticas, asegurando **rendimiento**, **disponibilidad** y **tolerancia a fallos**.

---

## 📚 Referencias
- [AWS Auto Scaling Docs](https://docs.aws.amazon.com/autoscaling/)
- [AWS Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)
- [AWS CloudWatch Docs](https://docs.aws.amazon.com/cloudwatch/)
- [AWS Elastic Load Balancing Docs](https://docs.aws.amazon.com/elasticloadbalancing/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
