# 📬 Desafío: Configurar un Servicio de Notificación o Mensajería en AWS

## 🎯 Objetivo
Poner en práctica los fundamentos de notificación y mensajería usando **Amazon SNS** o **Amazon SQS** desde tu cuenta de **AWS Academy**.

---

## ✅ Opción A: Amazon SNS (Modelo Publicador–Suscriptor)

### 1. Accede a la Consola de AWS
- Inicia sesión en tu cuenta de **AWS Academy**.
- En el buscador, escribe y selecciona **Amazon SNS**.

### 2. Crear un Tópico SNS
- Haz clic en **Create topic**.
- Tipo: `Standard`.
- Nombre: `notificaciones-demo`.
- Guarda el tópico y copia el ARN generado.

### 3. Crear una Suscripción
- Dentro del tópico, ve a **Subscriptions** → **Create subscription**.
- Protocolo: `Email`.
- Endpoint: ingresa tu correo electrónico.
- Confirma la suscripción desde tu bandeja de entrada (verifica spam si no llega).

### 4. Publicar un Mensaje
- Regresa al tópico y haz clic en **Publish message**.
- Completa los campos:
  - Subject: `Mensaje de prueba SNS`
  - Message body: `Este es un mensaje enviado desde Amazon SNS`
- Haz clic en **Publish message**.

### 5. Verificar Entrega
- Revisa tu correo electrónico para ver si llegó el mensaje.
- También puedes ir a la pestaña **Metrics** o **CloudWatch** y revisar:
  - `NumberOfMessagesPublished`
  - `NumberOfNotificationsDelivered`

---

## ✅ Opción B: Amazon SQS (Modelo de Cola)

### 1. Crear una Cola
- Desde la consola de AWS, busca y entra a **Amazon SQS**.
- Haz clic en **Create queue**.
- Tipo: `Standard`.
- Nombre: `miCola`.
- Configura los parámetros básicos (puedes dejar por defecto).

### 2. Enviar un Mensaje
- Dentro de la cola, haz clic en **Send and receive messages**.
- En `Message body`, escribe: `Hola desde SQS`.
- Haz clic en **Send message**.

### 3. Recibir un Mensaje
- En la misma vista, haz clic en **Poll for messages**.
- Si hay mensajes, aparecerán listados.
- Selecciona uno y revisa el contenido.

### 4. Borrar Mensaje
- Después de leer el mensaje, haz clic en **Delete** para eliminarlo.
- Esto asegura que fue procesado correctamente.

### 5. (Opcional) Integrar SNS + SQS
- Ve al tópico SNS → **Subscriptions** → **Create subscription**.
- Protocolo: `Amazon SQS`.
- Elige tu cola como destino.
- Ahora, cada publicación en SNS se envía también a la cola SQS.

---

## 🛡️ Consideraciones Adicionales

### Seguridad
- Configura políticas de acceso para controlar quién puede publicar o recibir mensajes.
- Habilita cifrado con **AWS KMS** si lo deseas.

### Retención de Mensajes (solo SQS)
- Puedes ajustar el período de retención hasta 14 días.

---

## ⌛ Tiempo Estimado
Entre **1 y 2 horas**, dependiendo de tu experiencia previa con la consola de AWS.

---

## ➕ Extras (Plus)
- Usar **SNS** para enviar notificaciones por **SMS** o **email**.
- Configurar retención personalizada en **SQS**.
- Combinar **SNS + SQS** para simular el patrón pub-sub con consumidores desacoplados.

---

## ⚠️ Condición
No se requiere una entrega formal. Puedes compartir capturas o logs con tus compañeros para fomentar el aprendizaje colaborativo.

---

## Desarrollo

### SNS

<img src="..\Img\M4\L6\M4-L6-Ejercicio-01.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-02.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-03.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-04.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-05.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-06.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-07.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-08.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-09.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-10.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-11.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-12.png">

### SQS

<img src="..\Img\M4\L6\M4-L6-Ejercicio-13.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-14.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-15.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-16.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-17.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-18.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-19.png">
<img src="..\Img\M4\L6\M4-L6-Ejercicio-20.png">
