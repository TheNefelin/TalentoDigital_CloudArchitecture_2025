# 📘 Resumen del Manual: API Gateway

## 🌐 Introducción

En arquitecturas distribuidas y *serverless*, las **APIs** son el
mecanismo principal de comunicación.\
**Amazon API Gateway** es un servicio gestionado que permite crear,
publicar, mantener, monitorear y proteger APIs a cualquier escala.\
Se integra con **AWS Lambda, EC2 y otros servicios cloud**, abstrae la
infraestructura y facilita la seguridad.

------------------------------------------------------------------------

## 🎯 Aprendizaje esperado

-   Diseñar e implementar una **API segura y escalable** usando Amazon
    API Gateway.\
-   Aplicar buenas prácticas de seguridad, monitoreo y despliegue en
    entornos serverless.

------------------------------------------------------------------------

## 📄 Conceptos fundamentales de diseño de APIs

-   **API** = contrato de interacción entre software (generalmente vía
    HTTP/HTTPS).\
-   **Elementos clave**:
    -   Recurso → entidad expuesta (`orders`, `users`).\
    -   URI → identificador (`/orders/123`).\
    -   Verbo → acción (GET, POST, PUT, DELETE, PATCH).\
    -   Representación → formato (JSON, XML).\
    -   Estado de solicitud → código HTTP (200, 400, 500).

**Principios de diseño:** - Consistencia en URIs y verbos.\
- Versionado explícito (`/v1/`).\
- Uso adecuado de códigos HTTP.\
- Documentación clara (OpenAPI / Swagger).\
- Seguridad desde el diseño (auth, validación).

------------------------------------------------------------------------

## ☁️ Amazon API Gateway

-   Servicio que recibe peticiones, aplica seguridad y enruta a backends
    (Lambda, EC2, HTTP externos).

**Funciones principales:** - **Seguridad**: IAM, Cognito, JWT, API Keys,
WAF.\
- **Rendimiento**: caché, compresión GZIP, throttling.\
- **Operación**: métricas, stages, despliegue canario.\
- **Monetización**: planes de uso, cuotas.\
- **Protocolos**: REST, HTTP, WebSocket.

**Casos de uso comunes:** - Backend para apps móviles/web.\
- Pasarela unificada para microservicios.\
- Exposición segura de Lambdas.\
- WebSockets (chat en tiempo real).\
- APIs monetizadas.

------------------------------------------------------------------------

## 🔧 Implementación de API Gateway

### Integración con servicios cloud

-   **Lambda Proxy** → pasa petición completa a Lambda.\
-   **Lambda Non‑Proxy** → mapeo explícito.\
-   **EC2 Integration** → API Gateway como *reverse proxy*.

### Ejemplo paso a paso (Lambda)

1.  Crear función Lambda GET `/hello`.\
2.  En API Gateway → crear API REST → recurso `/hello` → método GET.\
3.  Seleccionar Lambda Proxy Integration.\
4.  Deploy en *stage* `dev` y probar.

### Autenticación y autorización

-   **IAM Roles**: acceso interno (firma SigV4).\
-   **Cognito/JWT**: usuarios finales, soporta OAuth2.\
-   **Lambda Authorizer**: lógica personalizada (RBAC/ABAC).\
-   **API Keys + Usage Plans**: monetización y control de cuota.

### Políticas de seguridad

-   AWS WAF contra ataques comunes.\
-   TLS 1.2+ y certificados ACM.\
-   Throttling y cuotas para mitigar DDoS.\
-   Validación de parámetros y cuerpos.

------------------------------------------------------------------------

## ⚙️ Operación de API Gateway

### Estrategias de despliegue

-   **Stages**: dev, test, prod.\
-   **Canarios** y **blue/green**.\
-   **Rollback automático** con métricas.\
-   Infraestructura como código (SAM, CDK, CloudFormation, Serverless
    Framework).

### Monitorización y logs

-   **Métricas**: 4XX/5XX Errors, Latency, Count (CloudWatch).\
-   **Lambda backend**: duración, invocaciones, errores (CloudWatch +
    X‑Ray).\
-   **Logs detallados**: requests/responses en CloudWatch Logs.\
-   **Tracing**: latencia end‑to‑end con AWS X‑Ray.

**Buenas prácticas:** - Alertas en 5XX y latencia p99.\
- Dashboards en CloudWatch/Grafana.\
- Logging en S3 para auditoría.

------------------------------------------------------------------------

## ✅ Conclusión

Amazon API Gateway permite diseñar, implementar y operar **APIs seguras
y escalables**, aplicando seguridad, monitoreo y despliegues
automatizados.\
Es clave en arquitecturas serverless modernas.

------------------------------------------------------------------------

## 📚 Referencias

-   [AWS API Gateway Developer
    Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)\
-   [Best Practices for REST
    APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-rest-api-best-practices.html)\
-   [Using API Gateway with AWS
    Lambda](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-invoke-lambda-function.html)\
-   [Fielding, R. T. -- REST
    Dissertation](https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm)\
-   [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
