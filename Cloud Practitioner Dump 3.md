# Cloud Practitioner Dump 3

#### 1

The security team of a business demands that all Amazon EC2 workloads run on certified Amazon Machine Images (AMIs).

Which AWS service should the organization utilize to ensure that its EC2 instances are utilizing authorized AMIs?

- A. Amazon CloudWatch
- B. Amazon Inspector
- C. AWS Config
- D. AWS Trusted Advisor

C

#### 2

Which of the following is a managed computing service provided by AWS?

- A. Amazon SWF
- B. Amazon EC2
- C. AWS Lambda
- D. Amazon Aurora

C

### 3

Which service should be utilized to determine the expenses associated with launching a new project on AWS?

- A. AWS TCO Calculator
- B. AWS Simple Monthly Calculator
- C. AWS Cost Explorer API
- D. AWS Budgets

B

pricing calculator는 architecture에 대해 미리 계산을 할 수 있음

cost explorer는 사용량을 시각화하여 보여주고, 비용 예측, 적합한 saving plan을 찾아준다.

#### 4

A developer has an AWS account and requires access to the test database of another account.

Which Amazon Web Services (AWS) service or capability can the developer use to access the test database?

- A. Amazon Macie
- B. Security groups
- C. IAM roles
- D. AWS Trusted Advisor

C

#### 5

A user with minimal familiarity with AWS services want to rapidly create a scalable Node.js application in the AWS Cloud.
Which deployment service should be utilized for the application?

- A. AWS CloudFormation
- B. AWS Elastic Beanstalk
- C. Amazon EC2
- D. AWS OpsWorks

B

#### 6 :star:

A small independent software vendor (ISV) wishes to launch its application on Amazon Web Services (AWS). Customers of the ISV must be able to safely access the application using their own AWS accounts.

Which AWS service or feature may be used by the ISV to offer secure access to its application?

- A. Virtual private gateway
- B. AWS Client VPN
- C. Internet gateway
- D. AWS PrivateLink

B

AWS Client VPN is a fully managed service that provides customers with the ability to securely access AWS and on-premises resources from any location using

#### 7

Which AWS Cost Management tool provides the most detailed information about your AWS bill?

- A. AWS Cost Explorer
- B. AWS Budgets
- C. AWS Cost and Usage report
- D. AWS Billing dashboard

C

cost and usage reporsts - 자세하게 리소스/ account별/ 기간별로 분석

cost allocation tags - resource마다 태깅하여 분류

billing dashboard - overview, summary, resource proportion

cost explorer - 시각화, 비용예측, optimal saving plan

#### 8

Which AWS Trusted Advisor checks are accessible to AWS Basic Support customers? (Select two.)

- A. Service limits
- B. High utilization Amazon EC2 instances
- C. Security groups ג€" specific ports unrestricted
- D. Load balancer optimization
- E. Large number of rules in an EC2 security groups

A, C

#### 9

Which of the following services falls under the AWS serverless platform category?

(서버리스 서비스는?)

- A. Amazon EMR
- B. Elastic Load Balancing
- C. AWS Lambda
- D. AWS Mobile Hub

C

amazon emr은 hadoop map reduce 기반 분산 데이터 분석 시스템이다.

#### 10

Which of the following security-related acts is free?

- A. Calling AWS Support
- B. Contacting AWS Professional Services to request a workshop
- C. Accessing forums, blogs, and whitepapers
- D. Attending AWS classes at a local university

C

#### 11

A business would want to monitor the CPU use of its Amazon EC2 resources.
Which Amazon Web Services (AWS) service should the business use?

- A. AWS CloudTrail
- B. Amazon CloudWatch
- C. AWS Cost and Usage report
- D. Amazon Simple Notification Service (Amazon SNS)

B

#### 12

How does AWS accelerate the provisioning of IT resources?

- A. It supplies an online IT ticketing platform for resource requests.
- B. It supports automatic code validation services.
- C. It provides the ability to programmatically provision existing resources.
- D. It automates the resource request process from a company's IT vendor list.

C

#### 13

Which login credentials for the AWS Management Console adhere to security best practices? (Select two.)

- A. An access key
- B. Multi-factor authentication
- C. X.509 certificates
- D. A secret key
- E. User name and password

B, E

sign in to the AWS Management Console

