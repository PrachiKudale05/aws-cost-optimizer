# AWS Automated Cost Optimizer

## Project Summary

Designed and implemented a serverless AWS automation solution that automatically identifies and stops running Amazon EC2 instances on a scheduled basis to reduce unnecessary cloud costs.

The solution leverages an event-driven architecture using Amazon EventBridge and AWS Lambda to eliminate manual infrastructure monitoring while improving resource utilization through AWS managed services.

---

## Key Highlights

* Built a fully serverless cost optimization solution using AWS services
* Automated EC2 instance management using AWS Lambda
* Implemented scheduled automation with Amazon EventBridge
* Dynamically identified and stopped running EC2 instances using Python (Boto3)
* Configured IAM roles following the least-privilege security model
* Integrated Amazon CloudWatch for monitoring and execution logging
* Reduced unnecessary AWS infrastructure costs through automation

---

## Architecture

Amazon EventBridge Scheduler → AWS Lambda → Amazon EC2 → Stop Running Instances → Amazon CloudWatch Logs

---

## Technologies Used

### AWS Services

* Amazon EventBridge Scheduler
* AWS Lambda
* Amazon EC2
* AWS IAM
* Amazon CloudWatch

### Programming Language

* Python

### AWS SDK

* Boto3

---

## Workflow

1. Amazon EventBridge triggers the AWS Lambda function based on a scheduled cron expression.
2. Lambda authenticates using an IAM execution role.
3. Lambda scans the AWS account for running EC2 instances.
4. Running instance IDs are retrieved dynamically using the EC2 DescribeInstances API.
5. Lambda invokes the StopInstances API to stop active EC2 instances.
6. Amazon CloudWatch captures execution logs and monitoring details.
7. The automation completes without requiring any manual intervention.

---

## Skills Demonstrated

* Serverless Computing
* Event-Driven Architecture
* Cloud Automation
* AWS Lambda
* Amazon EventBridge
* Amazon EC2
* AWS IAM
* Amazon CloudWatch
* Infrastructure Automation
* Python Development
* Boto3 SDK
* Cloud Cost Optimization (FinOps)

---

## Business Value

This solution demonstrates how cloud-native automation can reduce operational costs by automatically shutting down unused EC2 instances. By eliminating manual monitoring and scheduling, the project improves cloud resource utilization, enhances operational efficiency, and supports FinOps best practices without requiring dedicated servers.

---

## Future Enhancements

* Automatically start EC2 instances during business hours
* Stop only tagged development instances
* Amazon SNS email notifications
* Slack or Microsoft Teams integration
* Multi-region EC2 management
* CloudWatch alarms for failures
* AWS Cost Explorer integration
* Cost optimization dashboard

---

## Author

**Prachi Kudale**

AWS Cloud | Python Developer | DevOps Enthusiast
