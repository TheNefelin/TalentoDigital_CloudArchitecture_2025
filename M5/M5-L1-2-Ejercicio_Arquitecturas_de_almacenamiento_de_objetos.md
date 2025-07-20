# Ejercicio: Arquitecturas de Almacenamiento de Objetos  

## Desafío 1: Investigación de Arquitecturas en Grandes Plataformas  

### **Servicios y Casos de Uso**  
- **Amazon S3**:  
  - **Casos de uso**:  
    - Respaldo de datos (ej. copias de seguridad automatizadas).  
    - Distribución de contenido estático (imágenes, videos) integrado con CloudFront (CDN).  
    - Data lakes para análisis con Athena/Redshift.  
  - **Escalabilidad**: Escalado automático sin límite, replicación multi-región.  
  - **Acceso**: URLs públicas o firmadas (presigned URLs) con expiración.  

- **Azure Blob Storage**:  
  - **Casos de uso**:  
    - Archivado de datos (ej. Azure Archive Storage).  
    - Almacenamiento para aplicaciones SaaS (documentos, logs).  
    - Integración con Azure Synapse para Big Data.  
  - **Escalabilidad**: Niveles de acceso (hot/cool/archive) para optimizar costos.  
  - **Acceso**: URLs con SAS (Shared Access Signatures) para acceso temporal.  

- **Google Cloud Storage**:  
  - **Casos de uso**:  
    - Hosting de datasets para ML (ej. TensorFlow).  
    - Streaming de videos (integrado con CDN).  
  - **Escalabilidad**: Almacenamiento multi-regional con clases (Standard, Nearline, Coldline).  

### **Arquitectura Orientada a URL**  
- **Ejemplo**: Plataformas como Netflix usan URLs de S3 + CloudFront para entregar videos.  
  - **Proceso**:  
    1. Video almacenado en S3.  
    2. CloudFront distribuye el contenido desde edge locations.  
    3. URLs únicas por usuario (con firma temporal para seguridad).  

---

## Desafío 2: Cuadro Comparativo (Amazon S3 vs Azure Blob Storage)  

| **Característica**         | **Amazon S3**                          | **Azure Blob Storage**                |  
|----------------------------|----------------------------------------|----------------------------------------|  
| **Modelo de costos**       | Pago por GB/mes + solicitudes. Clases: Standard, Intelligent-Tiering, Glacier. | Pago por GB/mes + transacciones. Niveles: Hot, Cool, Archive. |  
| **Tipos de almacenamiento** | - S3 Standard (frecuente acceso). <br> - S3 Glacier (archivado). | - Hot (acceso frecuente). <br> - Cool (acceso esporádico). <br> - Archive (acceso raro). |  
| **Seguridad**              | - Cifrado AES-256. <br> - IAM + políticas de bucket. | - Cifrado SSE. <br> - RBAC + SAS. |  
| **Accesibilidad vía URL**  | URLs públicas o presigned (expiración configurable). | URLs con SAS (firmas temporales). |  
| **Casos de uso**           | - CDN + streaming. <br> - Data lakes. <br> - Backup. | - Aplicaciones empresariales. <br> - Archivado legal. <br> - IoT data. |  

---

## Resolución Adicional (Opcional)  

### **Ejemplo de Implementación en AWS**:  
1. **Caso**: Respaldo automatizado de una base de datos.  
   - **Servicios**:  
     - AWS Backup → S3 (Standard para acceso rápido, Glacier para históricos).  
   - **URLs**: Generación de enlaces temporales para restaurar archivos.  

2. **Caso**: Distribución de imágenes en una app móvil.  
   - **Servicios**:  
     - S3 + CloudFront (CDN) + Lambda@Edge para optimización.  
   - **URLs**: Presigned URLs con validez de 1 hora.  

---

## Recursos Utilizados  
- [Amazon S3](https://aws.amazon.com/es/s3/)  
- [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/)  
