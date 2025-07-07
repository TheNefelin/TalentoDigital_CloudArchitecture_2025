# Servicios de Red en la Nube - Fundamentos de Tecnología Cloud

## Introducción
Los servicios de red en la nube permiten interconectar recursos, aislar sistemas y garantizar seguridad en entornos cloud. Incluyen VPC, conexiones dedicadas y gestión de tráfico DNS.

**Aprendizaje esperado**: Comparar servicios de red cloud para resolver problemáticas organizacionales.

---

## 1. ¿Qué es un servicio de red en la nube?
Infraestructuras y configuraciones que permiten comunicación segura y eficiente entre recursos en la nube.

### Beneficios:
- **Escalabilidad**: Ajuste dinámico de ancho de banda.
- **Flexibilidad**: Aislamiento de entornos y redes híbridas.
- **Seguridad**: Controles granulares y cifrado sin hardware adicional.
- **Costo-efectividad**: Elimina inversión en infraestructura física.

### Consideraciones:
- Modelo de responsabilidad compartida (proveedor vs. cliente).
- Cumplimiento normativo (regiones y regulaciones).
- Diseño de alta disponibilidad (redundancia y balanceo).

---

## 2. Virtual Private Cloud (VPC)
### 2.1 Aislación de servicios
Segmentación lógica de redes virtuales para seguridad y privacidad.

### 2.2 Componentes clave:
- **Subred pública**: Acceso a Internet via Internet Gateway.
- **Subred privada**: Acceso restringido (requiere NAT Gateway/VPN).
- **NACLs**: Filtrado de tráfico a nivel de subred (stateless).
- **Grupos de seguridad**: Firewalls a nivel de instancia.

### 2.3 Ventajas vs. Desventajas
| Ventajas | Desventajas |
|----------|-------------|
| Aislamiento estricto | Complejidad en configuraciones multi-región |
| Conexiones cifradas | Gestión adicional de subredes/NACLs |

**Caso de uso**: ERP con BD en subred privada y aplicación web en subred pública.

---

## 3. Conexiones Dedicadas
### 3.1 AWS Direct Connect
Enlace físico privado (50 Mbps - 100 Gbps) entre on-premise y la nube.

### 3.2 Comparación: VPN vs. Direct Connect
| Aspecto       | VPN (IPSec)          | Direct Connect         |
|---------------|---------------------|-----------------------|
| Seguridad     | Cifrado IPSec       | Tráfico privado        |
| Rendimiento   | Depende de Internet | Alta capacidad/baja latencia |
| Costo         | Bajo                | Elevado (enlace físico) |

**Casos de uso**: Migración de grandes volúmenes de datos, aplicaciones sensibles a latencia.

---

## 4. Gestión de Tráfico (Route 53)
Servicio DNS con ruteo inteligente y alta disponibilidad.

### 4.1 Funcionalidades:
- **Registro de dominios** (A, CNAME, MX).
- **Ruteo**: Geográfico, ponderado o failover.
- **Chequeos de salud**: Redirección automática ante fallos.

**Caso de uso**: Aplicación global con endpoints regionales y failover automático.

### 4.2 Consideraciones:
- Mitigación de DDoS.
- Costo por consultas DNS y chequeos de salud.

---

## 5. Resumen Comparativo
| Servicio       | Objetivo                     | Ventajas                          | Desafíos                     |
|----------------|-----------------------------|-----------------------------------|------------------------------|
| VPC            | Aislar redes virtuales      | Control granular y seguridad      | Complejidad de administración|
| VPN Site-to-Site| Conexión cifrada on-premise | Configuración rápida y bajo costo | Dependencia de Internet      |
| Direct Connect | Enlace físico dedicado      | Latencia estable y alta seguridad | Costos elevados              |
| Route 53       | DNS y ruteo inteligente     | Alta disponibilidad global        | Costo por consultas          |

---

## Cierre
Los servicios de red en la nube son clave para arquitecturas seguras y escalables. La elección depende de:
- Requerimientos de ancho de banda/latencia.
- Niveles de seguridad.
- Optimización de costos.

