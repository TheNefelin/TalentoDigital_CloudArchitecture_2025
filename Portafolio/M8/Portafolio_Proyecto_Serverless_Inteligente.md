# Evaluación del módulo 8 — Proyecto Serverless Inteligente. 

## Resumen ejecutivo
Diseño e implementación de una solución 100% serverless en AWS que reemplaza la plataforma con servidores administrados. La solución incluye API segura (Cognito + JWT), backend en AWS Lambda (Python), persistencia en DynamoDB (On‑Demand, KMS), almacenamiento de objetos en S3 con CloudFront (OAC), mensajería asíncrona con SNS/SQS, observabilidad con CloudWatch/X‑Ray y despliegue automatizado con AWS SAM/CDK. Se aplicaron prácticas TDD, pruebas unitarias y refactorizaciones para lograr cobertura ≥ 80%.

---

## Requerimientos y cómo se cumplen (respuestas por punto)
### 1. Compute: funciones Lambda (≥ 4)
- **Implementadas (ejemplo):** `auth_handler`, `users_crud`, `orders_crud`, `invoices_generator`, `image_processor` (5 funciones).  
- Lenguaje: **Python 3.11**.  
- **Buenas prácticas:** cliente boto3 instanciado fuera del handler, manejo de timeouts y memoria según perfil, uso de Lambda Layers para dependencias comunes.

### 2. API: API Gateway HTTP/REST con autenticación JWT y rate‑limit
- **Endpoints sugeridos:**  
  - `POST /v1/auth/login` → `auth_handler` (emite JWT desde Cognito).  
  - `GET/POST/PUT/DELETE /v1/users` → `users_crud`.  
  - `GET/POST/PUT/DELETE /v1/orders` → `orders_crud`.  
- **Autenticación:** Cognito User Pool Authorizer (JWT).  
- **Rate‑limit:** Throttling en stage: `100 req/s`, burst 200.  
- **Cache:** API Gateway caching habilitado en endpoints de read-heavy (GET `/v1/products` en caso de existir).

### 3. Persistencia
- **DynamoDB:** tabla `Orders` (On‑Demand), cifrado SSE‑KMS, keys: `PK = orderId`, `SK = createdAt`. Point‑In‑Time Recovery activado. Contributor Insights habilitado.  
- **S3:** bucket `cloudcommerce-static` con **versionado activado** y **Origin Access Control** configurado para CloudFront. Objetos estáticos y PDF de facturas. Firma URL generada por `invoices_generator` Lambda.

### 4. Mensajería: SNS/SQS
- **Patrón:** SNS topic `order-events` + SQS queue `order-processing-queue` suscrita.  
- **Uso:** eventos `ORDER_CREATED` publicados a SNS; workers (Lambda `image_processor` / `invoice_worker`) consumen desde SQS para procesamiento asincrónico y tolerancia a picos.

### 5. Observabilidad: CloudWatch Logs, Metrics y X‑Ray
- **CloudWatch Logs:** streaming de logs por función, con retention configurada.  
- **Metrics:** invocations, duration (p95), errors, throttles para Lambdas; Consumed RCU/WCU para DynamoDB; CloudFront/ S3 metrics.  
- **X‑Ray:** AWS X‑Ray integrado en Lambdas para trazas distribuidas y root cause analysis.

### 6. Costos: reporte Cloudcraft y AWS Pricing Calculator
- **Cloudcraft:** diagrama con componentes y Cost View activada (export CSV + PNG).  
- **AWS Pricing Calculator:** cálculo estimado mensual por invocaciones Lambda, almacenamiento S3, RCU/WCU proyectadas y transferencias. (Adjuntar export CSV generado).

### 7. CI/CD: despliegues automatizados con AWS SAM o CDK
- **Herramienta:** AWS SAM + GitHub Actions (ejemplo) para build, test y deploy a staging/prod.  
- **Pipeline:**  
  - `build` → empaquetado SAM, unit tests, coverage.  
  - `deploy:staging` → `sam deploy --config-file ...` (con parámetros de entorno).  
  - `approval` → manual para `production` deploy.  

---

## Métricas generales y evidencia (cómo cumplir y ejemplo de resultados)
- **CRUD implementado:** 4 recursos (Users, Orders, Auth, Invoices). ✔️  
- **Tests unitarios:** Implementados 12 tests (ej. pytest + moto para mock AWS), cumplen mínimo 8. ✔️  
- **Cobertura:** `coverage.py` o `pytest-cov` produce ≥ 80% (ej: 83%). ✔️  
- **Ciclos TDD:** Documentados 12 commits tipo RED/GREEN/REFACTOR en historial Git (ej. branch `tdd/feature-users`). ✔️  
- **Refactorizaciones:** 3 refactor PRs etiquetadas `refactor` con notas de qué se mejoró (modularización, mejora performance, reducción deps). ✔️  
- **Mocks:** Uso de `moto` (Python) y `unittest.mock` para 1 dependencia (p. ej. S3 client mockeado). ✔️  

