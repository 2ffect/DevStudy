from pprint import pprint

### 전치 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
reverse = list(map(list, zip(*matrix)))

### 90도 시계방향 회전
turn_90 = list(map(list, zip(*matrix[::-1])))
