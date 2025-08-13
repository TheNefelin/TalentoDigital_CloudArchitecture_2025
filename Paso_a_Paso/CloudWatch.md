## **CloudWatch**:
### CloudWatch - Dashboards
- **Dashboard name**: artema-architecture-monitoring
- **Metrics**: Line
- **EC2 Metrics**:
  - CPUUtilization (Average, per instance)
  - NetworkIn/NetworkOut
  - StatusCheckFailed  
- **RDS Metrics**:
  - DatabaseConnections
  - CPUUtilization
  - FreeStorageSpace
- **ALB Metrics**:
  - RequestCount
  - TargetResponseTime
  - HealthyHostCount
- **Lambda Metrics**:
  - Invocations
  - Errors
  - Duration
- **SQS Metrics**:
  - NumberOfMessagesReceived
  - NumberOfMessagesDeleted
  - ApproximateNumberOfVisibleMessages

### CloudWatch - Alarms
- **High CPU EC2**
  - **Name**: artema-alarm-ec2-high-cpu
  - **Metric**: EC2 CPUUtilization
  - **Threshold**: > 80% for 2 consecutive periods
  - **Action**: Send notification to SNS + Trigger Auto Scaling
- **RDS Connection Count**
  - **Name**: artema-alarm-rds-connections
  - **Metric**: RDS DatabaseConnections
  - **Threshold**: > 15 connections
  - **Action**: Send notification to SNS
- **SQS Message Backlog**
  - **Name**: artema-alarm-sqs-backlog
  - **Metric**: SQS ApproximateNumberOfVisibleMessages
  - **Threshold**: > 10 messages for 5 minutes
  - **Action**: Send notification to SNS
- **Lambda Errors**
  - **Name**: artema-alarm-lambda-errors
  - **Metric**: Lambda Errors
  - **Threshold**: > 3 errors in 5 minutes
  - **Action**: Send notification to SNS

### CloudWatch - Billing
- **Static**: check
- **Greater**: check
- **than…**: 23 USD
- **Alarm state trigger**: In alarm
- **Select an existing SNS topic**: check
- **Send a notification to…**: artema-sns
- **Name**: artema-alarm-monthly-cost

---
