# 📘 Resumen del Manual: Sitios web simples con tecnología serverless en la nube

## 🌐 Introducción

El alojamiento de sitios web estáticos en la nube mediante servicios
serverless permite entregar contenido rápido, seguro y disponible sin
gestionar servidores.\
**Amazon S3** provee almacenamiento económico y duradero, mientras que
**CloudFront** actúa como CDN para reducir latencia y mejorar la
experiencia.

------------------------------------------------------------------------

## 🎯 Aprendizaje esperado

-   Implementar sitios web simples con tecnología serverless en la
    nube.\
-   Aplicar buenas prácticas de seguridad, escalabilidad y
    automatización.

------------------------------------------------------------------------

## 📄 Sitios web estáticos

Los sitios web estáticos usan archivos **HTML, CSS, JS e imágenes** sin
procesamiento en servidor.\
Son ideales para: - Páginas corporativas - Documentación - Blogs (Hugo,
Jekyll, Gatsby) - Landing pages

**Ventajas frente a sitios dinámicos:** - Simplicidad (sin backend) -
Escalabilidad sencilla - Costos bajos - Menor superficie de ataque

------------------------------------------------------------------------

## ☁️ Amazon S3

Pasos para alojar un sitio: 1. Crear bucket con nombre DNS-compatible.\
2. Habilitar *Static Website Hosting*.\
3. Subir archivos (index.html, error.html, assets/).\
4. Configurar permisos de acceso (recomendado: OAC).

------------------------------------------------------------------------

## 🌍 Amazon CloudFront (CDN)

Beneficios: - Menor latencia (edge locations cercanas)\
- Reducción de carga en el origen\
- Seguridad integrada (WAF, Shield, TLS)\
- Escalabilidad global

**Configuración básica:** 1. Crear distribución con S3 como origen\
2. Activar Origin Access Control (OAC)\
3. Configurar Default Root Object (index.html)\
4. Habilitar compresión y HTTP/2\
5. (Opcional) Asociar dominio + TLS con ACM

------------------------------------------------------------------------

## 🔗 Flujo de solicitud (S3 + CloudFront)

Usuario → DNS (Route 53) → CloudFront Edge → (cache hit?)\
- Sí → Respuesta\
- No → S3 → CloudFront → Respuesta + cache

------------------------------------------------------------------------

## ⚙️ Procedimiento completo

1.  Crear bucket en S3 y habilitar hosting estático\
2.  Subir archivos del sitio (CLI: `aws s3 sync`)\
3.  Crear distribución CloudFront\
4.  Configurar OAC y políticas IAM\
5.  Asociar dominio y certificado TLS\
6.  Automatizar despliegue con GitHub Actions o CodePipeline

------------------------------------------------------------------------

## 🔒 Seguridad y buenas prácticas

-   **OAC**: acceso seguro entre CloudFront y S3\
-   **Block Public Access** en S3 activado\
-   **AWS WAF** para mitigar ataques (SQLi, XSS, bots)\
-   **Versionado y lifecycle policies** en S3\
-   **Logs de acceso** en S3 y CloudFront

------------------------------------------------------------------------

## ✅ Conclusión

Este enfoque permite desplegar sitios web estáticos de forma **segura,
escalable y económica**, simplificando la operación y aplicando buenas
prácticas de la industria.

------------------------------------------------------------------------

## 📚 Referencias

-   [AWS CloudFront -- Getting
    Started](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.html)\
-   [Hosting a static website on Amazon
    S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html)\
-   [Using origin access
    control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)\
-   [Introduction to CDNs -- Google](https://web.dev/caching-cdn/)\
-   [Static site generators --
    Netlify](https://www.netlify.com/with/static-site-generators/)
