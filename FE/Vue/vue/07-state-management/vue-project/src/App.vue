<template>
  <div class="container">
    <!-- Header -->
    <header class="header">
      <div class="title">청년정책 커뮤니티</div>
      <nav class="nav">
        <a href="#">청년정책</a>
        <a href="#">청년소식</a>
        <a href="#">청년지원</a>
        <a href="#">청년신문고</a>
        <a href="#">청년정책조정위원회</a>
        <a href="#">소개</a>
      </nav>
    </header>

    <!-- Main Content -->
    <main class="main">
      <section class="policy-section">
        <h2>청년정책, 검색과 챗봇으로 쉽게 찾아보세요!</h2>
        <p>
          국민내일배움카드, 교육훈련, 청년월세지원, 청년내일저축, 창업지원 등 키워드로 찾아보세요.
        </p>
        <div class="buttons">
          <button>인기있는 청년 정책은?</button>
          <button>취업관련 지원금 찾아줘</button>
          <button>주거 관련 지원금 알려줘</button>
          <button>자기소개서 컨설팅 문의</button>
          <button>청년 창업자금 알려줘</button>
        </div>
        <div class="chatbot">
          <img src="#" alt="Chatbot">
          <button>챗봇 바로가기</button>
        </div>
      </section>

      <!-- User Panel -->
      <aside class="user-panel">
        <div class="user-info">
          <h3>김재희님 환영합니다!</h3>
          <p>- | - | 남자 | -</p>
          <button>퍼스널정보 설정</button>
        </div>
        <div class="user-stats">
          <div>
            <span>내가 스크랩한 정책</span>
            <span>0개</span>
          </div>
          <div>
            <span>내게 맞는 정책</span>
            <span>3451개</span>
          </div>
          <button>공공 마이데이터 서비스</button>
        </div>
        <div class="user-links">
          <button>공공 마이데이터</button>
          <button>개인정보 설정</button>
          <button>로그아웃</button>
        </div>
      </aside>
    </main>
  </div>
</template>

<script setup>
// 필요한 경우 컴포넌트 로직 추가
</script>

<style scoped>
.container {
  font-family: Arial, sans-serif;
  padding: 20px;
  max-width: 1200px;
  margin: auto;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #ddd;
  padding-bottom: 10px;
}

.title {
  font-size: 24px;
  font-weight: bold;
}

.nav a {
  margin: 0 10px;
  text-decoration: none;
  color: #333;
}

.main {
  padding: 20px 0;
}

.policy-section {
  background: #f0f8ff;
  padding: 20px;
  border-radius: 8px;
}

.policy-section h2 {
  color: #007bff;
  margin-bottom: 10px;
}

.policy-section p {
  margin-bottom: 20px;
  color: #555;
}

.buttons button {
  margin: 5px;
  padding: 8px 12px;
  background-color: white;
  border: 1px solid #ccc;
  border-radius: 4px;
  cursor: pointer;
}

.chatbot {
  margin-top: 20px;
  display: flex;
  align-items: center;
}

.chatbot img {
  width: 50px;
  height: 50px;
  margin-right: 10px;
}

.chatbot button {
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.user-panel {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  margin-top: 20px;
  padding: 15px;
}

.user-info h3 {
  font-size: 18px;
  margin-bottom: 5px;
}

.user-info button,
.user-stats button,
.user-links button {
  padding: 6px 12px;
  margin-top: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: #f8f8f8;
  cursor: pointer;
}

.user-links {
  margin-top: 10px;
  display: flex;
  justify-content: space-around;
}
</style>
