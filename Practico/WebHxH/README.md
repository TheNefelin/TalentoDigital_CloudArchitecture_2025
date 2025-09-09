## **S3 Bucket**: Almacenamiento Estático
```bash
hxhweb-s3/
├── css/
├── data/
├── img/
├── js/
├── index.html
└── error.html
```

### Bucket
- **Name**: hxhweb-bucket
- **Object Ownership**: ACLs desactivados
- **Block all public access**: uncheck
- **Versioning**: Disable
- **Encryption**: SSE-S3
- **Bucket Key**: Enable

### Properties - Static website hosting (Opcional levantar sitio web)
- **Static website hosting**: ✅ Activado
- **Hosting type**: Host a static website
- **Index document**: index.html
- **Error document**: error.html

### Permissions - Bucket Policy
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::hxhweb-bucket/*"
        }
    ]
}
```