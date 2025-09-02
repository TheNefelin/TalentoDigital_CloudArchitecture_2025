
# 📚 Resumen — Introducción a la Arquitectura Serverless

## Introducción
La **computación sin servidor (serverless)** revoluciona el desarrollo cloud al abstraer la administración de servidores, delegando la infraestructura al proveedor y permitiendo que los equipos se centren en la lógica de negocio.  
Permite aplicaciones **escalables, modulares y de rápida entrega**.

**Objetivo de la lección:**  
Describir los conceptos fundamentales de la arquitectura serverless para la creación de microservicios escalables.

---

## 1. ¿Qué es una arquitectura sin servidor?
Modelo cloud donde el proveedor administra automáticamente los recursos, escalado y mantenimiento.

**Características clave:**
- **Provisionamiento automático:** recursos bajo demanda → elimina planificación de capacidad.
- **Escalado dinámico:** escala a cero sin tráfico y horizontalmente bajo carga.
- **Pago por uso:** facturación por invocaciones y tiempo de ejecución.
- **Gestión delegada:** parches y disponibilidad manejados por el proveedor.
- **Orientación a eventos:** funciones disparadas por HTTP, colas o cambios en BD.

---

## 2. Ventajas y desventajas

**Ventajas:**
- Escalabilidad automática.  
- Costos optimizados.  
- Desarrollo más rápido.  
- Alta disponibilidad inherente.  
- Seguridad administrada.  

**Desventajas:**
- *Cold starts* (latencia inicial).  
- Límites de tiempo de ejecución (ej. 15 min en AWS Lambda).  
- Observabilidad compleja.  
- *Vendor lock-in* (dependencia del proveedor).  
- Restricciones de entorno.  

---

## 3. Functions as a Service (FaaS)
Permite ejecutar funciones en respuesta a eventos, sin aprovisionar servidores.  
Cada función es **efímera, stateless y escalable**.

**Proveedores:**  
- **AWS Lambda**: 15 min máx.  
- **Azure Functions**: 10 min (consumo).  
- **Google Cloud Functions**: 9–60 min.  

**Buenas prácticas:** funciones pequeñas, pocas dependencias, stateless, uso de *layers*.

---

## 4. Backend as a Service (BaaS)
Servicios backend listos (auth, BD en tiempo real, storage, notificaciones) accesibles por APIs.

**Comparación:**  
- **FaaS:** control total sobre la lógica, ideal para procesamiento puntual.  
- **BaaS:** servicios preconstruidos, ideal para apps móviles/web rápidas.  

Ejemplos: Firebase, AWS Amplify, Supabase.

---

## 5. Servicios comunes serverless en la nube

| Categoría      | AWS            | Azure                | Google Cloud     |
|----------------|----------------|----------------------|------------------|
| Compute (FaaS) | Lambda         | Functions            | Cloud Functions  |
| Orquestación   | Step Functions | Durable Functions    | Workflows        |
| Mensajería     | SNS / SQS      | Service Bus / Events | Pub/Sub          |
| Bases de datos | DynamoDB       | Cosmos DB            | Firestore        |
| API Gateway    | API Gateway    | API Management       | API Gateway      |
| Storage        | S3             | Blob Storage         | Cloud Storage    |
| Analytics      | Kinesis        | Event Hubs           | Dataflow         |

---

## 6. Casos de uso comunes

✅ Procesamiento de datos en tiempo real.  
✅ Backends para apps móviles y web.  
✅ Automatización de tareas DevOps.  
✅ Chatbots y asistentes virtuales.  
✅ Pipelines ETL event-driven.  
✅ APIs REST/GraphQL con escalado elástico.  

**No recomendable en:**  
- Procesos largos o con estado.  
- Requisitos de latencia <10 ms.  
- Dependencias nativas pesadas.  

---

## Conclusión
La arquitectura serverless permite **microservicios escalables, costo-eficientes y rápidos de desplegar**.  
Sin embargo, su adopción debe evaluarse considerando **latencia, dependencia del proveedor y límites de ejecución**.

---

## Referencias
- AWS. *What is serverless?* https://aws.amazon.com/serverless/  
- Roberts, M. *Serverless Architectures*. https://martinfowler.com/articles/serverless.html  
- Google Cloud. *Serverless computing*. https://cloud.google.com/serverless  
- Microsoft. *Serverless computing*. https://azure.microsoft.com/en-us/solutions/serverless/  
