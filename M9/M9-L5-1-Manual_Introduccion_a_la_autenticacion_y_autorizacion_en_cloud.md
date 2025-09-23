# Resumen: Introducción a la Autenticación y Autorización en Cloud

## Introducción
La **autenticación (authN)** y la **autorización (authZ)** son la primera línea de defensa en aplicaciones cloud.  
- **AuthN:** verifica *quién eres*.  
- **AuthZ:** determina *qué puedes hacer*.  

En entornos cloud la correcta gestión de identidades es crítica. **Amazon Cognito** simplifica la creación de flujos de inicio de sesión, federación de usuarios externos y generación de credenciales temporales de AWS.

---

## 1. Conceptos básicos
| Concepto | ¿Qué verifica? | Pregunta | Ejemplo |
|----------|----------------|----------|---------|
| **Autenticación** | Identidad del usuario | ¿Quién eres? | Login con correo y contraseña |
| **Autorización** | Permisos del usuario | ¿Qué puedes hacer? | Acceso de solo lectura a un bucket S3 |

**Importancia:**  
- Evitar accesos no autorizados y fugas de datos.  
- Aplicar principio de menor privilegio y facilitar auditorías.  

---

## 2. Gestión de identidades en apps web y móviles
- **Flujos web tradicionales:** cookies + sesiones.  
- **SPAs/móviles:** tokens JWT (OAuth 2.0 / OpenID Connect).  
- **Desafíos comunes:** rotación de tokens, sincronización en múltiples dispositivos, escalabilidad global sin estado.  

---

## 3. Autenticación y autorización con Amazon Cognito

### 3.1 Arquitectura general
- **User Pools:** directorio de usuarios, login, MFA, soporte OAuth 2.0 / OIDC.  
- **Identity Pools (Federated Identities):** intercambian tokens por credenciales temporales de AWS (STS).  

| Característica | User Pool | Identity Pool |
|----------------|-----------|---------------|
| Almacena usuarios | ✔ | — |
| OAuth 2.0 / OIDC | ✔ | — |
| Genera credenciales AWS | — | ✔ |
| Políticas IAM basadas en roles | — | ✔ |

### 3.2 Crear un Identity Pool
1. Cognito → Federated Identities → Create Identity Pool.  
2. Activar autenticación anónima (opcional).  
3. Asociar User Pool o IdP externo.  
4. Cognito crea roles IAM *Authenticated* y *Unauthenticated*.  
5. Ajustar políticas con **principio de menor privilegio**.  

### 3.3 Conexión con IdP externos
- **Social:** Google, Facebook, Apple.  
- **Corporativo (SAML/OIDC):** Azure AD, Okta, ADFS.  
- Pasos: registrar app en IdP → configurar en User Pool → definir callback/logout URLs.  

### 3.4 Ejemplo con Google
- Crear credenciales en Google Cloud Console.  
- Copiar Client ID/Secret en Cognito User Pool.  
- Usar Hosted UI o SDK Amplify.  

### 3.5 Roles y grupos
- Grupos en User Pool → asignar precedencia → mapear a roles IAM en Identity Pool.  
- Permite separar perfiles: admin, editor, viewer.  

---

## 4. Buenas prácticas
| Área | Recomendación | Beneficio |
|------|---------------|-----------|
| **MFA** | Activar MFA obligatorio (SMS/TOTP). | Protege contra robo de credenciales. |
| **Gestión de tokens** | Access token = 1h, Refresh = 30d. | Reduce ventana de compromiso. |
| **Rotación de secretos** | Usar AWS Secrets Manager + Lambda. | Cumplimiento y menor exposición. |
| **Políticas de acceso** | Permisos mínimos por rol. | Alineado a *least privilege*. |
| **Privacidad** | Enmascarar atributos sensibles, cifrar en tránsito y reposo. | Cumple GDPR/CCPA. |

---

## 5. Privacidad y cumplimiento
- No almacenar PII fuera de User Pools.  
- Auditar con **CloudTrail + Cognito Logs**.  
- Verificar región de almacenamiento de datos.  
- Usar *Advanced Security Features* de Cognito (detección de credenciales comprometidas).  

---

## Conclusión
Una implementación correcta de **authN y authZ** en cloud:  
- Mejora experiencia de usuario.  
- Protege activos contra accesos indebidos.  
- Facilita cumplimiento normativo.  

**Amazon Cognito** centraliza directorio de usuarios, federación y credenciales temporales, permitiendo a los equipos enfocarse en la lógica de negocio.

---

## Referencias
- [Amazon Cognito Developer Guide](https://docs.aws.amazon.com/cognito/latest/developerguide/)  
- [OAuth 2.0 RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749)  
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)  
- [AWS Amplify Auth](https://docs.amplify.aws/lib/auth/getting-started/q/platform/js/)  
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)  