- Create a strong password for your AWS resources 
- Use a group email alias with your AWS account 
- Enable multi-factor authentication 
- Set up AWS IAM users, groups, and roles for daily account access 
- Delete your account’s access keys 
- Enable CloudTrail in all AWS regions

#### 14

Which cloud computing benefit can a business get by using AWS Regions to expand application availability to consumers in many countries?

- A. Pay-as-you-go pricing
- B. Capacity forecasting
- C. Economies of scale
- D. Global reach

D

#### 15

Which of the following deployment strategies allows clients to completely exchange capital IT expenditures for operational expenditures?

- A. On-premises
- B. Hybrid
- C. Cloud
- D. Platform as a service

C

#### 16 :star:

Which service may be used to monitor and get alerts for AWS account root user sign-in events through the AWS Management Console?

- A. Amazon CloudWatch
- B. AWS Config
- C. AWS Trusted Advisor
- D. AWS IAM

A

#### 17

IT systems should be structured in such a way that changes or failures in one component do not cascade to other components.

This is an illustration of which cloud architecture design principle?

- A. Scalability
- B. Loose coupling
- C. Automation
- D. Automatic scaling

B

#### 18

Which of the following are advantages of using Amazon RDS over an on-premises database? (Select two.)

- A. RDS backups are managed by AWS.
- B. RDS supports any relational database.
- C. RDS has no database engine licensing costs.
- D. RDS database compute capacity can be easily scaled.
- E. RDS inbound traffic control (for example, security groups) is managed by AWS.

A, D

참고 RDS는 managed 서비스이다(아직 serverless는 아님) 프로비저닝, OS 패치, replica를 통한 scalability, multi az를 통한 dr, 자동 백업 및 복구, storage는 EBS 베이스

#### 19

How can AWS customers exchange infrastructure costs for operational costs?

- A. Secure their physical infrastructure to prevent malicious attacks.
- B. Use AWS Budgets to ensure that spending on AWS resources does not exceed preset thresholds.
- C. Eliminate the electricity costs that are associated with the hosting of physical servers.
- D. Use AWS Auto Scaling to dynamically increase and decrease compute resources as needed.

D

(C의 전기세는 자본비용 아님)

#### 20

The compliance officer of a corporation requests access to the AWS Service Organization Control (SOC) reports.

Which Amazon Web Services (AWS) service or functionality should the compliance officer use to accomplish this task?

- A. AWS Artifact
- B. AWS Concierge Support
- C. AWS Support
- D. AWS Trusted Advisor

A

#### 21

Which AWS service will be responsible for tracking user activities on AWS?

- A. Amazon GuardDuty
- B. AWS Trusted Advisor
- C. AWS CloudTrail
- D. Amazon CloudWatch

C

#### 22

Which AWS services have automatic data backups by default?

- A. Amazon S3
- B. Amazon Aurora
- C. Amazon ElastiCache for Memcached
- D. Amazon Elastic File System (Amazon EFS)

B

#### 23

Which AWS service offers a self-service site for accessing AWS compliance reports on-demand?

- A. AWS Config
- B. AWS Certificate Manager
- C. Amazon Inspector
- D. AWS Artifact

D

#### 24

Which AWS service or tool keeps track of all AWS resources created?

- A. Amazon CloudFront
- B. Amazon CloudWatch
- C. AWS CloudTrail
- D. AWS Application Migration Service (CloudEndure Migration)

C

AWS Config (Rule)도 resource 변경 추적 가능

#### 25

Which Amazon Web Services (AWS) service should I use to generate a billing alarm?

- A. AWS Trusted Advisor
- B. AWS CloudTrail
- C. Amazon CloudWatch
- D. Amazon QuickSight

C

#### 26

What is a job in Amazon Web Services' Identity and Access Management (IAM) system?

- A. A user associated with an AWS resource
- B. A group associated with an AWS resource
- C. An entity that defines a set of permissions for use with an AWS resource
- D. An authentication credential associated with a multi-factor authentication (MFA) token

C

#### 27

What information may users access using AWS Artifact?

- A. AWS security and compliance documents
- B. A download of configuration management details for all AWS resources
- C. Training materials for AWS services
- D. A security assessment of the applications deployed in the AWS Cloud

A

#### 28

For one month, a business is testing a new customer-facing application on Amazon Elastic Compute Cloud (Amazon EC2).

Which pricing strategy is most appropriate?

