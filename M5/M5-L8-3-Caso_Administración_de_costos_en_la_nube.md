# 📊 Análisis de Caso: Administración y Monitoreo de Costos en la Nube

## 🏢 Empresa: CloudOpt Solutions

### 🎯 Situación Inicial

CloudOpt Solutions ha migrado su infraestructura a AWS, pero ha experimentado un aumento inesperado en los costos. Esto se ha atribuido a configuraciones inadecuadas, recursos infrautilizados y falta de monitoreo.

Como Ingeniero de la Nube, tu responsabilidad es evaluar y optimizar la administración de costos para mejorar la eficiencia y reducir el gasto.

---

## 1. 🔍 Análisis de Costos y Factores de Influencia

### 🧠 Factores que influyen en los costos
- **Uso de recursos:** CPU, memoria, almacenamiento, tráfico de red.
- **Modelo de facturación:** Pago por uso, instancias reservadas, Savings Plans.
- **Configuración inadecuada:** Instancias sobredimensionadas, servicios inactivos.
- **Falta de escalabilidad:** No utilizar escalado automático genera consumo constante.

### 💡 Estrategias de optimización
- Escalado automático según demanda (Auto Scaling Groups).
- Eliminación de recursos sin uso (snapshots, volúmenes, IPs elásticas).
- Uso de instancias reservadas y Savings Plans.
- Monitoreo activo con alarmas y alertas.
- Revisión periódica con Cost Explorer y Budgets.

---

## 2. ⚙️ Configuración y Monitoreo con AWS CloudWatch

### 🔔 Configuración de Alarmas

**Métricas monitoreadas:**
- CPUUtilization (EC2)
- DiskReadOps / DiskWriteOps
- NetworkIn / NetworkOut
- EstimatedCharges (Billing)

**Pasos de configuración:**
1. Accede a AWS CloudWatch > Métricas.
2. Selecciona la métrica (ej. EC2 > CPUUtilization).
3. Crea una alarma con umbral (ej. uso > 80% por 5 minutos).
4. Configura la acción de la alarma:
   - Integrar con un **SNS Topic**.
   - Enviar notificación por email/SMS.
5. Guardar y activar la alarma.

**Ejemplo CLI:**
```bash
aws cloudwatch put-metric-alarm   --alarm-name "HighCPU"   --metric-name CPUUtilization   --namespace AWS/EC2   --statistic Average   --period 300   --threshold 80   --comparison-operator GreaterThanThreshold   --dimensions Name=InstanceId,Value=i-xxxxxxxxxxxxxxxxx   --evaluation-periods 1   --alarm-actions arn:aws:sns:us-east-1:123456789012:MyTopic   --unit Percent
```

---

## 3. 📝 Informe y Cuadro Comparativo

### 📈 Informe de Métricas (simulado)
| Recurso       | Métrica           | Valor Promedio | Observaciones                 |
|---------------|-------------------|----------------|-------------------------------|
| EC2-Prod-01   | CPUUtilization    | 85%            | Carga alta constante          |
| EC2-Dev-02    | CPUUtilization    | 10%            | Subutilización, posible stop  |
| RDS-DB        | StorageUtilization| 70%            | Dentro de límites             |
| Billing       | EstimatedCharges  | $1,300 USD     | Por encima del presupuesto    |

### 📊 Cuadro Comparativo: Monitoreo Manual vs Automatizado

| Característica        | Monitoreo Manual              | Monitoreo Automatizado (CloudWatch)       |
|------------------------|-------------------------------|--------------------------------------------|
| Precisión              | Análisis manual               | Métricas en tiempo real                    |
| Rapidez de respuesta   | Revisión periódica            | Inmediata mediante alarmas                 |
| Escalabilidad          | Limitada                      | Escalable a múltiples servicios            |
| Costos                 | Más costoso y propenso a error| Menor costo y mayor eficiencia             |

---

## 4. ✅ Buenas Prácticas y Mejoras Adicionales

- Implementación de reportes automáticos con **Cost Explorer Reports**.
- Scripts para detener instancias EC2 fuera de horario laboral.
- Uso de **AWS Trusted Advisor** para recomendaciones de ahorro.
- Consolidación de cuentas bajo **AWS Organizations**.

---

## 5. 🧠 Reflexión Final

Este análisis permitió identificar recursos sobredimensionados y aplicar técnicas de optimización para controlar el gasto. El monitoreo automatizado con CloudWatch y SNS facilitó la respuesta proactiva. La adopción de buenas prácticas no solo redujo los costos sino que también mejoró la eficiencia operativa.

---

## 📬 Entregables

- ✔️ Análisis detallado de costos y estrategias.
- ✔️ Documentación paso a paso de alarmas y SNS.
- ✔️ Informe de métricas y comparativa de monitoreo.
- ✔️ Código de ejemplo con CLI.
- ✔️ Reflexión y buenas prácticas.

---

## 📚 Recursos

- [AWS CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/reference/)
- [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)