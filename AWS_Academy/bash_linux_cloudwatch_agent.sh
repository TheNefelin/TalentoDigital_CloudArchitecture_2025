#!/bin/bash
# Actualizar sistema
yum update -y

# Instalar Apache
yum install -y httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>EC2 Corriendo!!!</h1></html>' > /var/www/html/index.html

# Instalar CloudWatch Agent
yum install -y amazon-cloudwatch-agent

# Crear archivo de configuración mínimo
cat <<EOF > /opt/aws/amazon-cloudwatch-agent/bin/config.json
{
    "metrics": {
        "append_dimensions": {
            "InstanceId": "\${aws:InstanceId}"
        },
        "metrics_collected": {
            "mem": {
                "measurement": ["mem_used_percent"]
            },
            "disk": {
                "measurement": ["used_percent"],
                "resources": ["*"]
            }
        }
    }
}
EOF

# Iniciar CloudWatch Agent
/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
    -a fetch-config -m ec2 \
    -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json -s