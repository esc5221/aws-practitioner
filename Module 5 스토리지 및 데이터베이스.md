# Module 5: 스토리지 및 데이터베이스

## 인스턴스 스토어 및 Amazon EBS

#### 인스턴스 스토어

- EC2 인스턴스에 임시 블록 수준 스토리지 제공
- EC2 인스턴스와 물리적으로 연결됨
- 인스턴스와 수명이 동일한 디스크 스토리지
  - 인스턴스가 종료되면 인스턴스 스토어의 데이터가 손실됨
- 장기적으로 필요하지 않은 임시데이터 사용시에 적합

#### Amazon EBS (Amazon Elastic Block Store)

- EC2 인스턴스에서 사용할 수 있는 블록 수준 스토리지 볼륨
- EC2 인스턴스를 중지 또는 종료하더라도 연결된 EBS 볼륨의 모든 데이터를 사용 가능
- 복잡한 읽기, 변경시에 적합
- AZ 수준의 리소스
  - EC2를 연결하기 위해서는 동일한 AZ에 존재
- 볼륨이 자동으로 확장되지 않음
- 최대 16TiB
- 생성
  - 볼륨 구성을 정의하고 프로비저닝
  - EBS 볼륨을 EC2 인스턴스와 연결
- Amazon EBS 스냅샷을 통한 `증분 백업`
  - 초기 : 모든 데이터를 복사하여 백업
  - 이후 : 최근의 스냅샷 이후 변경된 데이터 블록만 저장

## Amazon S3

- Amazon Simple Storage Service
- WORM (한번 쓰기 여러번 읽기)에 특화
- 99.999999999% 신뢰도
- 무한대 저장 용량
  - 개별 객체는 5000GB 제한
- 웹 지원
  - 액세스 권한 제어 가능
  - 서버리스

#### 객체 스토리지

모든 파일을 완성된 개별 객체로 취급

- 데이터
  - 이미지, 동영상, 텍스트 문서, javascript 등 다양한 유형의 파일
- 메타데이터
  - 데이터의 내용
  - 사용 방법
  - 객체 크기
- 키
  - primary key

#### S3 Standard

- 자주 액세스하는 데이터용으로 설계
- 최소 3개의 AZ에 데이터를 저장
- 비용이 상대적으로 높음

#### S3 Standard-Infrequent Access (S3 Standard-IA)

- 자주 액세스하지 않는 데이터에 이상적
- S3 Standard와 비교해서 스토리지 가격은 더 저렴하고 검색 가격은 더 높음
- 최소 3개의 AZ에 데이터를 저장
- 자주 액세스하지는 않고 필요에 따라 고가용성이 요구되는 데이터에 적합

#### S3 One Zone-Infrequent Access (S3 One Zone-IA)

- 단일 AZ에 데이터를 저장
- S3 Standard-IA보다 낮은 스토리지 가격
- 스토리지 비용을 절감하거나, AZ 장애가 발생하더라도 데이터를 쉽게 복구할 수 있는 경우

#### S3 Intelligent-Tiering

- 액세스 패턴을 알 수 없거나 자주 변화하는 데이터에 이상적
- 객체당 소량의 우러별 모니터링 및 자동화 요금 부과

#### S3-Glacier

- 데이터 보관용으로 설계된 저비용 스토리지
- 객체를 몇 분에서 몇 시간 이내에 검색
- 보관된 고객 레코드나 이전 사진 또는 비디오 파일 저장

#### S3 Glacier Deep Archive

- 보관에 이상적인 가장 저렴한 객체 스토리지 클래스
- 객체를 12시간 이내에 검색



### EBS vs S3

- 사진 분석 웹사이트
  - 사용자 수천명이 동시에 URL을 통해 봐야함
  - 스토리지 로드에 비용을 절감
- 동영상 파일 관리 시스템
  - 대용량 파일을 개별 객체로 취급하는 경우 S3를 사용하면 매번 큰 객체를 새로 생성
  - EBS는 증분 백업을 통해 수정사항만 고침

## Amazon EFS (Elastic File System)

- 여러 클라이언트가 동시에 읽기 및 쓰기
  - 많은 수의 서비스 및 리소스가 동시에 동일한 데이터에 액세스해야 하는 사용 사례에 적합
  - 사용자, 애플리케이션, 서버
- Linux File System
  - 파일 경로를 통해 데이터에 액세스
- 여러 AZ에 걸쳐 데이터를 저장
  - Region에 종속
  - AWS Direct Connect로 온프레미스 서버와 연결 가능
- 리전 리소스
- 자동 확장
  - 중단하지 않고 페타바이트 규모로 확장

## Amazon RDS

- 관계형 데이터베이스를 실행할 수 있는 서비스
- 자동화된 관리형 서비스
  - 하드웨어 프로비저닝
  - 데이터베이스 설정
  - 패치 적용
  - 백업
- 서버리스 애플리케이션에서 DB를 쿼리하는 경우 조합이 좋다.
- 보안 옵션 제공
  - 저장 시 암호화와 전송 중 암호화 제공
- 엔진
  - Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle, MS SQL
  - Amazon Aurora
    - MySQL, PostgreSQL  호환
    - 리소스의 안정성 및 가용성 유지, 불필요한 IO를 줄여 DB 비용 절감
    - 고가용성이 필요한 경우 6개의 데이터 복사본을 3개의 AZ에 복제
    - 지속적으로 Amazon S3에 데이터를 백업

### 참고: 온 프레미스 데이터센터에서 클라우드로

- `리프트 앤 시프트`라는 작업을 통해 DB를 migration하여 Amazon EC2에서 실행되게 함

