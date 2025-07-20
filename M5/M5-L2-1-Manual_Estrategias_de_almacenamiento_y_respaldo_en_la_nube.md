# Resumen Manual: Estrategias de Almacenamiento y Respaldo en la Nube  

## **1. Almacenamiento On-Premise vs. Cloud**  
| **On-Premise** | **Cloud** |  
|----------------|----------|  
| Control total sobre infraestructura física. | Infraestructura gestionada por proveedor (AWS, Azure, GCP). |  
| Altos costos iniciales y de mantenimiento. | Pago por uso, escalabilidad bajo demanda. |  
| Escalabilidad limitada. | Replicación geográfica y alta disponibilidad. |  

**Híbrido**: Combina lo mejor de ambos (ej: datos críticos on-premise + archivos históricos en cloud).  

---

## **2. Estrategias de Almacenamiento en Cloud**  
- **Nube pública**: AWS S3, Azure Blob. Ideal para datos no sensibles y escalabilidad.  
- **Nube privada**: Para datos regulados (ej: salud, finanzas).  
- **Multi-cloud**: Evita dependencia de un solo proveedor.  
- **Tiered Storage**:  
  - **Hot**: Acceso frecuente (ej: bases de datos).  
  - **Cold**: Archivado económico (ej: Amazon Glacier).  

---

## **3. Beneficios y Costos**  
- **Beneficios**:  
  - Escalabilidad ilimitada.  
  - Acceso global.  
  - Reducción de mantenimiento.  
  - Redundancia y recuperación ante desastres.  
- **Costos**:  
  - Modelo "pay-as-you-go".  
  - Optimizable con políticas de ciclo de vida.  

---

## **4. Casos de Uso Clave**  
### **Migración al Cloud**  
- **Proceso**: Evaluación → Selección de herramientas (AWS DataSync) → Migración por fases.  
- **Ejemplo**: Bancos migrando data warehouses a S3 para reducir costos.  

### **Respaldo Híbrido**  
- **Arquitectura**:  
  - Copias locales para recuperación rápida.  
  - Réplicas en cloud (S3, Azure Blob) para redundancia.  
- **Herramientas**: Veeam, AWS Backup.  

### **VPC Híbrida**  
- **Uso**: Conectar servidores on-premise con cloud (AWS Direct Connect).  
- **Ejemplo**: Logs locales analizados en Athena (S3) + ML en la nube.  

---

## **5. Seguridad y Cumplimiento**  
- **Cifrado**: AES-256 en tránsito/reposo.  
- **Control de Acceso**: IAM + MFA.  
- **Auditoría**: Logs con AWS CloudTrail.  
- **Normativas**: GDPR, HIPAA, ISO 27001.  

---

## **6. Checklist para Implementación**  
1. **Diagnóstico**: Identificar datos críticos vs. archivables.  
2. **Proveedor**: Elegir según costos, ubicación y servicios.  
3. **Estructura**: Definir buckets (públicos/privados) y políticas de acceso.  
4. **Respaldo**: Automatizar con herramientas híbridas.  
5. **Monitorización**: Alertas y logs centralizados.  

---

## **Diagrama de Arquitectura Híbrida**  
```plaintext
┌──────────────────────┐    ┌──────────────────────┐
│   Data Center On-    │    │       AWS/Azure       │
│      Premise         │    │                      │
│ ┌──────────────────┐ │    │ ┌──────────────────┐ │
│ │  Servidores Locales│◄───►│ │  Buckets S3/Blob │ │
│ │  (Datos Críticos) │ │    │ │  (Cold Storage)  │ │
│ └──────────────────┘ │    │ └──────────────────┘ │
└──────────┬───────────┘    └──────────┬───────────┘
           │                           │
           ▼                           ▼
┌──────────────────────┐    ┌──────────────────────┐
│     VPN/Direct       │    │     Herramientas      │
│      Connect         │    │     de Análisis       │
└──────────────────────┘    └──────────────────────┘
```

```mermaid
graph TD
    subgraph On-Premise
        A[Servidores Locales<br>(Datos Críticos)] -->|VPN/Direct Connect| B
        A -->|Respaldos Diarios| C
    end

    subgraph Cloud[AWS/Azure/GCP]
        B[Buckets S3/Blob Storage<br>(Cold Storage)]
        C[Herramientas de Análisis<br>(Athena, BigQuery)]
        D[CDN<br>(CloudFront/Azure CDN)]
    end

    A -->|Datos Históricos| B
    B -->|Procesamiento| C
    B -->|Distribución| D

    style A fill:#f9f,stroke:#333
    style B fill:#9f9,stroke:#333
    style C fill:#99f,stroke:#333
    style D fill:#ff9,stroke:#333
```