# Administración de costos en la nube — Resumen de Caso

## 1. Contexto
CloudOpt Solutions detecta aumento de costos en AWS. Se requiere:
- Analizar factores de costo.
- Proponer optimizaciones.
- Configurar monitoreo (CloudWatch + SNS).
- Generar reportes de costos.
- Comparar monitoreo manual vs automatizado.  
*(Respetando límites del Lab: 9 instancias/región, 32 vCPU, 100 GB EBS, Lambda concurrency 10, sólo `us-east-1` y `us-west-2`)*.

---

## 2. Factores clave que impactan costos
- Sobredimensionamiento de instancias EC2.
- Uso excesivo de almacenamiento (EBS, S3, snapshots).
- Recursos inactivos (instancias, NAT, volúmenes).
- Modelos On-Demand en cargas estables (no uso de reservas).
- Límite de concurrency en Lambdas (lab: 10).
- Transferencia de datos entre regiones.

---

## 3. Estrategias de optimización
1. **Rightsizing**: reducir tamaños si CPU < 10% por 7 días.
2. **Apagado programado** fuera de horario.
3. **Eliminar recursos huérfanos** y snapshots viejos.
4. **Optimizar almacenamiento** con lifecycle policies.
5. **Auto Scaling** sin superar límites del lab.
6. **Alarmas de presupuesto** conservadoras para evitar desactivación.

---

## 4. Paso a paso esencial

### 4.1 Crear topic SNS y suscripción
```bash
aws sns create-topic --name NotifyOps --region us-east-1
aws sns subscribe   --topic-arn arn:aws:sns:us-east-1:123456789012:NotifyOps   --protocol email   --notification-endpoint correo@empresa.com
```

### 4.2 Alarma CloudWatch CPU alta
```bash
aws cloudwatch put-metric-alarm   --alarm-name EC2_CPU_HIGH   --metric-name CPUUtilization   --namespace AWS/EC2   --statistic Average   --period 300 --threshold 75   --comparison-operator GreaterThanThreshold   --dimensions Name=InstanceId,Value=i-0abcd1234   --evaluation-periods 1   --alarm-actions arn:aws:sns:us-east-1:123456789012:NotifyOps
```

### 4.3 Reporte de costos últimos 7 días
```bash
START=$(date -d "7 days ago" +%Y-%m-%d)
END=$(date +%Y-%m-%d)
aws ce get-cost-and-usage   --time-period Start=$START,End=$END   --granularity DAILY   --metrics UnblendedCost   --group-by Type=DIMENSION,Key=SERVICE
```




---

## 5. Monitoreo manual vs automatizado
| Criterio | Manual | Automatizado |
|---|---|---|
| Detección | Lenta | Inmediata |
| Escalabilidad | Mala | Alta |
| Costo humano | Alto | Bajo |
| Precisión | Variable | Consistente |
| Recomendación | Auditorías puntuales | **Usar** + revisión periódica |

---

## 6. Conclusión
Implementar CloudWatch + SNS y reportes automáticos permitirá:
- Detectar anomalías antes de que afecten presupuesto.
- Cumplir límites del lab y evitar suspensiones.
- Reducir costos por sobreuso y recursos ociosos.
- Mejorar eficiencia operativa combinando automatización y revisión manual.

| Componente AWS | Contribución a la Escalabilidad | Función principal |
|----------------|---------------------------------|-------------------|
| **EC2 (Elastic Compute Cloud)** | Permite aumentar o disminuir la capacidad de cómputo agregando o removiendo instancias según la carga. | Proporciona instancias virtuales para ejecutar aplicaciones, servicios y cargas de trabajo en la nube. |
| **ASG (Auto Scaling Group)** | Escala automáticamente el número de instancias EC2 en función de métricas o programaciones, manteniendo el rendimiento y optimizando costos. | Agrupa instancias EC2 y gestiona su creación/eliminación basándose en políticas definidas. |
| **ELB (Elastic Load Balancer)** | Distribuye tráfico entre múltiples instancias, evitando sobrecarga en un solo recurso y facilitando el escalado horizontal. | Balancea automáticamente el tráfico de red/HTTP hacia instancias EC2 registradas en uno o varios AZs. |
| **AZs (Availability Zones)** | Aumenta la resiliencia y escalabilidad al permitir distribuir la carga en múltiples zonas, reduciendo impacto de fallas en una sola ubicación. | Son centros de datos físicos separados dentro de una región AWS, interconectados para alta disponibilidad y baja latencia. |
