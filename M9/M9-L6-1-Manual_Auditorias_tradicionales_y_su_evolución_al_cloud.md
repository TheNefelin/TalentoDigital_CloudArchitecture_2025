# Resumen: Auditorías tradicionales y su evolución al Cloud

## Introducción

Las auditorías de seguridad surgieron para evaluar controles en centros
de datos tradicionales.\
Con el **cloud computing**, parte de la infraestructura pasa a un modelo
de **responsabilidad compartida**, requiriendo adaptar las metodologías
clásicas.

**Objetivo:** aplicar una evaluación de seguridad en arquitecturas cloud
según buenas prácticas.

------------------------------------------------------------------------

## 1. Auditorías tradicionales vs Cloud

  -------------------------------------------------------------------------------------
  Dimensión         Auditoría tradicional    Auditoría Cloud             Cambio clave
  ----------------- ------------------------ --------------------------- --------------
  Alcance físico    Visitas *in situ*,       Certificaciones del         Sin acceso
                    inspección de CPD        proveedor (ISO, SOC 2)      físico

  Acceso lógico     Revisión de sistemas     Revisión de IAM, roles, API Foco en
                    on‑premise               calls (CloudTrail)          identidad

  Responsabilidad   100% cliente             Cliente/proveedor           Delimitación
                                             compartida                  necesaria

  Herramientas      Escáneres locales,       Herramientas nativas (AWS   APIs en tiempo
                    scripts                  Config, Security Hub)       real
  -------------------------------------------------------------------------------------

### Componentes clásicos

1.  Alcance y objetivos\
2.  Inventario de activos\
3.  Evaluación de controles (físicos, lógicos, administrativos)\
4.  Pruebas de penetración\
5.  Análisis de hallazgos\
6.  Informe final y plan de remediación

### Cambios en Cloud

-   Elasticidad: recursos efímeros\
-   API-driven: revisión de logs (CloudTrail)\
-   Multirregión: soberanía y ubicación de datos

------------------------------------------------------------------------

## 2. Enfoques aplicables

-   **CSPM (Revisión de postura):** detectar configuraciones inseguras.\
-   **Auditoría basada en riesgos:** priorización según
    impacto/confidencialidad.\
-   **Pruebas de penetración cloud:** controles de red, IAM, apps.\
-   **Automatización continua (CA):** detección en tiempo real.

------------------------------------------------------------------------

## 3. Plan de auditoría Cloud

### 3.1 Nuevos componentes

-   Identidades (IAM, KMS)\
-   Redes virtuales (VPC, SG, NACL)\
-   Servicios gestionados (S3, RDS, Lambda)\
-   Automatización & CI/CD\
-   Registros y monitoreo (CloudTrail, CloudWatch)

### 3.2 Etapas

1.  **Planeación** → alcance, roles, cronograma\
2.  **Descubrimiento** → inventario de recursos vía API\
3.  **Evaluación de controles** → mapeo a CIS, ISO\
4.  **Pruebas técnicas** → escaneos y exploits\
5.  **Análisis y correlación** → priorización según riesgo\
6.  **Informe y cierre** → resultados y plan de acción

### 3.3 Consideraciones de acceso

-   Roles de solo-lectura para inventario\
-   Roles temporales para pruebas de penetración\
-   Acceso a registros cifrados\
-   Aprobación previa para cambios en recursos

------------------------------------------------------------------------

## 4. Ejecución y revisión

### 4.1 Evidencias

-   **Automáticas:** snapshots, findings de Security Hub\
-   **Manuales:** capturas, exportes de IAM

### 4.2 Conceptos clave

-   **Drift:** diferencia entre IaC y estado real\
-   **Least Privilege:** exceso de permisos\
-   **Segregación de ambientes:** Dev/Test/Prod separados

### 4.3 Ejemplo práctico

1.  Prowler genera reporte CIS\
2.  EventBridge alerta si S3 es público\
3.  Lambda corrige y etiqueta hallazgo

### 4.4 Análisis

-   Agrupación de hallazgos por criticidad\
-   Asignación de responsables y plazos

### 4.5 Informe final

-   **Ejecutivo:** KPIs, tendencias\
-   **Técnico:** evidencias, pasos\
-   **Plan de acción:** quick wins y mejoras a mediano plazo

### 4.6 Automatización de revisión

-   **Security Hub:** consolida hallazgos\
-   **Config Rules + Remediation:** corrige violaciones automáticamente

------------------------------------------------------------------------

## Conclusión

Las auditorías cloud requieren un enfoque **dinámico, basado en APIs y
automatización continua**.\
Aplicando las etapas de planeación a presentación de hallazgos, se
asegura el cumplimiento de **marcos internacionales**.

------------------------------------------------------------------------

## Referencias

-   AWS Security Hub Guidelines\
-   CIS AWS Foundations Benchmark\
-   Cloud Security Alliance -- CCM v4\
-   ISO 19011:2018\
-   NIST SP 800-115
