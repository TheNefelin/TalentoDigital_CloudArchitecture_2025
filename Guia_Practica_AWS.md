
# 🌩️ Guía práctica de AWS como servicio (con caso real)

## 🧭 1. ¿Qué es AWS?
**Amazon Web Services (AWS)** es la plataforma de servicios en la nube más usada del mundo. Permite a empresas y desarrolladores crear, desplegar y escalar aplicaciones sin gestionar servidores físicos.

### ¿Por qué usar AWS?
- Alta disponibilidad.
- Seguridad robusta.
- Escalabilidad automática.
- Paga solo por lo que usas.

---

## 🧱 2. Servicios fundamentales de AWS

| Categoría        | Servicio               | Qué hace                                              | Cómo se implementa                                           |
|------------------|------------------------|--------------------------------------------------------|---------------------------------------------------------------|
| **Cómputo**      | EC2                    | Crea servidores virtuales.                            | Lanzar una instancia con SO, conectarse vía SSH.              |
|                  | Lambda                 | Ejecuta funciones sin servidores.                     | Subir código y configurar evento disparador.                  |
| **Almacenamiento** | S3                  | Guarda archivos (PDFs, imágenes).                     | Crear un bucket y subir archivos vía consola o código.        |
|                  | EBS                    | Discos duros para EC2.                                | Adjuntar al lanzar EC2.                                       |
| **Base de datos** | RDS                  | Bases de datos SQL como MySQL.                        | Crear instancia y conectarse desde app externa.               |
|                  | DynamoDB               | Base de datos NoSQL.                                  | Crear tabla y usar vía SDK/API.                               |
| **Redes**        | VPC                    | Red privada virtual para tus servicios.               | Configurar subredes, gateways, ACLs.                          |
|                  | Route 53               | DNS y gestión de dominios.                            | Crear zona hospedada y apuntar dominio.                       |
| **Seguridad**    | IAM                    | Controla accesos por usuario y rol.                   | Crear roles y políticas con permisos mínimos necesarios.      |
| **DevOps**       | Elastic Beanstalk      | Despliegue de apps automático.                        | Subir código y configurar entorno.                            |
|                  | CloudFormation         | Infraestructura como código (IaC).                    | Plantillas YAML o JSON para desplegar recursos automáticamente.|
| **Monitoreo**    | CloudWatch             | Métricas y alertas.                                   | Configurar dashboards y alarmas.                             |
|                  | CloudTrail             | Registro de auditoría.                                | Activo por defecto en la cuenta AWS.                         |

---

## 🛠️ 3. Cómo iniciar con AWS
1. Crear una cuenta en https://aws.amazon.com/
2. Iniciar sesión en la consola: https://console.aws.amazon.com/
3. Probar servicios básicos (EC2, S3, RDS).

---

## 🧪 4. Caso práctico: Web para reservas de clases de yoga

### 🎯 Objetivo
Crear una app web para que usuarios reserven clases de yoga online.

### Servicios AWS usados:

| Necesidad                     | Servicio AWS   | Descripción práctica                                  |
|------------------------------|----------------|--------------------------------------------------------|
| Hospedar backend             | EC2            | Lanzar instancia con Node.js/Java.                    |
| Base de datos de reservas    | RDS            | Crear instancia MySQL para guardar usuarios/reservas. |
| Subir imágenes               | S3             | Guardar fotos de instructores, salas, etc.            |
| Control de acceso            | IAM            | Crear roles para que EC2 acceda a S3 y RDS.           |
| Monitorear uso del sistema   | CloudWatch     | Ver logs y métricas de las instancias.                |
| Acceso desde dominio         | Route 53       | Asociar dominio como yogaclases.com.                  |
| Despliegue automático        | Elastic Beanstalk | Subir backend en ZIP y dejar AWS manejarlo.       |

### Pasos simplificados:
1. Crear bucket S3 llamado `imagenes-yoga-reservas`.
2. Crear RDS con MySQL llamado `reservasdb`.
3. Subir backend en Node.js a EC2 o Elastic Beanstalk.
4. Configurar dominio y SSL con Route 53.
5. Monitorear con CloudWatch.

---

## 🔐 Recomendaciones de seguridad
- Activar autenticación multifactor (MFA).
- Nunca usar root para tareas diarias.
- Aplicar principio de menor privilegio (IAM).
- Cifrado en tránsito (HTTPS) y en reposo (S3, RDS).

---

## 📚 Recursos adicionales
- [AWS Free Tier](https://aws.amazon.com/free)
- [Documentación oficial](https://docs.aws.amazon.com/)
- [Architecting on AWS (curso gratuito)](https://explore.skillbuilder.aws/)
