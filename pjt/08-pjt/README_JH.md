# 08_pjt

## <역할 분배>
동영상 검색 결과 출력 (API 연동)
동영상 상세 정보 출력

## <학습한 내용, 배우고 느낀점>
1. v-if 사용 시 조건에 대한 문제
- `v-if="!store.laterVideos.includes(findVideo)"`가 동작하지 않음
- 버튼이 저장/취소 상태로 전환되지 않음
- 저장된 후에도 `"동영상 저장"` 버튼이 계속 보임

#### 핵심 원인
- `includes()`는 객체 참조 비교 → 같은 내용이라도 false 반환
- 해결: `some()`으로 `video.id.videoId === findVideo.id.videoId` 형태의 **값 비교** 사용

#### 해결 코드
```vue
<button
  v-if="!store.laterVideos.some(video => video.id.videoId === findVideo.id.videoId)"
  @click="addLater">
  동영상 저장
</button>

<button
  v-else
  @click="deleteLater">
  저장 취소
</button>
```
2. 저장/삭제 버튼 상태가 뒤로가기 시 반영되지 않음
- 뒤로 가기 후 디테일 페이지 재진입하면 버튼 상태가 초기화됨
- 로컬스토리지에는 저장돼 있는데 렌더링 상태가 초기처럼 보임

#### 핵심 원인
- 컴포넌트 마운트 시 laterVideos가 초기화된 상태에서 렌더링 됨
- Pinia에 persist 설정이 제대로 동작하지 않거나 loadFromLocalStorage() 누락됨

#### 해결 방법
- onMounted()에서 수동 로딩
```vue
onMounted(() => {
  store.loadFromLocalStorage()
})
```

## <어려웠던 부분>
- v-if가 DOM 제어에서는 훨씬 직관적이라는 것을 체감함
- 객체 비교의 함정을 처음 실전에서 겪음 → 값 비교 습관 중요
- DevTools 디버깅이 익숙해지면서 디버깅에 대한 두려움이 줄었음
- 저장 상태 유지와 반응형 렌더링의 연계 흐름을 명확히 이해하게 됨