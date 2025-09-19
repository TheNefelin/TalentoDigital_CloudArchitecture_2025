
# 📄 Caso: Crecimiento y Optimización de Recursos — CloudCommerce

**Rol:** Arquitecto cloud  
**Entorno:** AWS Academy (Lambda, API Gateway, DynamoDB, S3, CloudFront, CloudWatch, Budgets)

---

## 1) Análisis inicial — posibles causas del aumento de costos y degradación
**Causa 1 — Incremento de invocaciones de Lambda y duración alta**  
- Tráfico mayor produce más invocaciones; funciones con memoria mal dimensionada o lógica ineficiente aumentan la duración (ms) y el coste por ejecución.  
- Cold starts si hay muchas funciones con poca concurrencia o dependencias pesadas, incrementan latencia en horas pico.  

**Causa 2 — Acceso intensivo a DynamoDB y hot partitions**  
- Lecturas/escrituras concentradas en pocas claves (baja cardinalidad) generan *hot partitions*, throttling y latencias mayores; en modo Provisioned sin auto‑scaling, picos generan errores y reintentos que aumentan costos.  
- Uso ineficiente de patrones de acceso (consultas múltiples en lugar de diseño orientado a accesos) incrementa RCU/WCU consumidos.

**Causa 3 — Tráfico de objetos estáticos servido desde S3 sin CDN**  
- Peticiones directas a S3 en picos incrementan solicitudes GET/PUT y costos de salida (egress). Latencia para usuarios remotos aumenta sin caching distribuido (CloudFront).

---

## 2) Tres estrategias prácticas (pasos concretos en AWS Academy)

### Estrategia A — Activar caché en Amazon API Gateway
**Objetivo:** Reducir latencia y disminuir invocaciones a Lambda.  
**Pasos:**  
1. Identificar endpoints idempotentes / cachables (catálogos, listados, respuestas no críticas).  
2. En API Gateway (REST API caching): habilitar **Cache** para cada método; configurar **TTL** acorde al dato (ej. catálogos: `3600s` / 1h; datos de usuario: `60–300s`).  
3. Establecer **Cache key parameters** (headers, query strings, stage variables) que afecten la caché.  
4. Configurar invalidación programada desde pipeline CI/CD o por eventos (por ejemplo: POST/PUT que actualice recursos lanza invalidación de cache via CloudWatch Events / EventBridge -> invalidación).  
5. Monitorear efecto con métricas: CacheHitRate, CacheSizeBytes, IntegrationLatency.  
**Consideraciones:** No cachear respuestas sensibles; usar TTL cortos para datos frescos.

### Estrategia B — Desplegar CloudFront frente a S3 (Origin Access Control)
**Objetivo:** Mejorar latencia global, reducir egress y proteger buckets.  
**Pasos:**  
1. Crear distribución CloudFront con el bucket S3 como origen.  
2. Configurar **Origin Access Control (OAC)** o anteriormente OAI para restringir acceso directo al bucket; aplicar política de bucket que permita únicamente a CloudFront.  
3. Definir **Cache Policy** (incluir headers y query strings necesarios) y **Origin Shield** si se desea capa adicional de caching regional.  
4. Habilitar compresión automática (Brotli/GZIP) y configurar TTLs (respecto a `Cache-Control` de los objetos).  
5. Para contenido privado, usar **Signed URLs/Cookies**.  
6. Medir reducción de egress y latencia mediante CloudFront metrics (Requests, BytesDownloaded, CacheHitRate).  

### Estrategia C — Revisar y ajustar capacidad de DynamoDB
**Objetivo:** Reducir throttling, optimizar costos según patrón de tráfico.  
**Pasos de evaluación:**  
1. Revisar patrones de acceso (hot keys) con **CloudWatch / Contributor Insights** y métricas de ConsumedReadCapacityUnits/ConsumedWriteCapacityUnits, ThrottledRequests, PartitionCount.  
2. Si el tráfico es impredecible o con picos frecuentes → **On‑Demand** para evitar sobreprovisionamiento y manejar picos sin throttling.  
3. Si el tráfico es predecible → usar **Provisioned** con **Auto Scaling** (target utilization ~70–80%) para ahorrar costos.  
4. Re‑modelado de datos: aumentar cardinalidad de partition key (p.ej. incluir un prefijo o hashing) o usar single-table patterns con índices secundarios cuando convenga.  
5. Habilitar **DAX** (si muchas lecturas repetidas de los mismos items) para reducir RCU y latencia.  

