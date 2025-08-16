# 💼 Ejercicio de Aplicación #2: Implementación de una Arquitectura Monolítica

## 1. Desafío 🎯

### 📌 Sistemas de Mensajería en la Nube

Los **sistemas de mensajería en la nube** son servicios que permiten la
**comunicación asíncrona entre componentes de una aplicación**,
desacoplando procesos y mejorando la escalabilidad.\
Su importancia radica en que permiten manejar **grandes volúmenes de
datos**, garantizar la **entrega confiable de mensajes** y facilitar la
**integración de microservicios o aplicaciones monolíticas escalables**.

------------------------------------------------------------------------

### 📌 Amazon Simple Queue Service (SQS)

-   **Definición**: Servicio de colas gestionado por AWS para enviar,
    almacenar y recibir mensajes entre sistemas distribuidos.\
-   **Configuración básica**:
    1.  Crear una **cola SQS** desde la consola de AWS.\
    2.  Enviar mensajes a la cola utilizando la **SDK de AWS o la
        consola**.\
    3.  Recibir mensajes con consumidores que procesan y eliminan
        mensajes de la cola.\
    4.  Gestionar la cola configurando **políticas de acceso**,
        reintentos automáticos y **Dead Letter Queues (DLQ)** para
        mensajes fallidos.

------------------------------------------------------------------------

### 📌 Amazon Simple Notification Service (SNS)

-   **Definición**: Servicio de notificaciones que permite la
    **publicación y suscripción a mensajes** en tiempo real.\
-   **Configuración básica**:
    1.  Crear un **tema SNS** en la consola de AWS.\
    2.  Publicar mensajes en el tema mediante la consola o SDK.\
    3.  Suscribir **endpoints** (correo electrónico, SMS, colas SQS,
        funciones Lambda, etc.).\
    4.  Gestionar permisos de acceso mediante **políticas de control
        (IAM Policies)**.

------------------------------------------------------------------------

## 2. ¿Dónde se lleva a cabo? 👩‍💻

Este ejercicio se implementa en la plataforma **AWS Academy**, que
proporciona un entorno seguro para aprender y practicar con los
servicios de AWS.

------------------------------------------------------------------------

## 3. Tiempo de dedicación ⌛

⏱️ **Tiempo estimado:** 1 hora.

------------------------------------------------------------------------

## 4. Recursos 🛠

-   Manual: *Implementación de Servicios de Mensajería Cloud*\
-   Documentación oficial de AWS:
    -   [Amazon
        SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)\
    -   [Amazon
        SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)

------------------------------------------------------------------------

## 5. Plus ➕ Diagrama de Integración SQS + SNS

``` mermaid
flowchart TD
    A[Aplicación Monolítica] -->|Publica mensaje| B[SNS - Tema]
    B -->|Notificación| C[SQS - Cola 1]
    B -->|Notificación| D[SQS - Cola 2]
    C -->|Consumidor procesa mensajes| E[Servicio Interno 1]
    D -->|Consumidor procesa mensajes| F[Servicio Interno 2]
```

Este diagrama muestra cómo **SNS distribuye mensajes** a múltiples colas
SQS, que a su vez son consumidas por diferentes servicios dentro de una
arquitectura monolítica.

------------------------------------------------------------------------

✅ Con este ejercicio se cubren los conceptos fundamentales de
**mensajería en la nube** y su implementación práctica con **SQS y SNS**
en AWS.
