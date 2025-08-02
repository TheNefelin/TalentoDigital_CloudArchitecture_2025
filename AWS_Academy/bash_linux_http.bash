#!/bin/bash
yum install -y httpd       # Instala el servidor web Apache
systemctl enable httpd     # Habilita Apache para iniciar automáticamente al arrancar
systemctl start httpd      # Inicia el servicio Apache ahora
echo '<html><h1>EC2 Corriendo!!!</h1></html>' > /var/www/html/index.html  # Crea una página HTML básica
