# 웹 브라우저와 JavaScript
### 웹의 탄생 (1990)
- 초기 웹은 정적인 텍스트 페이지만 지원
- Tim Berners-Lee 경이 WWW, 하이퍼텍스트시스템을 고안하여 개발 URL, HTTP 최초 설계 및 구현

### 웹 브라우저의 대중화 (1993)
- Netsacpe 사의 최초 상용 웹 브라우저인 Netscape Navigator 출시
- 당시 약 90% 이상의 시장 점유율을 가짐
  - Netsacpe사는 웹의 동적인 기능을 만들기 위한 프로젝트를 시장

### JavaScript의 탄생 (1995)
- Netsacpe 소속 개발자 Brenda Eich에 의해 스트립트 언어 Mocha 탄생
- LiveScript라는 이름으로 본경 했다가 Java의 명성에 기대기 위해 JavaScript로 이름을 변경
- JavaScript는 Netsacpe Navigator 2.0 에 탑재되어 웹 페이지에 동적 기능을 추가하는데 사용됨

### JavaScript 파편화 (1996)
- Microsoft 가 자체 웹 브라우저인 인터넷 익스플로러(IE) 3.0에 JavaScript와 유사한 언어 JScript 도입
- 이 과정에서 많은 회사들이 독자적으로 JavaScript를 변경하여 자체 브라우저에 탑재
  - 파편화 시작

### 1차 브라우저 전쟁 (1995-2001)
- 웹 표준의 부재로 인해 각 기업에서 자체 표준을 확립하려는 상황 발생
  - 이는 웹 개발자들에게 큰 혼란을 주었으며, 결국 웹 표준의 중요성을 인식하는 계기가 됨

### ECMAScript 출시 (1997)
- ECMA에서 ECMAScript라는 표준 언어를 정의하여 발표(1997)
- 이 때 부터 JavaScript는 ECMAScript 표준에 기반을 두고 발전하기 시작

### 2차 브라우저 전쟁 (2004-2017)
- 웹 표준이 정의되었지만 당시 가장 높은 점유율을 가진 IE는 웹 표준을 지키지 않고 독자적 규격을 유지하며 웹 시장을 주도

### Chrome 브라우저의 등장 (2008)
- Google의 Chrome 브라우저 출시
- 출시 3년만에 Friefox의 점유율을 넘고 그로부터 반년 뒤 IE의 점유율을 넘어섬
- ECMA 표준화를 잘 지킨 브라우저

### Chrome이 우위를 점하게 된 이유
- 빠른 성능, 다양한 플랫폼 지원, 보안, Google 생태계 통합 등의 이유가 있지만 가장 중요했던 역할은 "적극적인 웹 표준 준수"
- 호환성이 높고 개발자 도구를 활용할 수 있음

### 2차 브라우저 전쟁의 영향
- 웹 기능이 크게 확장되며 웹 애플리케이션의 비약적인 발전을 이끌어 감
  - 웹의 기술적 발전과 웹 표준의 중요성

# ECMAScript
- Ecma International이 정의하고 있는 표준화된 스크립트 프로그래밍 언어 명세
- 스크립트 언어가 준수해야 하는 규칙, 세부사항 등을 제공

### ECMAScript와 JavaScript
- JavaScript는 ECMASCript 표준을 구현한 구체적인 프로그래밍 언어
- ECMASCript의 명세를 기반으로 하여 웹 브라우저나 Node.js 와 같은 환경에서 실행 됨
  - ECMASCript 는 JavaScript의 표준이며, JavaScript는 ECMASCript 표준을 따르는 구체적인 프로그래밍 언어
  - ECMASCript 는 핵심 언어를 정의하고, JavaScript는 ECMASCript 표준을 따라 구현된 언어로 사용됨

### ECMASCript의 역사
- ECMASCript 5 (ES5) 에서 안정성과 생산성을 크게 높임 (2009)
- ECMASCript 2015 (ES6) 에서 객체지향 프로그래밍 언어로써 많은 발전을 이루어, 역사상 가장 중요한 버전으로 평가됨 (2015)

### JavaScript의 현재
- 현재는 Chrome, FireFox, Safari, Microsoft Edge 등 다양한 웹 브라우저가 경쟁하고 있으며 모바일 등 시장이 다양화 되어있음
- 기존에 JavaScript는 브라우저에서만 웹 페이지의 종적인 기능을 구현하는 데에만 사용되었음
- 이후 Node.js (2009 출시) 로 인해 브라우저 외부에서도 실행 가능해져 서버 사이드 개발에도 사용되기 시작
- 다양한 프레임워크와 라이브러리들이 개발되면서 웹 개발 분야에서는 필수적 언어로 자리잡게 됨