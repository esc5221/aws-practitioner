# Module 4: 네트워킹

## AWS와의 연결: VPC

- 사용자 고유 프라이빗 네트워크
- AWS 리소스용 private IP의 범위를 정의
- EC2 인스턴스나 ELB같은 요소를 배치

#### 서브넷

- VPC 내의 IP 주소 모음
- 리소스를 그룹화
- 리소스는 주로 서브넷에 배치

#### IGW

- 인터넷 게이트웨이
- private 네트워크와 공개 인터넷의 트래픽을 연결
- `공개된 출입구`

#### VPN

- 가상 프라이빗 게이트웨이
- private 네트워크와 승인된 네트워크(온프레미스, 사내 데이터 센터)의 트래픽을 연결
- `비밀 버스`

- 여전히 공개된 트래픽에서 연결이 이루어진다는 점이 문제
  - 대역폭, 보안성

#### AWS Direct Connect

- 데이터 센터와 AWS로 이어지는 완전히 비공개인 전용 광섬유 연결



## 네트워크 액세스 제어: NACL, 보안 그룹

#### 퍼블릭 서브넷과 프라이빗 서브넷

- 게이트웨이에 대한 액세스 관리
  - 공개 / 비공개
- 트래픽 권한의 제어
  - 발신자와 통신 방식을 기준으로 권한을 검사
  - Network ACL에서 담당



#### Network ACL

- 서브넷 수준의 인바운드 및 아웃바운드 트래픽을 제어 (가상 방화벽)
  - 서브넷 내부의 인스턴스에 도달하는 패킷에 대해서는 평가하지 않음
- 발신자와 통신 방식을 승인 목록과 금지 목록에 따라 통과 여부 결정
- `default`: 모든 인바운드 및 아웃바운드 트래픽을 허용
  - 사용자 지정 NACL은 사용자가 허용할 트래픽을 지정하기 전까지 모든 트래픽을 거부
- 상태 비저장 패킷 필터링
  - 항상 규칙 목록에 따라 패킷을 허용 또는 거부
- `입국 심사대`



#### 보안 그룹

- 인스턴스 수준에서의 패킷을 평가
- `default`: 인스턴스로 향하는 모든 트래픽이 차단
  - 특정 유형의 트래픽을 수락하도록 수정
- 상태 저장 패킷 필터링
  - 이전의 패킷에 대한 허용/거부 여부를 기억한다.
- `건물 경비원`



## 글로벌 네트워킹

#### Route 53

- DNS 서비스
  - 도메인 네임과 IP주소 번역
- 라우팅 정책을 이용한 적절한 IP 엔드포인트로 라우팅
  - 엣지 로케이션 사용으로 근접성 제공
- 도메인 이름을 등록하는데도 사용





### 추가 자료

- [AWS의 네트워킹 및 콘텐츠 전송](https://aws.amazon.com/products/networking)
- [Amazon 네트워킹 및 콘텐츠 전송 블로그](https://aws.amazon.com/blogs/networking-and-content-delivery/)
- [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc)
- [Amazon VPC란 무엇입니까?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [Amazon VPC 작동 방식](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html)



#### 
