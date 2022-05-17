# Module 6: 보안

## 공동 책임 모델

- AWS 환경은 단일 객체가 아니므로 AWS와 고객이 공동으로 책임진다.

- 리소스를 안전하게 유지할 책임
  - 주택 소유자와 주택 건축업자 간의 관계
  - AWS 책임 (클라우드 자체)
    - 인프라
      - 리전, AZ, 엣지 로케이션, AWS 글로벌 인프라
      - 네트워크 인프라
      - 가상화 인프라
    - 리소스
      - 하드웨어, 컴퓨팅, 스토리지, DB, 네트워킹
    - SW
  - 고객 책임 (클라우드 내부)
    - 데이터 암호화
      - 클라이언트/ 서버
    - 네트워킹 트래픽 보호
    - OS, 네트워크, 방화벽
    - 플랫폼, 애플리케이션, 자격 증명 및 액세스 관리
      - 소프트웨어 패치 적용 등
    - 고객 데이터

## 사용자 권한 및 액세스

#### 루트 계정 사용자

- AWS 계정의 소유자
- 계정에 있는 모든 리소스에 액세스하고 제어
- MFA 활성화 필요
  - Multi-Factor Authentication
  - 이메일과 비밀번호 뿐만 아니라 인증을 위한 일회용 토큰도 요구

#### IAM

- AWS Identity and Access Management
- 액세스를 세부적으로 제어
- IAM 사용자
  - 기본적으로 어떤 권한도 없음
  - 사용자 권한을 명시적으로 부여
    - IAM 정책을 사용자와 연결
  - 최소 권한 원칙
    - 사용자에게 필요한 곳에 대한 액세스 권한만 부여
- IAM 그룹
  - 사용자 모음
  - IAM그룹을 정책에 연결하면 그룹의 모든 사용자가 권한을 부여 받음

- IAM 역할
  - 임시적인 사용자 권한을 부여
    - `포스트잇`에 가까움
  - 회사 자격 증명
    - 조직 내 모든 구성원에 대한 IAM 사용자 생성 방지
    - 회사 자격 증명을 IAM 역할에 매핑

## AWS Organizations

- 회사에 여러 AWS 계정이 존재하는 경우 조직 단위(OU)로 관리
- 통합 결제
- 계정의 계층적인 그룹화
  - 조직을 생성하여 AWS Organizations가 조직의 모든 계정에 대한 상위 컨테이너 루트를 생성

- 서비스 제어 정책(SCP)를 통해 조직의 계정에 대해 중앙 집중식 관리
  - 각 계정의 사용자 및 역할이 액세스할 수 있는 AWS 서비스, 리소스 액세스 권한을 정의
  - 조직 루트, OU, 개별 멤버 계정에 적용가능
- AWS 서비스 및 API 작업 액세스 제어

## 규정 준수

- 회사가 속한 업종이나 위치한 국가에 따라 특정 표준을 준수해야하는 경우
- 회사가 이러한 표준을 충족했는지 확인하는 절차가 필요
- AWS 보안 및 규정 준수 보고서, 일부 온라인 계약에 대한 온디맨드 액세스를 제공

#### AWS Artifact Agreements

- 회사에서 AWS 전체에서 특정 유형의 정보를 사용하기 위해 AWS와 계약을 체결해야하는 상황
- 개별 계정 및 AWS Organizations 내 모든 계정에 대한 계약을 검토, 수락 및 관리

#### AWS Artifact Reports

- 특정 규제 표준의 책임에 대한 정보에 액세스하는 경우
- 외부 감사 기관이 작성한 규정 준수 보고서를 제공

#### 고객 규정 준수 센터

- AWS 규정 준수에 대해 자세히 알아볼 수 있는 리소스를 포함
- 규정 준수 백서 및 설명서에 액세스
  - 주요 규정 준수 질문에 대한 AWS 답변
  - AWS 위험 및 규정 준수 개요
  - 보안 감사 체크리스트

## 서비스 거부 공격

#### DDoS 공격 사례

