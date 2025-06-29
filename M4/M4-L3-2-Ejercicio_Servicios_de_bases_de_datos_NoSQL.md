# 🧪 Desafío: Configuración e Implementación de una Base de Datos NoSQL en AWS

## 🎯 Objetivo
Configurar e implementar un servicio de base de datos NoSQL (Amazon DynamoDB) en la nube utilizando tu cuenta de AWS Academy, realizando operaciones básicas CRUD para familiarizarte con su funcionamiento.

---

## 🛠️ Herramientas y Entorno
- AWS Academy
- Consola web de Amazon DynamoDB

---

## ⏱️ Tiempo Estimado
1 a 2 horas, según tu experiencia con la consola AWS.

---

## ✅ Paso 1: Crear una tabla DynamoDB

1. Inicia sesión en tu cuenta de **AWS Academy**.
2. Abre el servicio **DynamoDB** desde la consola.
3. Haz clic en **"Create table"**.
4. Configura la tabla:
   - **Table name:** `Estudiantes`
   - **Partition key:** `idEstudiante` (tipo: String)
5. Deja los valores por defecto y haz clic en **"Create table"**.

---

## ✅ Paso 2: Insertar ítems

1. Abre la tabla `Estudiantes` > pestaña **Items** > **Create item**.
2. Inserta los siguientes registros:

```json
{
  "idEstudiante": "E001",
  "nombre": "Ana",
  "curso": "Matemáticas",
  "nota": 90
}
```
```json
{
  "idEstudiante": "E002",
  "nombre": "Luis",
  "curso": "Física",
  "nota": 85
}
```
```json
{
  "idEstudiante": "E003",
  "nombre": "Carla",
  "curso": "Historia",
  "nota": 78
}

```

3. JSON de AWS

```json
{
  "idEstudiante": { "S": "E001" },
  "nombre": { "S": "Ana" },
  "curso": { "S": "Matemáticas" },
  "nota": { "N": "90" }
}
```
```json
{
  "idEstudiante": { "S": "E002" },
  "nombre": { "S": "Luis" },
  "curso": { "S": "Física" },
  "nota": { "N": "85" }
}
```
```json
{
  "idEstudiante": { "S": "E003" },
  "nombre": { "S": "Carla" },
  "curso": { "S": "Historia" },
  "nota": { "N": "78" }
}
```

---

### ✅ Paso 3: Leer y consultar datos

#### 🔎 Scan (leer todos los ítems)

- Ve a **Explore table items** > opción **Scan** > clic en **Run** para visualizar todos los registros insertados.

#### 🔍 Query (consultar por clave primaria)

- Cambia a opción **Query**:
  - **Partition key:** `idEstudiante`
  - **Operator:** `=`
  - **Value:** `"E001"`
- Haz clic en **Run** para ver el resultado de la búsqueda.

---

### ➕ Plus: Crear un índice secundario (GSI)

1. Ve a la pestaña **Indexes** > clic en **Create index**.
2. Configura lo siguiente:
   - **Index name:** `CursoIndex`
   - **Partition key:** `curso` (tipo: String)
3. Haz clic en **Create index**.
4. Cuando el índice esté activo, podrás hacer queries por `curso`.

---

### ➕ Plus: Habilitar Streams

1. En tu tabla, ve a la pestaña **Exports and streams**.
2. En la sección **DynamoDB stream details**, haz clic en **Enable stream**.
3. Selecciona **New and old images**.
4. Confirma con **Enable**.

---

### 📘 Recursos adicionales

- [Documentación oficial de DynamoDB](https://docs.aws.amazon.com/amazondynamodb/index.html)

---

### 🧠 Conclusión

Con este ejercicio práctico habrás logrado:

- Realizar operaciones CRUD básicas en DynamoDB.
- Consultar ítems mediante **Scan** y **Query**.
- Crear un índice secundario para realizar búsquedas por otros campos.
- Habilitar **Streams** para monitorear cambios en tiempo real.

¡Buen trabajo completando el desafío! 🎉

---

# Desarrollo

<img src="..\Img\M4\L3\Ejercicio\M4-L3-Ejercicio-01.png">
<img src="..\Img\M4\L3\Ejercicio\M4-L3-Ejercicio-02.png">
<img src="..\Img\M4\L3\Ejercicio\M4-L3-Ejercicio-03.png">
<img src="..\Img\M4\L3\Ejercicio\M4-L3-Ejercicio-04.png">
<img src="..\Img\M4\L3\Ejercicio\M4-L3-Ejercicio-05.png">
<img src="..\Img\M4\L3\Ejercicio\M4-L3-Ejercicio-06.png">
<img src="..\Img\M4\L3\Ejercicio\M4-L3-Ejercicio-07.png">
<img src="..\Img\M4\L3\Ejercicio\M4-L3-Ejercicio-08.png">
