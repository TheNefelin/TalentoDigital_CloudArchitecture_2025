# Servicios de Bases de Datos NoSQL en la Nube

**M4: Fundamentos de Tecnología Cloud**  
**AE3:** Diferenciar los servicios asociados a las bases de datos NoSQL en la nube para satisfacer las necesidades de la organización.

---

## Introducción 🧑‍💻

En la era del Big Data, las bases de datos NoSQL (Not Only SQL) ofrecen:
- **Esquemas flexibles** para datos semiestructurados o no estructurados.  
- **Escalabilidad horizontal** y alto rendimiento.  
- **Tolerancia a fallos** y replicación nativa.  

Nos centraremos en los servicios AWS: DynamoDB, DocumentDB, Redshift, Neptune y ElastiCache.

---

## Aprendizaje esperado

Al finalizar, serás capaz de:
1. Diferenciar los servicios NoSQL en la nube según las necesidades organizacionales.

---

## 1. ¿Qué es una base de datos NoSQL?

- No usan un modelo de tablas rígidas (relacional).  
- Permiten **esquemas dinámicos**, **alto rendimiento** y **escalabilidad horizontal**.  
- Soportan distintos **niveles de consistencia** (eventual, fuerte, etc.).

---

## 2. Características comunes

1. **Almacenamiento clave‑valor o por documentos** (JSON, BSON, XML).  
2. **Escalado horizontal** añadiendo nodos.  
3. **Optimización** para lecturas/escrituras masivas.  
4. **Procesamiento distribuido** y replicación.

---

## 3. Casos de uso

- Aplicaciones web/móviles con alta concurrencia.  
- Sistemas de análisis de logs y monitorización.  
- Recomendaciones y análisis en tiempo real.  
- Catálogos de productos con formatos cambiantes.  
- IoT: ingestión continua de datos de dispositivos.

---

## 4. Tipos de bases NoSQL

| Tipo         | Formato          | Casos de uso                             | Ejemplos                      |
| ------------ | ---------------- | ----------------------------------------- | ----------------------------- |
| **Documental** | JSON/BSON/XML    | Catálogos, perfiles de usuario            | MongoDB, CouchDB, DocumentDB  |
| **Columnar**   | Columnas         | Analítica masiva, consultas agregadas     | Cassandra, HBase, Redshift    |
| **En memoria** | RAM              | Caché, ranking en tiempo real             | Redis, Memcached, ElastiCache |
| **Grafos**     | Nodos y aristas  | Redes sociales, detección de fraudes      | Neo4j, JanusGraph, Neptune    |

---

## 5. Alternativas en la nube (AWS)

### 5.1 DynamoDB (NoSQL clave‑valor y documental)
- **Escalado automático** y latencias de un dígito (ms).  
- Integración con Lambda, API Gateway, etc.  
- **Caso de uso:** Gestión de perfiles de usuario en microservicios.

### 5.2 DocumentDB (Documental compatible con MongoDB)
- Documentos JSON, alta disponibilidad multi-AZ.  
- Parches y backups gestionados.  
- **Caso de uso:** Sistemas de contenido web con estructuras dinámicas.

### 5.3 Redshift (Data warehouse columnar)
- Petabytes de datos en clústeres, consultas analíticas rápidas.  
- Integración con Kinesis, Glue y herramientas BI.  
- **Caso de uso:** Análisis de logs y reportes corporativos.

### 5.4 Neptune (Grafos)
- Compatible con Gremlin y SPARQL.  
- Replicación multi‑AZ, cifrado en reposo y tránsito.  
- **Caso de uso:** Recomendaciones y detección de fraudes en redes sociales.

### 5.5 ElastiCache (Caché en memoria)
- Soporta Redis y Memcached.  
- Réplicas, escalado y alta disponibilidad.  
- **Caso de uso:** Aceleración de sesiones de usuario y datos de alta frecuencia.

---

## 6. Comparativa de servicios

| Servicio   | Modelo                    | Escalabilidad           | Uso principal                          | Beneficios destacados                            |
| ---------- | ------------------------- | ----------------------- | -------------------------------------- | ------------------------------------------------ |
| **DynamoDB**   | Clave‑valor / Document     | Horizontal automático   | Alta concurrencia                      | Bajas latencias, serverless, pago por solicitud |
| **DocumentDB** | Documental (JSON)          | Lectura y almacenamiento| Aplicaciones MongoDB‑compatible         | API MongoDB, gestión automática                 |
| **Redshift**   | Columnar (Data Warehouse)  | Clúster escalable       | BI y análisis de grandes volúmenes     | Consultas rápidas en petabytes                  |
| **Neptune**    | Grafos                     | Almacenamiento           | Redes y relaciones complejas           | Consultas de grafo eficientes                   |
| **ElastiCache**| En memoria (Redis/Memcached)| Clústeres               | Caché y sesiones                       | Latencia ultrabaja, acelera aplicaciones        |

---

## 7. Ejemplos de casos de uso

- **DynamoDB**: Sistema de pedidos en tienda online con millones de transacciones diarias.  
- **DocumentDB**: Portal de noticias con atributos de artículo cambiantes.  
- **Redshift**: Dashboards analíticos de logs de marketing.  
- **Neptune**: Motor de recomendación en red social corporativa.  
- **ElastiCache**: Almacenamiento de metadatos en aplicación de streaming de música.

---
