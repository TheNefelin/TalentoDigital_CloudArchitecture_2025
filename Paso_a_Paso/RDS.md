
## **RDS**: Relational Database Service
### DRS Subnet Group
- **Name**: artema-rds-sng
- **Description**: Private subnet group para PostgreSQL
- **VPC**: artema-vpc
- **Availability Zones**:
    - us-east-1a
    - us-east-1b
- **Subnets**:
    - artema-subnet-private1-us-east-1a
    - artema-subnet-private2-us-east-1b

### PostgreSQL
- **Creation method**: Standard create
- **Engine type**: PostgreSQL
- **Templates**: Dev/Test
- **Availability and durability**: Multi-AZ DB instance deployment (2 instances)
- **DB instance**: artema-pgdb
- **Master username**: postgres
- **Credentials management**: ********
- **Instance configuration**:
    - Burstable classes (includes t classes)
    - db.t3.micro
- **Allocated storage**: 20 GiB
- **Enable storage autoscaling**: check
- **Compute resource**: Don’t connect to an EC2 compute resource
- **VPC**: artema-vpc
- **DB subnet group**: artema-rds-sng
- **Public access**: No
- **Security groups**: artema-sg-rds
- **Monitoring**: Database Insights - Standard
- **Enhanced Monitoring**: Disabled  

### Crear KMS para Exportar de RDS a S3 (Opcional)
- **Key type**: Key type
- **Key usage**: Encrypt and decrypt
- **Alias**: artema-rds-export-key
- **Description**: Clave para exportación de snapshots RDS a S3
- **Key policy**: 
```json
{
    "Version": "2012-10-17",
    "Id": "key-export-rds",
    "Statement": [
        {
            "Sid": "AllowRDSExport",
            "Effect": "Allow",
            "Principal": {
                "Service": "export.rds.amazonaws.com"
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "992136605746"
                }
            }
        },
        {
            "Sid": "AllowAdmin",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::992136605746:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        }
    ]
}
```

### Agregar Trust Policy al Rol actual LabRole (Opcional)
- **IAM → Roles → LabRole → Trust relationships → Edit trust policy**
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::992136605746:role/LabRole",
                "Service": [
                    "firehose.amazonaws.com",
                    // ... (todos los servicios existentes) ...
                    "ssm.amazonaws.com",
                    "export.rds.amazonaws.com"  // ¡Nuevo servicio agregado!
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```


### Respado Manual hacia S3 (Opcional)
#### 1. Take Snapshot
- **Snapshot type**: Manual
- **DB Instance**: artema-pgdb
- **Snapshot name**: artema-pgdb-manual-YYYYMMDD
#### 2. Exportar a S3
- **Export identifier**: artema-export-YYYYMMDD
- **S3 bucket**: artema-s3-storage
- **Prefix**: db_backups/
- **IAM Role**: LabRole
- **Amazon Resource Name**: ARN del KMS creado

### SQL
```sql
CREATE TABLE personajes_hxh (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo_nen VARCHAR(50) NOT NULL,
    edad INT NOT NULL,
    descripcion TEXT,
    img VARCHAR(100)
);
```

```sql
INSERT INTO personajes_hxh 
    (nombre, tipo_nen, edad, descripcion, img)
VALUES
    ('Gon Freecss', 'Enhancer', 12, 'Protagonista, con gran talento natural para el Nen.', 'gon.webp'),
    ('Killua Zoldyck', 'Transmuter', 12, 'Hijo de la familia asesina Zoldyck, amigo cercano de Gon.', 'killua.webp'),
    ('Kurapika', 'Conjurer', 17, 'Último sobreviviente del clan Kurta, busca venganza.', 'kurapika.webp'),
    ('Leorio Paradinight', 'Emitter', 19, 'Aspira a ser médico, es valiente y decidido.', 'leorio.webp'),
    ('Hisoka Morow', 'Transmuter', 28, 'Antagonista impredecible, disfruta de la pelea.', 'hisoka.webp'),
    ('Chrollo Lucilfer', 'Specialist', 30, 'Líder de la banda de ladrones Fantasma.', 'chrollo.webp'),
    ('Biscuit Krueger', 'Enhancer', 30, 'Maestra experimentada con apariencia joven.', 'biscuit.webp');
```

```sql
SELECT * FROM personajes_hxh;
```

---
