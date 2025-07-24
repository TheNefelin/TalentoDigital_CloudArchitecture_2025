
# ✅ Resolución del Ejercicio: Arquitectura en la Nube para Aplicación Web

## 🎯 Desafío
Diseñar una arquitectura de nube (pública, privada o híbrida) para una aplicación web utilizando AWS Academy, identificando los componentes clave y justificando su uso.

---

## 🌐 Arquitectura Elegida: Híbrida

Se opta por una **arquitectura híbrida**, combinando recursos de nube pública y privada para aprovechar la escalabilidad de la nube pública con la seguridad de entornos privados.

---

## 🧩 Componentes Clave y Justificación

- **VPC (Virtual Private Cloud):**  
  Aísla y controla el entorno de red. Permite definir subredes y políticas de acceso.

- **Subred Pública:**  
  - **Elastic Load Balancer (ELB):** Distribuye el tráfico entrante de manera uniforme entre las instancias de front-end.  
  - **Instancias EC2 (Front-End):** Servidores web que responden a solicitudes de los usuarios.

- **Subred Privada:**  
  - **Instancias EC2 (Back-End):** Procesan la lógica de negocio con acceso restringido.  
  - **Amazon RDS:** Base de datos relacional segura, utilizada para almacenar datos sensibles.

- **Conexión Segura (VPN o Direct Connect):**  
  Permite conectar la nube pública con sistemas privados, asegurando la transferencia segura de datos.

---

## 🖼 Diagrama de Arquitectura (Descriptivo)

```
+----------------------------+
|          VPC              |
| +--------+  +----------+  |
| | Pública|  | Privada  |  |
| | Subred |  | Subred   |  |
| |        |  |          |  |
| |  ELB   |  |  RDS     |  |
| |  EC2   |  |  EC2 BE  |  |
| +--------+  +----------+  |
|        \        /         |
|         \______/ VPN      |
+----------------------------+
```

---

## ✅ Beneficios del Diseño

- **Alta disponibilidad:** Uso de ELB y escalado automático.  
- **Seguridad:** Datos sensibles aislados en la subred privada.  
- **Flexibilidad:** Adaptable al crecimiento y cambios futuros.

---

## ⚠️ Posibles Limitaciones

- Mayor complejidad en integración y gestión.  
- Costos adicionales por conexiones seguras y servicios gestionados.

---

## 🔐 Estrategias de Seguridad y Control de Costos

- **Seguridad:**  
  - Uso de grupos de seguridad y listas de control de acceso.  
  - Encriptación en tránsito y en reposo.  
  - Políticas de IAM estrictas.

- **Costos:**  
  - Monitoreo con AWS CloudWatch.  
  - Escalado automático para optimizar el uso de recursos.  
  - Apagar instancias en tiempos de inactividad.

---

## 📄 Conclusión

La arquitectura híbrida ofrece un balance ideal entre seguridad, rendimiento y escalabilidad. Es adecuada para aplicaciones web que manejan información sensible pero requieren responder a alta demanda.

