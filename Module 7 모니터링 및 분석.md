# Module 7: 모니터링 및 분석

## Amazon CloudWatch

- 중앙 위치에서 모든 지표에 액세스
- AWS 인프라와 실행하는 애플리케이션의 실시간 모니터링
- 애플리케이션, 인프라 및 서비스에 대한 가시성 확보
- MTTR(평균 문제 해결 시간) 절감 및 TCO(총 소유비용) 개선
- 대시보드 기능
  - 비즈니스 용도, 애플리케이션 또는 리소스에 따라 별도의 대시보드를 사용자 지정

## AWS CloudTrail

- 포괄적인 API 감사 도구
  - DB 테이블에 row 추가, 사용자 권한 변경 등 모든 요청이 CloudTrail엔진에 logging됨
  - 모든 것을 logging한다.
    - 요청 수행한 작업자가 `누구인지`, `언제` API 호출을 전송했는지, `어디`에서 전송했는지, 
    - `응답`, `변경 내용`, `새로운 상태`, `요청 허용/거부 여부`
- 로그를 안전한 S3 버킷에 무제한으로 저장
- 감사자에게 규정을 준수했다는 근거자료로 쓰일 수 있다.

## AWS Trusted Advisor

- AWS 환경을 검사하고 AWS 모범 사례에 따른 실시간 권장 사항을 제시
- 비용 최적화, 성능, 보안, 내결함성, 서비스 한도의 항목에 대해서 검사
- 대시보드
  - 녹색 체크: 문제가 감시되지 않은 항목 수
  - 주황색 삼각형: 권장 조사 항목
  - 빨강색 원: 권장 조치 수



### 추가 자료

- [AWS 관리 및 거버넌스](https://aws.amazon.com/products/management-tools)
- [모니터링 및 관찰 기능](https://aws.amazon.com/products/management-tools/use-cases/monitoring-and-observability/)
- [구성, 규정 준수 및 감사](https://aws.amazon.com/products/management-tools/use-cases/configuration-compliance-and-auditing/)
- [AWS 관리 및 거버넌스 블로그](https://aws.amazon.com/blogs/mt/)
- [백서: 대규모 AWS 거버넌스](https://docs.aws.amazon.com/whitepapers/latest/aws-governance-at-scale/introduction.html)