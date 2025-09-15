- Crear bucket S3
```sh
aws s3api create-bucket --bucket <bucket-name> --region us-east-1
aws s3api create-bucket --bucket 20250915-s3site --region us-east-1
```

[whatismyip](https://www.whatismyip.com/)

- Agregar permisos a S3
```sh
cd python_3
python3 permissions.py
```
- Desde python_3 ejecutar
```sh
aws s3 cp ../resources/website s3://<bucket-name>/ --recursive --cache-control "max-age=0"
```

- Ir a S3 - index.html - URL del objeto
