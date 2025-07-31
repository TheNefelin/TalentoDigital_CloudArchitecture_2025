# Manual: Disponibilidad de Contenidos de Aplicaciones en Cloud

## 📘 Introducción
La disponibilidad de contenidos en la nube es esencial para garantizar una experiencia fluida, rápida y segura. Este manual explora conceptos y arquitecturas que permiten escalar, proteger y distribuir contenido eficientemente en entornos cloud.

## 🎯 Aprendizaje Esperado
- Comprender disponibilidad de contenidos en la nube.
- Identificar y clasificar tipos de contenido sensible.
- Aplicar arquitecturas con EC2 Auto Scaling y ELB.
- Analizar el uso de CloudFront como CDN.
- Diseñar arquitecturas resilientes con EC2, ELB, CloudFront y Route 53.

---

## 🧱 Aplicaciones que entregan contenido
Son sistemas que distribuyen datos, imágenes, videos, etc. Requieren:
- Alta disponibilidad y baja latencia.
- Escalabilidad automática.
- Arquitecturas modulares y distribuidas.
- Mecanismos de caching y balanceo de carga.

Ejemplos: Netflix, YouTube, App Store, redes sociales, portales educativos.

---

## 🔐 Clasificación de Contenidos Sensibles
Tipos de contenido:
- Público
- Interno
- Confidencial
- Restringido

Buenas prácticas:
- Políticas de acceso y control.
- Encriptación en tránsito y en reposo.
- Uso de etiquetas y metadatos.
- Cumplimiento normativo (GDPR, leyes locales).
- Revisión continua y ajustes según el contexto.

---

## ⚙️ Arquitecturas con EC2 Auto Scaling y ELB
- **EC2 Auto Scaling**: Ajuste dinámico de instancias según demanda.
- **ELB**: Distribuye tráfico entre instancias disponibles.
- Alta tolerancia a fallos al usar múltiples zonas de disponibilidad.
- Escalado predictivo y reactivo.
- Implementación de despliegue continuo sin afectar disponibilidad.

---

## 🌐 CloudFront como CDN
- Red de distribución de contenido global (Edge Locations).
- Cacheo de contenido estático y dinámico.
- Reducción de latencia y carga sobre backend.
- Soporte para HTTPS, WAF, signed URLs/cookies.
- Personalización de caché e invalidación de contenido.

---

## 🧩 Arquitectura integrada con Route 53
Servicios integrados:
- **EC2 Auto Scaling**
- **ELB**
- **CloudFront**
- **Route 53**: Gestión DNS con routing geográfico, failover, etc.

Beneficios:
- Escalabilidad global.
- Reducción de latencia.
- Alta disponibilidad ante fallos zonales.
- Protección de contenido y balanceo eficiente.

---

## 🔗 Integración con Direct Connect
- **Direct Connect**: Canal privado y seguro entre on-premise y AWS.
- Arquitectura híbrida: VPC + subredes + Auto Scaling + ELB.
- Ideal para organizaciones con cargas críticas o reguladas.
- Optimización de costos por transferencia de datos.
- Requiere políticas claras de seguridad y monitoreo.

---

## 📝 Cierre
El diseño de arquitecturas resilientes en la nube es clave para garantizar la disponibilidad de contenidos. Con EC2 Auto Scaling, ELB, CloudFront, Route 53 y Direct Connect, se pueden crear soluciones robustas, seguras y eficientes para usuarios a nivel global.

---

## 📚 Referencias
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
- [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/)
- [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)
- [Amazon Route 53](https://aws.amazon.com/route53/)
- [AWS Direct Connect](https://aws.amazon.com/directconnect/)
- [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/)
