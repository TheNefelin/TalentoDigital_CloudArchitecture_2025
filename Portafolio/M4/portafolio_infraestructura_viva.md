# Portafolio: Infraestructura Viva

> Proyecto desarrollado en el entorno de AWS Academy Learner Lab

## 🧭 Introducción

La solución "Infraestructura Viva" propone la migración de un entorno on-premise hacia la nube de AWS, aprovechando herramientas gratuitas y servicios compatibles con el entorno de laboratorio de AWS Academy. Se considera una arquitectura basada en buenas prácticas de seguridad, disponibilidad, escalabilidad y bajo costo.

---

### ✅ Objetivo:
Diseñar una red segura y segmentada en la nube para soportar los servicios internos y públicos del sistema.

### 🔧 Servicios usados:
- Amazon VPC
- Subnetting (subredes públicas)
- Internet Gateway
- Tabla de enrutamiento
- Grupos de seguridad (Security Groups)

### 🏗️ Implementación:
- **VPC:** `acme-vpc-vpc` (CIDR: `10.0.0.0/16`)
- **Subredes públicas:**
  - `acme-vpc-subnet-public1-us-east-1a` (CIDR: `10.0.1.0/24`)
  - `acme-vpc-subnet-public2-us-east-1b` (CIDR: `10.0.2.0/24`)
- **Internet Gateway:** creado y asociado a la VPC
- **Tabla de enrutamiento pública:** con ruta `0.0.0.0/0` apuntando al Internet Gateway
- **Asociación:** Subredes públicas asociadas explícitamente a la tabla pública
- **Grupo de seguridad (SG):**
  - Reglas de entrada:
    - HTTP (80) desde `0.0.0.0/0`
    - HTTPS (443) desde `0.0.0.0/0`
    - SSH (22) desde IP personal (solo para EC2 si aplica)

> ⚠️ **Nota:** Se omite la configuración de NAT Gateway para evitar el consumo del presupuesto del entorno de laboratorio, según las restricciones de AWS Academy.

## 🚀 Próximos pasos:
1. Crear buckets en S3 (estándar y archivo)
2. Configurar ciclo de vida y respaldos
3. Crear tabla en DynamoDB
4. Desplegar función Lambda conectada a DynamoDB
5. Continuar con EC2/RDS si aplica según el presupuesto

---

## 🔐 Restricciones
Este portafolio se ajusta a las siguientes restricciones de AWS Academy Learner Lab:
- Uso exclusivo del rol `LabRole`
- No se permite crear usuarios IAM
- Recursos limitados por presupuesto
- Regiones disponibles: `us-east-1` y `us-west-2`

---

<img src=".\img\P04.png">

---

# Portafolio - Infraestructura Viva

## 🧱 1. Arquitectura Base: VPC Personalizada

### 🎯 Objetivo
Diseñar y desplegar una red virtual privada (VPC) completamente desde cero para alojar todos los servicios necesarios de la propuesta "Infraestructura Viva".

---

## 🧩 Crear y Configuración VPC (Virtual Private Cloud)

| Parámetro                        | Valor                        | Descripción / Propósito                                                                 |
| -------------------------------- | ---------------------------- | --------------------------------------------------------------------------------------- |
| **Nombre de la VPC**             | `acme`                   | Nombre asignado a tu red privada virtual.                                               |
| **CIDR IPv4**                    | `10.0.0.0/20`                | Rango de direcciones IP privadas disponibles para toda la VPC (incluye subredes).       |
| **CIDR IPv6**                    | *Sin bloque*                 | No se está utilizando IPv6 en esta configuración.                                       |
| **Tenencia**                     | Predeterminado               | Indica que las instancias EC2 no serán dedicadas (comparten hardware).                  |
| **Zonas de disponibilidad (AZ)** | `us-east-1a`, `us-east-1b`   | Alta disponibilidad: recursos distribuidos entre 2 zonas de AWS.                        |
| **Subredes públicas (2)**        | `10.0.1.0/24`, `10.0.2.0/24` | Subredes accesibles desde Internet (ideal para Load Balancers, NAT Gateway, etc.).      |
| **Subredes privadas (2)**        | `10.0.3.0/24`, `10.0.4.0/24` | Subredes sin acceso directo desde Internet (ideal para RDS, instancias backend, etc.).  |
| **Gateway NAT**                  | En `1 AZ`                    | Permite que subredes privadas accedan a Internet de forma segura (sin recibir tráfico). |
| **VPC Endpoint (S3)**            | Gateway a S3                 | Permite acceso privado al servicio S3 desde subredes privadas, sin salir a Internet.    |
| **DNS - Resolución**             | Habilitada                   | Permite a recursos resolver nombres DNS (por ejemplo, `amazonaws.com`).                 |
| **DNS - Nombres de host**        | Habilitada                   | Asigna nombres DNS internos a instancias (ej: `ip-10-0-1-10.ec2.internal`).             |

