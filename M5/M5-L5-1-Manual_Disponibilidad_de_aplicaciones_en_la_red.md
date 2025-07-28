# 📘 Manual: Disponibilidad de Aplicaciones en la Red

## 🧑‍💻 Introducción

La disponibilidad continua de las aplicaciones es crucial en arquitecturas modernas en la nube. Este manual aborda estrategias para garantizar la alta disponibilidad, incluyendo tolerancia a fallos, escalabilidad, balanceo de carga y zonas de disponibilidad.

---

## 🎯 Aprendizajes Esperados

- Definir tolerancia a fallos.
- Explicar estrategias de escalabilidad.
- Describir beneficios del balanceo de carga.
- Reconocer la importancia de zonas de disponibilidad.
- Identificar componentes clave para la disponibilidad.
- Aplicar buenas prácticas en infraestructuras resilientes.
- Analizar casos de uso reales.

---

## 🛠️ Disponibilidad de Aplicaciones en la Red

### 🔄 Tolerancia a Fallos

- Capacidad de seguir operando ante fallos de hardware/software.
- Técnicas:
  - **Replicación activa/pasiva**
  - **Diversificación geográfica**
  - **Failover automático**
- Desafíos:
  - Mayor complejidad y costos.
  - Inconsistencias de datos (replicación asíncrona).
  - Necesidad de monitoreo continuo y pruebas (Chaos Engineering).

---

## 📈 Estrategias de Escalabilidad

- **Vertical**: aumentar capacidad de un servidor.
- **Horizontal**: añadir instancias (preferida para alta disponibilidad).
- Herramientas:
  - **Auto Scaling Groups**
  - **Load Balancers**
  - **Base de datos escalables (Aurora, DynamoDB)**
- Recomendaciones:
  - Separación por capas (microservicios, contenedores).
  - Escalabilidad independiente de cada componente.

---

## ⚖️ Balanceo de Carga

- Distribuye tráfico entre servidores para:
  - Mejorar rendimiento.
  - Aumentar disponibilidad.
  - Asegurar tolerancia a fallos.

### Tipos:
- **Capa 4** (Transporte): IP y puertos.
- **Capa 7** (Aplicación): rutas, cookies, headers.

### Estrategias:
- **Round Robin**
- **Least Connections**
- **IP Hash**

Servicios: ELB (AWS), Azure Load Balancer, entre otros.

---

## 🌍 Zonas de Disponibilidad

- Zonas de datos independientes dentro de una región.
- Aportan:
  - Redundancia
  - Aislamiento de fallos
  - Baja latencia
- Recomendación: desplegar recursos en al menos dos zonas para continuidad operativa.

---

## 🏗️ Arquitecturas de Alta Disponibilidad

Ejemplo típico en AWS:

- **Capa presentación**: ELB en 2+ zonas.
- **Capa lógica**: EC2 en Auto Scaling Groups.
- **Capa de datos**: Amazon RDS Multi-AZ.
- **Almacenamiento**: Amazon S3 replicado.
- **Contenido**: CloudFront (CDN).

Estrategias adicionales:
- Arquitecturas híbridas
- Disaster Recovery (replicación entre regiones)

---

## 🧪 Casos de Uso Reales

Sectores que aplican alta disponibilidad:

- 🛒 Comercio electrónico (Amazon, MercadoLibre)
- 🎵 Streaming (Netflix, Spotify)
- 💳 Financieras (Visa, Mastercard)
- 🏥 Salud (historia clínica electrónica)
- 🚖 Movilidad (Uber, Booking)
- 🏛️ Gobierno (portales ciudadanos)
- 🎓 Educación e investigación
- 🏢 Empresas (ERP, CRM, Microsoft 365)

---

## ✅ Conclusión

La alta disponibilidad es un pilar de las aplicaciones modernas. Requiere:

- Arquitecturas distribuidas y redundantes
- Balanceo de carga y escalado automático
- Evaluación constante de riesgos
- Cultura de prevención y mejora continua

---

## 📚 Referencias

- [AWS Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
- [Azure Load Balancer Overview](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-overview)
- [Google Cloud Docs](https://cloud.google.com/docs/overview)
