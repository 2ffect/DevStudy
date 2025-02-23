# 일타싸피 대비
import math

# 수구, 목적구, 포켓(구멍)의 좌표가 주어질 때
# 목적구를 맞춰 포켓으로 보내기 위해 수구가 진행되어야 할 각도, 목적구 까지의 거리를 구해보자

my_ball = list(map(int, input().split()))
target_ball = list(map(int, input().split()))

# 포켓볼의 포켓은 6개 이지만 가장 가까이 있는 한 군데의 포켓 좌표만 주어진다고 가정
pocket = list(map(int, input().split()))

# 공의 반지름
r = 2.75

# 포켓 기준
# dx, dy = 수구와 포켓
dx = pocket[0]-my_ball[0]
dy = pocket[1]-my_ball[1]
# tx, ty = 목적구와 포켓
tx = pocket[0]-target_ball[0]
ty = pocket[1]-target_ball[1]
# nx, ny = 수구와 목적구
nx = my_ball[0]-target_ball[0]
ny = my_ball[1]-target_ball[1]

# 가 의 각도 계산
theta_1 = math.degrees(math.atan2(dy, dx))

# 포켓과 수구의 거리 (a)
a = math.sqrt(dx**2 + dy**2)

# 포켓과 목적구의 거리 (b)
b = math.sqrt(tx**2 + ty**2)

# 수구와 목적구의 거리 (c)
c = math.sqrt(nx**2 + ny**2)

# 다 의 각도 계산
da = ((a**2 + b**2 - c**2) / (2 * a * b))
theta_3 = math.degrees(math.acos(da))

# d의 거리 (수구와 접점의 거리) - 목적구를 맞추기 위해서 수구를 보내야 하는 최소한의 거리
d = math.sqrt(a**2 + (b + 2 * r)**2 - 2 * a * (b + 2 * r) * math.cos(math.radians(theta_3)))

# 나 의 각도 계산
na = ((a**2 + d**2 - (b + 2 * r)**2) / (2 * a * d))
na = max(-1, min(1, na))
theta_2 = math.degrees(math.acos(na))

# 수구의 진행각도
result_degrees = (theta_1 + theta_2)

print(d, result_degrees)

# 스테이지 1~3은 될 때 까지 노가다 조정하면서 한 번에 넣으면 된다.
# 4는...? 목적구가 2개다 가까운거 하나 넣고, 다른 목적구의 위치를 받아와?
# ... 1목적구 2목적구 2개로 받아오고,,, 계산 2번 노가다 해.?????
# .......근데 이게 맞나...
# 너무 그냥 각도,거리만 계산 한 거 같은데