sudo yum install stress -y
sudo apt-get install stress -y

stress --cpu 1 --timeout 400s
stress --cpu 4 --timeout 300s
stress --vm 1 --vm-bytes 1G --timeout 400s
stress --vm 2 --vm-bytes 1G --timeout 120s
stress --cpu 2 --io 1 --vm 1 --vm-bytes 512M --timeout 180s
stress-ng --cpu 4 --vm 2 --vm-bytes 1G --timeout 60s

stress-ng --cpu 1 --vm 1 --vm-bytes 1G --timeout 360s
# --cpu 1: Crea 1 worker consumiendo 100% de un núcleo de CPU.
# --vm 1: Crea 1 worker consumiendo memoria.
# --vm-bytes 1G: Reserva 1GB de RAM (ajústalo si tu instancia tiene menos memoria).
# --timeout 120s: Ejecuta la prueba por 2 minutos.

pkill stress 