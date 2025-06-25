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

## ⏳ Tiempo estimado

- **Duración**: entre 1 y 2 horas  
- Dependerá de tu experiencia previa con la consola de AWS y el uso de políticas de ciclo de vida.

---

## 🛠️ Recursos

- [Documentación oficial de Amazon S3](https://docs.aws.amazon.com/s3/index.html)
- Herramientas opcionales:
  - **Cyberduck**, **S3 Browser**, o la **CLI de AWS** (para exploración avanzada)

---
