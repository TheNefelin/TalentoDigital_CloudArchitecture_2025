# Desafío: Desplegar y Probar un Servicio de Cómputo en la Nube

## 🎯 Objetivo

Lanzar una instancia de cómputo en la nube utilizando **Amazon EC2** desde tu cuenta de **AWS Academy**, y verificar su funcionamiento conectándote por SSH y desplegando un servicio web básico (“Hello World”).

---

## 📌 Actividades

### 1. Lanzar una instancia EC2

**Tipo sugerido:**  
`t2.micro` o `t3.micro` (gratis dentro del Free Tier si está disponible)

**Pasos:**

1. Inicia sesión en [AWS Academy](https://awsacademy.instructure.com/).
2. Accede al servicio **EC2** desde la consola de AWS.
3. Haz clic en **Launch Instance**.
4. Configura los siguientes elementos:
   - **Nombre:** HelloWorldEC2
   - **AMI:** Amazon Linux 2 (u otra compatible)
   - **Tipo de instancia:** `t2.micro` o `t3.micro`
   - **Par de claves (Key pair):** Crear uno nuevo o usar uno existente. Guarda el archivo `.pem`.
   - **Red y subred:** Utiliza las predeterminadas (VPC y subnet por defecto).
   - **Grupo de seguridad:**
     - Permitir tráfico **SSH (puerto 22)** desde tu IP.
     - Permitir tráfico **HTTP (puerto 80)** desde cualquier origen (`0.0.0.0/0`).

5. Haz clic en **Launch Instance**.

---

### 2. Verificar su funcionamiento

#### A. Conexión vía SSH

1. Abre un terminal (o usa PuTTY en Windows).
2. Conéctate usando el comando:

```bash
ssh -i "tu-clave.pem" ec2-user@<IP-PÚBLICA>
```

> Asegúrate de que el archivo `.pem` tenga los permisos correctos:

```bash
chmod 400 tu-clave.pem
```

---

#### B. Desplegar un servidor web básico (“Hello World”)

1. Ya dentro de la instancia, instala Apache:

```bash
sudo yum update -y
sudo yum install httpd -y
```

2. Inicia el servicio:

```bash
sudo systemctl start httpd
sudo systemctl enable httpd
```

3. Crea una página HTML básica:

```bash
echo "Hello World desde EC2" | sudo tee /var/www/html/index.html
```

4. Abre tu navegador y visita: `http://<IP-PÚBLICA>`

---

## ✅ Resultado Esperado

- Instancia EC2 lanzada correctamente.
- Conexión por **SSH** establecida.
- Página web de prueba visible desde el navegador.

---

## 🔎 Exploración Opcional (Plus ➕)

- Configura **Auto Scaling Group** para escalar EC2 automáticamente.
- Cambia el tipo de instancia manualmente para evaluar escalabilidad.
- Consulta logs del servidor:

```bash
sudo cat /var/log/httpd/access_log
```

---

## 🛠 Requisitos y Herramientas

- Cuenta activa en **AWS Academy**.
- Acceso a la consola de **EC2**.
- (Opcional) Cliente SSH:
  - PuTTY (Windows)
  - OpenSSH (Linux/macOS)

---

## ⏱ Tiempo Estimado

- **1 a 2 horas**, según tu experiencia con despliegue y configuración.

---

## 📚 Recursos de Apoyo

- [Amazon EC2 – Documentación oficial](https://docs.aws.amazon.com/es_ec2/index.html)
- [Amazon Linux – Guía de usuario](https://docs.aws.amazon.com/amazon-linux/)
- [Guía de grupos de seguridad EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)

---

## 🧠 Reflexión Final

Este desafío te permite practicar principios fundamentales de servicios de cómputo como:

- **Elasticidad**
- **Pago por uso**
- **Automatización y despliegue rápido**

Y comprobar el funcionamiento real de un entorno cloud.

---

# Desarrollo

## Caso 1

<img src="..\Img\M4\L4\Ejercicio\M4-L4-Ejercicio-01.png">
<img src="..\Img\M4\L4\Ejercicio\M4-L4-Ejercicio-02.png">
<img src="..\Img\M4\L4\Ejercicio\M4-L4-Ejercicio-03.png">
<img src="..\Img\M4\L4\Ejercicio\M4-L4-Ejercicio-04.png">

- [Usuario de Windows: Uso de SSH para conectarse
](https://labs.vocareum.com/web/4167329/4299576.0/ASNLIB/public/docs/lang/es-es/README.html?vockey=f89ce645f829c1a0904304c4a4d0d451e954df78d817cda84241cdb9aa964845#sshwindows)

<img src="..\Img\M4\L4\Ejercicio\M4-L4-Ejercicio-05.png">
<img src="..\Img\M4\L4\Ejercicio\M4-L4-Ejercicio-06.png">
<img src="..\Img\M4\L4\Ejercicio\M4-L4-Ejercicio-07.png">
<img src="..\Img\M4\L4\Ejercicio\M4-L4-Ejercicio-08.png">
<img src="..\Img\M4\L4\Ejercicio\M4-L4-Ejercicio-09.png">
<img src="..\Img\M4\L4\Ejercicio\M4-L4-Ejercicio-10.png">
<img src="..\Img\M4\L4\Ejercicio\M4-L4-Ejercicio-11.png">
<img src="..\Img\M4\L4\Ejercicio\M4-L4-Ejercicio-12.png">
<img src="..\Img\M4\L4\Ejercicio\M4-L4-Ejercicio-13.png">
<img src="..\Img\M4\L4\Ejercicio\M4-L4-Ejercicio-14.png">
<img src="..\Img\M4\L4\Ejercicio\M4-L4-Ejercicio-15.png">