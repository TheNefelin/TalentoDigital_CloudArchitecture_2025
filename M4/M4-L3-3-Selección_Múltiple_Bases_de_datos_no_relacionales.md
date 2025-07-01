# 📚 Preguntas y Respuestas sobre Bases de Datos NoSQL

## ✅ Pregunta 1

**Enunciado:**
Para una aplicación de registro de ubicaciones de usuarios en tiempo real, ¿qué ventaja ofrece una base de datos NoSQL de tipo documento?

**Respuesta correcta:**
c. Facilita cambios frecuentes en la estructura de los datos sin necesidad de modificar un esquema fijo

**Explicación:**
Las bases de datos documentales son ideales para esquemas flexibles. En aplicaciones de ubicación geográfica, donde los datos pueden cambiar frecuentemente, la estructura flexible permite agregar nuevos campos sin afectar la base de datos global.

---

## ✅ Pregunta 2

**Enunciado:**
En un escenario donde se requieren altas tasas de lectura y escritura para procesar millones de solicitudes de usuarios, ¿cuál es una característica esencial de las bases de datos NoSQL?

**Respuesta correcta:**
b. Escalabilidad horizontal que permita distribuir la carga en múltiples nodos

**Explicación:**
Las bases NoSQL escalan horizontalmente para soportar millones de operaciones concurrentes. Esto permite mantener alta disponibilidad y rendimiento agregando nodos al clúcster.

---

## ✅ Pregunta 3

**Enunciado:**
Se planea implementar un sistema de recomendación de productos en línea. ¿Cuál de estos tipos de bases de datos NoSQL resulta más adecuado para representar relaciones complejas entre clientes, productos y categorías?

**Respuesta correcta:**
a. Grafos

**Explicación:**
Las bases de datos de grafos son ideales para modelar relaciones entre entidades. Permiten consultas complejas como recomendaciones basadas en afinidad o comportamiento compartido entre usuarios y productos.

---

## ✅ Pregunta 4

**Enunciado:**
Verdadero o Falso: “Una base de datos NoSQL columnar es adecuada para análisis de grandes volúmenes de datos, ya que permite procesar rápidamente agregaciones sobre columnas específicas.”

**Respuesta correcta:**
Verdadero

**Explicación:**
Las bases columnar almacenan los datos por columnas, lo que permite procesar grandes volúmenes de datos de manera eficiente y realizar consultas analíticas rápidas sobre campos específicos.

---

## ✅ Pregunta 5

**Enunciado:**
Verdadero o Falso: “Amazon DynamoDB (un servicio NoSQL en la nube) utiliza un modelo de datos clave-valor y está optimizado para alta disponibilidad y baja latencia.”

**Respuesta correcta:**
Verdadero

**Explicación:**
DynamoDB es una base de datos NoSQL de tipo clave-valor que ofrece baja latencia, alta disponibilidad y escalabilidad automática. Es ideal para aplicaciones que requieren respuesta inmediata.

---

## ✅ Pregunta 6

**Enunciado:**
En un sistema de mensajería instantánea que maneja conversaciones entre millones de usuarios, ¿por qué razón podrías preferir una base de datos NoSQL?

**Respuesta correcta:**
b. Porque maneja grandes volúmenes de datos con escalabilidad horizontal y respuesta rápida

**Explicación:**
La escalabilidad horizontal y el rendimiento predecible hacen que NoSQL sea ideal para sistemas de mensajería con alto tráfico. Ofrece baja latencia incluso en picos de uso intensivo.

---

## ✅ Pregunta 7

**Enunciado:**
Si una organización necesita agregar nuevos atributos a los registros de usuarios de manera frecuente y no desea realizar cambios estructurales complejos en su base de datos, ¿qué tipo de base de datos NoSQL recomienda?

**Respuesta correcta:**
c. Documental

**Explicación:**
Las bases documentales permiten almacenar datos en forma de JSON con estructura flexible. Son ideales cuando se necesita agregar nuevos atributos sin cambiar el esquema global.

---

## ✅ Pregunta 8

**Enunciado:**
Verdadero o Falso: “Los modelos de consistencia eventual son típicos en las bases de datos NoSQL, permitiendo alta disponibilidad a costa de demorar la sincronización de datos entre nodos.”

**Respuesta correcta:**
Verdadero

**Explicación:**
La consistencia eventual es común en NoSQL y sistemas distribuidos. Prioriza disponibilidad y tolerancia a particiones, permitiendo que los datos se sincronicen con el tiempo.

---