- A. Reserved Instances
- B. Spot Instances
- C. On-Demand Instances
- D. Dedicated Hosts

C

#### 29

Which AWS service detects security groups that provide users with unlimited access to AWS resources?

- A. AWS CloudTrail
- B. AWS Trusted Advisor
- C. Amazon CloudWatch
- D. Amazon Inspector

B

#### 30

Which of the following is a shared control mechanism between the client and Amazon Web Services?

- A. Providing a key for Amazon S3 client-side encryption
- B. Configuration of an Amazon EC2 instance
- C. Environmental controls of physical AWS data centers
- D. Awareness and training

D

`Shared Control`

- AWS provides the requirements for the infrastructure 
- Customer must provide their own control implementation within their use of AWS services. 
- Examples
  - Patch Management
    - AWS is responsible for patching and fixing flaws within the infrastructure, but customers are responsible for patching their guest OS and applications. 
  - Configuration Management
    - AWS maintains the configuration of its infrastructure devices, but a customer is responsible for configuring their own guest operating systems, databases, and applications. 
  - Awareness & Training
    - AWS trains AWS employees, but a customer must train their own employees.

#### 31

Which of the following may be used to restrict access to an Amazon Storage Service (Amazon S3) bucket to specified users?

- A. A public and private key-pair
- B. Amazon Inspector
- C. AWS Identity and Access Management (IAM) policies
- D. Security Groups

C

#### 32 :star:

A business that operates on the AWS Cloud must generate distinct invoices for each environment, such as development, testing, and production.

How is this accomplished?

- A. Use multiple AWS accounts
- B. Use resource tagging
- C. Use multiple VPCs
- D. Use Cost Explorer

A (그러나 examptopic 답은 B)

#### 33

Utilizing AWS Identity and Access Management (IAM) to restrict access to just the resources necessary to complete a job is referred to as:

- A. restricted access.
- B. as-needed access.
- C. least privilege access.
- D. token access.

C

#### 34

Why is it advantageous to utilize Elastic Load Balancers in conjunction with applications?

- A. They allow for the conversion from Application Load Balancers to Classic Load Balancers.
- B. They are capable of handling constant changes in network traffic patterns.
- C. They automatically adjust capacity.
- D. They are provided at no charge to users.

B

capacity는 auto scaling

#### 35

Which free AWS service or tool assists in identifying underused Amazon EC2 instances and idle Amazon RDS DB instances?

- A. Cost Explorer
- B. AWS Budgets
- C. AWS Organizations
- D. AWS Trusted Advisor

D

#### 36

Which of the following describes Amazon S3? (Select two.)

- A. A global file system
- B. An object store
- C. A local file store
- D. A network file system
- E. A durable storage system

B, E

파일이 아닌 오브젝트를 저장하는 것, durable함을 보장함

#### 37

Which AWS services or features contribute to the reduction of network latency for a geographically scattered user base? (Select two.)

- A. Amazon VPC
- B. Elastic Load Balancer
- C. Amazon CloudFront
- D. AWS Direct Connect
- E. AWS Global Accelerator

C, E

#### 38

A business want to evaluate a third-party ecommerce solution before committing to its long-term usage.

Which AWS service or tool will serve as the foundation for this effort?

- A. AWS Marketplace
- B. AWS Partner Network (APN)
- C. AWS Managed Services
- D. AWS Service Catalog

A

The AWS Marketplace enables qualified partners to market and sell their software to AWS Customers

#### 39

Which Amazon Web Services (AWS) offering provides permanent storage for a file system?

- A. Amazon S3
- B. Amazon EC2 instance store
- C. Amazon Elastic Block Store (Amazon EBS)
- D. Amazon ElastiCache

C

#### 40

Which AWS services can be used to collect information about the activities of an AWS account? (Select two.)

- A. Amazon CloudFront
- B. AWS Cloud9
- C. AWS CloudTrail
- D. AWS CloudHSM
- E. Amazon CloudWatch

C, E

#### 41

Which of the following Amazon Web Services (AWS) services is serverless? (Select two.)

- A. AWS Lambda
- B. Amazon Elasticsearch Service
- C. AWS Elastic Beanstalk
- D. Amazon DynamoDB
- E. Amazon Redshift

A, D

#### 42

