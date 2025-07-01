# Tabla de Servicios AWS en Learner Lab (Chile)

📅 **Actualizado:** 24/06/2025

---

## Servicios Disponibles

| Servicio AWS          | Disponible | Límites y Restricciones                                                                                     |
|-----------------------|------------|--------------------------------------------------------------------------------------------------------------|
| **EC2**               | ✅         | - Instancias: nano, micro, small, medium, large (On-Demand).<br>- Máx. 9 instancias por región (us-east-1/us-west-2).<br>- Máx. 32 vCPU en total (ej: 32 t2.micro).<br>- EBS hasta 100 GB (gp2/gp3/sc1).<br>- Usar `vockey` en us-east-1; crear par nuevo en otras regiones. |
| **RDS**               | ✅         | - Motores: Aurora, Oracle, SQL Server, MySQL, PostgreSQL, MariaDB.<br>- Instancias: nano, micro, small, medium.<br>- Almacenamiento hasta 100 GB (gp2).<br>- No soporta Enhanced Monitoring. |
| **S3**                | ✅         | - Acceso completo (lectura/escritura).<br>- No se pueden crear vaults en Glacier.                           |
| **Lambda**            | ✅         | - Máx. 10 ejecuciones concurrentes.<br>- Usar `LabRole` para permisos.                                      |
| **SageMaker**         | ✅         | - Instancias: ml.t3.medium, ml.t3.large, ml.t3.xlarge, ml.m5.large, ml.m5.xlarge.<br>- Máx. 2 notebooks y 2 apps.<br>- Requiere configuración manual de dominio y perfil. |
| **Cloud9**            | ✅         | - Instancias: nano, micro, small, medium, large, c4.xlarge.<br>- Usar SSH en la configuración de red.       |
| **Elastic Beanstalk** | ✅         | - Instancias: nano, micro, small, medium, large.<br>- Usar `LabRole` y `LabInstanceProfile`.                |
| **DynamoDB**          | ✅         | - Sin límites específicos (sujeto a permisos IAM).                                                           |
| **IAM**               | ⚠️         | - Acceso limitado.<br>- No se pueden crear usuarios/grupos.<br>- Solo se permite usar roles (ej: `LabRole`). |
| **VPC**               | ✅         | - Configuración estándar de subredes públicas/privadas.<br>- El NAT Gateway consume mucho presupuesto.      |
| **EMR**               | ✅         | - Instancias: nano, micro, small, medium, large.<br>- Máx. 32 vCPU en total (ej: 4 m4.large).<br>- Clústeres se terminan al finalizar sesión. |
| **CloudFormation**    | ✅         | - Usar `LabRole` para stacks.                                                                               |
| **Secrets Manager**   | ✅         | - Sin restricciones específicas.                                                                            |
| **Regiones Permitidas**| 🌎        | - Solo `us-east-1` y `us-west-2`. Otras regiones muestran errores de acceso.                                |

---

## 🚫 Restricciones Generales

- **Presupuesto**: Si se excede el presupuesto, **la cuenta se desactiva permanentemente** (se pierden todos los recursos).

---

## 🔐 Conectividad SSH

- **Windows**: Usar PuTTY con archivo `.ppk` (descargable desde AWS Details).
- **Mac/Linux**: Usar:
```bash
  ssh -i labsuser.pem ec2-user@<IP-pública>
```

## 🧪 Sesiones de Lab
- Las instancias EC2 se detienen al cerrar sesión, pero se reinician la próxima vez.
- SageMaker no se reinicia automáticamente.

## 💰 Recomendaciones para Ahorrar Costos
- Detener o terminar EC2, RDS y SageMaker si no se usan.
- Usar instancias pequeñas (t3.micro en lugar de large).
- Monitorear el presupuesto con AWS Cost Explorer o Trusted Advisor.
- Eliminar recursos no esenciales usando Tag Editor.

## ⚠️ Notas Clave
- Cuidado: Lanzar más de 20 instancias EC2, aunque sean pequeñas, desactiva la cuenta inmediatamente.
