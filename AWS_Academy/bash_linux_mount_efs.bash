# sin privilegios
sudo yum install -y amazon-efs-utils
mkdir CARPETA_COMPARTIDA
ls
cd CARPETA_COMPARTIDA
pwd # ruta absoluta de la carpeta
cd
sudo mount -t efs -o tls fs-0ef13b0195e7f8442:/ /home/ec2-user/CARPETA_COMPARTIDA
df -hT
ls /home/ec2-user/CARPETA_COMPARTIDA
echo "Datos Compartidos" | tee /home/ec2-user/CARPETA_COMPARTIDA/PruebaEFS.txt

# con privilegios
sudo su
yum install -y amazon-efs-utils
mkdir SHARED_FOLDER
ls
cd SHARED_FOLDER
pwd # ruta absoluta de la carpeta
cd
mount -t efs -o tls fs-0ef13b0195e7f8442:/ /home/ec2-user/SHARED_FOLDER
df -hT
ls /home/ec2-user/SHARED_FOLDER
cat /home/ec2-user/SHARED_FOLDER/PruebaEFS.txt