#!/bin/bash

# Actualizar sistema e instalar dependencias
yum update -y
rpm -Uvh https://packages.microsoft.com/config/centos/7/packages-microsoft-prod.rpm
yum install dotnet-sdk-8.0 -y
yum install git -y

cd /tmp
rm -rf AWS_ChatService_.NET8  # Limpiar si existe
git clone https://github.com/TheNefelin/AWS_ChatService_.NET8.git
cd AWS_ChatService_.NET8

dotnet restore
dotnet publish AWS_ChatService_API/AWS_ChatService_API.csproj -c Release -o /tmp/AWS_ChatService_.NET8/AWS_ChatService_API

# Parar aplicación actual
sudo pkill -f dotnet

# Hacer backup
cp -r /var/app/current /var/app/backup-$(date +%Y%m%d-%H%M%S)

# Reemplazar aplicación
rm -rf /var/app/current/*
cp -r /tmp/AWS_ChatService_.NET8/* /var/app/current/
chown -R webapp:webapp /var/app/current/

sleep 5
ps aux | grep dotnet | grep -v grep

# Limpiar archivos temporales
cd /tmp
rm -rf AWS_ChatService_.NET8 nueva-app


#########################################################

# Ver el contenido actual del web.config
cat /var/app/current/web.config

# Verificar que se inició el proceso correcto
ps aux | grep dotnet
netstat -tulpn | grep :5000
