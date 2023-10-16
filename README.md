## 1. 프로젝트 소개
ol_cdump_2020-11-30.txt 라는 도서정보를 담은 txt 파일을 정렬 하는 것이 목표.
목표 달성을 위해 다양한 문제 사항이 나타날 것으로 보이며,
각종 설정, 명령어, 알고리즘 최적화를 통해 문제 사항을 극복 하는 것이 필요할 것으로 예상됨.

## 2. 샘플 데이터
압축된 파일 ol_cdump_2020-11-30.txt.gz ( 약 23GB ) 을 다운로드 받아서
압축을 해제 한 다음 사용 ( 압축 해제시 약 132GB ) .

프로그램 개발 초기에는 상위 일부 데이터만을 사용하여 진행 할 것을 추천.
(예. 상위 1000줄 , 1만줄 , 10만줄)

(이 프로젝트는 신입사원 교육용 이었으며 아래 파일은 용량 때문에 내부의 별도 웹 서버를 사용 하였음)
( [ol_cdump_2020-11-30.txt.gz 다운로드](http://backup-moon.intra.coremaxtech.com/ddfile/ol_cdump_2020-11-30.txt.gz) )

위 파일은 Open Library 사이트의 complete dump 파일이며 , 외부 사용자는 아래 주소에 접속하여 다운로드 가능.

https://openlibrary.org/developers/dumps

또는

https://openlibrary.org/data/ol_dump_latest.txt.gz

```
$ ls -al ol_cdump_2020-11-30.txt.gz 
-rw-rw-r-- 1 humanstar humanstar 24086769190 12월 16 01:40 ol_cdump_2020-11-30.txt.gz
$ 

$ time md5sum ol_cdump_2020-11-30.txt.gz 
a15625e4dc298ceb4d864018f6e89732  ol_cdump_2020-11-30.txt.gz

real	2m1.831s
user	0m56.779s
sys	0m9.202s
$

$ ls -al ol_cdump_2020-11-30.txt
-rw-r--r-- 1 human humanstar 140864063700 12월 16 15:14 ol_cdump_2020-11-30.txt
$ 

$ time md5sum ol_cdump_2020-11-30.txt
a699445f2a2b2156ddaa573fc94a3430  ol_cdump_2020-11-30.txt

real	15m14.907s
user	5m21.612s
sys	0m44.708s
$ 
```
## 3. 정렬 기준.
4번째 컬럼인 날짜+시간 을 기준으로 오름차순 정렬.
샘플 파일 데이터 예제
```
/type/author	/authors/OL5345269A	1	2008-10-03T20:38:12.544508	{"last_modified": {"type": "/type/datetime", "value": "2008-10-03T20:38:12.544508"}, "type": {"key": "/type/author"}, "name": "Bi", "key": "/authors/OL5345269A", "revision": 1}
/type/author	/authors/OL5345270A	1	2008-10-03T20:38:37.118889	{"last_modified": {"type": "/type/datetime", "value": "2008-10-03T20:38:37.118889"}, "type": {"key": "/type/author"}, "name": "Bianco Nicholas", "key": "/authors/OL5345270A", "revision": 1}
/type/author	/authors/OL5345265A	1	2008-10-02T21:00:12.012264	{"last_modified": {"type": "/type/datetime", "value": "2008-10-02T21:00:12.012264"}, "type": {"key": "/type/author"}, "name": "Crisp, Tony", "key": "/authors/OL5345265A", "revision": 1}
/type/author	/authors/OL5345268A	1	2008-10-03T13:50:01.827605	{"last_modified": {"type": "/type/datetime", "value": "2008-10-03T13:50:01.827605"}, "type": {"key": "/type/author"}, "name": "Jean-Pierre ROSSIE", "key": "/authors/OL5345268A", "revision": 1
```

## 4. 참고 사항.
데이터 크기가 큰 만큼 외부 정렬을 1차 혹은 다수 차례 진행해야 목적을 달성 할 수 있을 것임.

