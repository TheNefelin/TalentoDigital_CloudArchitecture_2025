# Servicios de Notificación y Mensajería en la Nube

## Introducción
Los servicios de notificación y mensajería en la nube permiten la comunicación asíncrona entre aplicaciones distribuidas, garantizando escalabilidad y desacoplamiento. En este contexto se analizan **Amazon SNS** y **Amazon SQS**, dos servicios clave en AWS.

---

## 1. ¿Qué es un servicio de notificación y mensajería?

- **Envío/recepción de eventos:** Conecta sistemas desacoplados.
- **Asegura entrega:** Reintentos o almacenamiento temporal si el sistema está inactivo.
- **Escalabilidad:** Se adapta al crecimiento.
- **Desacoplamiento:** Los componentes interactúan vía mensajes.

### Importancia
- **Procesamiento asíncrono**
- **Notificaciones oportunas**
- **Fiabilidad ante fallos**

---

## 2. Amazon SNS (Simple Notification Service)

### 2.1 Modelo Publicador-Suscriptor (Pub/Sub)
- Un publicador envía mensajes a un *tópico*.
- Múltiples suscriptores reciben el mensaje mediante diferentes protocolos.

### 2.2 Tópicos y Suscripciones
- **Tópico:** Canal lógico de publicación.
- **Suscripción:** Define protocolo y destino (HTTP, SMS, email, Lambda, etc.)

### 2.3 Protocolos de entrega comunes
| Protocolo     | Uso típico                            |
|---------------|----------------------------------------|
| HTTP/S        | Webhooks, aplicaciones web             |
| Email         | Notificaciones por correo              |
| SMS           | Mensajes de texto                      |
| AWS Lambda    | Procesamiento serverless               |
| Amazon SQS    | Encadenamiento con colas de mensajes   |

### 2.4 Escalabilidad y Fiabilidad
- Alta capacidad de mensajes diarios.
- Políticas de reintento y reenvío.

### 2.5 Integración
Con CloudWatch, Lambda, S3, DynamoDB, etc. Automatiza flujos de trabajo.

### 2.6 Caso de uso
Notificaciones multicanal en e-commerce:
- **SMS:** Confirmación al cliente.
- **Email:** Notificación al equipo de ventas.
- **Lambda:** Actualiza registro histórico.

---

## 3. Amazon SQS (Simple Queue Service)

### 3.1 Modelo de colas
- **Productores** colocan mensajes en la cola.
- **Consumidores** extraen mensajes (pull).

### 3.2 Tipos de colas
- **Estándar:**
  - Alta disponibilidad y throughput.
  - Orden no garantizado.
- **FIFO:**
  - Orden garantizado y sin duplicados.
  - Menor rendimiento comparado con estándar.

### 3.3 Escalabilidad y durabilidad
- Procesamiento masivo.
- Almacenamiento replicado entre zonas de disponibilidad.
- Retención de mensajes: 1 min a 14 días.

### 3.4 Caso de uso
Procesamiento de imágenes por microservicios. Cada archivo genera un mensaje en SQS que se procesa de forma independiente.

---

## 4. Seguridad, Rendimiento y Costos

### 4.1 Seguridad
- Políticas de acceso y cifrado con AWS KMS.

### 4.2 Rendimiento
- **SNS:** Ideal para notificaciones en tiempo real.
- **SQS:** Depende del tipo de cola. Estándar > FIFO en rendimiento.

### 4.3 Costos
- Basado en número de peticiones y volumen de datos.
- Optimizar retención (SQS) y suscripciones (SNS).

---

## 5. Comparativa: SNS vs SQS

| Servicio | Patrón              | Entrega | Uso Principal                             | Orden       |
|----------|---------------------|---------|-------------------------------------------|-------------|
| SNS      | Publicador-Suscriptor | Push    | Notificaciones a múltiples destinos       | No garantizado |
| SQS Est. | Cola de mensajes     | Pull    | Procesamiento asíncrono masivo            | No garantizado |
| SQS FIFO | Cola de mensajes     | Pull    | Procesamiento ordenado (ej. transacciones) | Garantizado   |

---

## ¿Cuándo usar cada uno?

### Usar SNS:
- Para notificaciones en tiempo real a distintos canales.
- Cuando se requiere distribuir el mismo mensaje a varios destinos.

### Usar SQS:
- Para tareas pesadas en segundo plano.
- Cuando se necesita control de flujo y procesamiento desacoplado.

