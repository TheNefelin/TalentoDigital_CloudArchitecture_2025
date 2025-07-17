# ☁️ Proyecto Nube Sólida

---

## 📘 1. Introducción general (Resumen del proyecto)

### 🏢 Unidad solicitante:
Área de Infraestructura y Seguridad de una empresa tecnológica.

### 🧩 Situación:
La empresa se encuentra en proceso de migración hacia la nube para mejorar sus servicios. Las soluciones actuales presentan:
- Problemas de escalabilidad
- Costos elevados
- Baja resiliencia

### 🎯 Objetivo del proyecto:
Diseñar una arquitectura conceptual en la nube que:
- Aplique fundamentos cloud
- Use el modelo cliente-servidor
- Incorpore escalabilidad, resiliencia y seguridad

---

## 📋 2. Requerimientos del proyecto

### Requerimientos generales:
- Aplicación de fundamentos de cloud computing
- Principios de diseño arquitectónico (modularidad, resiliencia, etc.)
- Integración del modelo cliente-servidor
- Justificación de decisiones técnicas

### Requerimientos técnicos:
- Asignación adecuada de modelos de servicio (IaaS, PaaS, SaaS, FaaS)
- Elección de modelo de implementación (pública, privada o híbrida)
- Esquema conceptual de arquitectura
- Documentación con diagramas y atributos de calidad

---

## 👣 3. Desarrollo por etapas

## 🧾 Lección 1: Introducción a la Computación en la Nube

### 🎯 Objetivo
Comprender los conceptos fundamentales de la computación en la nube y sus beneficios.

### 📄 Fundamentos resumidos

| Concepto                  | Descripción breve |
|---------------------------|-------------------|
| Cloud Computing           | Modelo para acceder a recursos TI por internet |
| Autoservicio              | Los usuarios consumen recursos sin intervención humana |
| Elasticidad               | Escala automática según la demanda |
| Multitenencia             | Recursos compartidos entre múltiples usuarios |
| Medición del servicio     | Paga solo por lo que usas |

### 🚀 Beneficios
- _Disponibilidad 24/7_
- _Costos optimizados_
- _Escalabilidad automática_
- _Despliegue rápido_

### 🌐 Modelos de Despliegue

| Modelo        | Descripción                            | Ventajas                              | Desventajas                  |
|---------------|----------------------------------------|----------------------------------------|------------------------------|
| Nube Pública  | Infraestructura compartida             | Bajo costo, escalable                  | Menor control de seguridad   |
| Nube Privada  | Infraestructura dedicada               | Control total                          | Costosa                      |
| Nube Híbrida  | Combina pública y privada              | Equilibrio entre control y flexibilidad | Complejidad técnica          |

---

## 🧩 Lección 2: Modelos de Servicio en la Nube

### 🎯 Objetivo
Asignar y justificar modelos de servicio para cada componente.

### 🧠 Explicación general

| Modelo   | Descripción                                        |
|----------|----------------------------------------------------|
| IaaS     | Infraestructura como servicio (máquinas virtuales) |
| PaaS     | Plataforma como servicio (entorno gestionado)      |
| SaaS     | Software como servicio (aplicaciones completas)    |
| FaaS     | Función como servicio (ejecución por evento)       |

### 🧱 Asignación de servicios

| Componente             | Modelo de Servicio | Justificación                                    |
|------------------------|--------------------|--------------------------------------------------|
| Frontend (Web/App)     | SaaS               | Hosting como servicio (ej: Netlify, Firebase)    |
| Backend / API          | FaaS               | Escalabilidad automática                         |
| Base de Datos          | PaaS               | Gestión simplificada, backups incluidos          |
| Autenticación          | SaaS               | Uso de servicios externos seguros                |
| Infraestructura de Red | IaaS               | Control sobre la configuración de redes          |

### 🧱 Asignación de modelos de servicio con justificación

