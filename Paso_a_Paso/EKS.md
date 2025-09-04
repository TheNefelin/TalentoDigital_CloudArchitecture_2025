## **EKS**: Elastic Kubernetes Service
### Clusters
- **Configuration options**: Custom configuration
- **Use EKS Auto Mode**_ uncheck
- **Name**: node-microservices-demo
- **Cluster IAM role**: LabEksClusterRole
- **EKS API**: check
- **ARC Zonal shift**: disabled
- **VPC**: default
- **Subnets**: default
- **Additional security groups**: node-sg-service
- **Cluster endpoint access**: Public and private

### Clusters - Compute - Add node group
- **Name**: ng-general
- **Node IAM role**: LabRole
- **AMI type**: Amazon Linux 2023 (x86_64)
- **Instance types**: t3.medium
- **Disk size**: 20 GiB
- **Desired size**: 2
- **Minimum size**: 2
- **Maximum size**: 4
- **Subnets** default

### Clusters - Resources - Workload ???

## **CloudShell**:
### Create .yaml and upload
- auth-service.yaml
- orders-service.yaml
- products-service.yaml

### Update Kubernete Config (Connect kubectl to EKS)
```sh
aws eks update-kubeconfig --name node-microservices-demo --region <REGION>
``` 
```sh
kubectl get nodes
```
```sh
kubectl apply -f aws-auth-service.yaml
kubectl apply -f aws-orders-service.yaml
kubectl apply -f aws-products-service.yaml
```
```sh
kubectl get all
```
- optional
```sh
kubectl delete all --all
kubectl delete configmap --all
kubectl delete secret --all
```

---