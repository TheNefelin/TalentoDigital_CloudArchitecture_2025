# Resumen: El Modelo de Compliance y Seguridad Automatizada

## Introducción
La adopción acelerada de la nube requiere **cumplimiento normativo** y **seguridad automatizada**.  
En la nube aplica el modelo de **responsabilidad compartida**: el proveedor asegura la infraestructura y el cliente configura y monitorea.  
Este manual explica servicios AWS, ejemplos y buenas prácticas para lograr cumplimiento continuo y automatizado.

---

## 1. ¿Qué es Compliance en la nube?
El **compliance** es cumplir leyes, normas y políticas internas.  
En la nube implica:

| Aspecto | On-Premise | Nube |
|---------|------------|------|
| Control infraestructura | Total | Compartido |
| Auditorías | Manuales y periódicas | Continuas y automatizadas |
| Escalabilidad controles | Limitada | Automática (IaC, APIs) |
| Actualización normativa | Lenta | Dinámica (certificaciones proveedor) |

**Adopción en AWS:**  
- Uso de **IaC (CloudFormation, Terraform)**.  
- Políticas IAM con **least privilege**.  
- Servicios gestionados que generan evidencias en tiempo real.

---

## 2. ¿Qué es Seguridad Automatizada?
Controles que se despliegan y corrigen **sin intervención humana**.  
**Beneficios:**  
1. Velocidad.  
2. Coherencia (menos errores humanos).  
3. Escalabilidad (gobernar múltiples cuentas/regiones).  
4. Trazabilidad (cambios auditables).

---

## 3. Servicios AWS Clave para Compliance

| Servicio | Propósito | Caso de uso | Cuándo usar |
|----------|-----------|-------------|-------------|
| **AWS Config** | Inventario + evaluación continua de configuraciones | Detectar buckets públicos, claves KMS sin rotación, SG abiertos | Necesitas alertas inmediatas y remediación automática |
| **Audit Manager** | Evidencias e informes de auditoría (ISO 27001, SOC 2, HIPAA) | Preparar auditorías sin recolectar logs manuales | Reducir tiempo y costo de auditorías |
| **CloudWatch** | Monitoreo, métricas, logs y alarmas | Cumplir requisitos de registro (NIST 800-53) y activar respuestas automáticas | Observabilidad integral |
| **GuardDuty** | Detección de amenazas (ML + firmas) | Alertar sobre IAM comprometido, criptominería, accesos TOR | Inteligencia gestionada sin infraestructura adicional |
| **Macie** | Descubrimiento y protección de datos sensibles (PII, PHI) en S3 | Clasificar y proteger datos personales, cumplir GDPR/CCPA | Evitar fugas de datos confidenciales |

### 3.1 Mejores prácticas
- **IaC + CI/CD**: integrar Config en plantillas.  
- **Multi-cuenta con Organizations**: centralizar seguridad.  
- **Respuesta automatizada**: EventBridge + Lambda.  
- **Conformance Packs**: despliegue de reglas agrupadas.

### 3.2 Ejemplos prácticos
- **Config**: regla `s3-bucket-server-side-encryption-enabled` + remediación SSE-KMS.  
- **Audit Manager**: framework que combine ISO 27001 + GDPR.  
- **CloudWatch**: métrica de latencia API <200 ms + alarma SNS.  
- **GuardDuty**: bloquear IPs sospechosas con WAF.  
- **Macie**: clasificar PII en buckets financieros diariamente.

---

## 4. Arquitectura de Referencia
Flujo:  
1. Config detecta bucket público.  
2. EventBridge dispara Lambda → aplica política privada.  
3. GuardDuty analiza actividad sospechosa.  
4. CloudWatch registra métricas.  
5. Audit Manager consolida evidencias para auditoría.  

---

## 5. Costos y Límites Clave
| Servicio | Facturación | Límite gratuito |
|----------|-------------|-----------------|
| **Config** | Evaluaciones + snapshots | 7.5 h/mes de grabación |
| **Audit Manager** | Evaluaciones + almacenamiento | 30 días de prueba |
| **CloudWatch** | Métricas, logs, alarmas | 10 métricas + 5 GB logs |
| **GuardDuty** | Eventos analizados | 30 días de prueba |
| **Macie** | Objetos escaneados (GB) | 30 días de prueba |

**Optimización:** análisis selectivo en Macie, exclusiones en Config, retención ajustada en CloudWatch.

---

## 6. Comparación On-Premise vs AWS

| Capacidad | On-Premise | AWS | Ventaja AWS |
|-----------|------------|-----|-------------|
| Configuración | Chef InSpec | Config | Integración nativa + remediación automática |
| Auditoría | Splunk + scripts | Audit Manager | Evidencias listas y estandarizadas |
| Monitoreo | Nagios | CloudWatch | Métricas integradas por servicio |
| Amenazas | Suricata/IDS | GuardDuty | ML gestionado sin mantenimiento |
| Protección de datos | Symantec DLP | Macie | Descubrimiento automático en S3 |

---

## Conclusión
El compliance y la seguridad automatizada son fundamentales en la nube.  
Con AWS Config, Audit Manager, CloudWatch, GuardDuty y Macie, se logra una postura de seguridad continua, auditable y alineada a estándares internacionales.

---

## Referencias
- [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/)  
- [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/)  
- [Amazon CloudWatch](https://docs.aws.amazon.com/cloudwatch/)  
- [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/)  
- [Amazon Macie](https://docs.aws.amazon.com/macie/)  
- [AWS Security Hub](https://docs.aws.amazon.com/securityhub/)  
- [CIS AWS Foundations Benchmark](https://www.cisecurity.org/benchmark/amazon_web_services)  
