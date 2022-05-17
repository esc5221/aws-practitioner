# Module 8: 요금 및 지원

## AWS 프리 티어

#### 상시 무료

- 프리티어가 만료되지 않음
- AWS Lambda: 매월 100만 건의 호출(최대 320만 초의 컴퓨팅 시간)
- SageMaker, Comprehend Medical, DynamoDB, SNS, Cognito

#### 12개월 무료

- 12개월 동안 사용해볼 수 있음
- S3: 최대 5GB 스토리지

#### 평가판

- 정해진 기간만큼만 사용해볼 수 있음
- LightSail: 750시간을 사용할 수 있는 1개월 평가판

## AWS 요금 개념

#### AWS 요금 적용 방식

- 온디맨드
  - 사용한 만큼만 지불
- Saving Plans
  - 일정 사용량을 약속하고 온디맨드에 비해 싼 요금을 지불
- Volume 기반 할인
  - 계층화된 요금
  - 사용량이 증가함에 따라 단위 비용이 낮아지는 경우
    - e.g. S3

#### AWS 요금 계산기

- AWS 서비스 탐색, AWS 기반 사용 사례에 대한 비용 추정
- 인스턴스 구성 사항에 따른 AWS 리전 및 유형별로 예상 비용을 비교

#### 참고: Amazon S3 요금

- 스토리지
  - 객체의 크기, 스토리지 클래스, 저장한 기간
- 요청 및 데이터 검색
  - 객체 및 버킷에 수행한 요청에 대해 비용을 지불
- 데이터 전송 
  - 다른 Amazon S3 버킷 간 데이터 전송 혹은 동일한 region의 다른 서비스로 데이터 전송하는 경우는 무료
  - 송수신한 데이터에 대해서는 비용을 지불
  - S3 -> CloudFront, 동일한 리전의 EC2 인스턴스로의 데이터도 비용이 들지 않음
- 관리 및 복제
  - 활성화한 스토리지 관리 기능에 대해 비용을 지불
  - 인벤토리, 분석, 객체 태그 지정

#### 결제 대시보드

- 월별 누계금액 비교
- 사용량 예측
- 서비스별 프리티어 사용량 확인
- Cost Explorer를 통한 예산 생성
- Saving Plans 구매 및 관리

#### 통합 결제

- AWS Organizations 기반
- 조직에 있는 모든 연결 계정의 결합된 비용 추적
- 계정 전체에서의 대량 할인 요금
- Saving plans 및 예약 인스턴스 공유

## AWS 예산

- 예산 생성
- 서비스 사용, 서비스 비용 및 인스턴스 예약 계획
- 정보가 하루에 세번 업데이트
- 예산 금액 초과 or 초과 예상 알림 설정 가능

## AWS Cost Explorer

- 콘솔을 통해 시간 경과에 따라 AWS 비용 및 사용량을 시각화, 이해, 관리할 수 있는 도구
- 사용자 지정 필터 및 그룹(시간별, 상위 사용량)을 적용하여 데이터를 분석할 수 있다.
- 시간 경과에 따라 AWS 비용을 분석함으로써 향후 비용 및 예산 수립 방법에 대한 결정을 내릴 수 있음.

## AWS Support Plan

#### AWS Basic Support

- 24시간 연중 무휴 고객 서비스
- 문서 
- 백서 
- 지원 포럼
- AWS Trusted Advisor
  - 제한됨
- AWS Personal Health Dashboard
  - 이벤트 발생 시 알림 및 수정 지침을 제공하는 도구

#### AWS Developer Support

- Basic Support 지원
- 이메일로 고객 지원 서비스 액세스
  - 12 시간 이내 답변 가능

#### AWS Buisiness Support

- Basic 및 Developer Support
- 요구사항에 적합한 AWS 제품, 기능 및 서비스 식별을 위한 사용 사례
- AWS Trusted Advisor
  - 전체 모범 사례 제공
- 클라우드 지원 엔지니어에 직접 전화
  - 1 hour SLA
- 인프라 이벤트 관리
  - 대규모 기획에 도움

#### AWS Enterprsie Support

- Basic, Developer, Buisiness
- 비즈니스 크리티컬 워크로드에 대한 상담
  - 15min SLA
- 기술 지원 관리자 (TAM)
  - 컨시어지 지원 팀의 일부
  - 고객의 환경을 모니터링
  - 최적화 지원
  - 인프라 이벤트 관리
  - 운영 검토
  - Well-Architected 검토
    - 프레임워크를 사용해 고객과 함께 검토
    - 운영 우수성, 보안, 안정성, 성능 효율성, 비용 최적화

## AWS Marketplace

- Independent Software Vendor의 소프트웨어 리스팅이 포함된 디지털 카탈로그
- AWS 아키텍처에서 실행되는 소프트웨어를 검색하고 평가, 구매 가능
- 인프라 제품, 비즈니스 애플리케이션, 데이터 제품, DevOps와 같은 여러 범주의 제품을 제공
- 대부분 온디맨드 옵션도 제공하고 있음
- 중심 기능
  - 사용자 지정 약관 및 가격
  - private market place
  - 비용 관리 도구



### 추가 자료 

- [AWS 요금](https://aws.amazon.com/pricing)
- [AWS 프리 티어](https://aws.amazon.com/free)
- [AWS 비용 관리](https://aws.amazon.com/aws-cost-management/)
- [백서: AWS 요금 적용 방식](https://d1.awsstatic.com/whitepapers/aws_pricing_overview.pdf)
- [백서: AWS 경제성 소개](https://d1.awsstatic.com/whitepapers/introduction-to-aws-cloud-economics-final.pdf)
- [AWS Support](https://aws.amazon.com/premiumsupport)
- [AWS 지식 센터](https://aws.amazon.com/premiumsupport/knowledge-center/)