```mermaid
graph TD
  VPC[VPC (Red Virtual Privada)]
  
  VPC --> SubredPublica[Subred Pública]
  VPC --> SubredPrivada[Subred Privada]
  
  SubredPublica --> EC2Publica[EC2 (Servidor Público)]
  SubredPrivada --> EC2Privada[EC2 (Servidor Privado)]
  
  VPC --> IGW[Internet Gateway (IGW)]
  
  IGW -->|Conexión a Internet| Internet[Internet]
  
  SubredPublica -->|Tabla de rutas apunta a IGW| RutasPublicas[Tabla de Rutas Pública]
  SubredPrivada -->|Tabla de rutas no apunta a IGW| RutasPrivadas[Tabla de Rutas Privada]
  
  VPC --> ACL[Network ACL]
  ACL --> SubredPublica
  ACL --> SubredPrivada
```