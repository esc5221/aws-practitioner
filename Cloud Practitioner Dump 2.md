# Cloud Practitioner Dump 2

dumps from examtopic in descending order (start: Question#800 ~ )

#### 1

Which of the following may be used by an Amazon Web Services (AWS) client to create a new Amazon Relational Database Service (Amazon RDS) cluster?

- A. AWS Concierge
- B. AWS CloudFormation
- C. Amazon Simple Storage Service (Amazon S3)
- D. Amazon EC2 Auto Scaling
- E. AWS Management Console

B, E

#### 2 :star:

Which of the following security measures safeguards an AWS account's access? (Select two.)

- A. Enable AWS CloudTrail.
- B. Grant least privilege access to IAM users.
- C. Create one IAM user and share with many developers and users.
- D. Enable Amazon CloudFront.
- E. Activate multi-factor authentication (MFA) for privileged users.

B, E

#### 3 :star:

Which Amazon EC2 pricing model is the MOST cost effective for a non-stop workload that runs for 24 hours once a year?

- A. On-Demand Instances
- B. Reserved Instances
- C. Spot Instances
- D. Dedicated Instances

A

#### 4

Which of the following statements is true about the AWS Well-Architected Framework's pillars? (Select two.)

- A. Multiple Availability Zones
- B. Performance efficiency
- C. Security
- D. Encryption usage
- E. High availability

B, C

operational excellence, security, reliability, performance efficiency, cost optimization, sustainability

#### 5 

Which of the following is a benefit of Amazon EC2 instances over on-premises servers? (Select two.)

- A. Pay-as-you-go pricing
- B. Automation
- C. Self-maintenance of servers
- D. Agility
- E. Access to physical hosts

A, D

#### 6

Which of the following services will automatically scale as online traffic increases?

- A. AWS CodePipeline
- B. Elastic Load Balancing
- C. Amazon EBS
- D. AWS Direct Connect

B

#### 7

A solutions architect must manage a fleet of Amazon EC2 instances to ensure that any instances that fail are replaced.

Which Amazon Web Services (AWS) offering should the solutions architect utilize?

- A. Amazon Elastic Container Service (Amazon ECS)
- B. Amazon GuardDuty
- C. AWS Shield
- D. AWS Auto Scaling

D - ELB와 연계하여 fault tolerance를 간접적으로 제공

#### 8

An application is executed on many Amazon EC2 instances that concurrently access a shared file system.

Which Amazon Web Services (AWS) storage service should be used?

- A. Amazon EBS
- B. Amazon EFS
- C. Amazon S3
- D. AWS Artifact

B

#### 9

How can one Amazon Web Services account use Reserved Instances from another Amazon Web Services account?

- A. By using Amazon EC2 Dedicated Instances
- B. By using AWS Organizations consolidated billing
- C. By using the AWS Cost Explorer tool
- D. By using AWS Budgets

B

#### 10

Which service allows risk audits by monitoring and recording account activities on a continuous basis, including user actions in the AWS Management Console and AWS SDKs?

- A. Amazon CloudWatch
- B. AWS CloudTrail
- C. AWS Config
- D. AWS Health

B

c.f) `AWS config`는 compliance(보안 룰)을 직접 지정하고 monitor 및 감사한다 (e.g. 제한 없는 SSH access가 있는지)

#### 11

What distinguishes Amazon S3 cross-region replication?

- A. Both source and destination S3 buckets must have versioning disabled
- B. The source and destination S3 buckets cannot be in different AWS Regions
- C. S3 buckets configured for cross-region replication can be owned by a single AWS account or by different accounts
- D. The source S3 bucket owner must have the source and destination AWS Regions disabled for their account

C

참고로 source, dest의 versioning이 필요하고 IAM permission을 S3 bucket에 줘야한다. 다른 계정의 S3 bucket끼리도 replication이 가능하다.

#### 12

Which of the following is an illustration of how migrating to the AWS Cloud lowers initial costs?