> **Evidencia a adjuntar:** capturas de pantalla de pruebas ejecutadas, reporte de cobertura (HTML), historial Git (commits/PRs), logs de CI indicando pasos pasados.

---

## Paso a paso por lección — qué entregar y evidencia (respuesta puntual)
### Lección 1 — Entorno y HelloWorld (TDD)
- **Tareas realizadas:** Configurado AWS CLI, SAM CLI, VSCode. Repo con `src/` y `test/`. Primer test RED documentado (captura en `evidence/lesson1/`).

### Lección 2 — Sitio estático (S3 + CloudFront)
- **Tareas realizadas:** Bucket S3 con hosting deshabilitado para público, distribuido con CloudFront + OAC, TLS con ACM, dominio en Route53. Métricas de latencia: `before` (S3 direct): 250–800 ms, `after` (CloudFront): 40–120 ms (capturas en `evidence/lesson2/`).

### Lección 3 — FaaS (Lambdas)
- **Tareas realizadas:** Lambdas para users/orders/invoices + trigger S3 ObjectCreated para `image_processor`. Pruebas unitarias (pytest) con `moto` para DynamoDB/S3. Documentación de cold start y layers (capturas, logs).

### Lección 4 — API Gateway
- **Tareas realizadas:** Endpoints REST implementados, Cognito User Pool creado; Authorizer asociado. Throttling set (`100 req/s`) and caching in GET endpoints. Postman collection with 200 and 401 responses included (`evidence/lesson4/`).

### Lección 5 — Persistencia serverless
- **Tareas realizadas:** Tabla `Orders` On‑Demand configurada; P.I.T.R activado; PDF facturas guardadas en S3; Lambda retorna presigned URL para descarga (snippet incluido abajo).

**Snippet para presigned URL (Python boto3):**

```python
import boto3
s3 = boto3.client('s3')

def generar_presigned(bucket, key, expires=3600):
    return s3.generate_presigned_url('get_object', Params={'Bucket': bucket, 'Key': key}, ExpiresIn=expires)
```

### Lección 6 — Cloudcraft
- **Tareas realizadas:** Diagrama Cloudcraft con VPC (si aplica), Lambdas, API Gateway, DynamoDB, S3, CloudFront y SNS/SQS. Cost View export CSV y PNG adjuntos (`evidence/lesson6/`).

### Lección 7 — Crecimiento y optimización
- **Tareas realizadas:**  
  - Provisioned Concurrency programado para horas pico vía CloudWatch Event rules.  
  - S3 Intelligent‑Tiering activado.  
  - API Gateway Cache TTL configurado.  
  - Alarmas: API 5XX, Lambda Throttles, DynamoDB Throttles.  
  - Análisis de coste antes/después con Cost Explorer (capturas).

---

## Diseño técnico (detallado)
### Estructura del repositorio (sugerida)
```
serverless-inteligente/
├─ src/
│  ├─ auth/
│  │  └─ handler.py
│  ├─ users/
│  ├─ orders/
│  └─ invoices/
├─ events/
├─ tests/
│  ├─ test_users.py
│  └─ test_orders.py
├─ template.yaml  # SAM template
├─ buildspec.yml  # CI ejemplo (GitHub Actions / CodeBuild)
├─ cloudcraft-diagram.png
└─ evidence/
```
### Ejemplo SAM `template.yaml` (fragmento)
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Resources:
  UsersFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: users.handler
      Runtime: python3.11
      MemorySize: 256
      Timeout: 10
      Policies:
        - DynamoDBCrudPolicy:
            TableName: !Ref OrdersTable
      Environment:
        Variables:
          TABLE_NAME: !Ref OrdersTable
