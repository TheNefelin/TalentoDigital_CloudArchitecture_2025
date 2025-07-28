# ☁️ Ejercicio: Diseño de Arquitectura Altamente Disponible para una Aplicación Web

## 🎯 1. Desafío

Diseñar un esquema arquitectónico que asegure **alta disponibilidad**, **tolerancia a fallos** y **escalabilidad** para una plataforma de ventas online. 

---

## 🧩 a. Respuestas

### ➤ ¿Cómo implementarías la estrategia de tolerancia a fallos?

- Utilizar **instancias EC2** replicadas en al menos **dos zonas de disponibilidad** diferentes.
- Configurar **bases de datos en modo Multi-AZ**, con réplicas de lectura y backups automáticos.
- Implementar **Elastic Load Balancer (ELB)** para redirigir el tráfico automáticamente.
- Utilizar **Route 53** con políticas de failover y chequeo de salud.
- Añadir **almacenamiento redundante** (ej. Amazon S3 con replicación entre regiones).

---

### ➤ ¿Qué elementos incluirías para balancear la carga entre servidores?

- **Application Load Balancer (ALB)** para distribuir el tráfico HTTP/HTTPS entre instancias EC2.
- Políticas de **salud** para detectar instancias no operativas.
- Configuración para balancear tráfico entre múltiples zonas de disponibilidad.

---

### ➤ ¿Qué zonas de disponibilidad incluirías y por qué?

- Al menos **dos zonas de disponibilidad** (ej. `us-east-1a` y `us-east-1b`).
- Justificación:
  - En caso de que una AZ falle (por corte de energía, falla técnica o desastre), la otra podrá **mantener la operación sin interrupciones**.
  - Reduce el riesgo de **Single Point of Failure (SPOF)**.

---

### ➤ ¿Qué componentes considerarías esenciales para lograr escalabilidad y resiliencia?

- **Auto Scaling Group**: ajusta el número de instancias EC2 según demanda.
- **Amazon RDS Multi-AZ**: alta disponibilidad y failover automático de base de datos.
- **Amazon CloudWatch**: monitoreo de métricas y alertas ante fallos.
- **Route 53**: gestión de DNS y failover geográfico.
- **Amazon S3**: almacenamiento seguro y redundante para archivos estáticos y respaldos.
- **WAF + IAM**: políticas de seguridad y control de acceso.

---

## 📈 b. ¿Cómo tu diseño permitiría continuidad operativa ante fallos?

- Si una instancia EC2 falla, el **Auto Scaling Group** lanza una nueva.
- Si una zona completa falla, el **Load Balancer** redirige automáticamente el tráfico a la otra zona disponible.
- La **base de datos Multi-AZ** asegura que siempre haya una réplica activa en otra zona.
- Las copias de seguridad y réplicas aseguran la **recuperación de datos**.
- El sistema de monitoreo y alarmas alerta de forma temprana sobre problemas en el sistema.

---

## 👩‍💻 2. ¿Dónde se lleva a cabo?

- Puedes usar herramientas como [Draw.io](https://app.diagrams.net), Lucidchart o Creately para diagramar.
- Redactar este documento en Markdown, PDF o Word según prefieras.

---

## ⌛ 3. Tiempo Estimado

- Aproximadamente **1 hora**

---

## 🛠️ 4. Recursos

- [https://app.diagrams.net](https://app.diagrams.net)
- Documentación oficial de AWS:
  - Auto Scaling
  - Load Balancer
  - Multi-AZ RDS
  - CloudWatch
  - Route 53

---

## ➕ 5. Plus (opcional)

### ✔️ Escenario Cloud (AWS)

- Todo lo mencionado anteriormente usando servicios como EC2, ELB, RDS, S3, CloudWatch, Route 53.

### ✔️ Escenario On-Premise

- Uso de balanceadores físicos o virtuales (HAProxy, NGINX).
- Servidores replicados en diferentes datacenters.
- Sistemas RAID y backups locales/remotos.
- Monitoreo con Zabbix o Prometheus.
- DNS con failover manual o automatizado.

### ✔️ Monitoreo Proactivo

- **Amazon CloudWatch**: alarmas, dashboards y logs centralizados.
- **Health checks** automatizados.
- Notificaciones por **SNS o correo electrónico**.

### ✔️ Buenas Prácticas de Seguridad

- Configuración de **WAF (Web Application Firewall)**.
- Uso de **grupos de seguridad** e IAM con principio de menor privilegio.
- Monitoreo de accesos con AWS CloudTrail.
- Encriptación en tránsito y en reposo.

---

## 🧠 6. Conclusión

Esta arquitectura proporciona un entorno robusto, capaz de resistir fallos en servidores o zonas completas. A través de escalabilidad automática, balanceo de carga y replicación geográfica, se garantiza la **continuidad operativa**, **bajo tiempo de inactividad** y una experiencia de usuario consistente.

---

## 🖼️ Diagrama 


---
