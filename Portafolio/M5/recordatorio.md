# Evaluación del Módulo 5: Arquitecturas Cloud Básicas

## Consigna del Proyecto
**Empresa:** Alkemy  
**Área solicitante:** Infraestructura Cloud  

### Situación Inicial
La empresa está modernizando su infraestructura y migrando servicios a la nube. Requiere diseños de arquitecturas cloud que garanticen escalabilidad, disponibilidad y eficiencia en costos, combinando modelos públicos, privados e híbridos, con balanceo de carga, escalabilidad automática y mensajería asíncrona.

---

## Objetivo
Diseñar arquitecturas cloud básicas aplicando buenas prácticas para garantizar:
- Escalabilidad  
- Disponibilidad  
- Eficiencia en costos  

Incluyendo componentes como almacenamiento, cómputo, red, mensajería y gestión de costos.

---

## Requerimientos
### Generales
- Aplicar buenas prácticas en diseño cloud.  
- Justificar elección de componentes.  
- Considerar costos, seguridad y disponibilidad.  

### Técnicos
1. **Almacenamiento**: Servicio de objetos (ej. AWS S3, Azure Blob Storage).  
2. **Respaldo**: Mecanismo de backup y recuperación (ej. Snapshots, AWS Backup).  
3. **Modelo de nube**: Elegir entre pública, privada o híbrida.  
4. **Escalabilidad**: Auto Scaling y balanceo de carga (ej. AWS ELB, Kubernetes).  
5. **Mensajería**: Servicio asíncrono (ej. AWS SQS, Azure Service Bus).  
6. **Costos**: Estimación detallada (ej. AWS Pricing Calculator).  

---

## Paso a Paso (8 Lecciones)

### Lección 1: Almacenamiento de Objetos
- **Objetivo**: Definir estrategia base.  
- **Tareas**:  
  1. Seleccionar almacenamiento de objetos (ej. AWS S3 para alta durabilidad).  
  2. Integrarlo al flujo arquitectónico (ej. Conexión con aplicaciones vía API).  

### Lección 2: Respaldo en la Nube
- **Objetivo**: Políticas de backup.  
- **Tareas**:  
  1. Diseñar respaldos automatizados (ej. Copias diarias en AWS Glacier).  
  2. Definir recuperación ante fallos (ej. Restauración en 24h).  

### Lección 3: Modelo de Nube
- **Objetivo**: Elegir modelo (pública/híbrida).  
- **Tareas**:  
  1. Justificar elección (ej. Híbrida para datos sensibles en privada + escalabilidad en pública).  

### Lección 4: Escalabilidad
- **Objetivo**: Auto Scaling.  
- **Tareas**:  
  1. Diseñar grupo de Auto Scaling (ej. AWS EC2 con métricas de CPU).  
  2. Integrar con balanceador (ej. AWS ALB).  

### Lección 5: Disponibilidad en Red
- **Objetivo**: Alta disponibilidad.  
- **Tareas**:  
  1. Balanceo de carga multi-AZ (ej. AWS ELB en 3 zonas).  

### Lección 6: Distribución de Contenidos
- **Objetivo**: CDN y seguridad.  
- **Tareas**:  
  1. Implementar CDN (ej. AWS CloudFront).  
  2. Proteger con WAF (ej. AWS WAF).  

### Lección 7: Mensajería Asíncrona
- **Objetivo**: Comunicación entre servicios.  
- **Tareas**:  
  1. Diseñar colas (ej. AWS SQS para desacoplar microservicios).  

### Lección 8: Gestión de Costos
- **Objetivo**: Optimizar costos.  
- **Tareas**:  
  1. Estimación mensual (ej. $500/mes con AWS).  
  2. Monitoreo con herramientas (ej. AWS Cost Explorer).  

---

## Entregables
- **Por lección**:  
  - Informe técnico + diagrama + costos parciales.  
- **Final**:  
  - Documento consolidado con:  
    - Arquitectura completa.  
    - Diagramas integrados.  
    - Justificaciones y costos totales.  

---

## Referencias
- [AWS Architecture Center](https://aws.amazon.com/architecture/)  
- [Google Cloud Framework](https://cloud.google.com/architecture)  
- [Azure Architecture](https://learn.microsoft.com/es-es/azure/architecture/)  

---

## Portafolio
Incluir como caso práctico destacando:  
- Diseño integral.  
- Estrategias de escalabilidad y disponibilidad.  
- Diagramas y análisis de costos.  

¡Éxitos!  
**Equipo Alkemy**