A web developer with minimal experience of AWS networking technologies such as Amazon Virtual Private Cloud, Elastic Load Balancing, and Auto Scaling want to host a highly available web application.
Which AWS service would manage the deployment automatically and alleviate the developer's complexity?

- A. AWS CodeDeploy
- B. AWS Resource Access Manager
- C. AWS Elastic Beanstalk
- D. AWS CloudFormation

C

#### 43

Which step will provide documentation that will assist a business in determining if its usage of the AWS Cloud complies with applicable regulatory standards?

- A. Running Amazon GuardDuty
- B. Using AWS Artifact
- C. Creating an AWS Support ticket
- D. Evaluating AWS CloudTrail logs

B

#### 44 :star:

A corporation has numerous AWS accounts inside AWS Organizations and want to limit the advantage of Amazon EC2 Reserved Instances to a single account.

Which course of action should be followed?

- A. Purchase the Reserved Instances from master payer account and turn off Reserved Instance sharing.
- B. Enable billing alerts in the AWS Billing and Cost Management console.
- C. Purchase the Reserved Instances in individual linked accounts and turn off Reserved Instance sharing from the payer level.
- D. Enable Reserved Instance sharing in the AWS Billing and Cost Management console.

A

#### 45

Which AWS feature will result in a lower total cost of ownership (TCO) for the customer?

- A. Shared responsibility security model
- B. Single tenancy
- C. Elastic computing
- D. Encryption

C

#### 46

Which AWS service simplifies the process of creating and managing AWS users and groups, as well as providing them with free secure access to AWS resources?

- A. AWS Direct Connect
- B. Amazon Connect
- C. AWS Identity and Access Management (IAM)
- D. AWS Firewall Manager

C

#### 47

Among the benefits of migrating infrastructure from an on-premises data center to the AWS Cloud include the following:

- A. it allows the business to eliminate IT bills.
- B. it allows the business to put a server in each customer's data center.
- C. it allows the business to focus on business activities.
- D. it allows the business to leave servers unpatched.

C

#### 48

Which Amazon VPC feature allows users to monitor IP traffic to and from Amazon EC2 instances?

- A. Security groups
- B. Elastic network interfaces
- C. Network ACLs
- D. VPC Flow Logs

D

#### 49

Which Amazon Web Services (AWS) offering allows customers to deploy infrastructure as code by automating the provisioning process?

- A. Amazon GameLift
- B. AWS CloudFormation
- C. AWS Data Pipeline
- D. AWS Glue

B

#### 50

What are some of the benefits of Reserved Instances? (Select two.)

- A. They provide a discount over on-demand pricing.
- B. They provide access to additional instance types.
- C. They provide additional networking capability.
- D. Customers can upgrade instances as new types become available.
- E. Customers can reserve capacity in an Availability Zone.

A, E

#### 51

A user has a stateless and restartable application that will operate for two hours at a time on an Amazon EC2 instance.

Which method of buying is the MOST cost-effective?

- A. On-Demand Instances
- B. Reserved Instances
- C. Dedicated Instances
- D. Spot Instances

D

#### 52

Who is responsible for patching the Amazon RDS guest operating system?

- A. The AWS Product team
- B. The customer Database Administrator
- C. Managed partners
- D. AWS Support

A

#### 53

What services does Amazon CloudFront offer?

- A. Automatic scaling for all resources to power an application from a single unified interface
- B. Secure delivery of data, videos, applications, and APIs to users globally with low latency
- C. Ability to directly manage traffic globally through a variety of routing types, including latency-based routing, geo DNS, geoproximity, and weighted round robin
- D. Automatic distribution of incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and AWS Lambda functions

B

#### 54

Which security service on AWS detects and categorizes sensitive data or intellectual property automatically?

- A. Amazon GuardDuty
- B. Amazon Macie
- C. Amazon Inspector
- D. AWS Shield

B

#### 55

How can a business separate the expenses of production and non-production workloads on Amazon Web Services (AWS)?

- A. Create Identity and Access Management (IAM) roles for production and non-production workloads.
- B. Use different accounts for production and non-production expenses.
- C. Use Amazon EC2 for non-production workloads and other services for production workloads.
- D. Use Amazon CloudWatch to monitor the use of services.

B

#### 56

A third-party auditor has demanded that a business give a list of all its IAM users, together with the status of the individuals' credentials and access keys.

What is the MOST SIMPLE method of delivering this information?

