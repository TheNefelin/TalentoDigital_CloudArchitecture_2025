# 📘 Diseño Inicial de Arquitectura – Proyecto "BarCraft Pedidos Web"

## 1. Resumen del Proyecto
"BarCraft" es una aplicación web que permite a los clientes del bar realizar pedidos de cerveza artesanal desde sus teléfonos móviles. Al mismo tiempo, el personal del bar (cajeros o garzones) puede gestionar los pedidos desde una interfaz interna.

## 2. Alcance
- Módulo de cliente: visualización del menú, selección de productos, envío de pedidos.
- Módulo interno: gestión de pedidos entrantes, estado del pedido, control de stock básico.
- Despliegue inicial en entorno AWS (cloud pública).
- Sin integración con sistemas de pago en esta primera etapa.

## 3. Requisitos
### 3.1 Requisitos funcionales
- [x] Listado de productos (cervezas, snacks)
- [x] Envío de pedidos por parte del cliente
- [x] Gestión de estado del pedido (pendiente, en preparación, entregado)
- [x] Acceso diferenciado (cliente vs. personal del bar)

### 3.2 Requisitos no funcionales
- Alta disponibilidad mínima (99.5%)
- Escalabilidad automática en caso de eventos especiales
- Seguridad básica con autenticación para el módulo de gestión
- Tiempo de carga aceptable (< 2s en dispositivos móviles)

## 4. Arquitectura Propuesta
### 4.1 Descripción general
La aplicación está compuesta por un frontend web estático para los clientes, y un backend serverless para manejar pedidos. El módulo de gestión accede a las mismas APIs, pero con autenticación y roles diferenciados.

### 4.2 Diagrama de arquitectura
```mermaid
graph TD
  U[🧑 Usuario] --> CDN[🌐 CDN (CloudFront)]
  CDN --> FE[💻 Frontend (React/Next.js)]
  FE --> AG[🔀 API Gateway]

  AG --> MSU[👤 Microservicio: Usuarios]
  AG --> MSP[📦 Microservicio: Productos]
  AG --> MSPay[💳 Microservicio: Pagos]

  MSU --> DB1[(🗄️ Azure SQL)]
  MSP --> DB2[(🌌 Cosmos DB)]
  MSPay --> Stripe[🔐 Stripe (Pasarela de Pagos)]

  AG --> Redis[(⚡ Redis Cache)]
  AG --> Monitor[📈 Azure Monitor]
```

### 4.3 Componentes principales
| Componente         | Servicio AWS             | Descripción                            |
|--------------------|--------------------------|----------------------------------------|
| Frontend cliente   | S3 + CloudFront          | Sitio estático accesible públicamente  |
| Backend API        | API Gateway + Lambda     | Lógica para pedidos y gestión interna  |
| Base de datos      | Amazon DynamoDB          | Almacén NoSQL para pedidos y productos |
| Autenticación      | Amazon Cognito           | Registro/login para gestión interna    |
| Notificaciones     | Amazon SNS (opcional)    | Avisos internos de nuevos pedidos      |
| Métricas           | Amazon CloudWatch        | Logs y monitoreo de uso                |

## 5. Seguridad
- IAM con permisos mínimos para funciones Lambda
- Uso de HTTPS para todo el tráfico
- Acceso autenticado mediante Cognito para módulo interno
- CloudFront con políticas de acceso restringido

## 6. Networking
- Arquitectura sin servidores expuestos (serverless)
- Todas las funciones ejecutan en subred privada
- API Gateway como única entrada pública

## 7. Escalabilidad y Alta Disponibilidad
- Lambda y DynamoDB escalan automáticamente
- CloudFront acelera el sitio estático globalmente
- Arquitectura sin punto único de fallo

## 8. Backup y Recuperación
- DynamoDB con backups automáticos habilitados
- CloudWatch Logs para auditoría básica
- Recuperación simple en base a exportaciones

## 9. Costeo Estimado
| Servicio           | Costo estimado mensual |
|--------------------|------------------------|
| S3 + CloudFront    | $5                     |
| Lambda             | $2 (uso bajo)          |
| DynamoDB           | $10                    |
| Cognito            | $0 (primeros usuarios) |
| Total estimado     | ~$17                   |

## 10. Riesgos Identificados
| Riesgo                      | Impacto | Mitigación                          |
|----------------------------|---------|-------------------------------------|
| Picos inesperados de uso   | Medio   | Escalado automático con Lambda/SNS  |
| Perdida de conectividad    | Bajo    | Modo offline no requerido ahora     |
| Errores en control de stock| Medio   | Validaciones simples por ahora      |

## 11. Anexos
- [AWS Serverless Application Model (SAM)](https://docs.aws.amazon.com/serverless-application-model/)
- [Diseño de referencia: Web App Serverless AWS](https://aws.amazon.com/architecture/serverless-web-app/)
- Lista de prioridades para iteración 2: pagos online, stock dinámico por producto