| Componente             | Modelo de Servicio | Justificación                                                                 |
|------------------------|--------------------|------------------------------------------------------------------------------|
| Frontend (Web/App)     | SaaS               | Permite alojar fácilmente la interfaz en servicios gestionados como Firebase o Netlify, sin preocuparse por infraestructura. Ideal para despliegue rápido y alta disponibilidad. |
| Backend / API          | FaaS               | AWS Lambda o Google Cloud Functions permiten ejecutar funciones bajo demanda, con escalabilidad automática y sin necesidad de administrar servidores. |
| Base de Datos          | PaaS               | Usar RDS o Cloud SQL simplifica la administración, ya que incluye backups automáticos, escalabilidad y alta disponibilidad sin gestión manual. |
| Autenticación          | SaaS               | Servicios como Auth0 o Firebase Authentication proveen seguridad robusta, fácil integración y cumplen estándares como OAuth2. Reduce errores y tiempo de desarrollo. |
| Red / Infraestructura  | IaaS               | Se requiere control total sobre la configuración de red, subredes, reglas de firewall y acceso. IaaS como Amazon VPC ofrece flexibilidad completa. |

---

## ☁️ Lección 3: Modelos de Implementación

### 🎯 Objetivo
Elegir el modelo de implementación (público, privado, híbrido).

### 🧪 Comparativa

### ☁️ Comparativa de Modelos de Implementación

| Modelo         | Ventajas                                                             | Desventajas                                                   |
|----------------|----------------------------------------------------------------------|----------------------------------------------------------------|
| Nube Pública   | Bajo costo, rápida implementación, escalabilidad automática.         | Menor control sobre seguridad y ubicación de los datos.        |
| Nube Privada   | Mayor control, cumplimiento normativo, personalización total.        | Costos más altos, requiere administración y mantenimiento.     |
| Nube Híbrida   | Combina control y flexibilidad, permite integración progresiva.      | Mayor complejidad técnica e integración entre entornos.        |

### ✅ Modelo seleccionado: Nube Híbrida

**Justificación:**

Se optó por una **nube híbrida** debido a que combina lo mejor de los dos mundos: la **escalabilidad y eficiencia** de la nube pública con el **control y seguridad** de una nube privada para los componentes más sensibles.

Este modelo permite, por ejemplo:
- Desplegar el backend y el frontend en la nube pública (para aprovechar la elasticidad y menor costo).
- Mantener la base de datos y los servicios de autenticación en una nube privada o entorno controlado (para cumplir requisitos de seguridad o normativas de datos).

Además, la arquitectura híbrida facilita una **migración progresiva** desde sistemas tradicionales hacia la nube, lo que se alinea con el contexto actual del negocio que está en proceso de modernización, sin comprometer la continuidad operativa ni la seguridad.

---

## 🏗️ Lección 4: Principios de Diseño Arquitectónico

### 🎯 Objetivo
Aplicar principios fundamentales de diseño para construir una arquitectura modular, resiliente y segura, basada en el modelo cliente-servidor.

---

### 🔧 Principios aplicados en la arquitectura

| Principio        | Aplicación práctica en el diseño                                     |
|------------------|----------------------------------------------------------------------|
| **Modularidad**  | Separación clara entre frontend, backend, autenticación y base de datos. |
| **Desacoplamiento** | Uso de funciones FaaS (Lambda) que interactúan por eventos/API Gateway. |
| **Elasticidad**  | Uso de servicios autoescalables como Lambda y S3.                    |
| **Resiliencia**  | Replicación en múltiples zonas, balanceo de carga, retry y fallback. |
| **Seguridad**    | IAM, roles mínimos necesarios, encriptación en tránsito y reposo.    |

---

### 🗺️ Esquema conceptual de arquitectura (cliente-servidor)

```mermaid
graph TD
  A[Usuario] --> B[Frontend - S3 - hosting estático]
  B --> C[API Gateway]
  C --> D[Lambda Functions]
  D --> E[Base de Datos - RDS]
  D --> F[Auth0 / Firebase Auth]
```

