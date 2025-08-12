#!/bin/bash
# Script para validar y reparar Nginx en instancias Elastic Beanstalk con .NET

echo "=== 1. Verificando si la aplicación .NET está corriendo ==="
ps aux | grep dotnet | grep -v grep

echo
echo "=== 2. Mostrando puertos en escucha para dotnet ==="
sudo netstat -tulnp | grep dotnet || echo "No se encontró dotnet escuchando."

echo
echo "=== 3. Revisando estado de Nginx ==="
sudo systemctl status nginx --no-pager

echo
echo "=== 4. Si Nginx no está activo, se habilita y arranca ==="
sudo systemctl enable nginx
sudo systemctl start nginx

echo
echo "=== 5. Verificando nuevamente puertos en escucha ==="
sudo lsof -i -P -n | grep LISTEN

echo
echo "=== 6. Mostrando configuración de Nginx para Elastic Beanstalk ==="
if [ -f /etc/nginx/conf.d/elasticbeanstalk/00_application.conf ]; then
    cat /etc/nginx/conf.d/elasticbeanstalk/00_application.conf
else
    echo "Archivo de configuración no encontrado."
fi

echo
echo "=== Validación completa ==="
