yum install stress -y
stress --cpu 1
pkill stress 

#########################################

yum install stress-ng -y
stress-ng --cpu 2
stress-ng --cpu 2 --cpu-load 80 --timeout 60s
