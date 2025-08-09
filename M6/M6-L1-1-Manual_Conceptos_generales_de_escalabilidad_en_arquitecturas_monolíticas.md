
# 📚 Conceptos Generales de Escalabilidad en Arquitecturas Monolíticas

## 🧑‍💻 Introducción
Este manual explica las bases y estrategias para escalar arquitecturas monolíticas sin modificar su estructura central. 
Se revisan dos enfoques principales:
- **Escalamiento vertical**: Aumentar recursos en un solo servidor.
- **Escalamiento horizontal**: Replicar la aplicación completa en varias instancias.

También se abordan temas clave como:
- Externalización del estado.
- Uso de cachés distribuidos.
- Manejo de sesiones y consistencia de datos.

## 🎯 Aprendizaje esperado
Contrastar características de la arquitectura monolítica con distintos enfoques de escalamiento para resolver necesidades organizacionales.

## 1️⃣ Conceptos Generales
- **Escalabilidad**: Capacidad de un sistema para manejar más carga o datos sin perder rendimiento.
- Factores clave: capacidad de crecimiento, rendimiento y optimización de recursos.

## 2️⃣ Arquitecturas Monolíticas
- **Definición**: Todos los módulos integrados en una única unidad desplegable.
- **Características**: Alta cohesión, fuerte acoplamiento, despliegue único.

## 3️⃣ Ventajas y Desventajas (vs. Microservicios)
**Ventajas**:
- Simplicidad inicial.
- Baja latencia interna.
- Integración unificada.

**Desventajas**:
- Escalabilidad limitada.
- Mantenimiento complejo.
- Actualizaciones rígidas.

| Aspecto          | Monolítica                  | Microservicios               |
|------------------|-----------------------------|------------------------------|
| Desarrollo       | Rápido y simple              | Requiere planificación       |
| Escalabilidad    | Global (vertical)            | Independiente por servicio   |
| Mantenimiento    | Complejo en grandes sistemas | Modular                      |
| Comunicación     | Directa, baja latencia       | Por red, posible mayor latencia |

## 4️⃣ Casos de Uso
- Aplicaciones pequeñas/medianas.
- Proyectos de desarrollo rápido.
- Sistemas con carga predecible.

Ejemplos: ERP, CRM, aplicaciones web internas.

## 5️⃣ Importancia de la Escalabilidad
- Mantener tiempos de respuesta.
- Optimizar uso de recursos.
- Evitar cuellos de botella.

## 6️⃣ Enfoques de Escalabilidad
- **Vertical**: Más CPU, RAM o almacenamiento en un servidor.
- **Horizontal**: Varias instancias con balanceador de carga.

**Requisitos para horizontal**:
- Almacenamiento de sesiones en sistemas externos (Redis, Memcached).
- Cachés distribuidos.
- Bases de datos compartidas.

## 7️⃣ Comparativa Vertical vs. Horizontal
| Característica   | Vertical                    | Horizontal                   |
|------------------|-----------------------------|------------------------------|
| Implementación   | Más recursos en un servidor | Varias instancias            |
| Costo inicial    | Menor                       | Mayor                        |
| Punto único fallo| Alto                        | Bajo                         |
| Flexibilidad     | Limitada                    | Alta                         |

## 8️⃣ Estrategias de Particionamiento
- **Datos**: 
  - Horizontal: por criterios (ej. región).
  - Vertical: por columnas/funciones.
- **Carga**: balanceadores o proxies.

## 9️⃣ Escalabilidad de la Capa de Datos
- Optimización de consultas (índices, vistas).
- Replicación para lectura.
- Sharding para paralelizar.

## 🔟 Escalabilidad de la Capa de Aplicación
- Clustering.
- Balanceo interno.
- Procesos paralelos para tareas críticas.

## ✍️ Cierre
El manual provee una guía completa para escalar arquitecturas monolíticas, destacando ventajas, desventajas, enfoques y técnicas que permiten mantener el rendimiento ante el crecimiento.

## 📚 Referencias
- [Patterns of Enterprise Application Architecture – Martin Fowler](https://martinfowler.com/books/eaa.html)
- [MySQL Scalability](https://dev.mysql.com/doc/refman/8.0/en/scalability.html)
- [NGINX Load Balancing](https://www.nginx.com/resources/glossary/load-balancing/)
- [Software Engineering – Ian Sommerville](https://www.pearson.com/us/higher-education/program/Sommerville-Software-Engineering-10th-Edition/PGM363462.html)
