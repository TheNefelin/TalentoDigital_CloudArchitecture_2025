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

<img src=".\img\P4.png">

---

# Portafolio - Infraestructura Viva

## 🧱 1. Arquitectura Base: VPC Personalizada

### 🎯 Objetivo
Diseñar y desplegar una red virtual privada (VPC) completamente desde cero para alojar todos los servicios necesarios de la propuesta "Infraestructura Viva".

---

## 🧩 Configuración VPC

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

### 🔐 Grupo de Seguridad
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
