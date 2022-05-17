# Module 3: 글로벌 인프라 및 안정성

### 참고: 고가용성(high availity), 내결함성(fault tolerance)



### 리전 선택

#### 데이터 거버넌스 및 법적 요구 사항 준수

- 회사와 정부의 규제에 따라 특정 지역이 아닌 리전에 데이터를 반출하지 못하는 경우
  - 회사의 모든 데이터를 영국 내부에 유지해야 한다는 규정이 있는 경우 런던 리전을 선택

#### 고객과의 근접성

- 고객과 가까운 리전을 선택
  - 콘텐츠를 더 빠르게 제공할 수 있다.

#### 리전 내에서 사용 가능한 서비스

- AWS의 서비스가 원하는 리전에서 제공하지 않는 경우를 고려

#### 요금

- 리전마다 서비스 이용 요금이 다르다
  - 정부 세금이나 운영 정책에 따라 운영 비용이 다르다.



### 가용 영역(AZ)

리전 내의 단일 데이터 센터 또는 데이터 센터 그룹

- 서로 수십 키로씩 떨어짐
  - 지연시간이 $<10ms$ 정도로 충분히 가까움
  - 재해 발생에 대한 내결함성 유지



### Edge location

- 고객이 전 세계 곳곳에 있어 가용중인 AWS 리전과 고객이 멀리 떨어진 경우
  - 일부 고객만을 위해 근접한 AWS 리전에 새로 인스턴스를 생성하는 것은 불필요
  - 가까운 리전에 복사본을 저장하거나 캐싱한다.
- CloudFront와 Route 53(DNS service)가 실행되는데 사용된다.

### Amazon CloudFront

- Edge location에서 실행되는 Contents Delivery Network이다.
- 전세계의 사용자에 대해 통신 속도를 효과적으로 높인다.



### AWS Outposts

- AWS 인프라 및 서비스를 온프레미스 데이터 센터로 확장
  - 기업에서 자체 데이터 센터로 AWS 서비스를 사용하고 싶은 경우
- 사용자의 데이터 센터 내부에  정상적으로 작동하는 소형 리전을 설치한다.
  - AWS가 소유하고 운영, AWS의 모든 기능을 사용할 수 있다.
  - 사용자의 건물에 격리된다.



### AWS 서비스 프로비저닝 도구

#### AWS Management Console

- 웹 기반 인터페이스
- 시각적 정보 확인에 유용
- 수동
  - 다양한 화면을 오가며 클릭하고 원하는 모든 구성을 설정해야하는 불편함
  - 수동 프로비저닝이므로 실수가 발생할 여지가 있음
- 사용자가 학습하기에 좋다

#### AWS CLI

- 터미널에서 AWS 서비스의 API를 호출
- 작업을 스크립트화하고 반복할 수 있음
- 스크립트를 예약하거나 다른 프로세스에서 트리거하는 방식으로 실행 가능

#### AWS SDK

- 다양한 프로그래밍 언어로 AWS 리소스와 상호작용
- 수동으로 리소스를 생성하지 않아도 됨

#### AWS Elastic Beanstalk

- EC2 기반

- 사용자가 코드 및 구성 설정을 제공
- 작업을 수행하는 데 필요한 리소스를 자동 배포
  - 용량 조정
  - 로드 밸런싱
  - 자동 조정
  - 애플리케이션 상태 모니터링

#### AWS Cloud Formation

- 인프라를 코드로 취급
- CloudFormation템플릿상에서 리소스를 정의
- CloudFormation이 템플릿을 파싱하고 사용자가 정의한 모든 병렬 리소스의 프로비저닝을 시작
  - 템플릿을 여러 계정이나 리전에서 동일하게 실행하고 동일한 환경을 제공
  - 완전한 자동화이므로 인적 오류가 발생할 여지가 적다.





### 추가 자료

- [글로벌 인프라](https://aws.amazon.com/about-aws/global-infrastructure/)
- [AWS 글로벌 인프라 대화형 맵](https://www.infrastructure.aws/)
- [리전 및 가용 영역](https://aws.amazon.com/about-aws/global-infrastructure/regions_az)
- [AWS 네트워킹 및 콘텐츠 전송 블로그](https://aws.amazon.com/blogs/networking-and-content-delivery/)
- [AWS 기반 구축을 위한 도구](https://aws.amazon.com/tools/)
- [AWS 고객 성공 사례: 콘텐츠 전송](https://aws.amazon.com/solutions/case-studies/?customer-references-cards.sort-by=item.additionalFields.publishedDate&customer-references-cards.sort-order=desc&awsf.customer-references-location=*all&awsf.customer-references-segment=*all&awsf.customer-references-product=product%23vpc|product%23api-gateway|product%23cloudfront|product%23route53|product%23directconnect|product%23elb&awsf.customer-references-category=category%23content-delivery)