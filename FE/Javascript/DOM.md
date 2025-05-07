# DOM
## 개요
### 웹 브라우저에서의 JavaScript
- 웹 페이지의 동적인 기능을 구현

- JavaScript 실행 환경 종류
  1. HTML script 태그
  2. js 확장자 파일
  3. 브라우저 Console

### 문서 구조
- HTML 문서는 상자들이 중첩된 형태로 볼 수 있음
- 각 상자는 객체이며 이 객체와 상호작용 하여 어떤 HTML 태그를 나타내는지, 어떤 콘텐츠가 포함되어 있는지 등을 알아 낼 수 있음
- 이 표현을 Document Object Model 줄여서 DOM 이라고 부름


### DOM (Document Object Model)
- 웹 페이지 (Document) 를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공
- 문서 구조, 스타일, 내용 등을 변경할 수 있도록 함

### DOM API
- 다른 프로그래밍 언어가 웹 페이지에 접근 및 조작할 수 있도록 페이지 요소들을 객체 형태로 제공하여 이에 따른 메서드 또한 제공

### document 객체
- 웹 페이지를 나타내는 DOM 트리의 최상위 객체
  - HTML 문서의 모든 컨텐츠에 접근하고 조작할 수 있는 진입점
- DOM 에서 모든 요소, 속성, 텍스트는 하나의 객체
- 모두 document 객체의 하위 객체로 구성 됨

### DOM tree
- HTML 태그를 나타내는 elements의 node는 문서의 구조를 결정
- 이들은 다시 자식 node를 가질 수 있음 (ex. documenet.body)
  - 객체 간 상속 구조가 존재

### DOM 핵심
- 문서의 요소들을 객체로 제공하여 다른 프로그래밍 언어에서 접근하고 조작할 수 잇는 방법을 제공하는 API

## DOM 선택
### DOM 조작 시 기억해야 할 것
- 조작 순서
  1. 조작 하고자 하는 요소를 선택 (또는 탐색)
  2. 선택된 요소의 콘텐츠 또는 속성을 조작

### 선택 메서드
- document.querySelector(selector)
  - 요소 한 개 선택
  - 제공한 선택자를 만족하는 첫 번째 element 객체를 반환 (없다면 null 반환)
- document.querySelectorAll(selector)
  - 요소 여러 개 선택
  - 제공한 선택자를 만족하는 NodeList를 반환

## DOM 조작
1. 속성 조작
  - 클래스 속성 조작
  - 일반 속성 조작
2. HTML 콘텐츠 조작
3. DOM 요소 조작
4. 스타일 조작

### 속성 조작
1. 클래스 속성 조작
  - 'classList' property
    - 요소의 클래스 목록을 DOMTokenList(유사 배열) 형태로 반환
  <br>
  1. classList 메서드
    - element.classList.add()
      - 지정한 클래스 값을 추가
    - element.classList.remove()
      - 지장한 클래스 값을 제거
    - element.classList.toggle()
      - 클래스가 존재한다면 제거하고 false를 반환
      - 존재하지 않으면 클래스를 추가하고 true를 반환


2. 일반 속성 조작
  - Element.getAttribute()
    - 해당 요소에 지정된 값을 반환(조회)
  - Element.setAttribute(name, value)
    - 지정된 요소의 속성 값을 설정
    - 속성이 이미 있으면 기존 값을 갱신(아니면 지정된 이름과 값으로 새 속성 추가)
  - Element.removeAttribute()
    - 요소에서 지정된 이름을 가진 속성 제거

### HTML 콘텐츠 조작
- 'textContent' property
  - 요소의 텍스트 콘텐츠를 표현

### DOM 요소 조작
#### DOM 요소 조작 메서드
- document.createElement(tagName)
  - 작성한 tagName의 HTML 요소를 생성하여 반환
- Node.appendChild()
  - 한 Noed를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
  - 추가된 Node 객체를 반환
- Node.removeChild()
  - DOM에서 자식 Node를 제거
  - 제거된 Node를 반환

### style 조작
- 'style' property
  - 해당 요소의 모든 style 속성 목록을 포함하는 속성

# 용어 정리
## Node
- DOM의 기본 구성 단위
- DOM 트리의 각 부분은 Node라는 객체로 표현됨
  - Document Node => HTML 문서 전체를 나타내는 노드
  - Element Node => HTML 요소를 나타내는 노드 (태그)
  - Text Node => HTML 텍스트 (Element Node 내의 텍스트 컨텐츠)
  - Attribute Node => HTML 요소의 속성을 나타내는 노드

## NodeList
- DOM 메서드를 사용해 선택한 Node의 목록
- 배열과 유사한 구조
- Index로 각 항목에 접근 가능
- JavaScript의 배열 메서드 사용 가능
- querySelectorAll() 에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간을 반영하지 않음

## Element
- Node의 하위 유형
- Elemnet는 DOM 트리에서 HTML 요소를 나타내는 특별한 유형의 Node
  - 모든 Element는 Node 이지만, 모든 Node가 Element 인 것은 아님

## Parsing
- 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정