---

<img src=".\img\P04-VPC-01.png">
<img src=".\img\P04-VPC-02.png">

---

## ⚙️ Crear y Configuración de Grupo de Seguridad 
### 🔐 acme-sg-rds

- **Nombre**: acme-sg-rds
- **Descripción**: Permite acceso a la base de datos PostgreSQL desde Lambda y desde el admin para pruebas.
- **VPC**: acme-vpc

| Regla | Tipo        | Protocolo | Puerto | Origen/Destino  | Descripción                                       |
| --------- | ----------- | --------- | ------ | --------------- | ------------------------------------------------- |
| Entrada   | PostgreSQL  | TCP       | 5432   | `MI_IP/32`      | Permitir acceso temporal a PostgreSQL desde pgAdmin |
| Salida    | All Traffic | All       | All    | `0.0.0.0/0`     | Permitir todas las salidas (por defecto)          |

---

## 🧾 Crear y Configuración de grupo de subredes de base de datos

| **Atributo**                | **Valor**                                         | **Motivo / Justificación**                                                                     |
| --------------------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Nombre**                  | `acme-rsd-gsr`                                    | Nombre identificador del grupo de subredes para RDS. Sigue convención de nombres del proyecto. |
| **Descripción**             | `Grupo de subredes privadas para RDS`             | Describe el uso general del grupo, enfocado en subredes privadas.                              |
| **VPC**                     | `acme-vpc`               | VPC personalizada del proyecto donde están definidas las subredes necesarias.                  |
| **Zonas de disponibilidad** | `us-east-1a`, `us-east-1b`                        | Cobertura multi-AZ para garantizar alta disponibilidad.                                        |
| **Subred 1**                | `acme-subnet-private1-us-east-1a` (`10.0.3.0/24`) | Subred privada en `us-east-1a`, ideal para aislar servicios backend como RDS.                  |
| **Subred 2**                | `acme-subnet-private2-us-east-1b` (`10.0.4.0/24`) | Subred privada en `us-east-1b`, garantiza redundancia multi-AZ.                                |
| **Subred 3**                | `acme-subnet-public1-us-east-1a` (`10.0.1.0/24`)  | Subred pública en `us-east-1a`, permite acceso desde internet si el RDS lo permite.            |
| **Subred 4**                | `acme-subnet-public1-us-east-1b` (`10.0.1.0/24`)  | Subred pública en `us-east-1b`, garantiza redundancia multi-AZ.            |

---

<img src=".\img\P04-RDS-SG-01.png">

---

## 🔧 Crear y Configuración RDS (Relational Database Service)

| **Atributo**                       | **Valor**               | **Motivo / Justificación**                                                                                     |
| ---------------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Método de creación**             | Creación estándar       | Permite control total sobre la configuración personalizada.                                                    |
| **Motor de base de datos**         | PostgreSQL              | Motor de código abierto, robusto y ampliamente utilizado.                                                      |
| **Versión del motor**              | PostgreSQL 17.4-R1      | Última versión estable disponible, incluye mejoras de rendimiento y seguridad.                                 |
| **Plantilla**                      | Producción              | Configura por defecto alta disponibilidad y mejores prácticas.                                                 |
| **Alta disponibilidad**            | Multi-AZ (2 instancias) | Proporciona redundancia entre zonas de disponibilidad; tiempo de actividad del 99.95%.                         |
| **ID de instancia**                | `acme-pgdb`             | Nombre identificador único y descriptivo para la instancia.                                                    |
| **Usuario maestro**                | `postgres`              | Usuario administrador por defecto para PostgreSQL.                                                             |
| **Administración de credenciales** | Autoadministrado        | Permite definir manualmente la contraseña, útil para configuraciones rápidas o personalizadas.                 |
| **Contraseña maestra**             | \*\*\*\*\* (oculta)     | Clave de acceso al usuario administrador.                                                                      |
| **Clase de instancia**             | `db.t3.micro`           | Instancia de bajo costo ideal para desarrollo o cargas ligeras.                                                |
| **Tipo de almacenamiento**         | SSD gp3                 | Almacenamiento rápido y flexible, recomendado para la mayoría de casos.                                        |
| **Almacenamiento asignado**        | 20 GiB                  | Tamaño mínimo recomendado, escalable más adelante.                                                             |
| **Recurso de cómputo EC2**         | No aplica               | No se está conectando directamente a una instancia EC2.                                                        |
| **Tipo de red**                    | IPv4                    | Configuración básica de red en VPC.                                                                            |
| **VPC asociada**                   | `acme-vpc`              | VPC personalizada que contiene tus subredes y recursos relacionados.                                           |
| **Grupo de subredes**              | `acme-rds-gsn`          | Define las subredes privadas donde se alojará la instancia RDS.                                                |
| **Acceso público**                 | Sí                      | Permite conexión externa (por ejemplo, desde pgAdmin). Necesita configuración adicional en grupo de seguridad. |
| **Grupo de seguridad**             | `acme-sg-rds`           | Controla qué IPs/puertos pueden acceder a la RDS. Debe permitir entrada por el puerto 5432 (PostgreSQL).       |

