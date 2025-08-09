yum install stress -y

stress --cpu 2 --timeout 300s
stress --vm 1 --vm-bytes 2G --timeout 60s
stress --cpu 2 --vm 1 --vm-bytes 2G --timeout 300s

pkill stress 

#########################################

yum install stress-ng -y
stress-ng --cpu 2 --cpu-load 80 --timeout 60s
