# 🧠 Ejercicio: Administración y Monitoreo de Costos en la Nube

## 🎯 Desafío

Implementar una solución para administrar y monitorear los costos de una infraestructura en la nube, utilizando los conceptos y herramientas estudiados.

---

## 1. 📊 Análisis de Costos

### a. Factores que influyen en los costos en la nube

- **Uso de recursos:** CPU, memoria, almacenamiento, ancho de banda.
- **Modelo de facturación:** Pago por uso, suscripción, tarifas fijas.
- **Configuración de servicios:** Elección de instancias, bases de datos, servicios complementarios.
- **Estrategias de escalabilidad:** Escalado vertical y horizontal según demanda.

### b. Importancia del monitoreo de costos

El monitoreo es esencial para:
- Detectar desviaciones de consumo.
- Prevenir sobrecostos.
- Optimizar recursos y cumplir con los presupuestos.
- Tomar decisiones proactivas y fundamentadas.

---

## 2. ⚙️ Configuración de Monitoreo con AWS CloudWatch

### 🧭 Pasos para configurar una alarma en CloudWatch

1. **Definir la métrica clave**
   - Ejemplo: `CPUUtilization` para una instancia EC2.
   - Navegar en la consola de AWS a: **CloudWatch > Métricas**.
   - Buscar la métrica deseada (ej. EC2 > CPUUtilization).

2. **Crear una alarma**
   - Hacer clic en **“Crear alarma”**.
   - Seleccionar la métrica definida.
   - Establecer el umbral: p. ej., uso mayor al 80% durante 5 minutos.

3. **Configurar notificaciones**
   - Seleccionar o crear un tema SNS.
   - Configurar correo electrónico o SMS como destinatario.

4. **Activar la alarma**
   - Revisar toda la configuración.
   - Guardar y habilitar la alarma.

### 🖥️ Comando de ejemplo con AWS CLI

```bash
aws cloudwatch put-metric-alarm   --alarm-name "HighCPUUtilization"   --metric-name CPUUtilization   --namespace AWS/EC2   --statistic Average   --period 300   --threshold 80   --comparison-operator GreaterThanThreshold   --dimensions Name=InstanceId,Value=i-0123456789abcdef0   --evaluation-periods 1   --alarm-actions arn:aws:sns:us-east-1:123456789012:MySNSTopic   --unit Percent
```

### 📈 Diagrama de integración

```text
+----------------+        +----------------+       +----------------+
|   AWS EC2      | -----> |  CloudWatch    |-----> |     SNS        |
| (Instancia)    |        |  (Métricas)    |       | (Notificación) |
+----------------+        +----------------+       +----------------+
```

---

## 3. 📋 Cuadro Comparativo: Monitoreo Manual vs Automatizado

| Característica        | Monitoreo Manual                   | Monitoreo Automatizado (CloudWatch)         |
|------------------------|------------------------------------|---------------------------------------------|
| Precisión              | Depende del análisis humano        | Métricas en tiempo real                     |
| Rapidez de respuesta   | Lenta, revisión periódica          | Inmediata con alertas automáticas           |
| Escalabilidad          | Limitado a la capacidad humana     | Altamente escalable                         |
| Costo y eficiencia     | Costoso por intervención constante | Optimizado mediante automatización          |

---

## 4. 🧪 Entorno de Pruebas

- Documentación en **Visual Studio Code**.
- Simulación usando **AWS Academy** y/o **SQLiteOnline**.
- Complementado con CLI y consola de AWS.

---

## 5. ➕ Plus (Opcional)

- Se integró **AWS SNS** para alertas automáticas.
- Puedes compartir este proyecto en GitHub para feedback y colaboración.

---

## 6. ✅ Conclusión

Este ejercicio demuestra cómo configurar y automatizar el monitoreo de costos y rendimiento en la nube utilizando **AWS CloudWatch**. Implementar estas herramientas permite mantener un control económico y técnico efectivo, garantizando un uso óptimo de la infraestructura cloud.

---

## 📚 Recursos

- [AWS CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Documentation](https://aws.amazon.com/documentation/)
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/)