# Microservicios Orquestados en EKS

## Arquitectura de la Solución
La solución propuesta consta de un conjunto de microservicios desplegados en **Amazon EKS (Elastic Kubernetes Service)**, orquestados mediante `eksctl` y configurados para soportar resiliencia, escalabilidad y comunicación interna.

### Componentes Clave:
- **API Gateway**: expone los endpoints REST y GraphQL hacia clientes externos.
- **Microservicios**: implementados con Spring Boot, siguiendo TDD, con JWT para autenticación.
- **Service Discovery**: gestionado con **AWS Cloud Map**.
- **Resiliencia**: implementada con **Resilience4j** (reintentos, circuit breakers, rate limiters).
- **Escalabilidad**: configurada con **HPA (Horizontal Pod Autoscaler)**.
- **Mensajería asíncrona**: **SNS/SQS** para comunicación desacoplada.
- **Métricas y monitoreo**: Prometheus + Grafana.

---

## Desarrollo de Microservicios con TDD
1. **Pruebas unitarias primero** con JUnit y Mockito.
2. Implementación mínima para pasar pruebas.
3. Refactorización asegurando cobertura > 80%.
4. Integración continua en GitHub Actions.

---

## Autenticación con JWT
- Generación de tokens firmados con RSA.
- Validación en cada request vía filtro de Spring Security.
- Expiración configurable y refresh tokens habilitados.

---

## Resiliencia con Resilience4j
- **CircuitBreaker**: aísla fallos de dependencias externas.
- **Retry**: reintenta operaciones críticas.
- **RateLimiter**: protege contra sobrecarga.

---

## Orquestación con EKS
- Creación del clúster:
  ```bash
  eksctl create cluster --name microservicios-cluster --region us-east-1 --nodes 3
  ```
- Despliegue con **Helm** o manifiestos YAML.
- **Ingress Controller** para enrutamiento.

---

## Escalado Automático con HPA
Ejemplo de manifiesto:
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: microservicio-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: microservicio
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

---

## Comunicación Asíncrona con SNS/SQS
- SNS para publicación de eventos.
- SQS para colas persistentes entre microservicios.

---

## Métricas y Monitoreo
- **Prometheus** para recolección.
- **Grafana** para dashboards.
- Alarmas configuradas en **CloudWatch**.

---

## Checklist de Implementación
- [x] Definición de arquitectura.
- [x] Implementación de microservicios con TDD.
- [x] JWT y seguridad.
- [x] Resilience4j para resiliencia.
- [x] Orquestación en EKS.
- [x] HPA configurado.
- [x] SNS/SQS para mensajería.
- [x] Monitoreo con Prometheus/Grafana.
