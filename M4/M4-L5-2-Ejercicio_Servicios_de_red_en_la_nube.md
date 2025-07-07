# 🎯 Desafío: Configuración de VPC Básica en AWS

## Objetivo
Crear una VPC con subredes pública/privada y control de tráfico en AWS Academy.

## 📋 Requisitos previos
- Cuenta activa en AWS Academy
- Acceso a la consola de Amazon VPC

## ⏳ Tiempo estimado
1-2 horas (dependiendo de experiencia)

---

## 🛠️ Paso 1: Crear una VPC personalizada
1. Accede a la consola de AWS:
   - Ve a Services > VPC
2. Crear VPC:
   - Click en "Your VPCs" > Create VPC
   - Configura:
     - Name tag: MiVPC-Desafio
     - IPv4 CIDR: 10.0.0.0/16 (ejemplo)
     - Deja el resto por defecto
   - Click en Create

---

## 🌐 Paso 2: Configurar subredes
### Subred Pública
1. Crear subred:
   - Ve a Subnets > Create subnet
   - Selecciona tu VPC (MiVPC-Desafio)
   - Configura:
     - Name tag: Public-Subnet
     - Availability Zone: us-east-1a (ejemplo)
     - IPv4 CIDR: 10.0.1.0/24
   - Click en Create

2. Asociar Internet Gateway:
   - Ve a Internet Gateways > Create internet gateway
     - Name: IGW-MiVPC
     - Attach a tu VPC

3. Configurar tabla de rutas:
   - Ve a Route Tables
   - Edita la tabla asociada a Public-Subnet:
     - Agrega ruta: 0.0.0.0/0 → Target: IGW-MiVPC

### Subred Privada
1. Crear subred:
   - Mismo proceso, pero con:
     - Name tag: Private-Subnet
     - IPv4 CIDR: 10.0.2.0/24
   - No asociar Internet Gateway

---

## 🔒 Paso 3: Configurar Security Group (Opcional)
1. Crear Security Group:
   - Ve a Security Groups > Create security group
   - Configura:
     - Name: SG-Web-Access
     - VPC: MiVPC-Desafio
   - Agrega reglas:
     - Entrante: HTTP (80), HTTPS (443), SSH (22) desde tu IP
     - Saliente: All traffic

---

## 🚀 Paso 4: Probar comunicación (Opcional)
### En subred pública:
1. Lanzar instancia EC2:
   - Usa AMI Amazon Linux
   - Asigna a Public-Subnet
   - Asocia SG-Web-Access
2. Conectar via SSH:
   bash
   ssh -i "tu-key.pem" ec2-user@<IP-Pública>

### En subred privada:
1. Lanzar instancia sin IP pública
2. Verificar conectividad:
   - Desde la instancia pública:
   bash
   ping <IP-privada>

---

## ➕ Plus: NAT Gateway para subred privada
1. Crear NAT Gateway:
   - Ve a NAT Gateways > Create NAT Gateway
   - Asigna a Public-Subnet y elige Elastic IP
2. Configurar ruta en subred privada:
   - Edita su tabla de rutas:
     - 0.0.0.0/0 → Target: NAT Gateway

---

## ✅ Verificación final
| Componente       | Estado     |
|------------------|------------|
| VPC              | ✔️ Creada  |
| Subred Pública   | ✔️ Con IGW |
| Subred Privada   | ✔️ Aislada |
| Security Group   | ✔️ Reglas  |
| NAT Gateway      | ✔️ (Plus)  |

---

## 📚 Recursos adicionales
- Documentación oficial VPC: https://docs.aws.amazon.com/vpc/index.html
- Guía de NAT Gateway: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html

> 💡 Tip: Usa AWS CloudFormation para automatizar este proceso en futuros proyectos

---

# Desarrollo