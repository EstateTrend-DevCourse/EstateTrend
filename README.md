# EstateTrend
## 프로젝트 주제
주택 실거래 API를 통한 주택 거래 동향 시각화
## 프로젝트 개요

### 1. 내용
실제 이루어진 주택 거래에 대한 자료를 활용하여 지역별 주택 거래의 동향을 시각화한다.
시/도, 시/구/군, 읍/면/동 별 지역의 주택매매와 관련된 통계 정보를 확인할 수 있고, 지도로 시각화하여 지역의 통계 정보를 편리하게 파악할 수 있다.

### 2. 기간
  2023.11.06(월) ~ 2023.11.10(금)

### 3. 기술스택
   
  | 분류 | 기술|
  |---|---|
  | 언어 |Python|
  | 백엔드 |Django framework|
  | 프론트엔드|Html, CSS|
  | 라이브러리 | requests, pandas, folium, |
  | 버전관리 및 협업 도구|Git, slack, gather, Zoom|
  
 - 활용 데이터 : 주택 실거래 정보 공공 API

### 4. 팀원 역할 소개
   
  |이름||역할|기여도|
  | ---|---| ---| ---|
  |이서림 |@srlee056 | 프로젝트 구조 설계, 백엔드 구현| 20%|
  |이상진 |@MineTime23 | 데이터 프로세스(ETL) |20%|
  |김해빈 |@HaeeBin | 데이터 시각화 페이지 구현 |20%|
  |이지형 |@jeremy714 | 프로젝트 모델 구현, 백엔드 구현 | 20%|
  |권예은 |@yeeeeeeen700 | 프론트엔드 구현 | 20%|

## 프로젝트 구현
### 구조
- 프로젝트 아키텍쳐


![Image](https://github.com/EstateTrend-DevCourse/EstateTrend/assets/40015447/1af45f41-6ee3-4836-b774-1dacda90666f)


- Django Model erd


![Image](https://github.com/EstateTrend-DevCourse/EstateTrend/assets/40015447/b89b084b-3f6b-4ff9-9079-af33071b0f00)


### 기능
- 웹페이지를 통해 하위 지역 목록, 주택 거래 정보, 지도를 표시
- 하위 지역 목록 아이템을 클릭할 경우, 해당 지역의 데이터가 반영된 페이지로 이동 
- 시각화된 자료
  - 거래정보 : 거래 량, 평균 집값 등 해당 지역의 데이터를 문자로 표시
  - 지도 : 하위 지역의 거래량을 지도에 색상으로 표시
![웹 페이지 캡쳐]

## 프로젝트 실행 방법
### 패키지 설치
- 프로젝트 clone or 파일 다운로드 

- python 3.12 version 가상환경 생성 후 활성화
```
python3.12 -m venv {venv name}
source {venv name}/bin/activate
```

- 프로젝트 폴더로 이동 후 패키지 다운로드
```
cd estatetrend
pip install -r requirements.txt
```
### 웹 페이지 구동
- API에서 데이터를 새로 받아와 저장하는 경우
```
python manage.py callapi
```

- 서버 실행
```
python manage.py runserver
```