---

<img src=".\img\P04-RDS-01.png">
<img src=".\img\P04-RDS-02.png">
<img src=".\img\P04-RDS-03.png">
<img src=".\img\P04-RDS-04.png">
<img src=".\img\P04-RDS-05.png">
<img src=".\img\P04-RDS-06.png">
<img src=".\img\P04-RDS-07.png">

---

```sql
CREATE TABLE productos (
    id VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    img VARCHAR(100),
    precio NUMERIC(10,2) NOT NULL,
    stock INT NOT NULL,
    categoria VARCHAR(50),
    destacado BOOLEAN NOT NULL
);
```

```sql
INSERT INTO productos 
  (id, nombre, descripcion, img, precio, stock, categoria, destacado)
VALUES
  ('prod-001', 'Dinamita Triple X', '¡Explosión garantizada! Ideal para túneles falsos en cañones.', 'dinamita.png', 49.99, 120, 'Explosivos', TRUE),
  ('prod-002', 'Imán Industrial ACME', 'Poder de atracción insuperable. No se hace responsable por atraer rocas, trenes o el propio Coyote.', 'iman.png', 89.50, 60, 'Herramientas', FALSE),
  ('prod-003', 'Yunque Volador', 'Clásico ACME. No garantizamos precisión en la caída.', 'yunque.png', 199.90, 15, 'Pesados', TRUE);
```

```sql
SELECT * FROM productos;

DROP TABLE IF EXISTS productos;
```














---
---


> Para acme-sg-public (Grupo de Seguridad Público)
- Reglas de Entrada (Inbound):

| Tipo  | Protocolo | Puerto | Origen              | Descripción                    |
| ----- | --------- | ------ | ------------------- | ------------------------------ |
| HTTP  | TCP       | 80     | 0.0.0.0/0           | Permitir tráfico HTTP público  |
| HTTPS | TCP       | 443    | 0.0.0.0/0           | Permitir tráfico HTTPS público |
| SSH   | TCP       | 22     | Tu IP o 0.0.0.0/0\* | Acceso SSH para administración |

- Reglas de Salida (Outbound):

Permitir todo (0.0.0.0/0) en todos los puertos (por defecto está así, no necesitas cambiar).

> Para acme-sg-backend (Grupo para Backend: Lambda, RDS, etc.)
Reglas de Entrada (Inbound):

- Reglas de Entrada (Inbound):

| Tipo              | Protocolo | Puerto  | Origen                 | Descripción                            |
| ----------------- | --------- | ------- | ---------------------- | -------------------------------------- |
| HTTPS             | TCP       | 443     | `acme-sg-public` (ID)  | Permitir tráfico seguro desde frontend |
| PostgreSQL        | TCP       | 5432    | `acme-sg-public` (ID)  | Permitir acceso a RDS desde frontend   |
| TCP personalizado | TCP       | 0-65535 | `acme-sg-backend` (ID) | Comunicación interna entre backend     |

- Reglas de Salida (Outbound):

| Tipo  | Protocolo | Puerto | Destino   | Descripción                                       |
| ----- | --------- | ------ | --------- | ------------------------------------------------- |
| DNS   | UDP       | 53     | 0.0.0.0/0 | Resolución de nombres                             |
| DNS   | TCP       | 53     | 0.0.0.0/0 | Resolución de nombres                             |
| HTTPS | TCP       | 443    | 0.0.0.0/0 | Acceso a internet vía NAT (AWS SDK, S3, DynamoDB) |

---

<img src=".\img\P04-GS-01.png">
<img src=".\img\P04-GS-02.png">
<img src=".\img\P04-GS-03.png">
<img src=".\img\P04-GS-04.png">
<img src=".\img\P04-GS-05.png">
<img src=".\img\P04-GS-06.png">

---

## 📦 Almacenamiento (Amazon S3)