> Puedes agregar aquí un diagrama visual o usar herramientas como draw.io o mermaid.

---

## 🔐 Lección 5: Atributos de Calidad en la Arquitectura en la Nube

### 🎯 Objetivo
Incorporar los atributos clave de calidad en el diseño arquitectónico: **resiliencia**, **seguridad** y **escalabilidad**, garantizando una solución robusta, segura y adaptable a la demanda.

---

### ⚙️ Atributos de calidad aplicados

| Atributo       | Estrategia aplicada                                                                 |
|----------------|--------------------------------------------------------------------------------------|
| **Resiliencia**| - Uso de múltiples zonas de disponibilidad (AZ) en RDS y Lambda.                    |
|                | - Mecanismos de retry automático en funciones Lambda.                                |
|                | - API Gateway para distribuir el tráfico y manejar picos de carga.     |
|                | - Monitorización con CloudWatch para detección temprana de fallos.                  |
| **Seguridad**  | - Control de acceso mediante IAM con principio de menor privilegio.                 |
|                | - Encriptación de datos en tránsito (TLS) y en reposo (AES-256 en RDS/S3).           |
|                | - Autenticación externa segura (Auth0 / Firebase Authentication).                   |
|                | - Configuración de reglas de seguridad (Security Groups, políticas VPC).            |
| **Escalabilidad** | - Uso de AWS Lambda y S3 (escalan automáticamente según demanda).                 |
|                | - Diseño sin servidor que permite escalar horizontalmente sin afectar la UX.        |
|                | - Posibilidad de agregar nuevas funciones o microservicios sin alterar el sistema.  |

---

### 🧩 Integración de los atributos en la arquitectura

- Los componentes están distribuidos en servicios escalables y desacoplados, asegurando que un fallo en uno no afecte a los demás.
- La combinación de servicios gestionados y sin servidor minimiza los puntos de falla y facilita la recuperación.
- El diseño contempla escenarios de carga variable, con una arquitectura que crece o se contrae automáticamente.
- La seguridad está integrada desde la base con autenticación robusta, cifrado y control de acceso granular.

---

### 🧪 Ejemplo práctico

> Si la aplicación web recibe una cantidad inesperada de usuarios, el CDN (CloudFront) y el bucket de S3 escalan automáticamente, mientras que Lambda crea instancias bajo demanda para manejar las peticiones sin afectar el rendimiento ni los costos.

---

## 🛠️ Desarrollo en AWS Alchemy Lab

A continuación, se describen los pasos para implementar la arquitectura conceptual en el entorno AWS Alchemy Lab, considerando las restricciones típicas de la plataforma.

### 1. Acceso a AWS Alchemy Lab
- Inicia sesión en AWS Educate o Alchemy Lab con tus credenciales.
- Abre la consola de AWS.

### 2. Configuración de la red (VPC)
- Crea una VPC con al menos una subred pública para hospedar los recursos.
- Configura un Internet Gateway y asocia la tabla de rutas para acceso a Internet.

### 3. Despliegue del Frontend
- Usa un bucket de S3 para alojar el contenido estático del frontend (HTML, CSS, JS).
- Habilita el hosting estático en el bucket.

### 4. Backend sin servidor (Lambda)
- Crea funciones Lambda para la lógica del backend.
- Configura API Gateway para exponer las funciones como endpoints REST.

### 5. Base de datos (RDS)
- Despliega una instancia de RDS (MySQL o PostgreSQL) en la VPC.
- Configura los grupos de seguridad para permitir acceso desde Lambda.

### 6. Seguridad
- Define roles y políticas IAM mínimos para que Lambda acceda a RDS y S3.
- Aplica reglas de firewall (Security Groups) para restringir acceso solo a los recursos necesarios.

