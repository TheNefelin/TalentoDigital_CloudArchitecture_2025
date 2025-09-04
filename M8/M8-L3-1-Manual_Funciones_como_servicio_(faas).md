# 📘 Resumen del Manual: Funciones como Servicio (FaaS)

## 🌐 Introducción

Las **Functions as a Service (FaaS)** son el núcleo del paradigma
*serverless*.\
Permiten ejecutar pequeños fragmentos de código en la nube sin gestionar
servidores.\
**AWS Lambda** lidera este modelo gracias a su integración con más de
200 servicios y facturación granular por milisegundo.

------------------------------------------------------------------------

## 🎯 Aprendizaje esperado

-   Implementar servicios basados en funciones en un entorno cloud.\
-   Aplicar buenas prácticas de arquitectura, seguridad y
    automatización.

------------------------------------------------------------------------

## 🔎 ¿Qué es FaaS?

-   Modelo de computación en el que se ejecutan **funciones de corta
    duración** en respuesta a **eventos**.\
-   Parte del ecosistema **serverless** (infraestructura abstraída).

**Diferencias clave con Serverless en general:** - FaaS = ejecución de
funciones.\
- Serverless = conjunto de servicios gestionados (BD, colas, APIs).\
- Escalado automático y facturación por uso.

------------------------------------------------------------------------

## ⚡ Características y beneficios

-   **Stateless** → facilita escalado y pruebas.\
-   **Arranque bajo demanda** → costos cero cuando no hay tráfico.\
-   **Granularidad funcional** → despliegues independientes.\
-   **Integración nativa de eventos** → sistemas reactivos.\
-   **Observabilidad integrada** → métricas, logs y trazas (CloudWatch).

Ejemplo: procesar imágenes en S3 solo cuando ocurre un evento
*ObjectCreated*.

------------------------------------------------------------------------

## 🏗️ Principios y buenas prácticas

1.  **Single Responsibility** → cada función resuelve una tarea
    específica.\
2.  **Stateless & Idempotent** → no depender de estado local.\
3.  **Cold Start Friendly** → minimizar dependencias, paquete \< 50MB.\
4.  **Observabilidad** → structured logging y tracing (AWS X-Ray).\
5.  **Seguridad Least Privilege** → políticas IAM mínimas.\
6.  **CI/CD** → automatización con SAM, CDK o Serverless Framework.

------------------------------------------------------------------------

## 📡 Arquitectura Event‑Driven (AWS Lambda)

Eventos soportados:\
- **HTTP** → API Gateway, ALB\
- **Almacenamiento** → S3, EFS\
- **Mensajería** → SQS, SNS, Kinesis, EventBridge\
- **Bases de datos** → DynamoDB Streams, Aurora\
- **Programados** → Cron/EventBridge Scheduler

**Ventajas:** - Desacoplamiento entre productores y consumidores.\
- Escalado automático según la tasa de eventos.\
- Resiliencia (reintentos y DLQ).

------------------------------------------------------------------------

## 💡 Casos de uso

-   **ETL en tiempo real** → transformar datos de Kinesis a Redshift.\
-   **Automatización DevOps** → ejecutar lint en CodeCommit.\
-   **IoT** → procesar telemetría y guardar en DynamoDB.\
-   **APIs REST/GraphQL** → con API Gateway.

------------------------------------------------------------------------

## 🖥️ Lenguajes soportados

-   **Nativos**: Node.js, Python, Java, Go, .NET, Ruby.\
-   **Custom Runtimes**: Rust, PHP, Elixir, etc. mediante *Lambda
    Layers*.\
-   Recomendación: elegir lenguaje con buen *cold start* y ecosistema.

------------------------------------------------------------------------

## 📝 Ejemplo de función (Python 3.12)

``` python
import json

def handler(event, context):
    name = event.get("queryStringParameters", {}).get("name", "mundo")
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": f"Hola, {name}!"})
    }
```

**Buenas prácticas de código:** - Manejar excepciones y códigos HTTP.\
- Usar *environment variables*.\
- Logging para depuración.

------------------------------------------------------------------------

## 🚀 Despliegue de funciones Lambda

-   **AWS Console** → interfaz gráfica.\
-   **AWS CLI** → scripting y CI/CD.\
-   **AWS SAM** → infraestructura como código.\
-   **AWS CDK** → definición en lenguajes de programación.\
-   **Serverless Framework** → multi-cloud, extensible.

------------------------------------------------------------------------

## 📞 Invocación de funciones

-   **Sincrónicas** → API Gateway, ALB, `aws lambda invoke`.\
-   **Asincrónicas** → S3, DynamoDB Streams, EventBridge, SQS.\
-   **Orquestadas** → Step Functions.

**Manejo de errores:** - Retries automáticos en asincrónicas.\
- Dead‑Letter Queues (SQS/SNS).\
- Lambda Destinations (éxito/fallo).

------------------------------------------------------------------------

## ✅ Conclusión

FaaS permite crear soluciones **ágiles, escalables y económicas**,
siguiendo buenas prácticas de seguridad, observabilidad y CI/CD.\
Con AWS Lambda se pueden implementar servicios basados en eventos que se
adaptan a múltiples casos de uso en la organización.

------------------------------------------------------------------------

## 📚 Referencias

-   [AWS Lambda Developer
    Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)\
-   [AWS Lambda Runtime
    API](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-api.html)\
-   [Event‑Driven Architectures on
    AWS](https://d1.awsstatic.com/whitepapers/serverless-event-driven-architectures.pdf)\
-   [Serverless Computing: Current
    Trends](https://arxiv.org/abs/1904.03424)\
-   [Serverless Architectures -- Martin
    Fowler](https://martinfowler.com/articles/serverless.html)
