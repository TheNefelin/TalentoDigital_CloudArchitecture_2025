
# 📚 Manual Resumido: Representación de una Arquitectura Cloud Serverless

## Introducción
Visualizar arquitecturas en la nube es clave para **comunicar diseño, detectar cuellos de botella y estimar costos**.  
En el contexto *serverless*, con componentes distribuidos, los diagramas claros son esenciales.  
Este módulo enseña a usar **Cloudcraft** para representar arquitecturas en AWS, interpretar diagramas y calcular costos.

---

## 1. Representación de arquitecturas sin servidor

### 1.1 Principios de diagramación efectiva
- **Claridad**: agrupar por dominios y usar etiquetas.
- **Consistencia**: íconos oficiales y colores estándar.
- **Abstracción adecuada**: niveles L1 (conceptual), L2 (servicios), L3 (recursos).
- **Flujo de datos**: flechas con protocolos (HTTP, SQS, Kinesis).
- **Seguridad**: delimitar VPCs, subredes, zonas públicas/privadas.

### 1.2 Elementos clave en arquitecturas serverless

| Categoría | Ejemplo | Representación |
|-----------|---------|----------------|
| Cómputo | Lambda | Ícono amarillo con rayo |
| Integración | API Gateway, EventBridge | Front door / bus central |
| Persistencia | S3, DynamoDB | Indicar clases de almacenamiento / modo |
| Mensajería | SQS, SNS, Kinesis | Flechas asíncronas |
| Seguridad | IAM, Cognito, WAF | Capa transversal aislada |

---

## 2. Ejemplos en Cloudcraft

### 2.1 API REST con Lambda y DynamoDB
- **Flujo**: API Gateway → Lambda (Auth) → Lambda (CRUD) → DynamoDB.
- Observabilidad: CloudWatch Logs + X-Ray.
- Seguridad: Cognito User Pool, WAF.
- Cloudcraft: agrupar Lambdas, etiquetar flechas (PutItem, Query), activar **Cost View**.

### 2.2 Procesamiento de imágenes bajo demanda
- **Flujo**: S3 (entrada) → Evento → Lambda (procesa) → S3 (salida) → CloudFront.
- Representación: S3 en azul, Lambda en amarillo, flechas punteadas.

### 2.3 Pipeline de streaming con Kinesis y Lambda
- **Flujo**: IoT devices → Kinesis → Lambda (transform) → DynamoDB + S3 Data Lake.
- Cloudcraft: representar shards y throughput.

---

## 3. Estimación de costos

### 3.1 Métricas principales

| Servicio | Unidad de cobro | Variables clave |
|----------|----------------|-----------------|
| Lambda | Invocaciones + ms | Duración, memoria |
| API Gateway | Llamadas | Tipo de API |
| S3 | GB-mes + solicitudes | Clase de almacenamiento |
| DynamoDB | RCU/WCU o RPS | On-Demand vs Provisioned |
| EventBridge | Eventos publicados | Internos vs externos |

### 3.2 Uso de Cost View en Cloudcraft
- Cada componente muestra costo estimado mensual.
- Ajustes en memoria de Lambda o RCU/WCU de DynamoDB actualizan costos.
- Reporte exportable en CSV.

### 3.3 Buenas prácticas de optimización
- **Right-sizing** en Lambda (ajuste de memoria, Power Tuning).
- **Arquitectura arm64** en Lambda (ahorro de costos).
- **Compresión y clases adecuadas en S3** (IA, Glacier).
- **Particiones balanceadas en DynamoDB**.
- **Caching** en API Gateway y CloudFront.
- **Compute Optimizer** para recomendaciones de configuración.

---

## ✅ Conclusión
Ahora puedes:
- Diagramar arquitecturas serverless en **Cloudcraft**.
- Interpretar y comunicar arquitecturas existentes.
- **Estimar costos** y optimizar diseños según mejores prácticas.

---

## 📚 Referencias
- [AWS Icons for Architecture Diagrams](https://aws.amazon.com/architecture/icons/)
- [AWS Pricing Calculator](https://calculator.aws/#/)
- [Serverless Land Patterns](https://serverlessland.com/patterns)
- [Well-Architected Framework – Serverless Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/)
