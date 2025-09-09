
# 📚 Manual Resumido: Implementación de Persistencia Serverless

## Introducción
La persistencia de datos es esencial en la nube. En arquitecturas *serverless*, AWS ofrece servicios gestionados que eliminan la administración de servidores y escalan automáticamente según la demanda.

Este módulo se centra en dos pilares:
- **Amazon S3** → Almacenamiento de objetos.
- **Amazon DynamoDB** → Base de datos NoSQL.

---

## 1. Servicios de persistencia sin servidor: visión general

| Categoría | Servicio | Tipo de datos | Modelo de cobro | Casos de uso |
|-----------|----------|---------------|-----------------|--------------|
| Almacenamiento de objetos | Amazon S3 | Archivos/blobs | GB‑mes + solicitudes | Backups, sitios estáticos, data lakes |
| Bases de datos NoSQL | Amazon DynamoDB | Clave‑valor, documentos | On‑Demand o aprovisionado | IoT, catálogos, sesiones, carritos |
| Bases de datos relacionales | Aurora Serverless v2 | SQL | ACU‑hora | Apps con picos irregulares |

---

## 2. Amazon S3 (almacenamiento de objetos)
### Casos de uso
- Archivos estáticos (imágenes, videos, documentos).
- Repositorios para Big Data y ML.
- Backup y recuperación.
- Artefactos de CI/CD.

### Configuración básica
1. Crear bucket con nombre DNS‑compatible.
2. Seleccionar clase de almacenamiento (Standard, IA, Glacier).
3. Habilitar **versionado**.
4. Definir **políticas de ciclo de vida**.
5. Activar **cifrado SSE-S3 o SSE-KMS**.

Recomendaciones: bloqueo de acceso público, logging, replicación multirregión.

### Uso en Lambda y EC2
- Lambda: usar *presigned URLs* para subir/descargar archivos grandes.
- EC2: montar S3 vía S3 FS o SDK (considerar costos de salida).

---

## 3. Amazon DynamoDB (base de datos NoSQL)
### Casos de uso
- Sesiones y carritos de compras.
- Telemetría IoT.
- Catálogos de productos.
- Sistemas de recomendaciones.

### Configuración básica
1. Seleccionar **modo de capacidad** (On-Demand o Provisioned).
2. Definir clave primaria.
3. Activar **cifrado y Point-In-Time Recovery**.
4. Usar índices secundarios (GSI, LSI).

### Modelo de datos
- Orientado a consultas, no a normalización.
- Tamaño máximo por ítem: 400 KB.
- Patrones: *single table design*, listas de adyacencia, series temporales.

### Escalabilidad y rendimiento
- Elegir claves de alta cardinalidad.
- Usar **DAX** para caché en memoria.
- **Global Tables** para replicación multi-región.

### Uso en Lambda y EC2
- Cliente fuera del handler en Lambda.
- En EC2: usar IAM Roles for EC2.

---

## 4. Políticas de acceso y seguridad
- Principio de menor privilegio.
- S3 OAC + CloudFront para objetos públicos seguros.
- VPC Endpoints para tráfico privado.
- Cifrado en tránsito y en reposo.

---

## 5. Estrategias de escalabilidad y rendimiento

| Estrategia | S3 | DynamoDB |
|------------|----|----------|
| Compresión | GZIP, Parquet | Datos binarios compactos |
| Particionado | Prefijos por fecha | Keys dispersas, sort keys de tiempo |
| Caching | CloudFront, Transfer Accel | DAX, caché en API Gateway |
| Monitoreo | Storage Lens, CloudWatch | CloudWatch, Contributor Insights |
| Concurrencia | Multipart Uploads | Adaptive Capacity |

---

## ✅ Conclusión
Has aprendido a usar **S3 y DynamoDB** como soluciones de persistencia serverless, configurarlas de forma segura y eficiente, e integrarlas con **Lambda y EC2** para aplicaciones escalables y resilientes.

---

## 📚 Referencias
- [Amazon DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Welcome.html)
- [Amazon S3 Developer Guide](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html)
- [Best Practices S3](https://docs.aws.amazon.com/whitepapers/latest/storage-design-patterns/overview.html)
- [NoSQL design for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-general-nosql-design.html)
- [Security Best Practices](https://aws.amazon.com/architecture/security-best-practices/)
