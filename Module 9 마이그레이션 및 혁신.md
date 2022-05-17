# Module 9: 마이그레이션 및 혁신

## AWS CAF

- AWS Cloud Adoption Framework

### Cloud Adoption Framework의 6가지 주요 관점

- 각 관점을 별개의 책임으로 해결한다.

#### 비즈니스 관점

- IT가 비즈니스 요구 사항을 반영하는지
- 분리된 비즈니스 전략과 IT 전략을 비즈니스 모델로 통합하도록 전환하는데 도움이 됨
- IT 투자가 주요 비즈니스 결과와 연계되도록 하는지
- 이해관계자
  - 비즈니스 관리자
  - 재무 관리자
  - 예산 소유자
  - 전략 이해당사자

#### 인력 관점

- 클라우드 채택을 성공하기 위한 조직 전반의 변화 관리 전략 개발
  - HR 직원이 조직 프로세스와 직원 기술을 업데이트하도록 함
- 조직 구조 및 역할, 새로운 기술 및 프로세스 요구 사항을 평가하고 격차를 파악
- 교육, 인력 배치 및 조직 변화의 우선 순위 지정
- 이해 관계자
  - 인사 관리
  - 인력 배치
  - 인력 관리자

#### 거버넌스 관점

- IT 전략이 비즈니스 전략에 부합하도록 조정하는 기술 및 프로세스에 중점
- 비즈니스 가치를 극대화, 위험을 최소화
- 클라우드 투자를 관리하고 측정하여 비즈니스 성과를 평가
- 이해 관계자
  - 최고 정보 책임자
  - 프로그램 관리자
  - 엔터프라이즈 아키텍트
  - 비즈니스 분석가
  - 포트폴리오 관리자

#### 플랫폼 관점

- 클라우드를 기반으로 한 새로운 솔루션 구현
- 온프레미스 워크로드를 클라우드로 마이그레이션하기 위한 원칙과 패턴
- 다양한 아키텍처 모델을 사용하여 IT 시스템의 구조와 그 관계를 이해하고 전달
- 이해 관계자
  - 최고 기술 책임자(CTO)
  - IT 관리자
  - 솔루션스 아키텍트

#### 보안 관점

- 가시성, 감사 가능성, 제어 및 민첩성에 대한 보안 목표 충족
- AWS CAF를 사용하여 조직의 요구사항을 충족
- 보안 제어의 선택 및 구현을 구성
- 이해 관계자
  - 최고 정보 보안 책임자
  - IT 보안 관리자
  - IT 보안 분석가

#### 운영 관점

- 비즈니스 이해 당사자와 합의된 수준까지 IT 워크로드를 구현, 실행, 사용, 운영 및 복구
- 기간별로 비즈니스를 수행하는 방법을 정의
- 이해 관계자
  - IT 운영 관리자
  - IT 지원 관리자

## 마이그레이션 전략

#### 리호스팅

- lift and shift
- 애플리케이션을 변경 없이 이전
- 신속하게 확장하여 비즈니스 사례를 충족하는 대규모 레거시 마이그레이션의 경우
- 이 경우도 꽤나 비용을 절감할 수 있는 경우가 있음
  - 이후 라이브 서버를 운영하며 AWS 이해도가 높아지면 다음 마이그레이션 전략으로 넘어가도 좋음

#### 리플랫포밍

- lift, tinker and shift
- 애플리케이션의 핵심 아키텍처는 변경하지 않고 이전
- 몇 가지 클라우드 최적화를 수행
  - MySQL -> Amazon Aurora

#### 리팩터링/아키텍처 재설계

- 클라우드 네이티브 기능을 사용하여 애플리케이션을 설계
- 사용 이유
  - 비즈니스 요구사항
  - 기존 환경의 애플리케이션에서 실현하기 까다로운 기능 추가
  - 확장 또는 성능 개선

#### 재구매

- 기존 라이선스슬 SaaS로 전환
- CRM(고객 관리 시스템)에서 Salesforce.com으로 마이그레이션

#### 유지

- 비즈니스에 중요한 애플리케이션을 소스 환경에 유지
- 마이그레이션 하기 위해서 대규모 리팩토링이 필요한 애플리케이션, 연기할 수 있는 워크로드의 경우