- A. Create an IAM user account for the auditor, granting the auditor administrator permissions.
- B. Take a screenshot of each user's page in the AWS Management Console, then provide the screenshots to the auditor.
- C. Download the IAM credential report, then provide the report to the auditor.
- D. Download the AWS Trusted Advisor report, then provide the report to the auditor.

C

IAM access advisor도 가능

#### 57

Utilizing Amazon Elastic Container Service (Amazon ECS) to deconstruct a monolithic design into microservices demonstrates the following:

- A. a loosely coupled architecture.
- B. a tightly coupled architecture.
- C. a stateless architecture.
- D. a stateful architecture.

A

#### 58 :star:

A user requires an automated security assessment report that identifies unauthorized network access to Amazon EC2 instances and their associated issues.

Which AWS service will be responsible for generating this evaluation report?

- A. EC2 security groups
- B. AWS Config
- C. Amazon Macie
- D. Amazon Inspector

d

Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS

#### 59

A firm is developing a business intelligence system and wants to include dashboards into the reporting process.

Which Amazon Web Services (AWS) service may be used?

- A. Amazon Redshift
- B. Amazon Elasticsearch Service (Amazon ES)
- C. Amazon QuickSight
- D. Amazon Athena

C

#### 60

A company is transferring its development and test environments to AWS to increase agility and cost savings. Given that these are not production workloads and the servers are not fully used, some downtime is to be anticipated.

Which Amazon EC2 price plan is the MOST cost-effective in order to achieve these requirements?

- A. Reserved Instances
- B. On-Demand Instances
- C. Spot Instances
- D. Dedicated Instances

B

#### 61

Which AWS service enables the safe, rapid, and economical migration or transit of exabyte-scale datasets into AWS?

- A. AWS Batch
- B. AWS Snowball
- C. AWS Migration Hub
- D. AWS Snowmobile

D

#### 62

Where can I obtain AWS compliance and certification reports?

- A. AWS Artifact
- B. AWS Concierge
- C. AWS Certificate Manager
- D. AWS Trusted Advisor

A

#### 63

A business is migrating its on-premises key-value database to the Amazon Web Services Cloud.

Which AWS service is appropriate for this scenario?

- A. Amazon RDS
- B. Amazon ElastiCache
- C. Amazon DynamoDB
- D. Amazon Redshift

C

#### 64

A user requires rapid deployment of a non-relational database on AWS. The user is not interested in administering the underlying hardware or database software.

Which AWS service is appropriate for this?

- A. Amazon RDS
- B. Amazon DynamoDB
- C. Amazon Aurora
- D. Amazon Redshift

B

#### 65

Which of the following AWS services may be used to administer a database independently?

- A. Amazon Route 53
- B. AWS X-Ray
- C. AWS Snowmobile
- D. Amazon Elastic Compute Cloud (Amazon EC2)

D

#### 66

Which of the following is an Amazon CloudWatch Logs feature? (Select two.)

- A. Summaries by Amazon Simple Notification Service (Amazon SNS)
- B. Free Amazon Elasticsearch Service analytics
- C. Provided at no charge
- D. Real-time monitoring
- E. Adjustable retention

D, E

sns는  cloudwatch alarm

#### 67

A business is in the market for a scalable data warehouse solution.

Which of the following AWS options would be most appropriate for your business?

- A. Amazon Simple Storage Service (Amazon S3)
- B. Amazon DynamoDB
- C. Amazon Kinesis
- D. Amazon Redshift

D

#### 68

Which of the following are AWS Global Accelerator's benefits? (Select two.)

- A. Reduced cost to run services on AWS
- B. Improved availability of applications deployed on AWS
- C. Higher durability of data stored on AWS
- D. Decreased latency to reach applications deployed on AWS
- E. Higher security of data stored on AWS

B, D

#### 69

Which of the following are AWS shared responsibility model customer responsibilities? (Select two.)

- A. Physical security of AWS facilities
- B. Configuration of security groups
- C. Encryption of customer data on AWS
- D. Management of AWS Lambda infrastructure
- E. Management of network throughput of each AWS Region

B, C

#### 70

Which AWS service enables customers to comply with contractual and regulatory data security obligations by using dedicated hardware appliances inside the AWS Cloud?

- A. AWS Secrets Manager
- B. AWS CloudHSM
- C. AWS Key Management Service (AWS KMS)
- D. AWS Directory Service

B