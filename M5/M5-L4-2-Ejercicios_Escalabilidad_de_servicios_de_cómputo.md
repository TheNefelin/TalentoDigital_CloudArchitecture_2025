# 💼 Ejercicio: Escalabilidad de Servicios de Cómputo (AWS)

## 🎯 Desafío

Implementar un entorno escalable en AWS configurando:

- Un grupo de **EC2 AutoScaling**.
- Un **Elastic Load Balancer (ELB)**.

---

## 👩‍💻 ¿Dónde se lleva a cabo?

- **Plataforma:** AWS Academy
- **Herramientas:** Consola AWS, editor de texto o herramienta de documentación

---

## ⌛ Tiempo Estimado

2 a 3 horas

---

## 🛠️ Recursos Utilizados

- AWS Academy
- Documentación oficial:
  - [EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
  - [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
- Editor de texto para documentar

---

## 🧩 Paso a Paso de la Configuración

### 1. Configuración del AutoScaling Group (ASG)

- **AMI usada:** Amazon Linux 2
- **Tipo de instancia:** t2.micro
- **Grupo de AutoScaling:**
  - Mínimo: 2 instancias
  - Máximo: 6 instancias
  - Deseado: 2 instancias
- **Política de escalado:**
  - Aumentar instancias si el uso de CPU > 70% durante 5 minutos.
  - Reducir instancias si el uso de CPU < 30%.

### 2. Configuración del ELB (Elastic Load Balancer)

- Tipo: Application Load Balancer
- Listeners: HTTP en puerto 80
- Regla de salud: `/` con código 200
- Asociado al grupo de AutoScaling
- Balancea tráfico entre instancias en distintas zonas de disponibilidad

---

## 💲 Análisis de Costos y Beneficios

### 📊 Costos Considerados

- Uso de instancias EC2 (por hora)
- Transferencia de datos salientes
- Costo del ELB por tráfico balanceado

### ✅ Beneficios

- **Escalado automático:** Adapta el número de instancias a la demanda real.
- **Alta disponibilidad:** Distribución de tráfico evita puntos únicos de falla.
- **Optimización de costos:** Solo se pagan los recursos en uso.
- **Recuperación automática:** El sistema reemplaza instancias con fallos.
- **Flexibilidad:** Puede integrarse con ECS/EKS para despliegues con contenedores.

---

## 📝 Reporte Explicativo

> Se configuró un grupo de AutoScaling con un mínimo de 2 y un máximo de 6 instancias EC2, utilizando políticas basadas en métricas de uso de CPU. El Elastic Load Balancer distribuye el tráfico entrante a través del puerto 80, asegurando disponibilidad y balanceo eficiente. Esta arquitectura permite adaptarse a picos de demanda de forma automática, garantizando que el sistema permanezca disponible incluso ante fallos de instancias. Adicionalmente, se considera la integración con ECS para aplicaciones en contenedores, lo que aumenta la flexibilidad y escalabilidad del entorno. Esta solución optimiza los costos al pagar únicamente por los recursos necesarios y mejora la resiliencia del sistema.

---
