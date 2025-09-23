# Resumen: Seguridad de Aplicativo en la Nube

## Introducción
En la nube, la **seguridad de las aplicaciones** abarca identidad, accesos, arquitectura resiliente y servicios gestionados contra amenazas externas.  
Este manual presenta prácticas para administrar accesos, aplicar autenticación y autorización, y usar servicios como **AWS IAM, Shield, WAF y CloudFront** para proteger aplicaciones.

---

## 1. Administración de Accesos e Identidad
- **IAM (Identity and Access Management):** gestiona identidades y permisos.  
- **Cuentas y Roles:** asignación de permisos específicos.  
- **Principio de menor privilegio:** solo los accesos necesarios.  
- **Buenas prácticas:** segregar ambientes (dev/test/prod).

### Autenticación y Autorización
- **Autenticación:** verifica identidad (contraseña, MFA, federación).  
- **Autorización:** define qué acciones están permitidas.  
- **Credenciales temporales:** con AWS STS.  
- **MFA:** esencial para seguridad adicional.

### Single Sign-On (SSO)
- **AWS SSO:** unifica acceso a múltiples cuentas/apps.  
- **Federación:** integración con AD, Okta u otros proveedores.  
- **Ventaja:** menos credenciales duplicadas y mayor trazabilidad.

---

## 2. Seguridad en el Diseño de Aplicaciones
1. **Capa de transporte y cifrado**  
   - HTTPS/TLS obligatorio.  
   - Certificados con ACM.  

2. **Microservicios y contenedores**  
   - Seguridad en cada servicio.  
   - Escaneo de imágenes (ECR Image Scanning).  

3. **Observabilidad y monitoreo**  
   - Logs centralizados en CloudWatch.  
   - Integración con SIEM externos.  

4. **Ciclo de desarrollo seguro**  
   - Pruebas de penetración periódicas.  
   - Escaneo estático/dinámico de código (SAST/DAST).  
   - Integración de seguridad en CI/CD.

---

## 3. Servicios de Seguridad Gestionados

### AWS Shield
- **Protección contra DDoS.**  
- **Tipos:**  
  - *Shield Standard:* automático y gratuito en servicios AWS.  
  - *Shield Advanced:* protección avanzada + soporte DRT.  
- **Configuración:** habilitar Shield Advanced en cargas críticas y combinarlo con WAF.

### AWS WAF (Web Application Firewall)
- **Protección contra amenazas web.**  
- **Reglas:**  
  - Administradas (SQLi, XSS).  
  - Personalizadas (IPs, headers, patrones).  
- **Integración:** con CloudFront o ALB para inspección de tráfico.  
- **Uso de rate-based rules** para detectar abuso.

### Arquitectura combinada Shield + WAF
- **CloudFront:** bloquea ataques en el edge.  
- **Load Balancers:** reglas a nivel de aplicación.  
- Protege contra ataques capa 3/4 (red/transporte) y capa 7 (aplicación).

---

## 4. Uso de CloudFront para Seguridad de Contenidos
- **DDoS protection** integrada por infraestructura distribuida.  
- **Restricciones de acceso:** geolocalización, URLs/cookies firmadas.  
- **Integración con WAF** para reglas personalizadas.  

**Casos de uso:**  
- Aplicaciones web globales con baja latencia y filtrado de tráfico.  
- Portales de e-commerce con caché y seguridad avanzada.  
- Distribución de contenido multimedia seguro.

---

## 5. Ejemplos y Casos de Uso

### Portal de e-learning
- Roles diferenciados para administradores e instructores.  
- WAF bloquea inyecciones SQL.  
- Shield Advanced + CloudFront para proteger contenido.

### Aplicación de comercio electrónico
- IAM + SSO unifican acceso.  
- WAF con reglas contra XSS y scraping.  
- CloudFront acelera distribución global.

### Portal corporativo interno
- Federación con Active Directory.  
- Shield Standard protege accesos internos.  
- Optimización de costos con configuraciones simples de WAF.

---

## Conclusión
La seguridad de aplicativos en la nube requiere:  
- Gestión de accesos robusta (IAM, MFA, SSO).  
- Arquitecturas resilientes con cifrado, monitoreo y ciclo seguro de desarrollo.  
- Servicios gestionados (Shield, WAF, CloudFront) que ofrecen protección continua frente a ataques.  

---

## Referencias
- [AWS IAM](https://docs.aws.amazon.com/iam/)  
- [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html)  
- [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/)  
- [AWS SSO](https://docs.aws.amazon.com/singlesignon/latest/userguide/)  
- [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/)  