- UDP flood
  - 다른 API에 요청을 보낸 후 response의 destination을 공격 대상의 IP로 설정
  - 서버는 원하지 않는 정보를 처리하기 위해 과부하가 생김
  - 보안 그룹은 트래픽의 scheme과 source로 트래픽을 제한할 수 있으므로 해결할 수 있음
    - 인스턴스가 아닌 AWS 네트워크 수준에서 작동(방화벽처럼)하므로 안전
- HTTP 수준 공격
  - 정상적으로 평범한 정보를 게속 요구하는 케이스, 그러나 수많은 요청을 보내도록 함
- Slowloris 공격
  - request 패킷을 보내는데 매우 느리게 보냄
  - 서버의 프론트엔드가 요청자의 느린 request를 입력받는데 과부하가 생김
    - 이후 도착할 request의 처리를 하지 못함
  - ELB로 프론트엔드와 백엔드 부분을 분리
    - 리전 수준에서 실행

#### AWS Shield

- DDoS 공격으로부터 애플리케이션을 보호하는 서비스
- Standard
  - 무료 서비스
  - 일반적인 DDoS 공격으로부터 보호
- Advanced
  - 상세한 공격 진단
  - 정교한 DDos 공격을 탐지하고 완화
  - CloudFront, Routee53, ELB와 같은 서비스와 통합됨
  - 사용자 지정 규칙을 통해 AWS WAF와도 통합할 수 있음

## 추가 보안 서비스

#### AWS KMS

- 암호화 키를 생성, 관리 및 사용

- 암호화 키를 사용하여 DB의 데이터를 encode, decode
- 키를 관리할 수 있는 IAM 사용자 및 역할을 지정 가능

#### SSL

- 리소스와 클라이언트를 연결할 때 SSL연결 기능을 제공
  - RedShift, SQS, S3, RDS 등에서 제공

#### Amazon Inspector

- 애플리케이션의 자동 보안 평가 수행
- 애플리케이션의 보안 및 규정 준수를 개선할 수 있는 서비스
  - EC2인스턴스에 대한 오픈 액세스 감시
  - 취약한 소프트웨어 버전 설치 체크
  - 이외 보안 모범 사례 위반 및 보안 취약성을 검사
- 보안 탐지 결과 목록을 제공
  - 심각도 수준에 따라 우선 순위를 결정

#### AWS WAF

- 웹 애플리케이션으로 들어오는 네트워크 요청을 모니터링할 수 있는 방화벽
- CloudFront, Application Load Balancer와 함께 작동
- 웹 ACL을 사용
  - NACL과 비슷

#### Amazon GuardDuty

- AWS 인프라 및 리소스에 대한 지능형 위협 탐지 기능 제공
- AWS 환경 내의 네트워크 활동 및 계정 동작을 지속적으로 모니터링

- AWS CloudTrail, Amazon VPC Flow Logs, DNS log 분석
- 위협에 대한 탐지 결과를 검토할 수 있도록 함
  - 문제 해결을 위한 권장 단계를 포함
  - 자동으로 문제 해결 단계를 수행하도록 Lambda 함수도 구성 가능

#### Security Hub



### 추가 자료

- [AWS의 보안, 자격 증명 및 규정 준수](https://aws.amazon.com/products/security)
- [백서: AWS 보안 소개](https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/welcome.html)
- [백서: Amazon Web Services - 보안 프로세스 개요](https://docs.aws.amazon.com/whitepapers/latest/aws-overview-security-processes/aws-overview-security-processes.pdf)
- [AWS 보안 블로그](https://aws.amazon.com/blogs/security/)
- [AWS 규정 준수](https://aws.amazon.com/compliance)
- [AWS 고객 성공 사례: 보안, 자격 증명 및 규정 준수](https://aws.amazon.com/solutions/case-studies/?customer-references-cards.sort-by=item.additionalFields.publishedDate&customer-references-cards.sort-order=desc&awsf.customer-references-location=*all&awsf.customer-references-segment=*all&awsf.customer-references-product=product%23vpc|product%23api-gateway|product%23cloudfront|product%23route53|product%23directconnect|product%23elb&awsf.customer-references-category=category%23security-identity-compliance)