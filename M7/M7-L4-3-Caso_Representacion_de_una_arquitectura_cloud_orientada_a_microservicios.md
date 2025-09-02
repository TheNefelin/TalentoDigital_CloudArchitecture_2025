
# 🧩 Caso resuelto — Representación de una Arquitectura Cloud Orientada a Microservicios (CloudServicesCo)

> **Contexto:** Modernización del monolito on‑premises hacia **AWS** con **microservicios** para mejorar escalabilidad, disponibilidad y velocidad de entrega.

---

## 1) Servicios clave seleccionados en AWS (mín. 5)

1. **Amazon API Gateway** — Entrada unificada para clientes web/mobile, validación de JWT, rate limiting.
2. **Amazon ECS (Fargate)** — Ejecución de contenedores sin administrar servidores (microservicios).
3. **Amazon RDS (Aurora MySQL)** — Transaccional para autenticación y pedidos.
4. **Amazon DynamoDB** — Catálogo de productos de lectura intensiva con latencias bajas.
5. **Amazon S3** — Almacenamiento de archivos estáticos (imágenes, reportes) y backups.
6. **Amazon CloudFront** — CDN para entregar contenido estático y media desde S3 con baja latencia.
7. **Amazon CloudWatch + AWS X-Ray** — Observabilidad (logs, métricas, trazas distribuidas).
8. **AWS Secrets Manager** — Gestión segura de secretos/credenciales.
9. **Elastic Load Balancer (ALB)** — Balanceo HTTP/HTTPS hacia tareas ECS dentro de VPC.
10. **Amazon VPC** — Segmentación de red (subnets públicas/privadas, Security Groups, NACLs).

> *Nota:* Kubernetes (EKS) también es válido; se elige **ECS Fargate** por simplicidad operativa en esta primera etapa.

---

## 2) Diagrama lógico de arquitectura (texto)

```
                   +---------------------------+
   Web/Mobile ---> |     Amazon API Gateway    | <--- Cognito (JWT opcional)
                   +-------------+-------------+
                                 |
                                 v
                         +-------+--------+
                         |   ALB (HTTP/S) |
                         +---+---------+--+
                             |         |
                 ------------+         +------------
                 |                               |
        +--------v-------+               +-------v--------+
        |  Auth Service  |               |  Orders Service|
        |  (ECS Fargate) |               | (ECS Fargate)  |
        +--------+-------+               +--------+-------+
                 |                               |
         +-------v-------+                +------v-------+
         |  RDS Aurora   |                |  RDS Aurora  |
         |  (MySQL)      |                |  (same cluster)
         +---------------+                +--------------+

                 +---------------------------------------+
                 |               Catalog Service         |
                 |              (ECS Fargate)           |
                 +--------------------+------------------+
                                      |
                               +------v------+
                               | DynamoDB    |
                               +-------------+

      +-----------------+                     +-------------------------+
      |      S3         |<-- assets/images -->|   CloudFront (CDN)      |
      +-----------------+                     +-------------------------+

  Observability: CloudWatch Logs/Metrics, X-Ray (tracing)
  Security: VPC (subnets privadas para ECS/RDS/DynamoDB), SG por capa, Secrets Manager
```

**Relaciones clave**
- API Gateway enruta por ruta/versión hacia ALB → tareas ECS (microservicios).
- **Auth** y **Orders** persisten en **RDS Aurora** (mismo clúster, esquemas separados).
- **Catalog** usa **DynamoDB** (lecturas rápidas, escalado automático).
- **S3 + CloudFront** sirven estáticos y media.
- Todo dentro de **VPC** con **Security Groups** y **subnets privadas** para backend.

---

## 3) Flujo de datos (end-to-end)

1. **Autenticación**
   - El cliente obtiene token (p. ej., **JWT** con Cognito o propio `Auth Service`).
   - API Gateway valida JWT (authorizer) y enruta al **Auth Service** cuando se requiera renovar/refrescar.