### 7. Pruebas
- Realiza pruebas de conexión entre Lambda y la base de datos.
- Prueba la carga del frontend desde S3.
- Verifica los endpoints REST vía API Gateway.

---

> Esta configuración evita el uso de servicios avanzados como CloudFront o CloudFlare, debido a las restricciones de AWS Alchemy Lab, enfocándose en servicios básicos para garantizar la compatibilidad con la plataforma

--- 

## ⚙️ VPC

| Opción                         | Configuración elegida       | Motivo técnico                                                                                      |
|-------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------|
| **Nombre de la VPC**          | `tec-vpc`                   | Uso de nomenclatura estándar del proyecto (`tec_`) para mantener orden y trazabilidad.              |
| **CIDR IPv4**                 | `10.0.0.0/16`               | Rango amplio que permite dividir en múltiples subredes públicas y privadas.                         |
| **Tenencia**                  | Predeterminado              | No se requiere hardware dedicado; se optimiza costo y es suficiente para el entorno educativo.       |
| **Zonas de disponibilidad**   | 2                           | Provee redundancia y alta disponibilidad en múltiples zonas.                                        |
| **Subredes públicas**         | 2                           | Necesarias para exponer recursos como S3, API Gateway o posibles EC2 con acceso público.            |
| **Subredes privadas**         | 2                           | Usadas para alojar servicios sensibles como RDS y funciones Lambda sin acceso directo a Internet.   |
| **NAT Gateway**               | Ninguna                     | Se evita para reducir costos; los recursos privados acceden a S3 mediante endpoint sin usar NAT.     |
| **Punto de enlace de S3**     | Gateway de S3               | Permite que Lambda en subred privada acceda a S3 sin requerir salida a Internet ni NAT.             |
| **DNS – nombres de host**     | Habilitado                  | Las instancias (como RDS o EC2) obtienen nombres DNS internos útiles para comunicación.             |
| **DNS – resolución**          | Habilitado                  | Permite que servicios internos (como Lambda) resuelvan nombres como `rds.amazonaws.com`.            |

---

<img src=".\img\P03-VPC-01.png">

---

## ⚙️ Security Group

### 🔐 Security Group: `tec-sg-admin`

- **Nombre**: tec-sg-admin
- **Descripción**: Administracion desde el PC local a servicios como PostgreSQL o SSH.
- **VPC**: tec-vpc

| Dirección | Tipo        | Protocolo | Puerto | Origen/Destino          | Descripción                              |
| --------- | ----------- | --------- | ------ | ----------------------- | ---------------------------------------- |
| Entrada   | PostgreSQL  | TCP       | 5432   | `MI_IP/32` o `Anywhere` | Acceso a PostgreSQL desde EC2 (pgAdmin instalado) |
| Entrada   | SSH         | TCP       | 22     | `MI_IP/32` o `Anywhere` | Acceso SSH a EC2 (si fuera necesario)    |
| Salida    | All Traffic | All       | All    | `0.0.0.0/0`             | Permitir todas las salidas (por defecto) |

---

<img src=".\img\P03-SG-01.png">

---

### 🔐 Security Group: `tec-sg-backend`

- **Nombre**: tec-sg-backend
- **Descripción**: Permite acceso a la base de datos PostgreSQL desde Lambda y desde el admin para pruebas.
- **VPC**: tec-vpc

| Dirección | Tipo        | Protocolo | Puerto | Origen/Destino  | Descripción                                       |
| --------- | ----------- | --------- | ------ | --------------- | ------------------------------------------------- |
| Entrada   | PostgreSQL  | TCP       | 5432   | `tec-sg-lambda` | Permitir acceso desde Lambda                      |
| Entrada   | PostgreSQL  | TCP       | 5432   | `tec-sg-admin`  | Permitir acceso desde instancia EC2 con SG admin  |
| Entrada   | PostgreSQL  | TCP       | 5432   | `MI_IP/32`      | Permitir acceso temporal a PostgreSQL desde pgAdmin |
| Salida    | All Traffic | All       | All    | `0.0.0.0/0`     | Permitir todas las salidas (por defecto)          |

