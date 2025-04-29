## 비동기 팔로우 구현
1. 팔로우 기능을 비동기로 바꿔준다.
  - 클릭을 누르면 (aEL -> 이벤트 핸들러 실행) -> axios?
  - axios를 클릭 이벤트가 발생하면 실행
    - url : follow 기능을 담당하는 url로
    - 백엔드로 DB 변화 요청 (POST)

  1. 프로필 페이지에 axios CND 작성
  2. 선택할 form 요소에 id 속성 지정 및 선택
    - 요청은 axios로 대체되기 때문에 action과 method 속성은 삭제
  3. 선택한 form 요소에 이벤트 핸들러 할당 -> submit 이벤트의 기본 동작은 취소하기
  4. axios 요청 코드 작성
    1. csrftoken 가져오는 법 & 전송 하는 법
    - 가져오기  
    ```js
    // name이 csrfmiddlewaretoken인 어떤 요소를 가져와 value만 가져옴,
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    ```
    - 보내기
      - axios 요청을 보낼 때 headers를 작성하여 아래와 같이 전송을 함께 보낸다.
    ```js
    axios({
      ...
    headers: {'X-CSRFToken': csrftoken},
      ...
    })
    ```

2. 백엔드는 무슨 일을 해야할까?
  - DB에 변화 일으키기
  - JSON으로 응답 할 serializer (view 함수 수정)
    - 팔로우 여부와 대상의 팔로워 수 -> dict -> JSON으로 바꿔 응답
  ```py
  # django가 http에 맞춰 JSON 형태의 데이터를 응답할 수 있도록 도와줌
  from django.http import JsonResponse

  @login_required
  def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
            # 제거 되었기 때문에 False
            is_follow = False
        else:
            person.followers.add(request.user)
            # 추가 했기 때문에 True
            is_follow = True
    context = {
        # 현재 팔로우 여부
        'is_follow' : is_follow,
        # person의 팔로워 수
        'follower_count' : person.followers.count() 
    }
    # context 정보를 JSON으로 바꿔서 반환
    return JsonResponse(context)
  ```

3. 응답 받은 데이터로 DOM 요소 조작
  - JSON으로 상대방의 follower 수와 나의 상태를 받아와야 함
  ```js
  // 현재 person의 팔로워 수를 보여주는 spanTag
  const followerConstSpan = document.querySelector('#followers-count')
  const followbutton = document.querySelector('#follow-button')

  axios({
        url : "{% url 'accounts:follow' person.pk %}",
        method : 'POST',
        headers: {'X-CSRFToken': csrftoken},
      })
        .then((response) => {
          // JSON으로 상대방의 follower 수와 나의 상태를 받아와야 함
          // const { follower_count, is_follow } = response.data
          const followerCount = response.data.follower_count
          followerConstSpan.textContent = followerCount 

          const isfollow = response.data.is_follow
          // isfollow 의 값이 true면 Unfollow, false 면 follow
          followbutton.value = isfollow? 'Unfollow' : 'Follow'
        })
  ```

## 게시글 좋아요 구현
- 팔로우와 달리 좋아요 버튼이 여러개 있음
- 어떻게 구분할까 ?
  - 버블링 활용 최상단에 div 만들고 class 부여 후 가져오기
  - 각 아티클마다 id를 부여, url 에서 발생 시 event.target로 받아와 버블링 최상단에서 결정