#### 폐기

- 더 이상 필요하지 않은 애플리케이션을 제거

## AWS Snow 패밀리

- 온프레미스 데이터센터의 데이터를 클라우드로 옮길 때 문제사항
  - 인터넷으로 옮길 경우 대역폭 제한에 걸릴 수 있고 시간, 비용 문제가 발생한다

#### AWS Snowcone

- 소규모 엣지 컴퓨팅 및 데이터 전송 디바이스
- 2core CPU, 4GB 메모리, 8TB 가용 스토리지

#### AWS Snowball Edge

- Compute optimized option
  - 대규모 데이터 마이그레이션 및 반복 전송 워크플로
  - 큰 용량이 필요한 로컬 컴퓨팅
  - 스토리지
    - S3 호환 객체 스토리지를 위한 80TB의 HDD 용량
    - 블록 볼륨을 위함 1TB SATA SSd
  - 컴퓨팅
    - Amazon EC2 sbe1 인스턴스와 동일
    - 40개의 vCPU
    - 80GiB의 메모리
- Storage optimized option
  - 기계학습, 풀 모션 비디오분석, 분석 및 로컬 컴퓨팅 스택과 같은 사용 사례
  - 스토리지
    - S3 호환, EBS 호환을 위한 42TB 가용 HDD
    - EBS호환을 위한 7.68TB의 가용 NVME SSD 용량
  - 컴퓨팅
    - 52개의 vCPU
    - 208GiB 메모리
    - NVIDIA Tesla V100 GPU
    - C5, M5a, G3, P3 인스턴스와 동일한 Amazon EC2 sbe-c, sbe-g 인스턴스를 실행

#### AWS Snowmobile

- 최대 엑사바이트 규모의 데이터까지 전송
- 세미 트레일러 트럭으로 운반
  - 1대당 100페타바이트의 데이터를 전송

## AWS를 통한 혁신

#### VMware on AWS

- 온 프레미스 운영에서 VMware기반 인프라를 AWS로 바로 마이그레이션

#### 서버리스

- 사용자가 서버를 프로비저닝, 유지 관리 또는 관리할 필요가 없는 애플리케이션
- 개발자는 서버를 관리하고 운영하기 보다 핵심 제품에 집중

#### 인공지능

- AWS Transcribe
  - 음성 텍스트 변환
- AWS Comprehend
  - 텍스트에서 패턴 검색
- AWS Fraud Detector
  - 잠재적인 온라인 사기 행위 식별
- Amazon Lex
  - 음성 및 텍스트 챗봇 빌드

#### 기계학습

- Amazon SageMake
  - ML개발을 위한 ML 모델 빌드, 훈련, 배포

- Amazon Augmented AI (Amazon A2I)

#### 인공위성

- AWS Ground Station
  - 인공위성을 잠시 빌림



### 추가 자료

- [AWS에서의 마이그레이션 및 전송](https://aws.amazon.com/products/migration-and-transfer)
- [클라우드로의 매스 마이그레이션 프로세스](https://aws.amazon.com/blogs/enterprise-strategy/214-2/)
- [애플리케이션을 클라우드로 마이그레이션하는 6가지 전략](https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/)
- [AWS Cloud Adoption Framework](https://aws.amazon.com/professional-services/CAF/)
- [AWS 기본 사항: 핵심 개념](https://aws.amazon.com/getting-started/fundamentals-core-concepts/)
- [AWS Cloud Enterprise Strategy 블로그](https://aws.amazon.com/blogs/enterprise-strategy/)
- [AWS로 현대화 블로그](https://aws.amazon.com/blogs/modernizing-with-aws/)
- [AWS 고객 성공 사례: 데이터 센터 마이그레이션](https://aws.amazon.com/solutions/case-studies/?customer-references-cards.sort-by=item.additionalFields.publishedDate&customer-references-cards.sort-order=desc&awsf.customer-references-location=*all&awsf.customer-references-segment=*all&awsf.customer-references-product=product%23vpc|product%23api-gateway|product%23cloudfront|product%23route53|product%23directconnect|product%23elb&awsf.customer-references-category=category%23datacenter-migration)