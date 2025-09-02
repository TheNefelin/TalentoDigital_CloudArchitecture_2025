# Bastion
ssh -i "mi.pem" -L 5432:rds-privado.123.us-east-1.rds.amazonaws.com:5432 ec2-user@ip

# Remote
ssh -i "mi.pem" ec2-user@ip

# Copy files
scp -i "ruta.pem" -r "ruta-app" ec2-user@ip:/home/ec2-user/
