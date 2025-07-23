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

### 🔐 acme-sg-lambda

- **Nombre**: acme-sg-lamda
- **Descripción**: Permite que la funcion Lambda acceda a RDS PostgreSQL.
- **VPC**: acme-vpc

| Regla  | Tipo       | Protocolo | Puerto | Origen/Destino | Descripción                                                |
| ------ | ---------- | --------- | ------ | -------------- | ---------------------------------------------------------- |
| Salida | PostgreSQL | TCP       | 5432   | `acme-sg-rds`  | Permitir a Lambda conectarse a RDS PostgreSQL (SG del RDS) |
---

>[!IMPORTANT] Alert Las Lambdas no requieren reglas de entrada. Solo reglas de salida son necesarias para conexiones salientes (como a RDS).

---

<img src=".\img\P04-SG-01.png">

---

### 🔐 acme-sg-rds

- **Nombre**: acme-sg-rds
- **Descripción**: Permite acceso a la base de datos PostgreSQL desde Lambda y desde el admin para pruebas.
- **VPC**: acme-vpc

| Regla   | Tipo        | Protocolo | Puerto | Origen/Destino   | Descripción                                              |
| ------- | ----------- | --------- | ------ | ---------------- | -------------------------------------------------------- |
| Entrada | PostgreSQL  | TCP       | 5432   | `MI_IP/32`       | Permitir acceso temporal desde pgAdmin |
| Entrada | PostgreSQL  | TCP       | 5432   | `acme-sg-lambda` | Permitir conexion desde Lambda con acme sg rds          |
| Salida  | All Traffic | All       | All    | `0.0.0.0/0`      | Permitir todas las salidas                 |

---

<img src=".\img\P04-SG-02.png">

---

## 🧾 Crear y Configuración de grupo de subredes de RDS

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

## 🧮 Crear y Configuración Lambda (Cómputo Serverless)

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
| Seguridad        | Asociado al `acme-sg-lambda`  |

---

<img src=".\img\P04-FUN-01.png">
<img src=".\img\P04-FUN-02.png">

---

### psycopg2-binary
- Es una versión empaquetada de psycopg2 (con los binarios incluidos) que facilita su instalación sin compilar.

```
lambda-psycopg2-layer/
```

```bash
pip install pg8000 -t python
```

```
lambda-psycopg2-layer/
  └── python
```

### Lambda Layer
- python -> python.zip

| Parámetro                             | Valor                                                         | Descripción / Propósito                                                                                        |
| ------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Nombre**                            | `py-pg-layer`                                                 | Nombre identificativo de la capa para referenciarla fácilmente en tus funciones Lambda.                        |
| **Descripción**                       | Capa con librería pg8000 para conexión a PostgreSQL en Lambda | Explica que esta capa incluye la librería `pg8000` para conectar funciones Lambda a bases de datos PostgreSQL. |
| **Archivo ZIP**                       | `python.zip`                                                  | Archivo comprimido que contiene la carpeta `python` con todas las dependencias necesarias para la capa.        |
| **Arquitecturas compatibles**         | `x86_64`                                                      | Arquitectura de CPU para la cual la capa está construida; debe coincidir con la arquitectura de tu Lambda.     |
| **Versiones ejecutables compatibles** | `Python 3.13`                                                 | Versión(s) de Python en las que la capa puede usarse, debe coincidir con el runtime de tu función Lambda.      |

---

<img src=".\img\P04-FUN-03.png">

---

```python
import json
import pg8000.native
from decimal import Decimal

def lambda_handler(event, context):
    try:
        conn = pg8000.native.Connection(
            user="postgres",
            password="!nfra-48-x",
            host="acme-pgdb.ccgvhugzcj7m.us-east-1.rds.amazonaws.com",
            port=5432,
            database="postgres"
        )
        
        rows = conn.run("SELECT * FROM productos")
        columns = [desc["name"] for desc in conn.columns]
        result = [dict(zip(columns, row)) for row in rows]
        
        conn.close()

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(result, default=decimal_handler)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def decimal_handler(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError
```

---

<img src=".\img\P04-FUN-04.png">

---

## 🌐 Crear API Gateway para Lambda

<img src=".\img\P04-GW-01.png">
<img src=".\img\P04-GW-02.png">
<img src=".\img\P04-GW-03.png">
<img src=".\img\P04-GW-04.png">
<img src=".\img\P04-GW-05.png">
<img src=".\img\P04-GW-06.png">
<img src=".\img\P04-GW-07.png">

## 📦 Almacenamiento (Amazon S3)