2. **Catálogo (lecturas intensivas)**
   - Cliente → API Gateway → **Catalog Service (ECS)**.
   - El servicio consulta **DynamoDB** (claves por `productId` y GSI por `category`).
   - Respuesta cacheable por el cliente/CDN cuando aplique.

3. **Pedidos (transaccional)**
   - Cliente → API Gateway → **Orders Service (ECS)** (con token válido).
   - **Orders** verifica stock consultando **Catalog** (read model en DynamoDB) o un **endpoint interno**.
   - Inserta/actualiza pedido en **RDS Aurora** usando transacciones.
   - Emite **eventos de dominio** (p. ej., `OrderPlaced`) para integraciones futuras (cola/SNS/SQS).

4. **Estáticos y media**
   - Imágenes y archivos servidos desde **CloudFront** (origen **S3**). Uploads controlados vía pre‑signed URLs.

5. **Observabilidad y seguridad**
   - Logs/métricas en **CloudWatch**, trazas distribuidas con **X‑Ray**.
   - Secretos (credenciales DB, API keys) en **Secrets Manager**.
   - **SG**: ALB (80/443 público), ECS privado (solo desde ALB/API Gateway), RDS (solo desde SG de ECS), DynamoDB (endpoint VPC).

---

## 4) Estimación básica de costos (opcional, aproximada)

> **Escenario de referencia (estimativo no contractual):**
> - 3 microservicios en **ECS Fargate**, cada uno con ~0.5 vCPU / 1 GB RAM, **2 réplicas** c/u (prod).
> - **API Gateway**: ~5 millones de requests/mes.
> - **RDS Aurora**: 1 clúster pequeño en una AZ (dev/test) o multi‑AZ (prod).
> - **DynamoDB**: on‑demand con tráfico moderado.
> - **S3 + CloudFront**: 200 GB almacenados, 1 TB de egress/mes.
>
> **Contribuciones típicas al costo mensual** (de mayor a menor, según uso):
> 1. **RDS Aurora** (capacidad y almacenamiento, + multi‑AZ).
> 2. **ECS Fargate** (vCPU/GB‑h según réplicas y horas activas).
> 3. **API Gateway** (por millón de requests).
> 4. **CloudFront/S3** (transferencia de datos y requests).
> 5. **DynamoDB** (lectura/escritura on‑demand) y **CloudWatch/X‑Ray**.
>
> **Sugerencias de optimización:**
> - Auto‑scaling por CPU/latencia/cola; apagar réplicas nocturnas en entornos no‑prod.
> - Caché agresiva de catálogo en CloudFront y cliente.
> - Elegir **Aurora Serverless v2** para cargas variables.
> - **Savings Plans/RI** para cargas estables.
> - Centralizar logs con retención ajustada y métricas pertinentes.

---

## 5) Reflexión breve

- **Prevención de cuellos de botella:** el diagrama evidencia puntos críticos (DB transaccional, picos en API Gateway, tamaño de tareas ECS), facilitando pruebas de carga dirigidas y planes de escalado.
- **Comunicación del equipo:** una vista común (diagrama + flujo) alinea a desarrollo, seguridad y operaciones; acelera decisiones y reduce malentendidos.
- **Anticipación de costos:** separar responsabilidades (RDS vs DynamoDB; compute ECS vs CDN) permite focalizar optimizaciones y proyecciones realistas antes del despliegue.

---

## 6) Anexos (checklist rápido)

- [ ] Rutas de API definidas y versionadas (`/v1/auth`, `/v1/catalog`, `/v1/orders`).
- [ ] Health checks y **readiness/liveness** en contenedores.
- [ ] Auto‑scaling (ECS service + target tracking).
- [ ] Backups/retención: RDS snapshots, versiones S3, export DynamoDB.
- [ ] IaC (CloudFormation/Terraform/CDK) para reproducibilidad.
- [ ] Monitoreo SLO/SLI (latencia p95, error rate, saturación).
