# Module 2: 클라우드 컴퓨팅 서비스

## Elastic Load Balancing (ELB)

- 애플리케이션 트래픽을 EC2 인스턴스와 같은 여러 리소스에 자동으로 분산하는 서비스
- Auto Scaling 그룹으로 들어오는 모든 웹 트래픽의 단일 접점 역할
- 들어오는 트래픽의 양에 맞춰 EC2 인스턴스를 추가하거나 제거한다.
- 트래픽의 모든 요청이 로드 밸런서로 먼저 라우팅된다.
- EC2 인스턴스가 여러개라면 Elastic Load Balancing에 의해 트래픽을 여러 인스턴스에 분산시킴
- Elastic Load Balancing과 Amazon EC2 Auto Scaling은 서로 연동할 수 있다.
  - 뛰어난 성능과 가용성 제공
- ELB는 외부 트랙픽에만 사용되지 않는다.
  - 프론트엔드와 백엔드 인스턴스는 서로를 인식하고 있고, ELB가 리전 구조의 단일 URL로 프론트엔드 인스턴스와 백엔드 인스턴스를 분리한다. 



### 참고: `monolithic` vs `MicroService`

#### `monolithic`

- 애플리케이션의 여러 구성요소(DB, Server, 사용자 인터페이스, 비즈니스 로직)가 서로 강하게 결합된 아키텍처
- 한 구성요소에서 장애가 발생하면 다른 구성요소에서 장애가 발생하고, 전체 애플리케이션에서 장애가 발생할 수 있음

#### `Micro Service`

- 애플리케이션의 여러 구성요소가 느슨하게 결합된다.
- 단일 구성요소에 장애가 발생해도, 다른 구성요소들이 서로 통신하며 계속 작동한다. (가용성을 유지할 수 있다.)
- Amazon SNS, SQS는 애플리케이션의 구성요소들이 느슨한 결합을 유지할 수 있도록 도와준다.

## Amazon SQS (Simple Queue Service)

- 애플리케이션 구성 요소간의 메시지를 전송, 저장, 수신할 수 있는 메시지 큐이며 일종의 `버퍼 메모리`이다.
- 애플리케이션의 구성요소가 메시지를 대기열로 전송한다.
- 사용자 또는 서비스는 대기열에서 메시지를 검색하여 처리한 후 대기열에서 삭제한다.
- bottleneck이거나 장애가 있는 구성요소가 있더라도, 메시지를 잠시동안 버퍼함으로써 장애가 다른 구성요소로 전파되지 않도록 지연시킨다.

## Amazon SNS (Simple Notification Service)

- 게시/구독(pub/sub) 서비스이다.
  - 구독자는 원하는 주제의 알림만 전달받고 여러개의 주제의 알림을 한번에 전달 받을 수 있다.
- 주문 사항을 구독자에게 전달하도록 알림을 게시하는 서비스이다.
- 구독자는 웹 서버, 이메일 주소, lambda함수 등이 될 수 있다.

#### Amazon SMS (Simple Mailing Service)
- 비슷하지만 메일을 보내는 서비스

### 참고: `serverless` vs `EC2`

- EC2
  - 최소한의 손실로 프로비저닝하여 가동 및 실행할 수 있는 가상 머신
  - 하지만 인스턴스를 직접 설정 및 관리해야 한다.
    - 새 소프트웨어 패키지에 대한 패치
    - 인스턴스의 규모를 조정
    - 솔루션의 가용성이 높아지도록 아키텍처를 설계
- 서버리스
  - 코드가 서버에서 실행되지만 서버를 프로비저닝 하거나 관리할 필요가 없다
    - 기본적으로 기본 인프라나 인스턴스를 보거나 이용할 수 없다.
  - 애플리케이션의 용량을 조정할 수 있다.
    - 처리량 및 메모리와 같은 소비 단위를 수정
  - 서버리스 애플리케이션은 자동으로 확장되며 유연성이 높다.



## AWS Lambda

- 사용한 컴퓨팅 시간에 대해서만 비용을 지불
- 서버를 프로비저닝하거나 관리할 필요가 없이 코드를 실행할 수 있는 서비스
- 작동 방식
  - Lambda에 코드 업로드
  - 이벤트 소스에서 트리거되도록 코드 설정
  - 코드는 트리거될 때만 실행



## Amazon ECS (Elastic Container Service)

- 컨테이너식 애플리케이션을 실행
  - Docker 컨테이너 지원
- 확장이 자유로운 컨테이너 관리 시스템



## Amazon EKS (Elastic Kubernetes Service)

- Kubernetes를 실행하는 데 사용할 수 있는 완전 관리형 서비스
- 컨테이너식 애플리케이션을 대규모로 배포하고 관리하는데 사용



## AWS Fargate

- 컨테이너용 서버리스 컴퓨팅 엔진
  - ECS, EKS에서 작동
- 서버를 프로비저닝하거나 관리할 필요가 없어진다.
- 컨테이너를 실행하는 데 필요한 리소스에 대해서만 비용을 지불



### 추가 자료

- [AWS에서의 컴퓨팅](https://aws.amazon.com/products/compute)
- [AWS 컴퓨팅 블로그](https://aws.amazon.com/blogs/compute/)
- [AWS Compute Services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/compute-services.html)
- [실습 자습서: 컴퓨팅](https://aws.amazon.com/getting-started/hands-on/?awsf.getting-started-category=category%23compute&awsf.getting-started-content-type=content-type%23hands-on)
- [카테고리 심층 분석: 서버리스](https://aws.amazon.com/getting-started/deep-dive-serverless/)
- [AWS 고객 성공 사례: 서버리스](https://aws.amazon.com/solutions/case-studies/?customer-references-cards.sort-by=item.additionalFields.publishedDate&customer-references-cards.sort-order=desc&awsf.customer-references-location=*all&awsf.customer-references-segment=*all&awsf.customer-references-product=product%23vpc|product%23api-gateway|product%23cloudfront|product%23route53|product%23directconnect|product%23elb&awsf.customer-references-category=category%23serverless)