## Amazon DynamoDB

- 서버리스 데이터베이스
  - 완전 관리형
- NoSQL
  - 데이터
    - 항목
    - 속성
  - 스트레스 상황 대처에 유리
  - 단순하고 유연한 스키마
    - 속성 추가와 제거가 쉽다
  - 복잡한 쿼리는 구현하기 어렵다
    - 쿼리가 단순한 경향이 있음
  - 항목 모음에 집중
- 높은 확장성과 가용성
  - 여러 AZ와 리전에 대해 중복으로 데이터를 저장한다
    - 버튼 한번에 글로벌한 프로비저닝 가능
  - 성능 또한 뛰어나다
    - ms 단위의 응답시간

## Amazon Redshift

- 데이터 웨어하우징 서비스
  - 여러 원본에서 데이터를 수집
  - 데이터 간의 관계 및 추세를 파악
- 빅 데이터 분석
- ~엑사바이트 데이터를 대상으로 SQL 쿼리도 가능(?)
  - 최대 10배나 높은 성능

## AWS DMS

- SQL, NoSQL 기반 데이터베이스를 마이그레이션 할 수 있는 서비스
- 원본 데이터베이스를 대상 데이터베이스로 이동할 수 있다
  - 유형이 동일할 필요가 없다
  - 원본 데이터베이스가 중단될 필요가 없다.
    - 가동 중지 시간이 최소화
- case
  - homegeneous(동종)
    - 동일한 유형의 데이터베이스에서 이동
    - amazon ec2, rds, onpremis에서 cloud로 이동이 가능하다.
  - heterogeneous(이종)
    - 유형이 다른 데이터베이스간의 이동
    - `AWS Schema Conversion Tool`을 이용하여 schema를 변경
  - 개발 및 테스트 데이터베이스 마이그레이션
    - 프로덕션 사용자에게 영향을 주지 않고 애플리케이션을 테스트
  - DB 통합
    - 여러 DB를 단일 DB 베이스로 결합
  - 연속 데이터 복제
    - 일회성이 아닌 데이터의 진행 중 복제본을 다른 대상 원본으로 전송

## 추가 데이터베이스 서비스

- 모든 목적에 맞는 데이터베이스는 없다
  - 데이터를 데이터베이스 요구사항이 아닌 비즈니스 요구사항에 맞추어보기

#### Amazon DocumentDB

- Document based인 MongoDB를 기반으로 한다

- Dynamo DB보다 사소한 속성이 더 필요한 경우
- 완전한 콘텐츠 관리 시스템이 필요한 경우
- 콘텐츠 관리, 카탈로그, 사용자 프로필에 적합

#### Amazon Neptune

- GraphDB인 Neo4j를 기반으로 한다

- 소셜 네트워크 상에서 누가 누구와 연결되어 있는지?
  - 기존 DB로는 표현이 굉장히 어렵다.
- 네트워킹 및 추천 엔진, 사기 탐지에 유용하다.

#### Amazon Managed Blockchain

- 블록체인을 AWS 상에서 관리해주는 서비스
  - 신뢰도는 제공
  - 분산화 요소는 추가됨.

- 공급망을 추적해야 하지만 어떤 것도 손실해서는 안 되는 경우
- 100% 불변성을 요구하는 은행 또는 재무 기록

#### Amazon Quantum Ledger Database

- 100% 신뢰도가 있는 은행 또는 재무 기록이 필요한 경우
- 그러나 분산화되지 않은 시스템이 필요할 때
- 정부 규제 상 어떤 항목도 변경이 불가능할 때 필요한 시스템

#### Amazon ElastiCache

- DB에 캐싱 계층을 추가
- Memcached나 Redis 유형으로 제공됨

#### Amazon DynamoDB Accelerator (DAX)

- DynamoDB의 성능을 3배 정도 개선하도록 설계된 기본 캐싱 계층



### 추가 자료

- [AWS 기반 클라우드 스토리지](https://aws.amazon.com/products/storage)
- [AWS 스토리지 블로그](https://aws.amazon.com/blogs/storage/)
- [실습 자습서: 스토리지](https://aws.amazon.com/getting-started/hands-on/?awsf.getting-started-category=category%23storage&awsf.getting-started-content-type=content-type%23hands-on)
- [AWS 고객 성공 사례: 스토리지](https://aws.amazon.com/solutions/case-studies/?customer-references-cards.sort-by=item.additionalFields.publishedDate&customer-references-cards.sort-order=desc&awsf.customer-references-location=*all&awsf.customer-references-segment=*all&awsf.customer-references-product=product%23vpc|product%23api-gateway|product%23cloudfront|product%23route53|product%23directconnect|product%23elb&awsf.customer-references-category=category%23storage)
- [AWS Database Migration Service](https://aws.amazon.com/dms/)
- [AWS에서의 데이터베이스](https://aws.amazon.com/products/databases)
- [카테고리 심층 분석: 데이터베이스](https://aws.amazon.com/getting-started/deep-dive-databases/)
- [AWS 데이터베이스 블로그](https://aws.amazon.com/blogs/database/)
- [AWS 고객 성공 사례: 데이터베이스](https://aws.amazon.com/solutions/case-studies/?customer-references-cards.sort-by=item.additionalFields.publishedDate&customer-references-cards.sort-order=desc&awsf.customer-references-location=*all&awsf.customer-references-segment=*all&awsf.customer-references-product=product%23vpc|product%23api-gateway|product%23cloudfront|product%23route53|product%23directconnect|product%23elb&awsf.customer-references-category=category%23databases)