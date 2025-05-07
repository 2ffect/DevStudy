# 변수
## 개요
### 식별자(변수명) 작성 규칙
- 반드시 문자, 달러 ('&') 또는 밑줄 ('_')로 시작
- 대소문자를 구분
- 예약어 사용 불가
  - for, if, function 등

### 식별자(변수명) Naming case
- 카멜 케이스 (camelCase)
  - 변수, 객체, 함수에 사용
- 파스칼 케이스 (PacalCase)
  - 클래스, 성성자에 사용
- 대문자 스네이크 케이스 (SNAKE_CASE)
  - 상수(constants)에 사용

## 변수 선언 키워드
1. let
2. const

### 1. let
- 블록 스코프 (block scope)를 갖는 지역 변수를 선언
- 재할당 가능
- 재선언 불가능 !!
- ES6 에서 추가
```js
let number = 10 // 1. 선언 및 초기값 할당 (초기화)
number = 20     // 2. 재할당

let number = 10 // 1. 초기화
let number = 20 // 2. 재선언 불가 !
```

### 2. const
- 블록 스코프 (block scope)를 갖는 지역 변수를 선언
- 재할당, 재선언 불가능 !
- 그렇기 때문에 선언 시점에서 무조건 초기값을 지정해야 함
- ES6 에서 추가

```js
const number // const' declarations must be initialized.
```

### 블록 스코프 (block scope)
- if, for, 함수 등의 **'중괄호 {} 내부'** 를 가리킴 
- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가
```js
let x = 1
if (x === 1) {
  let x = 2

  console.log(x) // 2
}

console.log(x)   // 1
```

### const를 기본으로 사용해야 하는 이유
- 코드의 의도 명확화
  - 해당 병수가 재할당되지 않을 것임을 명확히 표현
  - 개발자들에게 변수의 용도와 동작을 더 쉽게 이해할 수 있게 해줌

- 버그 예방
  - 의도치 않은 변수 값 변경으로 인한 버그 예방
  - 큰 규모의 프로젝트나 팀 작업에서 중요

