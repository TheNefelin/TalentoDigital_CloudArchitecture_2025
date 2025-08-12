## **Route 53**: DNS

### Hosted zones
- **Domain name**: mediastreamlab.com
- **Description**: Dominio MediaStreamLab publico
- **Type**: Public hosted zone

### Create record
- **Record name**: www
- **Record type**: A – Routes traffic to an IPv4 address and some AWS resources
- **Alias**: check
- **Route traffic to**: 
  - Alias to Application and Classic Load Balancer
  - US East (N. Virginia) us-east-1
  - mediastream-lb-ec2
- **Routing policy**: Simple routing

### NS record (Copiar DNS a proveedor de dominio)
- **Value**:
  - ns-85.awsdns-10.com.
  - ns-1332.awsdns-38.org.
  - ns-1891.awsdns-44.co.uk.
  - ns-519.awsdns-00.net.