---

<img src=".\img\P03-SG-02.png">

---

### 🔐 Security Group: `tec-sg-lambda`

- **Nombre**: tec-sg-lambda
- **Descripción**: Permite que Lambda se comunique con recursos backend como RDS.
- **VPC**: tec-vpc

| Dirección | Tipo        | Protocolo | Puerto | Origen/Destino   | Descripción                          |
| --------- | ----------- | --------- | ------ | ---------------- | ------------------------------------ |
| Salida    | PostgreSQL  | TCP       | 5432   | `tec-sg-backend` | Permitir que Lambda acceda a la base |
| Salida    | All Traffic | All       | All    | `0.0.0.0/0`      | (Opcional) Permitir otras salidas    |

---

<img src=".\img\P03-SG-03.png">

---

### 🔐 Security Group: `Vincular Grupos`
- tec-sg-backend -> tec-sg-lambda
- tec-sg-lambda -> tec-sg-backend

---

<img src=".\img\P03-SG-04.png">
<img src=".\img\P03-SG-05.png">

---

## 🛢️ RDS - PostgreSQL

| Opción                             | Configuración                             | Motivo / Justificación                                     |
|-----------------------------------|-------------------------------------------|-------------------------------------------------------------|
| **Método de creación**            | Creación estándar                         | Permite control total sobre configuración                   |
| **Motor**                         | PostgreSQL 17.4-R1                        | Última versión estable soportada                            |
| **Plantilla**                     | Entorno de prueba                         | Entorno no productivo (desarrollo/test)                     |
| **Identificador de instancia**   | tec-pgdb                                  | Nomenclatura estandarizada                                  |
| **Usuario maestro**               | postgres                                  | Usuario por defecto y reconocido                             |
| **Contraseña**                    | Generada manualmente (segura)             | Control y reutilización futura                               |
| **Administración de credenciales**| Autoadministrado                          | Manejo manual sin Secrets Manager                            |
| **Clase de instancia**            | db.t4g.micro                              | Bajo costo, ideal para pruebas                               |
| **Almacenamiento**                | 20 GiB SSD (gp2)                          | Suficiente para pruebas, buena velocidad                     |
| **Acceso público**                | ✅ Sí                                     | Necesario para conectar desde pgAdmin4                       |
| **VPC**                          | tec-vpc                                   | VPC previamente creada                                      |
| **Subred**                      | Grupo de subredes automático              | Distribución en 2 AZs por VPC Wizard                         |
| **Grupo de Seguridad**           | tec-sg-backend                           | Seguridad centralizada, controla acceso Lambda y admin       |
| **Reglas en tec-sg-backend**    | PostgreSQL (TCP 5432) desde `tec-sg-lambda` y `tec-sg-admin` | Permite acceso desde Lambda y acceso temporal desde admin |
| **Tipo de red**                  | IPv4                                      | Suficiente para conexión desde red local                     |
| **Zona de disponibilidad**       | Sin preferencia                           | AWS distribuye según disponibilidad                         |
| **Proxy RDS**                    | No                                        | No necesario en entorno de pruebas                           |
| **Autenticación**                | Contraseña                                | Simple y funcional para laboratorio                          |
| **Certificado**                 | rds-ca-rsa2048-g1                         | Seguridad TLS activa                                         |
| **Performance Insights**         | Opcional (7 días)                         | Puede activarse para monitoreo básico                        |
| **Logs en CloudWatch**           | PostgreSQL, IAM errors, Update            | Trazabilidad y debugging básico                              |

---

