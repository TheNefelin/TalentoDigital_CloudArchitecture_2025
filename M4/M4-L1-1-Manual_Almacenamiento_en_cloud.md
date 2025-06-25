# 🗄️ Almacenamiento en la Nube – Resumen

## 🎯 Aprendizaje Esperado
- Evaluar servicios de almacenamiento de objetos y datos, tanto en pequeños como grandes volúmenes, según su uso en el tiempo.

---

## 1. 📦 Fundamentos del Almacenamiento Cloud

### ✅ Características clave:
- **Infraestructura gestionada por terceros**
- **Acceso remoto** desde cualquier lugar con Internet
- **Seguridad y escalabilidad**
- **Pago por uso**

### 📘 Conceptos básicos:
- **Disponibilidad:** acceso continuo (SLA de 99.9% o más)
- **Durabilidad:** replicación de datos para evitar pérdidas
- **Elasticidad:** escalar almacenamiento bajo demanda
- **Seguridad:** cifrado en tránsito y en reposo, auditoría y control de acceso

---

## 2. ☁️ Comparativa Cloud vs On-Premise

| Criterio          | Cloud                            | On-Premise                           |
|-------------------|----------------------------------|--------------------------------------|
| Costos iniciales  | Bajos (pago por uso)             | Altos (hardware, licencias)          |
| Mantenimiento     | A cargo del proveedor            | Interno (soporte, actualizaciones)   |
| Escalabilidad     | Rápida y elástica                | Limitada por hardware                |
| Disponibilidad    | Alta (SLA garantizado)           | Depende de redundancia local         |
| Seguridad         | Cifrado + cumplimiento normativo | Control físico local                 |
| Flexibilidad      | Integración con servicios cloud  | Limitada sin infraestructura moderna |
| Ubicación de datos| Centros de datos del proveedor   | Instalaciones propias                |

---

## 3. 🧰 Tipos de Almacenamiento y sus Propósitos

### 🔹 S3 (Simple Storage Service)
- **Objetos** en "buckets", ideal para contenido estático y backups
- Clases: Standard, IA, Intelligent-Tiering
- **Ventajas:** Escalable, económico, API REST
- **Desventajas:** No apto para transacciones en tiempo real
- **Ejemplo:** Imagenes, archivos, logs, almacén general

### 🔹 Glacier
- **Almacenamiento de archivo** a largo plazo
- **Ventajas:** Muy bajo costo
- **Desventajas:** Recuperación lenta (minutos u horas)
- **Ejemplo:** Copias de seguridad a largo plazo, retención por años, logs auditoria

### 🔹 EBS (Elastic Block Store)
- **Almacenamiento de bloques** para instancias EC2
- **Ventajas:** Alto rendimiento, baja latencia
- **Desventajas:** No ideal para datos fríos
- **Ejemplo:** Disco para el OS en EC2, bases de datos relacionales

### 🔹 EFS (Elastic File System)
- **Sistema de archivos compartido**, acceso simultáneo
- **Ventajas:** Escalable, simple de usar
- **Desventajas:** Costo alto para datos no compartidos
- **Ejemplo:** Directorios compartidos, repositorios de código

### 🔹 Storage Gateway
- **Puente entre on-premise y cloud**
- **Ventajas:** Caché local, útil para migraciones
- **Desventajas:** Mayor complejidad
- **Ejemplo:** Google Drive, Dropbox

---

## 4. 💰 Costos de Almacenamiento

- **Capacidad:** GB/mes
- **Operaciones:** Lecturas, escrituras, recuperaciones
- **Transferencia de datos salientes**
- **Clases de almacenamiento:** Diferentes precios según accesibilidad y durabilidad

**Consejo:** Usar herramientas de cálculo de costos para estimar gastos.

---

## 5. ⚙️ Estrategias de Uso

1. **Clasificación por frecuencia de acceso:**
   - EBS/EFS: Datos críticos y frecuentes
   - S3: Datos semi-frecuentes
   - Glacier: Archivos y datos inactivos

2. **Ciclo de vida de objetos (S3):**
   - Migrar automáticamente datos antiguos a clases más baratas (ej. Glacier)

3. **Integración on-premise + nube:**
   - Usar Storage Gateway para mantener caché local

4. **Supervisión y optimización de costos:**
   - Analizar patrones y ajustar almacenamiento

5. **Pruebas de rendimiento:**
   - Asegurar que el tipo de almacenamiento satisface la latencia y volumen requerido

---

## ✅ Conclusión

El almacenamiento en la nube ofrece **flexibilidad, escalabilidad y eficiencia de costos**, pero debe usarse con una **estrategia adecuada** que considere rendimiento, frecuencia de acceso y control de datos.
