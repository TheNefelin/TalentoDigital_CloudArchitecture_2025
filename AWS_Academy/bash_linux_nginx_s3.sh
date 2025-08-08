#!/bin/bash

# Actualizar sistema
yum update -y
# Instalar Nginx
yum install nginx -y
# Instalar AWS CLI
yum install awscli -y
# Debería mostrar tu información con LabRole
aws sts get-caller-identity
# Si funciona, continúa con el sync
aws s3 sync s3://mediastream-s3-storage/ /usr/share/nginx/html/
# Ver qué se descargó
ls -la /usr/share/nginx/html/
# Configurar permisos correctos
chown -R nginx:nginx /usr/share/nginx/html/
chmod -R 755 /usr/share/nginx/html/
# Parar Apache (que está corriendo actualmente)
systemctl stop httpd
systemctl disable httpd
# Habilitar e iniciar Nginx
systemctl enable nginx
systemctl start nginx
# Verificar que Nginx está corriendo
systemctl status nginx
# Probar desde la misma instancia
curl http://localhost
# Debería devolver tu HTML de Hunter x Hunter



#!/bin/bash
yum update -y
yum install nginx -y
yum install awscli -y
aws s3 sync s3://BUCKET_NAME/ /usr/share/nginx/html/
chown -R nginx:nginx /usr/share/nginx/html/
chmod -R 755 /usr/share/nginx/html/
systemctl stop httpd
systemctl disable httpd
systemctl enable nginx
systemctl start nginx



#!/bin/bash
yum update -y
yum install nginx -y
yum install awscli -y
aws s3 sync s3://mediastream-s3-storage/ /usr/share/nginx/html/
chown -R nginx:nginx /usr/share/nginx/html/
chmod -R 755 /usr/share/nginx/html/
systemctl stop httpd
systemctl disable httpd
systemctl enable nginx
systemctl start nginx
