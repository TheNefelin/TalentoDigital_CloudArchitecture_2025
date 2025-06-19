# Modelos de Implementación de Infraestructura: Casos de Uso

---

## 🏦 Escenario 1 - Banco Nacional

**Descripción:**  
Una entidad financiera con presencia nacional maneja datos sensibles de millones de clientes. Necesita garantizar seguridad, cumplimiento normativo y disponibilidad constante. Tiene presupuesto alto y equipos TI robustos.

**🔐 Modelo propuesto:** Privado

**📝 Justificación:**
- Maneja datos sensibles, por lo tanto tiene un fuerte enfoque en la seguridad.
- Cuenta con presupuesto alto y equipo TI interno bien entrenado.

**💡 Ejemplo real (opcional):**
- *Banco de Chile:* Aunque está migrando algunos servicios a la nube, mantiene muchos sistemas legados en infraestructura privada por temas regulatorios y de control.

---

## 🛒 Escenario 2 - Cadena de retail en expansión

**Descripción:**  
Una empresa de tiendas físicas quiere abrir su canal e-commerce y lanzar una app para clientes. Busca flexibilidad, velocidad de implementación y bajo costo inicial. Su infraestructura actual es limitada.

**🌐 Modelo propuesto:** Público

**📝 Justificación:**
- La empresa busca flexibilidad, rápida implementación y bajo costo inicial.
- Su infraestructura actual es limitada, lo que favorece el uso de nube pública.

**💡 Ejemplo real (opcional):**
- *Empresa maderera:* Migró temporalmente a la nube pública para realizar pruebas. Posteriormente eliminó todo y volvió a un entorno privado.

---

## 🏭 Escenario 3 - Fábrica industrial

**Descripción:**  
Una compañía de manufactura opera con sensores IoT que recolectan datos en tiempo real. Necesita almacenar algunos datos críticos en servidores locales, pero también procesar analítica avanzada en la nube.

**🔄 Modelo propuesto:** Híbrido

**📝 Justificación:**
- Almacena datos críticos localmente por razones de seguridad o latencia (privado).
- Utiliza la nube pública para procesamiento en tiempo real y analítica avanzada.

**💡 Ejemplo real (opcional):**
- *Empresa GPS en Chile:* Usaba la nube pública para análisis y logs, mientras los datos históricos se almacenaban en servidores privados.

---