---

## 3) Plan de monitoreo con Amazon CloudWatch (métricas, alarmas y dashboards)

### Métricas clave a monitorear (por servicio)
**Lambda**  
- `Invocations` (nº llamadas)  
- `Duration` (ms) — p95/p99  
- `Errors`, `Throttles`, `ConcurrentExecutions`  

**API Gateway**  
- `Count` (requests)  
- `4XX/5XXError` rates  
- `Latency` (p95)  
- `CacheHitCount` / `CacheMissCount` (si caching habilitado)  

**DynamoDB**  
- `ConsumedReadCapacityUnits` / `ConsumedWriteCapacityUnits`  
- `ProvisionedReadCapacityUnits` / `ProvisionedWriteCapacityUnits`  
- `ThrottledRequests`  
- `ConditionalCheckFailedRequests`  

**S3 / CloudFront**  
- S3: `NumberOfObjects`, `AllRequests`, `4xxErrors`, `5xxErrors`  
- CloudFront: `Requests`, `BytesDownloaded`, `TotalErrorRate`, `CacheHitRate`

**Cost / Usage**  
- `EstimatedCharges` (CloudWatch billing metric) por servicio o por linked account

### Alarmas recomendadas (umbrales ejemplo)
1. **Lambda Throttles > 0** (sustained 1–5 min) → Notificación a SNS + ejecutar playbook.  
2. **ConcurrentExecutions > 80% del límite** → Notificación y revisar limits/Reservas.  
3. **DynamoDB ThrottledRequests > 0** (sustained) → Escalar o cambiar a On‑Demand.  
4. **API Gateway 5XX rate > 1%** (5 min) → Notificación + investigar fallback.  
5. **CloudFront CacheHitRate < 80%** (monitor diario) → Revisar políticas de cache.  
6. **EstimatedCharges > 90% del presupuesto mensual** → Notificación inmediata.

### Dashboards recomendados
- **Operacional:** Latencia p95, invocations, errores por endpoint.  
- **Base de datos:** RCU/WCU, throttles, hot keys.  
- **Costos:** EstimatedCharges por servicio y forecast.  
- **Logs:** Widgets CloudWatch Logs Insights para errores críticos.

---

## 4) Configuración de AWS Budgets (detalle práctico)

**Tipo de presupuesto:** Cost budget (Monthly)  
**Ejemplo de configuración:**  
- **Budget amount:** `1000 USD` (reemplazar por monto real).  
- **Alerts:**  
  - 50% (Email/SNS) → equipo FinOps.  
  - 80% (Email + Slack + ticket) → equipo técnico + finanzas.  
  - 95% (Email urgente + acciones de mitigación) → detener lanzamientos no críticos.  
- **Segmentación:** Incluir tags (`CostCenter`, `Environment`, `Project`) para filtrar gasto por proyecto.  
- **Forecast alerts:** Activar alerta si forecast > 100% del budget.  
- **Acciones automatizadas:** Suscribir un Lambda/SNS que ejecute mitigaciones leves (e.g., pausar pipelines) cuando se alcance 95%.

---

## 5) Reflexión final — impacto esperado
Con estas medidas se espera:  
- **Reducción de costos:** menos invocaciones de Lambda, menor consumo RCU/WCU, reducción de egress por CloudFront.  
- **Mejor experiencia de usuario:** latencia reducida, menos errores en picos.  
- **Escalabilidad controlada:** auto‑scaling o On‑Demand para absorber picos sin intervención.  

---

## Anexos rápidos

**Invalidar cache API Gateway (CLI):**  
```bash
aws apigateway flush-stage-cache --rest-api-id <api-id> --stage-name <stage>
```

**Política S3 para permitir sólo CloudFront (ejemplo):**  
```json
{
  "Version":"2012-10-17",
  "Statement":[{
    "Effect":"Allow",
    "Principal":{"AWS":"arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity <ID>"},
    "Action":"s3:GetObject",
    "Resource":"arn:aws:s3:::mi-bucket/*"
  }]
}
```

---