```sql
-- Crear la tabla
CREATE TABLE personajes_hxh (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo_nen VARCHAR(50) NOT NULL,
    edad INT NOT NULL,
    descripcion TEXT,
    img VARCHAR(100)  -- nombre de archivo de imagen, ej: "gon.png"
);
```
```sql
-- Insertar registros
INSERT INTO personajes_hxh (nombre, tipo_nen, edad, descripcion, img) VALUES
('Gon Freecss', 'Enhancer', 12, 'Protagonista, con gran talento natural para el Nen.', 'gon.png'),
('Killua Zoldyck', 'Transmuter', 12, 'Hijo de la familia asesina Zoldyck, amigo cercano de Gon.', 'killua.png'),
('Kurapika', 'Conjurer', 17, 'Último sobreviviente del clan Kurta, busca venganza.', 'kurapika.png'),
('Leorio Paradinight', 'Emitter', 19, 'Aspira a ser médico, es valiente y decidido.', 'leorio.png'),
('Hisoka Morow', 'Transmuter', 28, 'Antagonista impredecible, disfruta de la pelea.', 'hisoka.png'),
('Chrollo Lucilfer', 'Specialist', 30, 'Líder de la banda de ladrones Fantasma.', 'chrollo.png'),
('Biscuit Krueger', 'Enhancer', 30, 'Maestra experimentada con apariencia joven.', 'biscuit.png');
```
```sql
-- Consultar para verificar
SELECT * FROM personajes_hxh;
```


<img src=".\img\P03-RDS-01.png">
<img src=".\img\P03-RDS-02.png">
<img src=".\img\P03-RDS-03.png">
<img src=".\img\P03-RDS-04.png">
<img src=".\img\P03-RDS-05.png">
<img src=".\img\P03-RDS-06.png">
<img src=".\img\P03-RDS-07.png">
<img src=".\img\P03-RDS-08.png">

---

## ⚙️ Lambda API

### Lambda
- **Nombre**: tec-lambda-api
- **Idioma**: Python 3.13
- **Rol de ejecución**: LabRole
- **VPC**: tec-vpc
- **Subredes**:
  - tec-subnet-privada-1
  - tec-subnet-privada-2
- **Grupos de seguridad**: tec-sg-lambda

### Capa
- **Nombre**: pg-layer
- **Descripción**: Descripción: Dependencia pg (PostgreSQL) para funciones Lambda en Node.js 22.x
- **Cargar un archivo .zip**: nodejs.zip
- **Arquitecturas compatibles**: x86_64
- **Versiones ejecutables compatibles**: Node.js 22.x

```bash
node --version
```

```bash
npm init -y
```

```bash
npm install pg
```

```
nodejs/
│
├── node_modules/
├── package-lock.json
└── package.json/
```

### Entorno
```
DB_HOST=endpoint.rds.amazonaws.com
DB_NAME=postgres
DB_USER=postgres
DB_PASS=contraseña
DB_PORT=5432
```

```javascript
const { Client } = require('pg');

exports.handler = async (event) => {
  const client = new Client({
    host: process.env.DB_HOST,
    port: parseInt(process.env.DB_PORT),
    user: process.env.DB_USER,
    password: process.env.DB_PASS,
    database: process.env.DB_NAME,
    ssl: {
      rejectUnauthorized: false,
    },
  });

  try {
    await client.connect();

    const result = await client.query('SELECT * FROM personajes_hxh');

    await client.end();

    return {
      statusCode: 200,
      body: JSON.stringify({
        message: 'Lista de personajes obtenida correctamente',
        data: result.rows,
      }),
    };
  } catch (err) {
    console.error('Error al obtener personajes:', err);
    return {
      statusCode: 500,
      body: JSON.stringify({
        error: 'No se pudieron obtener los personajes',
        detail: err.message,
      }),
    };
  }
};
```

<img src=".\img\P03-FUN-01.png">
<img src=".\img\P03-FUN-02.png">
<img src=".\img\P03-FUN-03.png">
<img src=".\img\P03-FUN-04.png">
<img src=".\img\P03-FUN-05.png">
<img src=".\img\P03-FUN-06.png">
<img src=".\img\P03-FUN-07.png">

---