- A. By replacing large variable costs with lower capital investments
- B. By replacing large capital investments with lower variable costs
- C. By allowing the provisioning of compute and storage at a fixed level to meet peak demand
- D. By replacing the repeated scaling of virtual servers with a simpler fixed-scale model

B

#### 13 :star:

Which of the following is an advantage of the AWS Compliance program for AWS customers? (Select two.)

- A. It verifies that hosted workloads are automatically compliant with the controls of supported compliance frameworks.
- B. AWS is responsible for the maintenance of common compliance framework documentation.
- C. It assures customers that AWS is maintaining physical security and data protection.
- D. It ensures the use of compliance frameworks that are being used by other cloud providers.
- E. It will adopt new compliance frameworks as they become relevant to customer workloads.

B, C

#### 14

Which of the following will increase the security of AWS Management Console access? (Select two.)

- A. AWS Secrets Manager
- B. AWS Certificate Manager
- C. AWS Multi-Factor Authentication (AWS MFA)
- D. Security groups
- E. Password policies

C, E

참고 : secrets manager는 RDS의 encryption을 자동화해주는 도구

certificate manager는 load balancer, cloudfront distributions, API gateway단에 SSL/TLS 인증을 쉽게 관리해주는 도구 (public TLS는 무료)

#### 15

Where can I get AWS compliance documentation, such as a SOC 1 report?

- A. Amazon Inspector
- B. AWS CloudTrail
- C. AWS Artifact
- D. AWS Certificate Manager

C

#### 16

Which AWS service provides in-memory data storage?

- A. Amazon Aurora
- B. Amazon RDS
- C. Amazon DynamoDB
- D. Amazon ElastiCache

D

#### 17 :star:

Which of the following is (not) an AWS responsibility?

- A. Setting up AWS Identity and Access Management (IAM) users and groups
- B. Physically destroying storage media at end of life
- C. Patching guest operating systems
- D. Configuring security settings on Amazon EC2 instances

B

내 생각엔 not이 오타다

#### 18

What is an AWS Availability Zone?

- A. One or more physical data centers
- B. A completely isolated geographic location
- C. One or more edge locations based around the world
- D. A data center location with a single source of power and networking

A

#### 19

Which Amazon S3 storage class enables customers to keep backup data for extended periods of time at the LOWEST possible cost?

- A. S3 Standard-Infrequent Access (S3 Standard-IA)
- B. S3 Standard
- C. S3 Glacier
- D. S3 One Zone-Infrequent Access (S3 One Zone-IA)

C

#### 20

How can a business account for network traffic, Amazon EC2, Amazon S3, and other AWS services on a department-by-department basis?

- A. Add department-specific tags to each resource
- B. Create a separate VPC for each department
- C. Create a separate AWS account for each department
- D. Use AWS Organizations

A

참고 examtopic에서는 정답이 C로 뜨지만 discussion에서는 A라고 하고, udemy에서 같은 문제를 A라고 함

#### 21

Which pricing model will terminate an Amazon EC2 instance that is already operating if capacity becomes temporarily unavailable?

- A. On-Demand Instances
- B. Standard Reserved Instances
- C. Spot Instances
- D. Convertible Reserved Instances

C

#### 22 :star:

A Cloud Practitioner must ascertain if any security groups in an Amazon Web Services account have been established to provide unlimited access to certain ports.

What is the MOST SIMPLE method to do this?

- A. Review the inbound rules for each security group in the Amazon EC2 management console to check for port 0.0.0.0/0.
- B. Run AWS Trusted Advisor and review the findings.
- C. Open the AWS IAM console and check the inbound rule filters for open access.
- D. In AWS Config, create a custom rule that invokes an AWS Lambda function to review rules for inbound access.

B

참고

Trusted Advisor 제공 기능

- S3 bucket permission
- security group - specific ports unrestricted
- IAM Use
- MFA on Root Account
- EBS Public Snapshots
- RDS Public Snapshots
- Service Limits
  - Set CloudWatch alarms when reaching limits
  - programmatic Access using AWS support API

#### 23

A company would like to protect its web applications from common web exploits that may affect availability, compromise security, or consume excessive resources. Which AWS service should they use?

