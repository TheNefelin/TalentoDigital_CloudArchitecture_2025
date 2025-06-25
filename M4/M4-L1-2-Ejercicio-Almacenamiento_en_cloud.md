# ☁️ Ejercicio Práctico: Almacenamiento de Objetos en la Nube con Amazon S3

## 🧭 Introducción

En este ejercicio práctico te adentrarás en uno de los pilares fundamentales de la computación en la nube: el **almacenamiento de objetos**.

La nube ofrece múltiples formas de almacenar información, cada una orientada a diferentes necesidades. A continuación se presenta una tabla comparativa de los servicios más comunes:

| **Servicio**         | **Tipo de almacenamiento** | **Uso recomendado**                                    | **Ventajas principales**                                 |
|----------------------|-----------------------------|--------------------------------------------------------|-----------------------------------------------------------|
| **Amazon S3**        | Almacenamiento de objetos   | Archivos, backups, medios, datos no estructurados      | Escalable, multiclase, gestión de ciclo de vida           |
| **Amazon EBS**       | Almacenamiento de bloques   | Volúmenes para instancias EC2, bases de datos          | Baja latencia, alta disponibilidad                        |
| **Amazon EFS**       | Almacenamiento de archivos  | Acceso compartido entre instancias Linux               | Multi-AZ, crecimiento automático                          |
| **Azure Blob Storage** | Almacenamiento de objetos | Datos no estructurados en Azure                        | Integración con el ecosistema Microsoft Azure             |
| **GCP Cloud Storage** | Almacenamiento de objetos  | Archivos, backups o datos analíticos en Google Cloud   | Consistencia global, clases de almacenamiento similares a S3 |

**¿Por qué Amazon S3 para este ejercicio?**

Amazon S3 es seleccionado debido a su:
- Amplia adopción en la industria.
- Facilidad de uso mediante consola web.
- Múltiples clases de almacenamiento.
- Inclusión en el **AWS Academy Free Tier**.
- Capacidad de simular políticas de ciclo de vida de forma visual y gratuita.

---

## 🎯 Desafío

**Objetivo principal**:  
Configurar un **bucket de almacenamiento en Amazon S3** y manejar el **ciclo de vida de objetos**, clasificando los archivos en:
- Clase de almacenamiento **Estándar**
- Clase de almacenamiento **Acceso poco frecuente (Infrequent Access)**

Además, podrás explorar transiciones a clases como **Amazon Glacier** o **Intelligent-Tiering**.

---

## 🧪 ¿Dónde se lleva a cabo?

- **Herramientas / Entorno**:
  - **Cuenta AWS Academy (Free Tier)**
  - Consola web de **Amazon S3**

- **Archivo final**:
  - Ninguno obligatorio, pero se recomienda guardar:
    - Capturas de pantalla
    - Mini reporte (pasos realizados y observaciones)

---

## 🛠️ Recursos

- [Documentación oficial de Amazon S3](https://docs.aws.amazon.com/s3/index.html)
- Herramientas opcionales:
  - **Cyberduck**, **S3 Browser**, o la **CLI de AWS** (para exploración avanzada)

---

# Desarrollo

### 1. Buscar y agregar S3

<img src="..\Img\M4\L1\Ejercicio\M4-L1-01.png">

### 2. Crear Bucket

<img src="..\Img\M4\L1\Ejercicio\M4-L1-02.png">

### 3. Crear Bucket
- **Definir tipo de Bucket**: Uso General
- **Nombre del Bucket**: s3-bucket-ejercicio-m4-l1
- **Region**: EE.UU. Este (Norte de Virginia) us-east-1
- **Propiedad de objetos**: ACL Deshabilitadas (Propiedad de la cuenta actual)
- **Configuración de bloqueo de acceso público para este bucket**: Bloquear todo el acceso público
- **Control de versiones de buckets**: Desactivar
- **Etiquetas - opcional**: Ninguno
- **Cifrado predeterminado**: 
  - Tipo de cifrado: Cifrado del servidor con claves administradas de Amazon S3 (SSE-S3)
  - 
- **Clave de bucket**: Habilitar
- **Configuración avanzada**: Desactivar
- **Crear Bucket**

<img src="..\Img\M4\L1\Ejercicio\M4-L1-03.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-04.png">

### 4. Agregar elementos al Bucket

- **Click en el nombre del Bucket**
- **Revision de opciones**
  - Metadatos
  - Propiedades
  - Permisos
  - Métricas
  - Administración
  - Puntos de acceso
- **Cargar Archivos**
- **Clase de almacenamiento**: Agrupación por niveles inteligente
- **Cifrado del lado del servidor**: No especificar una clave de cifrado
- **Sumas de comprobación**: La Recomendada
- **Etiquetas - opcional**: Ninguno
- **Ninguna**: Ninguno
- **Cargar**
- **Cerrar**

<img src="..\Img\M4\L1\Ejercicio\M4-L1-05.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-06.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-07.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-08.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-09.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-10.png">

### 5. Revisar elementos del Bucket

- **Click en elemento jpg**
- **Revisar URL**: o funciona por que el Bucket es privado
- **Click Abrir**: Se vera la Imagen

<img src="..\Img\M4\L1\Ejercicio\M4-L1-11.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-12.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-13.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-14.png">

### 6. Modificaciones

- **Crear Carpeta**
- **Nombrar Carpeta**
- **Crear Carpeta**
- **Mover elementos a la carpeta**
- **Trasladar**
- **Cerrar**

<img src="..\Img\M4\L1\Ejercicio\M4-L1-15.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-16.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-17.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-18.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-19.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-20.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-21.png">

### 7. Eliminar el Bucket
- **Vaciar el Bucket**
- **Elimiar**
- **Salir**
- **Seleccionar el Bucket**
- **Elimiar el Bucket**

<img src="..\Img\M4\L1\Ejercicio\M4-L1-22.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-23.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-24.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-25.png">
<img src="..\Img\M4\L1\Ejercicio\M4-L1-26.png">
