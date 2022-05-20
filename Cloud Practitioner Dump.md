# Cloud Practitioner Dump 1

dumps from examtopic in descending order (start: Question#864 ~ )

#### 1

Which AWS service or feature enables the establishment of a dedicated network connection between an organization's on-premises data center and the AWS Cloud?

- A. AWS Direct Connect
- B. VPC peering
- C. AWS VPN
- D. Amazon Route 53

D

#### 2

Which of the following enables an application running on an Amazon EC2 instance to write data securely to an Amazon S3 bucket without the need for long-term credentials?

- A. Amazon Cognito
- B. AWS Shield
- C. AWS IAM role
- D. AWS IAM user access key

C

#### 3

Which AWS security service protects applications against distributed denial of service threats by providing continuous detection and automated inline mitigations?

- A. Amazon Inspector
- B. AWS Web Application Firewall (AWS WAF)
- C. Elastic Load Balancing (ELB)
- D. AWS Shield

D

#### 4

What are the advantages of utilizing Amazon Web Services managed services such as Amazon ElastiCache and Amazon Relational Database Service (Amazon RDS)?

- A. They require the customer to monitor and replace failing instances.
- B. They have better performance than customer-managed services.
- C. They simplify patching and updating underlying OSs.
- D. They do not require the customer to optimize instance type or size selections.

C

#### 5

A business requires an increase in the response time for high-volume queries to its relational database.

Which AWS service should the business use to offload requests to the database and thereby reduce overall response times?

- A. Amazon DynamoDB Accelerator (DAX)
- B. Amazon ElastiCache
- C. Elastic Load Balancing
- D. AWS Global Accelerator

B

#### 6

Which AWS service level agreement includes a dedicated Technical Account Manager?

- A. Developer
- B. Enterprise
- C. Business
- D. Basic

B

#### 7

Which of the following Reserved Instance (RI) pricing schemes results in the greatest average savings over On-Demand pricing?

- A. One-year, No Upfront, Standard RI pricing
- B. One-year, All Upfront, Convertible RI pricing
- C. Three-year, All Upfront, Standard RI pricing
- D. Three-year, No Upfront, Convertible RI pricing

C

#### 8

Which component of the AWS global infrastructure is comprised of one or more distinct data centers, each with redundant power, networking, and connectivity, and located in their own facility?

- A. AWS Regions
- B. Availability Zones
- C. Edge locations
- D. Amazon CloudFront

B

#### 9

Which AWS service is used to pay AWS bills, track consumption, and manage budget costs?

- A. AWS Billing and Cost Management
- B. Consolidated billing
- C. Amazon CloudWatch
- D. Amazon QuickSight

A

#### 10

Which AWS service or feature optimizes network performance by routing traffic across AWS's global network infrastructure?

- A. Route table
- B. AWS Transit Gateway
- C. AWS Global Accelerator
- D. Amazon VPC

C

#### 11

Which of the following Amazon EC2 pricing structures enables users to leverage pre-existing server-bound software licenses?

- A. Spot Instances
- B. Reserved Instances
- C. Dedicated Hosts
- D. On-Demand Instances

C

#### 12

Which of the following benefits is accessible for Convertible Reserved Instances but NOT for Standard Reserved Instances?

- A. The instances can be exchanged for instances of a different instance size.
- B. The instances can be exchanged for instances of a different instance family.
- C. The instances can be changed to a different Availability Zone.
- D. The instances can be changed to a different AWS Region.

B

Convertible Reserved Instance can change the EC2 instance type, instance family, OS, scope and tenancy

#### 13

Which of the following services is a MySQL-compatible database that expands storage automatically as needed?

- A. Amazon Elastic Compute Cloud (Amazon EC2)
- B. Amazon Relational Database Service (Amazon RDS) for MySQL
- C. Amazon Lightsail
- D. Amazon Aurora

D

#### 14

What is the MINIMUM level of AWS Support that includes dedicated Technical Account Managers?

- A. Enterprise
- B. Business
- C. Developer
- D. Basic

A

#### 15

Which of the following relationships between regions, Availability Zones, and edge locations is correct?

- A. Data centers contain regions.
- B. Regions contain Availability Zones.
- C. Availability Zones contain edge locations.
- D. Edge locations contain regions.

B

#### 16

What is the AWS customer's share of duty under the AWS shared responsibility model?

- A. Physical access controls
- B. Data encryption
- C. Secure disposal of storage devices
- D. Environmental risk management

B

#### 17

What is the MINIMUM AWS Support plan level that provides access to the AWS Support API for users?

- A. Developer
- B. Enterprise
- C. Business
- D. Basic

C

#### 18

Which AWS service allows customers to monitor for certain words, values, or patterns and configure alerts based on metrics?

- A. AWS IQ
- B. Amazon Comprehend
- C. AWS CloudTrail
- D. Amazon CloudWatch Logs

D - With CloudWatch Logs, you can monitor your logs, in near real time, for specific phrases, values or patterns

#### 19

Which AWS service or resource facilitates the connection of on-premises applications to AWS Cloud-based storage and caches data locally for low-latency access?

- A. AWS Direct Connect
- B. AWS Storage Gateway
- C. Amazon S3
- D. AWS Snowball Edge

B - 참고로 storage gateway, cloudtrail logs, s3 glacier는 aws kms로 자동으로 encrypt된다.

#### 20

Which Amazon Web Services (AWS) service can notify you when personally identifiable information (PII) is stored in an Amazon S3 bucket?

- A. Amazon GuardDuty
- B. Amazon Macie
- C. Amazon Inspector
- D. AWS Trusted Advisor

B

#### 21

Which AWS infrastructure deployment model brings AWS computing, storage, database, and other select services closer to end users, allowing for the execution of latency-sensitive applications?

- A. AWS Regions
- B. Availability Zones
- C. Local Zones
- D. Edge locations

C

#### 22

What is the customer's obligation while using AWS Lambda?

- A. Operating system configuration
- B. Application management
- C. Platform management
- D. Code encryption

B (discussion about B & D)

#### 23

Which pricing model results in the most savings on Amazon Elastic Compute Cloud (Amazon EC2) for a database server that must be available for one year?

- A. Spot Instance
- B. On-Demand Instance
- C. Partial Upfront Reserved Instance
- D. No Upfront Reserved Instance

C

#### 24

Which AWS function or service allows for the collection of data about incoming and outgoing traffic in an AWS VPC infrastructure?

- A. AWS Config
- B. VPC Flow Logs
- C. AWS Trusted Advisor
- D. AWS CloudTrail

B

#### 25

Which design principles should be taken into account while architecting for the AWS Cloud?

- A. Think of servers as non-disposable resources
- B. Use synchronous integration of services
- C. Design loosely coupled components
- D. Implement the least permissive rules for security groups

C

D에서 보안그룹은 항상 permissive rule만 설정할 수 있으므로 아니다.

#### 26

Which AWS service offers suggestions for right-sizing Amazon Web Services (AWS) resources such as Amazon EC2 instances, Amazon Elastic Block Store (Amazon EBS) volumes, and Amazon RDS databases in order to help customers save money?

- A. Amazon Inspector
- B. AWS Trusted Advisor
- C. AWS Service Health Dashboard
- D. Amazon Forecast

B

#### 27 :star:

Which AWS service identifies security groups that provide unlimited Internet access to a limited number of ports?

- A. AWS Organizations
- B. AWS Trusted Advisor
- C. AWS Usage Report
- D. Amazon EC2 dashboard

B - performance와 security 관련 굉장히 다양하게 지원함

#### 28

A user is running an application on Amazon Web Services (AWS) and observes that one or more AWS-owned IP addresses are being used in a distributed denial-of-service (DDoS) assault.

Whom should the user first contact in this situation?

- A. AWS Premium Support
- B. AWS Technical Account Manager
- C. AWS Solutions Architect
- D. AWS Abuse team

D

#### 29

How should users go if they want to deploy an application in geographically remote areas?

- A. Install the application using multiple internet gateways.
- B. Deploy the application to an Amazon VPC.
- C. Deploy the application to multiple AWS Regions.
- D. Configure the application using multiple NAT gateways.

C - Each AWS Region is designed to be isolated from the other AWS Regions. This design achieves the greatest possible fault tolerance and stability. 문제 뜻이 애매모호함

#### 30

Which form of AWS storage is considered ephemeral(하루살이의) and is automatically erased when an instance is stopped or terminated?

- A. Amazon EBS
- B. Amazon EC2 instance store
- C. Amazon EFS
- D. Amazon S3

B

#### 31 :star:

Which AWS container service will assist the customer with the installation, operation, and scaling of the cluster management infrastructure?

- A. Amazon Elastic Container Registry (Amazon ECR)
- B. AWS Elastic Beanstalk
- C. Amazon Elastic Container Service (Amazon ECS)
- D. Amazon Elastic Block Store (Amazon EBS)

C - Amazon ECS eliminates the need to install, operate, and scale container management infrastructure, and simplifies the creation of environments with familiar AWS core features like Security Groups, Elastic Load Balancing, and AWS Identity and Access Management (IAM).

#### 32 

Which Amazon S3 storage class is optimal for providing access to data that has lower resilience(회복력) requirements but requires quick access in certain circumstances, such as duplicate backups?

- A. Amazon S3 Standard
- B. Amazon S3 Glacier Deep Archive
- C. Amazon S3 One Zone-Infrequent Access
- D. Amazon S3 Glacier

C

#### 33

Which pillar of the AWS Well-Architected Framework is focused on the ability to efficiently operate workloads, get visibility into operations, and constantly enhance supporting processes and procedures?

- A. Cost optimization
- B. Reliability
- C. Operational excellence
- D. Performance efficiency

C

#### 34 :star:

Which of the following is a software development framework that enables businesses to specify cloud resources as code and then deploy them using AWS CloudFormation?

- A. AWS CLI
- B. AWS Developer Center
- C. AWS Cloud Development Kit (AWS CDK)
- D. AWS CodeStar

C

#### 35

A business must use AWS Identity and Access Management (IAM) to associate an IAM policy with each IAM user in an AWS account.

Which solution satisfies this criterion?

- A. Attach the IAM policy to each IAM user.
- B. Attach the IAM policy to the IAM group containing all the IAM users.
- C. Attach the IAM policy to the IAM role containing all the IAM users.
- D. Apply the IAM policy to the entire AWS account.

B

#### 36

Which pillar of the AWS Well-Architected Framework requires timely resource provisioning and scaling as required to sustain effectiveness as demand changes?

- A. Cost optimization
- B. Security
- C. Operational excellence
- D. Performance efficiency

D

#### 37

A retailer want to create a highly available application that will be hosted on numerous Amazon EC2 instances.

How should the business deploy the EC2 instances in order to satisfy these requirements?

- A. Across multiple edge locations
- B. Across multiple VPCs
- C. Across multiple Availability Zones
- D. Across multiple AWS accounts

C

#### 38

Which of the Reserved Instance (RI) pricing models allows for modification of the RI's characteristics as long as the exchange results in the production of RIs of equal or higher value?

- A. Dedicated RIs
- B. Scheduled RIs
- C. Convertible RIs
- D. Standard RIs

C

#### 39

Which AWS service is used to evaluate the costs of hosting an application on-premises vs running it on the AWS Cloud?

- A. AWS Trusted Advisor
- B. AWS Simple Monthly Calculator
- C. AWS Total Cost of Ownership (TCO) Calculator
- D. Cost Explorer

C

#### 40

Which of the following statements accurately defines a security best practice that may be executed using AWS IAM?

- A. Disable AWS Management Console access for all users
- B. Generate secret keys for every IAM user
- C. Grant permissions to users who are required to perform a given task only
- D. Store AWS credentials within Amazon EC2 instances

C - MFA, password policy, remove unnecessary credential, using aws-defined policies possible, groups

#### 41

Which AWS service offers a straightforward and scalable shared file storage solution for use with AWS and on-premises Linux servers?

- A. Amazon S3
- B. Amazon Glacier
- C. Amazon Elastic Block Store (Amazon EBS)
- D. Amazon Elastic File System (Amazon EFS)

D

#### 42

How should a user deploy an application across geographically distinct locations?

- A. Deploy the application in different placement groups.
- B. Deploy the application to a VPC.
- C. Deploy the application to multiple AWS Regions.
- D. Deploy the application by using Amazon CloudFront.

C

#### 43

Which of the following is an Amazon Web Services (AWS) database service?

- A. Amazon Redshift
- B. Amazon Elastic Block Store (Amazon EBS)
- C. Amazon S3 Glacier
- D. AWS Snowball

A

#### 44

Utilizing AWS Config to track, audit, and analyze changes to AWS resources in order to provide traceability is an example of which pillar of the AWS Well-Architected Framework?

- A. Security
- B. Operational excellence
- C. Performance efficiency
- D. Cost optimization

A

#### 45

Which AWS service serves as a data extraction, transformation, and loading (ETL) tool, simplifying the process of preparing data for analytics?

- A. Amazon QuickSight
- B. Amazon Athena
- C. AWS Glue
- D. AWS Elastic Beanstalk

C

#### 46

Which AWS service enables manual instance creation based on resource requirements?

- A. Amazon EBS
- B. Amazon S3
- C. Amazon EC2
- D. Amazon ECS

C

#### 47 :star:

A business wishes to utilize an AWS service to monitor the health of application endpoints and to redirect traffic to healthy regional endpoints in order to increase application availability.

Which service will meet these criteria?

- A. Amazon Inspector
- B. Amazon CloudWatch
- C. AWS Global Accelerator
- D. Amazon CloudFront

C

Global Accelerator

No caching, proxying, performance for applications over TCP or UDP, good for HTTP for (static IP addres), fast regional failover

#### 48

Which of the following technologies enables a secure network connection between on-premises and Amazon Web Services (AWS)?

- A. Virtual Private Network
- B. AWS Snowball
- C. Amazon Virtual Private Cloud (Amazon VPC)
- D. AWS Mobile Hub

A

#### 49

A user must adhere to compliance and software licensing requirements that require a workload to be physically housed on a server.

Which Amazon EC2 instance pricing model will satisfy these criteria?

- A. Dedicated Hosts
- B. Dedicated Instances
- C. Spot Instances
- D. Reserved Instances

A - 
dedicated hosts: entire physical server in single partition
dedicated instances - no tenancy with others (can share within my account)

#### 50

Which AWS Well-Architected Framework pillar incorporates the AWS shared responsibility model?

- A. Operational excellence
- B. Performance efficiency
- C. Reliability
- D. Security

D

#### 51

Which AWS service enables the management of a PostgreSQL database for online transaction processing (OLTP)?

- A. Amazon DynamoDB
- B. Amazon Athena
- C. Amazon RDS
- D. Amazon EMR

C

#### 52 :star:

Which AWS service is intended to assist customers who want to use machine learning for natural language processing (NLP) but lack prior machine learning experience?

- A. Amazon Comprehend
- B. Amazon SageMaker
- C. AWS Deep Learning AMIs (DLAMI)
- D. Amazon Rekognition

A 

Comprehend - NLP, find `insights` and `relationships` in text

#### 53

Which AWS services take use of AWS edge locations? (Select two.)

- A. Amazon CloudFront
- B. AWS Shield
- C. Amazon EC2
- D. Amazon RDS
- E. Amazon ElastiCache

A, B

edge location - Route 53, CloudFront, Global Accelerator, Transfer Acceleration

cloud front and global accelerator are integrate with `AWS Shield`

#### 54

Which of the following BEST describes the Amazon Web Services (AWS) pricing model? (Select two.)

- A. Fixed-term
- B. Pay-as-you-go
- C. Colocation
- D. Planned
- E. Variable cost

B, E

#### 55

Which of the following AWS Global Infrastructure components consists of one or more separate data centers linked through low-latency links?

- A. Availability Zone
- B. Edge location
- C. Region
- D. Private networking

A

#### 56

A business want to develop new application workloads on the AWS Cloud rather than on-premises resources.

What costs may be saved by using the AWS Cloud?

- A. The cost of writing custom-built Java or Node .js code
- B. Penetration testing for security
- C. hardware required to support new applications
- D. Writing specific test cases for third-party applications.

C

#### 57

Which Amazon Web Services offering offers risk audits of an AWS account by monitoring and documenting user activity and source IP addresses?

- A. AWS X-Ray
- B. AWS Shield
- C. AWS Trusted Advisor
- D. AWS CloudTrail

D

`CloudTrail` 이벤트 히스토리, AWS API Call을 바탕으로 규정 준수, 계정활동 감사 수행

#### 58

Which Amazon RDS feature is most appropriate for achieving high availability?

- A. Multiple Availability Zones
- B. Amazon Reserved Instances
- C. Provisioned IOPS storage
- D. Enhanced monitoring

A

#### 59

Which AWS service enables the detection of unintentional data breaches including personally identifiable information (PII) and user credential data?

- A. Amazon GuardDuty
- B. Amazon Inspector
- C. Amazon Macie
- D. AWS Shield

C

#### 60

Which tool allows users who do not have an AWS account to estimate the cost of almost all AWS services?

- A. Cost Explorer
- B. TCO Calculator
- C. AWS Budgets
- D. Simple Monthly Calculator

B 

`TCO Calculator`는 계정이 없어도 접근 가능

#### 61

Which Amazon Web Services (AWS) service would you utilize to receive compliance reports and certificates?

- A. AWS Artifact
- B. AWS Lambda
- C. Amazon Inspector
- D. AWS Certificate Manager

A

c.f. `codeartifact` 패키지 저장소 / `guardduty` 머신 러닝으로 cloudtrail events, vpc flow, dns, kubernetes audit 로그들을 바탕으로 AWS account 보안 위협 발견, cryptocurrency attack을 방어

#### 62

Which of the following is an Amazon Web Services (AWS) managed service that is dedicated to extract, transform, and load (ETL) data?

- A. Amazon Athena
- B. AWS Glue
- C. Amazon S3
- D. AWS Snowball Edge

B

#### 63

Which of the following is a benefit of AWS's consolidated billing?

- A. Volume pricing qualification
- B. Shared access permissions
- C. Multiple bills per account
- D. Eliminates the need for tagging

A

#### 64

Which AWS service notifies customers when an AWS event may have an effect on their company's AWS resources?

- A. AWS Personal Health Dashboard
- B. AWS Service Health Dashboard
- C. AWS Trusted Advisor
- D. AWS Infrastructure Event Management

A