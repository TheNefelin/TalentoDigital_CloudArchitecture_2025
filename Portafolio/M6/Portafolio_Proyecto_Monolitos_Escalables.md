# Proyecto: Monolitos Escalables en AWS con .NET 8

## 📍 Situación inicial

Actualmente, la aplicación monolítica corre en un único servidor
on-premise, lo que provoca caídas en picos de tráfico y altos costos de
mantenimiento.\
La meta es migrar esta aplicación a **AWS Academy**, manteniendo el
enfoque monolítico pero asegurando **escalabilidad, disponibilidad y
monitoreo**.

------------------------------------------------------------------------

## 📋 Objetivo

Diseñar e implementar una arquitectura monolítica escalable en **AWS**,
aplicando:\
- Balanceo de carga (ELB).\
- Auto Scaling Groups en EC2.\
- Contenerización con Docker y ECR.\
- Mensajería asíncrona con SNS y SQS.\
- Monitoreo y buenas prácticas de infraestructura.

------------------------------------------------------------------------

## 🛠 Producto esperado

1.  Aplicación .NET 8 desplegada en EC2 con **ASG + ELB**.\
2.  Base de datos en **RDS (MySQL o PostgreSQL)** dentro de los límites
    de Academy.\
3.  Dockerfile y push de la imagen a **ECR**. (Opcional: despliegue
    ECS/Fargate).\
4.  Integración de **SNS (notificaciones)** y **SQS (procesamiento
    asíncrono)**.\
5.  Diagrama en **Cloudcraft** con costos estimados (AWS Pricing
    Calculator).

------------------------------------------------------------------------

## 🤝🏻 Requerimientos (adaptados a AWS Academy)

-   ✅ **EC2**: instancias `t2.micro` o `t3.micro` para pruebas, con
    ASG.\
-   ✅ **RDS**: MySQL/Postgres con máximo **100 GB gp2** (limitación
    Academy).\
-   ✅ **ECR + Docker**: crear repositorio y subir imagen de .NET 8.\
-   ✅ **SNS y SQS**: simular notificaciones y colas de procesamiento.\
-   ✅ **VPC y subredes**: usar configuración estándar Academy (evitar
    NAT Gateway por costo).\
-   ✅ **Cloudcraft**: generar diagrama y costos mensuales (mínimos).

------------------------------------------------------------------------

## 🔢 Métricas Generales

-   CRUD: 4 entidades (ejemplo: `Usuarios`, `Productos`, `Pedidos`,
    `Facturas`).\
-   Tests unitarios: 10 en total, con **xUnit o NUnit en .NET**.\
-   Cobertura: usar `coverlet` con mínimo 80%.\
-   TDD: al menos 12 ciclos RED-GREEN-REFACTOR.\
-   Refactorizaciones: 3--5.\
-   Mockito → En .NET usaremos **Moq** para mocking.

------------------------------------------------------------------------

## 👣 Paso a paso (resumido con respuestas)

### Lección 1 -- Fundamentos de Escalabilidad y TDD

-   Instalar **.NET 8 SDK**, `xUnit`, `coverlet`.\
-   Repo Git creado.\
-   Primer test `RED` implementado (ejemplo: validar creación de
    usuario).

### Lección 2 -- Implementación Monolítica en la Nube

-   Crear instancia EC2 (`t3.micro`).\
-   Crear RDS (MySQL 8).\
-   Deploy app con `dotnet publish` y configurar cadena de conexión.

### Lección 3 -- Escalabilidad y Alta Disponibilidad

-   Configurar **ASG basado en CPU \> 70%**.\
-   Crear **Application Load Balancer** para balanceo de tráfico.

### Lección 4 -- Contenerización con Docker

-   Crear `Dockerfile`:

    ``` dockerfile
    FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
    WORKDIR /app
    COPY . .
    ENTRYPOINT ["dotnet", "App.dll"]
    ```

-   Subir imagen a **ECR**.\

-   (Opcional) Comparar despliegue en ECS/Fargate (limitado en Academy).

### Lección 5 -- Servicios de Mensajería

-   Crear **SNS Topic** para notificaciones.\
-   Crear **SQS Queue** y suscripción desde SNS.\
-   Probar envío de mensajes desde app .NET con `AWSSDK.SQS`.

### Lección 6 -- Representación Cloud

-   Diagramar en **Cloudcraft**:
    -   VPC con 2 subredes públicas + 2 privadas.\
    -   EC2 en ASG con ALB.\
    -   RDS en subred privada.\
    -   ECR, SNS, SQS.\
-   Calcular costos (\~10--15 USD/mes usando Academy límites).

------------------------------------------------------------------------

## 🔍 Validación

-   Uso de servicios AWS permitido en Academy.\
-   Cumplimiento de métricas (CRUD, TDD, pruebas).\
-   Documentación clara con capturas.\
-   Diagrama Cloudcraft coherente y económico.

------------------------------------------------------------------------

# Desarrollo Paso a Paso

Usuario -> (POST Pedido) -> Monolito .NET (EC2 + Docker)
    |
    |---> Guarda en RDS
    |
    |---> Publica evento "DonacionCreado" en SNS
                 |
                 +--> Notificación email (subscripción)
                 +--> Notificación email (desubscripción)
                 +--> Notificación email (donacion)            
                 +--> Cola SQS "Facturacion"
                          |
                          +--> Worker .NET procesa facturación (en segundo plano)
                          +--> Actualiza stock en RDS
                          +--> Notificación email (factura) 

monolito