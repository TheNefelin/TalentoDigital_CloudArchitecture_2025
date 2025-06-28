# 📊 Análisis de Caso: Servicios de Bases de Datos Relacionales en la Nube

## 🏢 Situación Inicial

Una startup de comercio electrónico llamada **ShopNow** ha venido utilizando un servidor local para almacenar su información de productos, usuarios y pedidos. Con el crecimiento del negocio, han comenzado a enfrentar problemas de **rendimiento y disponibilidad**. 

El equipo de TI propone **migrar la base de datos a la nube**, aprovechando la alta disponibilidad, escalabilidad y el plan gratuito de AWS. Se optará por motores sin licencias adicionales como **MySQL o PostgreSQL**. También se requiere contar con **backups automáticos** y mecanismos simples de recuperación ante fallas.

## 👨‍💻 Rol Asignado

Asumes el rol de **Administrador de Bases de Datos (DBA)** encargado de:
- Diseñar, crear y configurar una instancia de Amazon RDS bajo el plan gratuito.
- Asegurar la seguridad y eficiencia en el acceso a datos.
- Preparar el entorno para futuras necesidades de escalado.

## ✅ Tareas a Realizar

### 1. Selección e Implementación del Motor de Base de Datos
- Ingresar a AWS Academy o AWS Free Tier.
- Crear una instancia RDS con MySQL o PostgreSQL.
- Seleccionar tamaño adecuado para una startup (por ejemplo, `db.t2.micro`).
- **Justificación del motor elegido**:
  - *MySQL*: Amplia comunidad, buena compatibilidad, ideal para proyectos pequeños-medianos.
  - *PostgreSQL*: Más potente en funciones avanzadas (JSONB, transacciones complejas), ideal si se requiere más flexibilidad futura.

### 2. Configuración de Seguridad y Accesibilidad
- Configurar **grupos de seguridad (Security Groups)** para permitir solo acceso desde:
  - IP local del DBA
  - Instancias de aplicación en la misma VPC
- Habilitar:
  - **Cifrado en tránsito (TLS/SSL)**
  - **Cifrado en reposo** (si el motor y plan lo permiten)

### 3. Diseño del Esquema y Creación de Tablas

Esquema básico:

```sql 
CREATE TABLE usuarios (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  correo VARCHAR(100) UNIQUE,
  contraseña VARCHAR(255)
);

CREATE TABLE productos (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  precio DECIMAL(10, 2),
  stock INT
);

CREATE TABLE pedidos (
  id SERIAL PRIMARY KEY,
  usuario_id INT REFERENCES usuarios(id),
  fecha DATE,
  monto_total DECIMAL(10, 2)
);
```

### 4. Respaldo y Restauración
- Activar **backups automáticos** en Amazon RDS.
- Realizar un **snapshot manual**.
- Pasos para restaurar desde snapshot:
  1. Ir a RDS > Snapshots
  2. Seleccionar snapshot y click en "Restore Snapshot"
  3. Crear nueva instancia desde dicho punto

### 5. Optimización y Monitoreo
- Habilitar métricas en **Amazon CloudWatch**:
  - Uso de CPU
  - Conexiones activas
  - Latencia de lectura/escritura
  - IOPS

📌 **Métricas críticas**:
- `DatabaseConnections`
- `ReadLatency` / `WriteLatency`
- `FreeableMemory`
- `CPUUtilization`

### 6. Prueba de Escalabilidad (Opcional)
- Para escalar, cambiar de `db.t2.micro` a `db.t3.medium` o superior.
- Para mayor carga de lectura, implementar **read replicas**.
- También es posible escalar almacenamiento sin interrupciones.

## 📬 Entregables Esperados

### 1. Informe escrito
- Elección y justificación del motor de base de datos
- Configuración de seguridad (Security Groups, cifrado)
- Diseño de tablas (con `CREATE TABLE` o diagrama)
- Activación de backups automáticos y snapshot manual
- Métricas clave en CloudWatch
- Reflexión sobre la escalabilidad futura

### 2. Evidencias gráficas
- Captura de pantalla de:
  - Instancia RDS creada
  - Tablas y esquema de base de datos
  - Configuración de backups y snapshots

### 3. Conclusiones
- **Ventajas frente a on-premise**:
  - Fácil despliegue
  - Alta disponibilidad
  - Reducción de tareas operativas

- **Consideraciones importantes**:
  - Control de costos en el tiempo
  - Configuración correcta de seguridad y acceso

- **Posibles pasos futuros**:
  - Escalado automático
  - Uso de read replicas
  - Migración a Aurora para mayor rendimiento

---

[Calculadora AWS](https://calculator.aws/#/?nc2=pr)

# Desarrollo

<img src="..\Img\M4\L2\Caso\M4-L2-Caso-01.png">
<img src="..\Img\M4\L2\Caso\M4-L2-Caso-02.png">
<img src="..\Img\M4\L2\Caso\M4-L2-Caso-03.png">
<img src="..\Img\M4\L2\Caso\M4-L2-Caso-04.png">
<img src="..\Img\M4\L2\Caso\M4-L2-Caso-05.png">
<img src="..\Img\M4\L2\Caso\M4-L2-Caso-06.png">
<img src="..\Img\M4\L2\Caso\M4-L2-Caso-07.png">
<img src="..\Img\M4\L2\Caso\M4-L2-Caso-08.png">
<img src="..\Img\M4\L2\Caso\M4-L2-Caso-09.png">
<img src="..\Img\M4\L2\Caso\M4-L2-Caso-10.png">
<img src="..\Img\M4\L2\Caso\M4-L2-Caso-11.png">
<img src="..\Img\M4\L2\Caso\M4-L2-Caso-12.png">
<img src="..\Img\M4\L2\Caso\M4-L2-Caso-13.png">
<img src="..\Img\M4\L2\Caso\M4-L2-Caso-14.png">
<img src="..\Img\M4\L2\Caso\M4-L2-Caso-15.png">