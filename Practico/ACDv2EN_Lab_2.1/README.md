- Versión AWS Cli
```sh
aws --version
```
- Listar los bucket de S3
```sh
aws s3 ls
```
- Subir list-buckets.py
- Leer el contendio de list-buckets.py
```sh
cat list-buckets.py
```
- Ejecutar list-buckets.py con Python
```sh
python3 list-buckets.py
```
- Copie un archivo de CloudShell a un bucket de S3.
```sh
aws s3 cp list-buckets.py s3://<bucket-name>
```
- Devuelve el almacenamiento disponible en el entorno de CloudShell.
```sh
df -H /home
```
- Descargar archivos desde s3
```sh
aws s3 cp s3://<bucket-name>/list-buckets.py .
```