- A. Auto Scaling Groups
- B. Shield
- C. CloudHSM
- D. Web Application Firewall

D

shield - DDOS protection

web application firewall - protect common web exploits on layer7, deploy on ALB, API Gateway, CloudFront

#### 24

You want to centrally automate security checks across several AWS accounts. Which AWS service can you use?

- A. Macie
- B. Detective
- C. CloudTrail
- D. Security Hub

D

security hub - comprehensive view of security state within aws/ compliance with security standards

cloudtrail - provides governance, compliance, audit for your AWS account

#### 25

Which service is a threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts and workloads?

- A. KMS
- B. WAF
- C. Inspector
- D. GuardDuty

D. 

GuardDuty - threat detection service, monitor malicious activity, unauthorized behavior

#### 26

Which AWS service is suitable for serving static websites?

- A. Amazon S3
- B. Amazon Route 53
- C. Amazon QuickSight
- D. AWS X-Ray

A

#### 27

Which of the following are benefits of using Amazon Web Services for cloud computing? (Select two.)

- A. Users can increase speed and agility by deploying services with just one click.
- B. Users receive a discount on hardware that they purchase for their data centers.
- C. Users can reserve excess capacity to ensure that resources are always available.
- D. Users trade variable expenses for capital expenses.
- E. Users benefit from massive economies of scale.

A, E

#### 28

Which of the following enables customers to create a dedicated network connection between their internal network and Amazon Web Services?

- A. AWS CloudHSM
- B. AWS Direct Connect
- C. AWS VPN
- D. Amazon Connect

B

#### 29

Which of the following services may be used to prevent network traffic from reaching a particular instance? (Select two.)

- A. Security groups
- B. Amazon Virtual Private Cloud (Amazon VPC) flow logs
- C. Network ACLs
- D. Amazon CloudWatcs
- E. AWS CloudTrail

A, C

#### 30 :star:

Which of the following AWS Cloud services may be used to administer a relational database for a customer?

- A. Amazon EC2
- B. Amazon Route 53
- C. Amazon ElastiCache
- D. Amazon DynamoDB

A

#### 31

A business is building an e-commerce website with the purpose of storing and processing credit card data. The organization is in need of information about AWS compliance reports and AWS agreements.

Which Amazon Web Services (AWS) offering enables on-demand access to these items?

- A. AWS Certificate Manager
- B. AWS Config
- C. AWS Artifact
- D. AWS CloudTrail

C

#### 32

Which Amazon Web Services (AWS) service or resource is serverless?

- A. AWS Lambda
- B. Amazon EC2 instances
- C. Amazon Lightsail
- D. Amazon ElastiCache

A

#### 33

Which managed service provided by AWS is used to host databases?

- A. AWS Batch
- B. AWS Artifact
- C. AWS Data Pipeline
- D. Amazon RDS

D

#### 34

Which of the following statements is true about AWS Local Zones?

- A. A cluster of data centers in one geographic location
- B. A site used by Amazon CloudFront to cache frequently accessed content
- C. An extension of an AWS Region to more granular locations
- D. One or more data centers with redundant power and networking

C

#### 35

Which AWS offering enables a business to build a relational database in the AWS Cloud?

- A. Amazon RDS
- B. Amazon DynamoDB
- C. Amazon ElastiCache
- D. Amazon S3

A

#### 36

Which AWS service enables customers to get on-demand security and compliance reports for AWS infrastructure?

- A. Amazon GuardDuty
- B. AWS Security Hub
- C. AWS Artifact
- D. AWS Shield

C

#### 37 :star:

A customer has an AWS account with a Business-level AWS Support subscription and need help managing a production service outage.

What should the user do?

- A. Contact the dedicated AWS technical account manager (TAM).
- B. Contact the dedicated AWS Concierge Support team.
- C. Open a business-critical system down support case.
- D. Open a production system down support case.

D

참고 

business support는 trusted advisor기능을 full로 사용, production workload에 대한 시스템 지원

enterprise support로 가야 concierge support team, TAM, business-critical workload에 대한 지원을 해줌

