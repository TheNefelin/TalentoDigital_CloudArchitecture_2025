# EC2 sin privilegios
pwd
sudo yum install -y amazon-efs-utils
mkdir CARPETA_COMPARTIDA
ls
cd CARPETA_COMPARTIDA
pwd # ruta absoluta de la carpeta
cd
sudo mount -t efs -o tls fs-0652e51a7506fc4f3:/ /home/ec2-user/CARPETA_COMPARTIDA
df -hT
ls /home/ec2-user/CARPETA_COMPARTIDA
echo "Datos Compartidos" | tee /home/ec2-user/CARPETA_COMPARTIDA/TestEFS.txt

# EC2 con privilegios
pwd
sudo su
yum install -y amazon-efs-utils
mkdir /home/ec2-user/SHARED_FOLDER
ls
cd SHARED_FOLDER
pwd # ruta absoluta de la carpeta
cd
mount -t efs -o tls fs-0652e51a7506fc4f3:/ /home/ec2-user/SHARED_FOLDER
df -hT
ls /home/ec2-user/SHARED_FOLDER
cat /home/ec2-user/SHARED_FOLDER/TestEFS.txt

###########################################################

echo "Datos Compartidos" | tee /home/ec2-user/CARPETA/TestEFS.txt
yum list installed
rpm -qa