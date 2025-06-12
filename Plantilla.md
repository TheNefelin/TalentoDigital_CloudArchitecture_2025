# 📘 Diseño Inicial de Arquitectura – Proyecto [Nombre del Proyecto]

## 1. Resumen del Proyecto
Breve descripción del objetivo del sistema, los usuarios clave y el problema que resuelve.

## 2. Alcance
- Funcionalidades incluidas en esta fase
- Exclusiones
- Límites técnicos

## 3. Requisitos
### 3.1 Requisitos funcionales
- [ ] Listar funcionalidades clave del sistema

### 3.2 Requisitos no funcionales
- Alta disponibilidad: [% uptime esperado]
- Escalabilidad: [automática / manual / vertical / horizontal]
- Seguridad: [cifrado, IAM, etc.]
- Tiempo de respuesta esperado: [ms/segundos]

## 4. Arquitectura Propuesta
### 4.1 Descripción general
Explicación textual de la arquitectura, cómo interactúan los componentes.

### 4.2 Diagrama de arquitectura
```mermaid
graph TD

```

*Incluir servicios como EC2, Lambda, RDS, S3, VPC, etc.*

### 4.3 Componentes principales
| Componente | Servicio AWS | Descripción |
|------------|--------------|-------------|
| Frontend   | S3 + CloudFront | Hosting estático |
| Backend    | API Gateway + Lambda | Lógica de negocio |
| Base de datos | Amazon RDS | PostgreSQL |
| Autenticación | Cognito | Gestión de usuarios |
| ...        | ...          | ...         |

## 5. Seguridad
- IAM roles y políticas clave
- Uso de grupos de seguridad y NACLs
- Cifrado en tránsito y en reposo
- Auditoría y monitoreo (CloudTrail, GuardDuty)

## 6. Networking
- VPC, subredes (públicas/privadas)
- Peering / VPN / Direct Connect (si aplica)
- Balanceadores de carga

## 7. Escalabilidad y Alta Disponibilidad
- Servicios utilizados para escalar
- Estrategias de distribución geográfica
- AWS Auto Scaling o ECS Fargate, por ejemplo

## 8. Backup y Recuperación
- Estrategias de backup (RDS snapshots, S3 versioning)
- Plan de recuperación ante desastres

## 9. Costeo Estimado
- Tabla de servicios con costos aproximados mensuales
- Recursos dimensionados para ambiente inicial (dev/staging/prod)

## 10. Riesgos Identificados
| Riesgo | Impacto | Mitigación |
|--------|---------|------------|
| Falta de experiencia con X | Medio | Capacitación previa o consultoría |
| Alta latencia esperada | Alto | Edge locations / CloudFront |
| ... | ... | ... |

## 11. Anexos
- Enlaces a documentación relevante
- Referencias a arquitectura de referencia de AWS
- Checklist de revisión (opcional)

---
