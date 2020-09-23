# 포트란 90/95

참고 블로그 : [https://sciphy.tistory.com/category/COM](https://sciphy.tistory.com/category/COM)
[추가 자료 업로드](https://www.notion.so/hyuncello/b3c2e2c91a3845a6ba6f5d5790656656)

# 간단한 구조

포트란 77의 포맷 ⇒ .for (픽스드 포맷)

포트란 90의 포맷 ⇒ .f90 (프리포맷)

## 주석

포트란 77 ⇒ C로 시작해서 작성

포트란 90 ⇒  !로 시작해서 작성

! 주석문은 그 줄의 끝까지

## 코딩  문자

알파벳 (대소문자 구별 안함)

숫자 1 2 3 4 5 6 7 8 9 0

언더스코어 _

사칙연산 + - * /

거듭제곱 **

대입연산자 =

각종 기호들 ( ) < > : ; . , ' " ! ? % & $

빈칸

## 문장

문장 끝에 세미콜론 **필요없음**

여러 줄을 쓸 때 끝에 &를 붙여서 이어짐을 표현

실행문과 비실행문으로 구분

ex) 연산, 수행, 대입 ⇒ 실행문

변수 선언 등 ⇒ 비실행문

## 레이블링

문장에 고유번호 부여

1부터 99999까지

## 기본구조

크게 3가지 영역

### 1. 선언영역

프로그램명, 변수 등이 선언

### 2. 실행영역

각종 계산 및 명령 수행

### 3. 종료영역

프로그램 닫기

서브루틴 및 모듈도 같은 구조 

## 선언 영역

### 프로그램 명 선언

PROGRAM *program_name*

PROGRAM문은 비실행문으로, 코드 첫줄에 오며, 프록그램의 이름을 컴파일러에게 전달

대소문자를 구별하지는 않지만  보통 키워드를 대문자로 쓰는 관습이 있다

프로그램 명에는 알파뉴머릭(숫자 문자 등) 과 언더스코어 ( _ )를 쓸 수 있다

### 변수선언

정수변수       INTEGER

실수형 변수  REAL

문자변수      CHARACTER

기본적인 구문

INTEGER  ::  *variable names*

CHARACTER [ ( len = length) ] :: *variable names*

length 부분에 숫자를 써넣으면, 문자열 데이터가 됨

(len =) 부분을 생략하면, 자동으로 길이가 1로 설정되고, 단일문자 변수가 됨

(len = 숫자) 대신 그냥 (숫자)로 써도 된다

## 실행 영역

4칙연산은 C와 같다

거듭제곱 존재 ( ** )

입출력함수

출력 WRITE

입력 READ

## 종료 영역

STOP문

END PROGRAM문

STOP은 Break문

END PROGRAM문은 더이상 컴파일 될 문장이 없음을 알려줌

## 예제 코드 (.f90)

```fortran
PROGRAM power

READ (*,*) x,y

z = x ** y

WRITE (*,*) z

END PROGRAM
```

ex) 17 1.5

70.09280

---

# 포트란의 기본 자료형과 행변환 함수

포트란의 기본 자료형 5개

정수형 INTEGER

실수형 REAL

복소형 COMPLEX

논리형 LOGICAL

문자형 / 문자열 CHARACTER

(세부적인  자료형 KIND, 배열은 DIEMSION, TYPE을 통한 사용자 정의 데이터형 사용가능)

선언 시 키워드와 함께 ::를 사용하는 것이 새로운 규약

호환을 위해서 생략해도 되지만.. 되도록 써주는 것이 좋음

## 1. 정수형 데이터 타입

정수형 상수는 점을 찍을 경우, 실수로 인식

ex) 100은 정수지만 100. 은 실수

정수형 데이터 메모리에 저장 시 기본 크기는 해당 컴퓨터의 word 사이즈에 의존

몇 바이트 형 및 정수형 데이터 타입을 쓸 것인가는 KIND를 사용해서 기술할 수 있음

INTEGER ( KIND = kindnumber ) :: variables

INTEGER ( kindnimber ) :: variables

kindnumber는 보통 바이트 수 나타냄.. but 컴퓨터/컴파일러에 의존적

사용하고자 하는 숫자가 몇바이트 정수형을 요구하는지를 체크하는 함수로 SELECTED_INT_KIND()함수 존재

SELECTED_INT_KIND( range )

10의 지수형 범위가 아니라, 그냥 해당 상수나, 해당 변수에 대해서 직접 KIND를 주는 내장함수로 KIND()가 있다

KIND( data )

## 2. 실수형 데이터 타입

실수형 상수에서 지수형표기법은 E,D 사용

(유효숫자 부분에 소숫점을 찍는게 원칙)

E = 싱글 프리시젼

D = 더블 프리시젼

C에서는 싱글프리시젼에 float, 더블 프리시젼 double

REAL ( KIND = *kind number )* :: *variables*

REAL ( *kind number* ) :: *variables*

() 의 kind는 옵션으로 생략하면 디폴트가 적용됨

## 3. 복소형 데이터 타입

기본형 타입으로 지정되어 있음

복소상수 = ( a,b )  ⇒ a + ib , a와 b는 자동으로 실수타입

COMPLEX ( KIND = *kind number* ) :: *variables*

COMPLEX ( *kind number* ) :: *variables*

```fortran
PROGRAM cmplx

COMPLEX :: z1, z2

z1 = (3,4) + (2,7)
z2 = (3,4) + (2,7)

WRITE (*,*) z1, z2

END PROGRAM
```

## 4. 논리형 데이터 타입

.TRUE

.FALSE

그냥 TRUE와 FALSE는 변수명이 됨

LOGICAL :: *variables*

## 5. 문자형 데이터 타입

포트란의 문자열 상수는 따옴표나 쌍따옴표 사용

예제) Man's best friend 타이핑하기

외따옴표 : 'Man''s best friend'

쌍따옴표 : "Man's best friend"

```fortran
PROGRAM str

WRITE (*,*) '"This is me."'

END PROGRAM
```

CHARACTER :: *single_character_variables*

CHARACTER ( len = *length* ) :: *string_variables*

CHARACTER ( *length* ) :: *string_variables*

즉, 길이를 넣어주면 문자열 / 안넣어주면 문자형
