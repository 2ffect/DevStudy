# Bootstrap Grid system
- 웹 페이지의 레이아웃을 조정하는데 사용되는 12개의 컬럼으로 구성된 시스템

## Grid system 목적
- 반응형 디자인을 지원해 웹 페이지를 모바일, 태블릿, 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움

## Grid system 기본요소
1. Container
   - Column 들을 담고 잇는 공간

2. Column
   - 실제 컨텐츠를 포함하는 부분

3. Gutter
   - 컬럼과 컬럼 사이의 여백 영역(상하좌우)

* 1개의 Row 안에 12개의 column 영역이 구성된다.
* 각 요소는 12개 중 몇 개를 차지할 것인지 지정
  

![alt text](/DevStudy/TIL/img_for_Python/Grid_system.png\).png)


# 반응형 웹 디자인 (Responsive Web Design)
- 디바이스의 종류나 화면 크기에 상관없이 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술


![alt text](/DevStudy/TIL/img_for_Python/Responsive_Web.png)

## Grid system breakpoints
- 웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점
  - 화면 너비에 따라 6개의 분기점 제공 (xs, sm, md, lg, xl, xxl)
  - 각 break point 마다 설정된 최대 너비 값 **"이상으로"** 화면이 커지면 grid system 동작이 변경 됨

* CSS 레이아웃 기술들은 각각 고유한 특성과 장단점을 가지고 있음
* 이들은 상호 보완적이며, 특정 상황에 따라 적합한 도구가 달라짐
* 최적의 기술을 선택하고 효과적으로 활용하기 위해서는 다양한 실제 개발 경험이 필수적

## UX(User Experience)
- 제품이나 서비스를 사용하는 사람들이 느끼는 전체적인 경험과 만족도를 개선하고 최적화하기 위한 디자인과 개발 분야

## UI(User Interface)
- 서비스와 사용자 간의 상호작용을 가능하게 하는 디자인 요소들을 개발하고 구현하는 분야