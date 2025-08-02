sudo yum update && sudo yum upgrade -y

# discos 
sudo su   # super usuario
lsblk     # lista de discos
fdisk -l  # obtener ruta
# partisionar discos
fdisk ruta  # fdisk /dev/nvme1n1
n           # nuevo o crear
p           # primario
- enter
- enter
w           # guardar
# formatear disco
lsblk
fdisk -l
mkfs.ext4 ruta  # mkfs.ext4 /dev/nvme1n1p1
# montar discos
mkdir /root/LINUX_1
cat /etc/fstab
blkid
nano /etc/fstab   # pergar el uuid sin comilla
# UUID=12345678-1234-1234-1234-123456789123  /root/LINUX_1  ext4  defaults 0 0 
ctrl-o + enter # guardar
ctrl-x + enter # salir
cat /etc/fstab
reboot