| Bucket Name       | Región      | Uso principal                | Acceso            | Ciclo de Vida         |
| ----------------- | ----------- | ---------------------------- | ----------------- | --------------------- |
| `acme-s3-static`  | `us-east-1` | Imágenes estáticas del sitio | Público o Privado | No                    |
| `acme-s3-archive` | `us-east-1` | Datos viejos a archivar      | Privado           | S3 Glacier en 30 días |

---

<img src=".\img\P04-S3-01.png">
<img src=".\img\P04-S3-02.png">
<img src=".\img\P04-S3-03.png">
<img src=".\img\P04-S3-04.png">
<img src=".\img\P04-S3-05.png">
<img src=".\img\P04-S3-06.png">
<img src=".\img\P04-S3-07.png">

---

## 🔧 Crear la base de datos NoSQL (DynamoDB)

| Atributo clave | Tipo   | Comentario                         |
| -------------- | ------ | ---------------------------------- |
| `id`           | String | Clave primaria (Partition Key)     |
| `nombre`       | String | Nombre del producto                |
| `descripcion`  | String | Detalle o descripción del producto |
| `img`    | String | URL en S3 para imagen del producto |                           |
| `precio`    | Number  | Precio del producto en USD                  |
| `stock`     | Number  | Cantidad disponible                         |
| `categoria` | String  | Categoría para clasificación                |
| `destacado` | Boolean | Marca si es producto destacado en la tienda |


```json
[
  {
    "id": { "S": "prod-001" },
    "nombre": { "S": "Dinamita Triple X" },
    "descripcion": { "S": "¡Explosión garantizada! Ideal para túneles falsos en cañones." },
    "img": { "S": "dinamita.png" },
    "precio": { "N": "49.99" },
    "stock": { "N": "120" },
    "categoria": { "S": "Explosivos" },
    "destacado": { "BOOL": true }
  },
  {
    "id": { "S": "prod-002" },
    "nombre": { "S": "Imán Industrial ACME" },
    "descripcion": { "S": "Poder de atracción insuperable. No se hace responsable por atraer rocas, trenes o el propio Coyote." },
    "img": { "S": "iman.png" },
    "precio": { "N": "89.50" },
    "stock": { "N": "60" },
    "categoria": { "S": "Herramientas" },
    "destacado": { "BOOL": false }
  },
  {
    "id": { "S": "prod-003" },
    "nombre": { "S": "Yunque Volador" },
    "descripcion": { "S": "Clásico ACME. No garantizamos precisión en la caída." },
    "img": { "S": "yunque.png" },
    "precio": { "N": "199.90" },
    "stock": { "N": "15" },
    "categoria": { "S": "Pesados" },
    "destacado": { "BOOL": true }
  }
]
```

<img src=".\img\P04-NDB-01.png">
<img src=".\img\P04-NDB-02.png">
<img src=".\img\P04-NDB-03.png">

---

## 🧮 Cómputo Serverless (AWS Lambda + API Gateway)

### 📌 Objetivo
- Crear una función Lambda escrita en Python que:
- Sirva como una API RESTful (vía API Gateway).
- Reciba una solicitud (GET/POST).
- Devuelva una respuesta JSON con algún dato estático o dinámico.
- Tenga permisos para leer desde el bucket acme-s3-static.

### ⚙️ Función Lambda

| Atributo         | Valor                          |
| ---------------- | ------------------------------ |
| Nombre           | `acme-lambda-api`              |
| Runtime          | Python 3.12 (o más reciente)   |
| Rol de ejecución | `LabRole`                      |
| VPC              | `acme-vpc` (subredes privadas) |
| Seguridad        | Asociado al `acme-sg-backend`  |

---

```python
import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('acme-products')

def lambda_handler(event, context):
    try:
        response = table.scan()
        items = response.get('Items', [])
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(items)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
```

<img src=".\img\P04-FUN-01.png">
<img src=".\img\P04-FUN-02.png">

---

## 🌐 Crear API Gateway para Lambda

<img src=".\img\P04-GW-01.png">
<img src=".\img\P04-GW-02.png">
<img src=".\img\P04-GW-03.png">
<img src=".\img\P04-GW-04.png">
<img src=".\img\P04-GW-05.png">
<img src=".\img\P04-GW-06.png">
<img src=".\img\P04-GW-07.png">
<img src=".\img\P04-GW-08.png">
<img src=".\img\P04-GW-09.png">
<img src=".\img\P04-GW-10.png">

## Crear RDS, para Testear

<img src=".\img\P04-RDS-01.png">
<img src=".\img\P04-RDS-02.png">
<img src=".\img\P04-RDS-03.png">
<img src=".\img\P04-RDS-04.png">
<img src=".\img\P04-RDS-05.png">
<img src=".\img\P04-RDS-06.png">