#### 38

What is the distinguishing feature of Convertible Reserved Instances (RIs)?

- A. Users can exchange Convertible RIs for other Convertible RIs from a different instance family.
- B. Users can exchange Convertible RIs for other Convertible RIs in different AWS Regions.
- C. Users can sell and buy Convertible RIs on the AWS Marketplace.
- D. Users can shorten the term of their Convertible RIs by merging them with other Convertible RIs.

A

can change the EC2 instance type, instance family, OS, scope and tenancy

#### 39

How does Amazon Web Services charge for AWS Lambda?

- A. Users bid on the maximum price they are willing to pay per hour.
- B. Users choose a 1-, 3- or 5-year upfront payment term.
- C. Users pay for the required permanent storage on a file system or in a database.
- D. Users pay based on the number of requests and consumed compute resources.

D

#### 40

A business wishes to host its MySQL databases on Amazon Web Services (AWS) while maintaining complete control over the operating system, database installation, and configuration.

Which Amazon Web Services (AWS) service should the business choose to host the databases?

- A. Amazon RDS
- B. Amazon EC2
- C. Amazon DynamoDB
- D. Amazon Aurora

B

#### 41

Which AWS service may be used to create a cloud-based contact center on-demand?

- A. AWS Direct Connect
- B. Amazon Connect
- C. AWS Support Center
- D. AWS Managed Services

B

Amazon connect는 virtual contact center이다.

다른 CRM system과 함께 적용 가능 connect -> lex -> lambda -> CRM

#### 42

What is the purpose of the AWS Simple Monthly Calculator?

- A. Compares on-premises costs to colocation environments
- B. Estimates monthly billing based on projected usage
- C. Estimates power consumption at existing data centers
- D. Estimates CPU utilization

B

#### 43

Which of the following is a critical architectural design concept to consider while developing cloud-based applications?

- A. Use multiple Availability Zones.
- B. Use tightly coupled components.
- C. Use open source software.
- D. Provision extra capacity.

A

#### 44

Which of the following advantages are associated with using AWS Trusted Advisor? (Select two.)

- A. Providing high-performance container orchestration
- B. Creating and rotating encryption keys
- C. Detecting underutilized resources to save costs
- D. Improving security by proactively monitoring the AWS environment
- E. Implementing enforced tagging across AWS resources

C, D

쉽게 생각해서 cost와 security 관련 조언을 해준다

#### 45

Which AWS service is used to encrypt Amazon EBS data?

- A. AWS Certificate Manager
- B. AWS Systems Manager
- C. AWS KMS
- D. AWS Config

C

c.f) S3는 KMS도 사용할 수 있지만 SSE를 보통 사용함

systems manager는 AMI에 깔려 있고, command, patch, configure를 자동으로 관리해줌 (secure shell 연결도 가능)

#### 46

A business has activated billing alerts in its AWS account and wishes to be notified through Amazon Simple Notification Service (Amazon SNS) anytime its monthly cost exceeds a predefined threshold.

Which AWS service or technology should the business use to do this?

- A. Amazon CloudWatch
- B. Cost Explorer
- C. AWS Cost and Usage Report
- D. AWS Pricing Calculator

A

#### 47

Which AWS service provides fully managed source control and secure Git-based repository hosting?

- A. AWS CodeCommit
- B. AWS CodeStar
- C. Amazon CodeGuru
- D. AWS CodePipeline

A

#### 48

Which AWS service or feature can be used to obtain information about the availability of all AWS services?

- A. AWS Personal Health Dashboard
- B. AWS CloudTrail
- C. AWS Service Health Dashboard
- D. Amazon CloudWatch

C

#### 49

Which responsibilities does AWS have under the shared responsibility approach for security and compliance?

- A. Granting access to individuals and services
- B. Encrypting data in transit
- C. Updating Amazon EC2 host firmware
- D. Updating operating systems

C

#### 50

A business that has just moved to AWS want to provide intelligent threat prevention and continuous monitoring across all of its AWS accounts.

Which AWS service should the business employ to accomplish this objective?

