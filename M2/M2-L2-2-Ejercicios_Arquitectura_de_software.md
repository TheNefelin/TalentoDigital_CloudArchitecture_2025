
# Desafío: Escenarios de Calidad para un Sistema de Gestión de Reservas en Línea

## 1. Atributos de Calidad Seleccionados

### 1.1 Seguridad
**Relevancia:** Protege los datos sensibles de los usuarios y garantiza que solo los usuarios autorizados accedan al sistema.

### 1.2 Rendimiento
**Relevancia:** Asegura tiempos de respuesta rápidos y capacidad para manejar múltiples usuarios simultáneamente, especialmente durante temporadas altas.

### 1.3 Usabilidad
**Relevancia:** Facilita la interacción del usuario con el sistema, aumentando la eficiencia y satisfacción del cliente.

---

## 2. Escenarios de Calidad

### 2.1 Seguridad

| Estímulo                                      | Contexto                                  | Respuesta Esperada                                       | Métrica de Respuesta                      |
|----------------------------------------------|-------------------------------------------|----------------------------------------------------------|-------------------------------------------|
| Intento de inicio de sesión con credenciales inválidas | Usuario intenta acceder desde un navegador desconocido | Denegar el acceso y registrar el intento                  | Tiempo de detección < 2s, registro en log |
| Ataque de inyección SQL                      | Envío de formulario con campos manipulados | El sistema bloquea el intento y lo registra               | 100% de ataques detectados y bloqueados   |
| Acceso a datos sensibles                     | Usuario intenta acceder a datos ajenos     | Mostrar mensaje de acceso denegado                        | 0% de acceso no autorizado                 |

### 2.2 Rendimiento

| Estímulo                                | Contexto                                 | Respuesta Esperada                                 | Métrica de Respuesta          |
|----------------------------------------|------------------------------------------|----------------------------------------------------|-------------------------------|
| 1000 usuarios acceden simultáneamente  | Día festivo con alta demanda             | El sistema mantiene operatividad y tiempos de respuesta aceptables | Respuesta < 2 segundos       |
| Carga masiva de reservas               | Operación en lote por backend            | Se procesa en menos de 5 minutos                   | Tiempo < 5 minutos            |
| Búsqueda de disponibilidad             | Usuario realiza búsqueda estándar        | Resultados mostrados rápidamente                   | Tiempo de respuesta < 1 segundo |

### 2.3 Usabilidad

| Estímulo                          | Contexto                          | Respuesta Esperada                              | Métrica de Respuesta                     |
|----------------------------------|-----------------------------------|-------------------------------------------------|------------------------------------------|
| Usuario nuevo ingresa al sistema| Primera interacción               | Puede completar una reserva sin ayuda           | Tasa de éxito del 95%                    |
| Usuario accede desde móvil      | Acceso a través de navegador móvil| La interfaz se adapta automáticamente           | Cumplimiento de diseño responsivo 100%   |
| Usuario busca ayuda             | Durante el proceso de reserva     | Encuentra una sección de ayuda contextual       | Tiempo para encontrar ayuda < 15 segundos|

---

## 3. Diagrama de Arquitectura

![Diagrama de Arquitectura del Sistema de Reservas](https://i.imgur.com/JqHkVRj.png)

**Descripción:**
- Frontend (Web y Móvil): Aplicación React + diseño responsivo.
- API Gateway: Administra solicitudes y redirecciona al microservicio correspondiente.
- Microservicios: Reservas, Autenticación, Catálogo, Notificaciones.
- Base de Datos: MySQL (reservas) y MongoDB (logs).
- Servicios de Seguridad: Autenticación JWT, Firewall Web, Monitor de intrusiones.
- CDN y Load Balancer: Mejoran el rendimiento y disponibilidad.

---

## 4. Conclusión

Estos escenarios de calidad están diseñados para garantizar que el sistema de gestión de reservas sea seguro, rápido y fácil de usar. La arquitectura propuesta facilita escalar los servicios, proteger los datos y proporcionar una experiencia de usuario satisfactoria.

---
