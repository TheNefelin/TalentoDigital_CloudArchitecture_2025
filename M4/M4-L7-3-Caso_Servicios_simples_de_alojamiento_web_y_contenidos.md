# 🧠 Caso: Servicios Simples de Alojamiento Web y Distribución de Contenidos en AWS

## 🏢 Situación Inicial
La empresa emergente **QuickMedia** desea lanzar rápidamente una página web para promocionar productos digitales. En el futuro, planean distribuir archivos estáticos y multimedia internacionalmente, por lo que requieren:

- Velocidad y confiabilidad global.
- Bajo costo.
- Fácil configuración en la nube.

## 🎯 Objetivo
Implementar una solución en la nube usando:
- **Amazon Lightsail** como hosting web.
- **Amazon CloudFront** como red de distribución de contenido (CDN).
- **AWS Free Tier** para mantener costos bajos.
- HTTPS para seguridad profesional.

---

## 📌 Rol del Especialista Cloud
### Tareas:
1. **Instancia en Amazon Lightsail**
   - Crear instancia (ej. WordPress o LAMP) para el sitio web.
2. **Almacenamiento de Contenido Estático**
   - Usar bucket S3 (Simple Storage Service) o almacenamiento local en la instancia.
3. **Integración con Amazon CloudFront (CDN)**
   - Distribuir contenido estático cacheado globalmente.

---

## 🛠 Instrucciones Técnicas

### 1. Creación del Hosting Web
- Accede a tu cuenta de **AWS Academy** o **AWS Free Tier**.
- En **Amazon Lightsail**, crea una instancia básica con stack preconfigurado (WordPress o LAMP).
- Configura un dominio:
  - Con **Amazon Route 53** o un proveedor externo.
  - Agrega registros DNS que apunten a la IP estática de Lightsail.

### 2. Seguridad y Certificados
- Abre puertos en el firewall de Lightsail:
  - HTTP (puerto 80)
  - HTTPS (puerto 443)
- Usa **AWS Certificate Manager (ACM)** o el sistema de certificados de Lightsail para habilitar SSL/TLS (HTTPS).

### 3. Distribución de Contenidos con CloudFront
- Crea una **CloudFront Distribution** con origen:
  - Tu instancia de Lightsail o un bucket S3.
- Configura el **cache behavior**:
  - Para servir imágenes,

### Modelo

```mermaid
graph TD
    Route53[Amazon Route 53 (DNS)]
    CloudFront[Amazon CloudFront (CDN)]
    Lightsail[Amazon Lightsail (Web Hosting)]
    Cert[AWS Certificate Manager (SSL/TLS)]
    Firewall[Security Group (HTTP/HTTPS)]

    Route53 -->|CNAME / Alias| CloudFront
    CloudFront -->|Origin Request| Lightsail
    CloudFront -->|SSL/TLS| Cert
    Lightsail -->|Allow 80 / 443| Firewall
```

---

# Desarrollo

<img src="..\Img\M4\L7\Caso\M4-L7-Caso-01.png">
<img src="..\Img\M4\L7\Caso\M4-L7-Caso-02.png">
<img src="..\Img\M4\L7\Caso\M4-L7-Caso-03.png">
<img src="..\Img\M4\L7\Caso\M4-L7-Caso-04.png">
<img src="..\Img\M4\L7\Caso\M4-L7-Caso-05.png">