- A. Amazon Macie
- B. Amazon GuardDuty
- C. AWS Shield
- D. Amazon Detective

B

#### 51

A database administrator is attempting to track down the individual who erased a vital Amazon Redshift cluster.

Which AWS service assists in monitoring and archiving such account activity?

- A. AWS CloudTrail
- B. AWS Organizations
- C. AWS Identity and Access Management (IAM)
- D. AWS Trusted Advisor

A

#### 52

What is the Amazon CloudWatch service?

- A. A code repository with customizable build and team commit features.
- B. A metrics repository with customizable notification thresholds and channels.
- C. A security configuration repository with threat analytics.
- D. A rule repository of a web application firewall with automated vulnerability prevention features.

B

#### 53

Which of the following benefits does AWS consolidated billing provide? (Select two.)

- A. The ability to receive one bill for multiple accounts
- B. Service limits increasing by default in all accounts
- C. A fixed discount on the monthly bill
- D. Potential volume discounts, as usage in all accounts is combined
- E. The automatic extension of the master account's AWS support plan to all accounts

A, D

#### 54

How is the AWS Enterprise Support Concierge team of experts able to assist users?

- A. Supporting application development
- B. Providing architecture guidance
- C. Answering billing and account inquires
- D. Answering questions regarding technical support cases

C

참고

Support Concierge - the Concierge Team are AWS billing and account experts that specialize in working with enterprise accounts. They will quickly and efficiently assist you with your billing and account inquiries, and work with you to implement billing and account best practices so that you can focus on what matters: running your business.

TAM - assist with the technical inquiries

#### 55

Which AWS service is perpetually free for users?

- A. Amazon S3
- B. Amazon Aurora
- C. Amazon EC2
- D. AWS Identity and Access Management (IAM)

D

#### 56

Which of the following functions as a virtual firewall at the Amazon EC2 instance level, allowing one or more instances to govern their own traffic?

- A. Access keys
- B. Virtual private gateways
- C. Security groups
- D. Access Control Lists (ACL)

C

#### 57

A business is contemplating adopting AWS to host a self-hosted database that needs nightly shutdowns for maintenance and cost savings.

Which service should the business utilize?

- A. Amazon Redshift
- B. Amazon DynamoDB
- C. Amazon Elastic Compute Cloud (Amazon EC2) with Amazon EC2 instance store
- D. Amazon EC2 with Amazon Elastic Block Store (Amazon EBS)

D

#### 58

A business wants to have a single AWS account for the whole organization and separate accounts for each department.
Which Amazon Web Services (AWS) service should the business employ to aggregate and manage all accounts?

- A. AWS Billing and Cost Management
- B. AWS Organizations
- C. AWS Identity and Access Management (IAM)
- D. AWS Resource Access Manager

B

#### 59

Which AWS Well-Architected Framework pillar focuses on the capacity to automatically recover from service interruptions?

- A. Security
- B. Performance efficiency
- C. Operational excellence
- D. Reliability

D (신뢰성)

#### 60

Which Amazon Web Services managed services are available for connecting an on-premises data center to the AWS network? (Select two.)

- A. AWS VPN
- B. NAT gateway
- C. AWS Direct Connect
- D. Amazon Connect
- E. Amazon Route 53

A, C

#### 61

 Which of the following is not a component of AWS's shared responsibility model?

- A. Patching operating system software
- B. Encrypting data
- C. Enforcing multi-factor authentication
- D. Auditing physical data center assets

D

참고 고객이 아닌 AWS의 책임은 무엇인가에 대한 질문

#### 62

Which AWS Support package includes a comprehensive set of AWS Trusted Advisor audits?

- A. Business and Developer Support
- B. Business and Basic Support
- C. Enterprise and Developer Support
- D. Enterprise and Business Support

D

#### 63

Which controls does AWS completely transfer to the client under the AWS shared responsibility model?

- A. Patch management controls
- B. Awareness and training controls
- C. Physical and environmental controls
- D. Configuration management controls

C

참고: 얘도 번역이 이상함 AWS만의 의무가 무엇인지로 해석해야함