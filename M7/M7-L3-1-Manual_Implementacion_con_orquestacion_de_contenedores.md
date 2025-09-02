# 📘 Resumen: Implementación con Orquestación de Contenedores

## 1. Administración de Contenedores con Amazon ECS

-   **Necesidad de administrar contenedores:**
    -   Empaquetado consistente y portable.
    -   Escalabilidad mediante más instancias.
    -   Mantenimiento centralizado.
-   **Clusters ECS:**
    -   ECS con EC2 → requiere gestionar servidores.
    -   ECS con Fargate → infraestructura administrada por AWS.
    -   Auto Scaling según métricas (CPU, memoria, requests).
-   **Definiciones de tareas:**
    -   Task Definition → describe ejecución (imagen, puertos,
        variables).
    -   Service → mantiene tareas activas e integra balanceadores.
    -   Fargate/EC2 → definen el entorno de ejecución.
-   **Respaldos y seguridad:**
    -   Imágenes almacenadas en **ECR**, con versionado y backups (S3,
        snapshots).
    -   IAM controla accesos a imágenes.
    -   ECR incluye **escaneo de vulnerabilidades**.

## 2. Orquestador de Contenedores Kubernetes

-   **Orquestador de contenedores:** automatiza despliegue, escalado,
    disponibilidad y seguridad.
-   **Kubernetes (K8s):** open source, escalable, tolerante a fallos.
-   **Ventajas:**
    -   Despliegues automatizados (rolling updates, canary).
    -   Escalabilidad horizontal.
    -   Alta disponibilidad (pods se reinician o migran).
    -   ConfigMaps y Secrets para parámetros y credenciales.

## 3. Despliegue de Aplicaciones con Kubernetes

-   **Amazon EKS:** servicio administrado de Kubernetes en AWS.
    -   AWS gestiona el control plane.
    -   Integración con IAM, ALB, CloudWatch.
-   **Cluster EKS:**
    -   Nodos (EC2 o Fargate), roles IAM, redes (VPC, subnets).
    -   Security groups para controlar tráfico.
-   **Recursos principales:**
    -   **Pod:** unidad básica con contenedores.
    -   **Service:** acceso estable con balanceo interno/externo.
    -   **Deployment:** gestiona versiones y réplicas.
-   **Herramientas:**
    -   **eksctl:** CLI para creación/gestión de clusters.
    -   **Kubernetes Dashboard:** interfaz gráfica de monitoreo.
-   **Infraestructura como código:**
    -   Manifiestos YAML para Pods, Services y Deployments.
    -   **kubectl:** CLI para aplicar, escalar y administrar.
-   **Despliegue web:**
    -   Services tipo LoadBalancer/Ingress.
    -   Estrategias: Rolling Update, Blue/Green.

## 4. Escalabilidad y Alta Disponibilidad con Kubernetes

-   **Horizontal Pod Autoscaler (HPA):**
    -   Escala réplicas según CPU, memoria o métricas personalizadas.
-   **Tolerancia a fallos:**
    -   Réplicas múltiples, Node Affinity y Anti-Affinity.
    -   Probes (liveness/readiness).
    -   Rollbacks automáticos.
-   **Casos de uso:**
    -   E-commerce con HPA en microservicios críticos.
    -   Streaming con escalado dinámico en EKS.
    -   Plataformas internas con Kubernetes Dashboard.

## 5. Cierre

La orquestación de contenedores con ECS y Kubernetes es esencial para
arquitecturas de microservicios robustas.\
Permite alta disponibilidad, escalabilidad, despliegues automatizados y
resiliencia ante fallos.\
Kubernetes y EKS destacan como soluciones líderes por su flexibilidad y
capacidad de integración con AWS.

------------------------------------------------------------------------

📚 **Referencias** - AWS ECS Developer Guide:
https://docs.aws.amazon.com/ecs/ - AWS EKS User Guide:
https://docs.aws.amazon.com/eks/ - AWS ECR Documentation:
https://docs.aws.amazon.com/ecr/ - CNCF: https://www.cncf.io/ - eksctl
Documentation: https://eksctl.io/ - Kubernetes Documentation:
https://kubernetes.io/docs/
