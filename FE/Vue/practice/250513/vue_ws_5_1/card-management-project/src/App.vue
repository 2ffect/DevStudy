<template>
  <header>
    <h1>명함 관리 페이지</h1>
  </header>
  <main>
    <p>명함을 관리하는 페이지 입니다. 여기에 명함 목록이 표시 됩니다.</p>
  </main>
  <article>

  </article>
  <footer>
    <p> &copy; 2025 My Business Cards</p>
  </footer>
</template>

<script setup>

</script>

<style scoped>
/* 전체 초기화 */
body {
  margin: 0;
  padding: 0;
  font-family: 'Arial', sans-serif;
  background-color: white;
}

/* 헤더를 페이지 맨 위에 블록처럼 배치 */
header {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 60px;
}

/* 헤더 내부 파란 박스 */
header h1 {
  background-color: dodgerblue;
  color: white;
  padding: 20px 40px;
  font-size: 1.8rem;
  font-weight: bold;
  border-radius: 4px;
  margin: 0;
}

/* 본문 텍스트 */
main {
  text-align: center;
  margin-top: 40px;
  color: #222;
  font-size: 1.05rem;
}

/* 푸터 고정 */
footer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #f2f2f2;
  text-align: center;
  padding: 10px 0;
  font-size: 0.9rem;
  color: #333;
  border-top: 1px solid #ccc;
}

</style>