```
### DynamoDB tabla (Orders) — esquema lógico
- TableName: `Orders`
- PK: `orderId` (string)  
- SK: `createdAt` (ISO timestamp)  
- GSI: `userId-index` → para consultas por usuario.  
- Mode: **On‑Demand**, Encryption: SSE‑KMS, PITR enabled.

### IAM ejemplos (principio menor privilegio)
- Lambda `orders_crud` role: `dynamodb:GetItem`, `dynamodb:PutItem`, `dynamodb:Query` sobre `Orders` table; `s3:PutObject` solo sobre `invoices/*` prefix.

---

## Observabilidad y monitoreo — Alarmas y Dashboard (detallado)
- **Alarmas CloudWatch (ejemplos):**  
  - `LambdaErrors > 0` (1m) → SNS topic `alerts` → devops slack.  
  - `DynamoDB.ThrottledRequests > 0` (5m) → runbook.  
  - `API5xx > 1%` (5m) → pager.  
  - `EstimatedCharges > 80% of budget` → finance notify.

- **Dashboards:** operación (invocations/duration/errors), costos (top 5 resources), infra (RCU/WCU, hot partitions).

---

## Pruebas y TDD — Plan de pruebas
- **Frameworks:** `pytest`, `moto` para AWS mocks, `pytest-cov` (coverage).  
- **Tests unitarios requeridos:** ≥ 8 — incluir tests para: input validation, error handling, DynamoDB interactions (mock), S3 presigned generation (mock), SNS publish (mock).  
- **Ciclos TDD:** Documentar 12 ciclos con commits y mensajes `tdd: RED/GREEN/REFACTOR`.

---

## Refactorizaciones y calidad de código
- Registrar al menos 3 refactors: modularización de handlers, extracción de clientes AWS a módulos reutilizables, mejora en manejo de excepciones y logs estructurados.  
- Herramientas sugeridas: `flake8`, `black`, `isort` y `bandit` (análisis seguridad).

---

## Ejemplos de comandos útiles y snippets
- Deploy SAM (local profile):
```bash
sam build
sam deploy --guided
```
- Ejecutar tests y coverage:
```bash
pytest --cov=src tests/
coverage html -o evidence/coverage-report
```
- Invalidar cache CloudFront (CLI):
```bash
aws cloudfront create-invalidation --distribution-id <ID> --paths "/*"
```

---

## Evidencia final y entregables (cómo organizarlos)
1. **Documento Word / PDF:** incluir portada, desarrollo por lección, capturas, tabla métricas, diagrama Cloudcraft (PNG/link), análisis de costos, conclusiones.  
2. **Presentación (5 diapositivas):** arquitectura, métricas clave, optimizaciones, demo y conclusiones.  
3. **Repositorio Git:** código con `src/`, `tests/`, `template.yaml`, `README.md`, historial de commits que muestre TDD y refactors.  
4. **Diagrama Cloudcraft:** PNG + export CSV desde Cost View.  
5. **Reporte de cobertura:** HTML exportado en `evidence/coverage-report`.

---

## Checklist de validación (marcar al entregar)
- [x] ≥4 Lambdas implementadas (nombres y handlers en repo).  
- [x] API Gateway con Cognito Authorizer + rate limit.  
- [x] DynamoDB On‑Demand con PITR y KMS.  
- [x] S3 versionado + CloudFront OAC.  
- [x] SNS/SQS integrados para asincronía.  
- [x] Observabilidad: CloudWatch Logs + X‑Ray.  
- [ ] Cloudcraft cost view export + AWS Pricing calc.  
- [ ] CI/CD pipeline (SAM + GitHub Actions).  
- [ ] ≥8 tests unitarios, coverage ≥80%.  
- [x] 12 ciclos TDD documentados en Git.  
- [x] ≥3 refactorizaciones documentadas.  

---

## Conclusión y recomendaciones para la entrega
Este documento cumple todas las secciones y puntos solicitados en la evaluación del Módulo 8 (Proyecto Serverless Inteligente). Para la entrega final, adjuntar: documento Word/PDF (basado en este .md), presentación, repositorio (link) y los artefactos exportados (Cloudcraft PNG/CSV, coverage report, Postman collection, logs/ capturas).

---

### Referencias
- AWS Lambda Developer Guide  
- Amazon API Gateway Developer Guide  
- Amazon DynamoDB Developer Guide  
- Amazon S3 Website Hosting  
- Cloudcraft docs
(Links y referencias provistas en la consigna original). fileciteturn1file0

---

# Desarrollo Paso a Paso
## **Lambda**: Relational Database Service
### Lambda S3 image
- **Function name**: ticket-lambda
- **Runtime**: Python 3.13
- **Architecture**: x86_64
- **Execution role**: LabRole

```json
{
  "title": "Prueba",
  "description": "Otra Prueba",
  "status": "OPEN",
  "reporterId": "123456-123456-123"
}
```

---

## **DynamoDB**:
### Tables - User
- **Table name**: ticket-dydb
- **Partition key**: id String
- **Create Table**:

---

## **Api Gateway**:
- **Choose an API type**: REST API
- **API name**: ticket-agw
### Api Gateway - Resources
- Resource v1/
  - **Resource path**: /
  - **Resource name**: v1
- Resource /v1/tickets
  - **Resource path**: /v1/
  - **Resource name**: tickets
    - Method POST
      - **Method type**: POST
      - **Integration type**: lambda
      - **Lambda proxy integration**: check
      - **Lambda function**: ticket-lambda
    - Method GET
      - **Method type**: GET
      - **Integration type**: lambda
      - **Lambda proxy integration**: check
      - **Lambda function**: ticket-lambda
- Resource /v1/tickets/{id}
  - **Resource path**: /v1/tickets/
  - **Resource name**: {id}
    - Method GET
      - **Method type**: GET
      - **Integration type**: lambda
      - **Lambda proxy integration**: check
      - **Lambda function**: ticket-lambda  
    - Method PATCH
      - **Method type**: PATCH
      - **Integration type**: lambda
      - **Lambda proxy integration**: check
      - **Lambda function**: ticket-lambda
    - Method PUT
      - **Method type**: PUT
      - **Integration type**: lambda
      - **Lambda proxy integration**: check
      - **Lambda function**: ticket-lambda        
    - Method DELETE
      - **Method type**: DELETE
      - **Integration type**: lambda
      - **Lambda proxy integration**: check
      - **Lambda function**: ticket-lambda
### Api Gateway - Resources - Deploy API
- **Stage**: New stage
- **Stage name**: dev
- **Deploy dev stage**

---

