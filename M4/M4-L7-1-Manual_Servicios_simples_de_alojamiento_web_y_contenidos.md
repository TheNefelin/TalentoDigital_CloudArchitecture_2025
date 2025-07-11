# Servicios Simples de Alojamiento Web y Contenidos (AWS)

## 📘 Fundamentos de Tecnología Cloud
**Objetivo:** Comparar servicios de alojamiento web y entrega de contenidos estáticos en la nube para resolver necesidades organizacionales.

---

## 🖥️ 1. Amazon Lightsail – Alojamiento Web Simple

### ¿Qué es?
Servicio de hosting sencillo que ofrece instancias (VMs), almacenamiento y redes en paquetes preconfigurados.

### ✅ Ventajas
- **Fácil de usar**: Plantillas para WordPress, LAMP, etc.
- **Costo fijo mensual**: CPU, RAM y almacenamiento incluidos.
- **Panel intuitivo**: Gestión de instancias, DNS, IP, backups.
- **Integración básica con AWS**: Compatible con S3, Route 53, CloudFront.

### ❌ Desventajas
- Poca flexibilidad para configuraciones avanzadas.
- Menos escalabilidad comparado con EC2 o ECS/EKS.
- Integraciones avanzadas requieren salir de Lightsail.

### 💡 Casos de Uso
- Blogs y tiendas online pequeñas/medianas.
- MVPs (Producto Mínimo Viable).
- Ambientes de desarrollo/pruebas rápidos.

> **Ejemplo**: Startup lanza sitio corporativo usando WordPress en Lightsail.

---

## 🌐 2. Amazon CloudFront – CDN (Content Delivery Network)

### ¿Qué es una CDN?
Red global de servidores que cachea y entrega contenido estático/dinámico desde el punto geográfico más cercano al usuario.

### 🚀 Beneficios
- **Menor latencia**
- **Descongestión del servidor origen**
- **Alta escalabilidad global**
- **Seguridad integrada**: HTTPS/TLS, AWS Shield (protección DDoS)

### 📂 Contenido Ideal para Distribuir
- Imágenes, CSS, JavaScript
- Videos, audios
- PDFs, software, archivos estáticos

### 🛡️ Seguridad
- **HTTPS/TLS**: Evita ataques tipo Man-In-The-Middle.
- **AWS Shield**: Protección DDoS automática.

### 💲 Costos
- Dependen de: 
  - Volumen de datos transferidos
  - Cantidad de requests
  - Ubicación geográfica (Edge Locations)
- **Optimización**: TTL de caché, invalidaciones, balance regional.

### 💡 Casos de Uso
- Front-end estático servido desde CloudFront
- Back-end en Lightsail, EC2 o contenedores
> **Ejemplo**: Plataforma e-learning distribuye recursos multimedia globalmente con CloudFront, lógica en otro servicio.

---

## 🔍 3. Comparativa Lightsail vs. CloudFront

| Servicio     | Funcionalidad Principal                              | Aplicación Típica                      | Costos                            |
|--------------|-------------------------------------------------------|----------------------------------------|------------------------------------|
| **Lightsail** | Hosting “todo en uno” (servidor + red + almacenamiento) | Sitios simples, apps ligeras           | Fijo mensual según plan            |
| **CloudFront**| CDN global (entrega de contenido en Edge Locations)   | Contenido estático/media distribuido   | Por GB transferido y cantidad de requests |

### 🔗 Integración Recomendada
**Lightsail + CloudFront**:
- Backend en Lightsail
- Archivos estáticos servidos globalmente desde CloudFront
- Reduce latencia y mejora seguridad ante picos de tráfico

---

## ✅ 4. Recomendaciones Finales

1. **Tamaño y complejidad**:
   - Lightsail: Ideal para soluciones simples.
   - CloudFront: Esencial si hay tráfico global o uso intensivo de archivos estáticos.

2. **Tráfico y ancho de banda**:
   - CDN se vuelve más relevante con más transferencia de datos.
   - Lightsail incluye límites, se cobra extra al superarlos.

3. **Seguridad**:
   - Lightsail: Certificados SSL/TLS y firewall básico.
   - CloudFront: HTTPS, AWS Shield, geo-restricción.

4. **Escalabilidad**:
   - Lightsail escala verticalmente.
   - Para crecimiento mayor → considerar EC2 o contenedores (ECS/EKS).

---

## 🧾 Glosario de siglas
- **CDN**: Content Delivery Network (Red de Entrega de Contenido)
- **MVP**: Minimum Viable Product (Producto Mínimo Viable)
- **EC2**: Elastic Compute Cloud (Máquinas virtuales de AWS)
- **S3**: Simple Storage Service (Almacenamiento de objetos)
- **ECS/EKS**: Elastic Container Service / Elastic Kubernetes Service
- **DNS**: Domain Name System
- **DDoS**: Distributed Denial of Service (Ataque de Denegación de Servicio Distribuido)
- **TLS/SSL**: Transport Layer Security / Secure Sockets Layer

