# Resumen: Principios de Seguridad en la Nube

## Introducción
La adopción de la nube ofrece flexibilidad, escalabilidad y eficiencia, pero introduce nuevos desafíos de seguridad. Este manual aborda los principios básicos, amenazas y buenas prácticas para proteger los activos en entornos cloud.

---

## 1. Conceptos Básicos

### 1.1 Desafío de la Seguridad en la Nube
- **Pérdida de control directo**: al usar servicios de terceros, el control sobre la infraestructura disminuye.  
- **Responsabilidad compartida**: el proveedor asegura la infraestructura, el cliente gestiona configuraciones y datos.  
- **Entornos multi-tenant**: varios clientes comparten recursos físicos, aumentando riesgos si no hay aislamiento adecuado.

### 1.2 Comparación On-Premise vs Nube
| Aspecto | On-Premise | Nube |
|---------|------------|------|
| Propiedad | Organización | Proveedor |
| Responsabilidad | Total | Compartida |
| Escalabilidad | Limitada | Ilimitada |
| Costos | Altos CAPEX | Pago por uso (OPEX) |
| Seguridad física | Control local | Delegada al proveedor |

### 1.3 Principios Fundamentales
1. **Responsabilidad compartida**.  
2. **Mínimo privilegio** (least privilege).  
3. **Cifrado de datos** en tránsito y en reposo.  
4. **Seguridad por diseño** desde el inicio de proyectos.  
5. **Monitoreo y alertas** continuas.

---

## 2. Principales Amenazas y Riesgos
1. **Acceso no autorizado** → robo o manipulación de datos.  
2. **Fuga de datos sensibles** → por configuraciones inseguras.  
3. **DoS/DDoS** → afectan disponibilidad y aumentan costos.  
4. **Inyección de código malicioso** → SQLi, XSS, serverless injection.  
5. **Suplantación de identidad** → phishing, keyloggers.  
6. **Ataques de fuerza bruta** → contraseñas débiles.  
7. **Vulnerabilidades de red** → firewalls mal configurados, protocolos inseguros.  
8. **Configuraciones erróneas** → principal causa de incidentes.  
9. **Incumplimiento normativo** → sanciones legales.  
10. **Falta de parches** → deja expuestas vulnerabilidades conocidas.

---

## 3. Buenas Prácticas y Recomendaciones
1. **Modelo de responsabilidad compartida** claro.  
2. **Gestión de identidades (IAM)** y MFA.  
3. **Cifrado en tránsito y reposo** (TLS, KMS).  
4. **Monitoreo y alertas** con herramientas cloud nativas y SIEM.  
5. **Automatización de seguridad** con IaC.  
6. **Plan de respuesta a incidentes** probado regularmente.  
7. **Pruebas y validaciones continuas** (pentesting, escaneo).  
8. **Cumplimiento normativo y certificaciones** (ISO, PCI DSS).  
9. **Gestión de parches y actualizaciones** regulares.

---

## Conclusión
La seguridad en la nube se basa en responsabilidad compartida, buenas prácticas y medidas preventivas. Con una estrategia integral, se pueden aprovechar los beneficios del cloud sin comprometer la seguridad.

---

## Referencias
- Cloud Security Alliance (2017). *Security Guidance v4*.  
- ISO/IEC 27017:2015.  
- NIST SP 800-144.  
- OWASP Cloud Security Project.
