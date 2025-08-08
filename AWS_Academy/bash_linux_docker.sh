# Para Amazon Linux 2
sudo su

yum update -y
# Instalar Docker Engine
dnf install -y docker
# Iniciar y habilitar el servicio
systemctl start docker
systemctl enable docker
# Agregar tu usuario al grupo Docker
usermod -a -G docker ec2-user
newgrp docker  # Para aplicar los cambios sin reiniciar sesión
docker --version
