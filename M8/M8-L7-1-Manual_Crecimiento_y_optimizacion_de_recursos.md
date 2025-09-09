
# 📚 Manual Resumido: Crecimiento y Optimización de Recursos

## Introducción
A medida que las cargas en la nube evolucionan, es crucial **optimizar recursos** para mantener la competitividad y sostenibilidad financiera.  
Una estrategia de crecimiento equilibrada debe considerar **costo, rendimiento y escalabilidad**, garantizando eficiencia sin desperdicio.

---

## 1. Importancia de la optimización de recursos

| Dimensión | Beneficio | Riesgo si no se optimiza |
|-----------|-----------|---------------------------|
| **Costo** | Reducción de gastos, mayor ROI | Sobreaprovisionamiento, desperdicio |
| **Rendimiento** | Experiencia de usuario consistente | Cuellos de botella, latencia alta |
| **Escalabilidad** | Absorber picos de tráfico | Fallas o degradación del servicio |

---

## 2. Estrategias de crecimiento

### 2.1 Uso de caché en API Gateway
- Cachea respuestas en **ElastiCache**.
- Beneficios: menos latencia, menos invocaciones de Lambda, ahorro de costos.
- Configuración: TTL por método, invalidación selectiva, tamaño de caché (0.5 GB – 237 GB).

| Patrón de acceso | TTL sugerido | Impacto |
|------------------|-------------|---------|
| Datos estáticos | 1h+ | Ahorro alto |
| Datos dinámicos | 1–5 min | Balance entre frescura y ahorro |

### 2.2 CloudFront
- **Origin Shield**: mejora compresión y reduce misiones.
- **Cache Policies**: seleccionar headers y query strings.
- **Signed URLs/Cookies**: control de acceso premium.
- Caso: migrar descargas S3 público → CloudFront + OAC → ahorro hasta **60%**.

### 2.3 Otras estrategias
- **Provisioned Concurrency en Lambda** para evitar cold starts.
- **Auto Scaling EC2** con políticas predictivas.
- **DynamoDB On-Demand o Provisioned + Auto Scaling** según el tráfico.

---

## 3. Monitoreo y análisis de recursos

### 3.1 Herramientas principales
- **CloudWatch Metrics**: CPU, memoria, latencia.
- **CloudWatch Logs**: registros de apps.
- **CloudWatch Synthetics**: canaries (pruebas E2E).
- **CloudWatch Evidently**: A/B testing.
- **AWS X-Ray**: trazas de latencia.

### 3.2 Identificación de patrones y cuellos de botella
- Dashboards con p95, throughput, error rate.
- **Contributor Insights**: detectar claves calientes en DynamoDB.
- **ServiceLens**: correlación de métricas, logs y trazas.

### 3.3 Automatización con alarmas y reglas
- Alarmas: detectar *Throttles > 0* en Lambda.
- Composite Alarms: condiciones múltiples (ej. errores 5XX + latencia).
- EventBridge Rules: acciones correctivas (aumentar memoria Lambda).

---

## 4. Optimización de costos en la nube

### 4.1 Estrategias de ahorro
| Estrategia | Servicio | Ahorro típico |
|------------|----------|---------------|
| Instancias Reservadas | EC2, RDS | 30–72% |
| Savings Plans | EC2, Lambda, Fargate | 17–66% |
| Spot Instances | EC2 | Hasta 90% |
| Graviton | EC2, Lambda | +20% eficiencia |
| S3 Intelligent-Tiering | S3 | 40% en datos poco accedidos |

### 4.2 Identificación y eliminación de recursos no usados
- **AWS Compute Optimizer**: downsizing o rightsizing.
- **Trusted Advisor**: instancias ociosas, IPs sin uso.
- **RDS Idle DB**: CPU < 1%, conexiones < 5.

### 4.3 Políticas de etiquetado y presupuestos
- **Tagging**: CostCenter, Environment, Project.
- **AWS Budgets**: alertas de gasto mensual y uso.
- **Cost Explorer**: análisis por etiquetas y predicciones.

---

## ✅ Conclusión
Con estas estrategias puedes equilibrar **costo, rendimiento y escalabilidad** en soluciones cloud.  
Desde cachés y CDNs hasta automatización de monitoreo y programas de ahorro, estas prácticas garantizan **operaciones eficientes y sostenibles**.

---

## 📚 Referencias
- [API Gateway caching](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html)  
- [AWS Well-Architected Framework – Cost Optimization](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/)  
- [AWS Cost Management Tools](https://aws.amazon.com/aws-cost-management/)  
- [CloudFront Performance Best Practices](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Performance.html)  
- [Optimizing Lambda Costs](https://aws.amazon.com/blogs/compute/optimizing-costs-serverless/)  
