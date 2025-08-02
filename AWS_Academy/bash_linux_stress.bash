sudo yum install stress -y

stress --cpu 1 --timeout 60s
stress --vm 1 --vm-bytes 1G --timeout 60s

stress-ng --cpu 1 --vm 1 --vm-bytes 1G --timeout 360s
# --cpu 1: Crea 1 worker consumiendo 100% de un núcleo de CPU.
# --vm 1: Crea 1 worker consumiendo memoria.
# --vm-bytes 1G: Reserva 1GB de RAM (ajústalo si tu instancia tiene menos memoria).
# --timeout 120s: Ejecuta la prueba por 2 minutos.

pkill stress 