# 🗃️ Servicios de Bases de Datos Relacionales en la Nube – Resumen

## 🎯 Aprendizaje Esperado
- Diferenciar los servicios asociados a bases de datos relacionales gestionadas en la nube para satisfacer las necesidades de la organización.

---

## 1. 📘 ¿Qué es un Servicio Gestionado de Base de Datos en la Nube?

Un servicio gestionado permite delegar al proveedor (AWS, Azure, GCP) tareas como:
- Instalación y configuración del motor de base de datos
- Parches y actualizaciones
- Administración de hardware y red
- Seguridad (cifrado, accesos)
- Backups automáticos
- Monitoreo y escalabilidad

### ✅ Beneficios:
- Menor carga operativa
- Alta disponibilidad (SLA)
- Escalabilidad automática
- Pago por uso

### ⚠️ Desventaja:
- Menor control directo sobre la infraestructura

---

## 2. 🔄 Amazon RDS: Alternativa de Base de Datos Relacional

Amazon RDS es un servicio gestionado que soporta:
- MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### Características:
- Facilidad de despliegue vía consola o API
- Backups automáticos
- Escalabilidad vertical
- Soporte Multi-AZ

📌 *Ejemplo*: Un e-commerce puede usar RDS MySQL para mantener su catálogo y escalar fácilmente en temporadas altas.

---

## 3. ⚙️ Escalabilidad en Amazon RDS

| Tipo de escalabilidad | Descripción |
|------------------------|-------------|
| **Vertical**           | Aumentar recursos (vCPU, RAM, almacenamiento) cambiando la clase de instancia |
| **Horizontal**         | Uso de *Read Replicas* (para consultas) y *Sharding* a nivel de aplicación |

✅ Beneficios:
- Ajuste rápido de recursos
- Alta disponibilidad
- Escalado sin comprar hardware físico

⚠️ Consideraciones:
- Cambios verticales pueden requerir reinicio
- Réplicas de lectura pueden tener latencia

---

## 4. 💰 Costos Asociados a RDS

| Componente             | Detalle |
|------------------------|---------|
| Clase de instancia     | Costo por hora/segundo |
| Almacenamiento         | Costo por GB/mes según tipo (GP2, GP3, IOPS) |
| Transferencia de datos | Salida se cobra, entrada suele ser gratuita |
| Backups                | Espacio gratuito hasta el tamaño de la BD |

---

## 5. 🆚 Comparativa: RDS vs On-Premise

| Criterio         | RDS (Cloud)                          | On-Premise                             |
|------------------|--------------------------------------|----------------------------------------|
| Implementación   | Rápida (minutos)                     | Lenta (instalación física)             |
| Escalabilidad    | Alta y elástica                      | Limitada al hardware                   |
| Costo inicial    | Bajo (pago por uso)                  | Alto (infraestructura propia)          |
| Mantenimiento    | Gestionado por el proveedor          | Interno, con más carga operativa       |
| Seguridad        | Cifrado, IAM, red privada            | Depende de recursos y prácticas locales|
| Disponibilidad   | SLA altos, Multi-AZ, backups         | Requiere redundancia propia            |
| Control total    | Limitado
