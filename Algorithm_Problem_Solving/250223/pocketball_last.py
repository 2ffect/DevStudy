import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = '오승연_3연승'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.

    # --- 기본 변수 설정 ---
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # --- 목표공 선택 (기존 로직 수정) ---
    # 후보: 선공이면 [1, 3, 5], 후공이면 [2, 4, 5]
    if order == 1:
        candidates = [1, 3, 5]
        opp_indices = [2, 4]  # 상대방의 목적구
    else:
        candidates = [2, 4, 5]
        opp_indices = [1, 3]

    # 상대 공들의 위치 (포켓되지 않은 경우)
    opp_balls = []
    for i in opp_indices:
        if balls[i][0] != -1 and balls[i][1] != -1:
            opp_balls.append((balls[i][0], balls[i][1]))


    # 함수: P->Q 경로에 상대 공이 존재하는지 판별
    def is_path_blocked(P, Q, opp_balls, threshold=5.0):
        # P, Q: (x,y) 좌표, threshold: 허용 오차
        px, py = P
        qx, qy = Q
        dx = qx - px
        dy = qy - py
        mag_sq = dx * dx + dy * dy
        if mag_sq == 0:
            return False
        for (ox, oy) in opp_balls:
            t = ((ox - px) * dx + (oy - py) * dy) / mag_sq
            if t < 0 or t > 1:
                continue
            proj_x = px + t * dx
            proj_y = py + t * dy
            if math.sqrt((ox - proj_x) ** 2 + (oy - proj_y) ** 2) < threshold:
                return True
        return False


    chosen_index = None
    for cand in candidates:
        if balls[cand][0] != -1 and balls[cand][1] != -1:
            candidate_pos = (balls[cand][0], balls[cand][1])
            if not is_path_blocked((whiteBall_x, whiteBall_y), candidate_pos, opp_balls, threshold=5.0):
                chosen_index = cand
                break
    # 만약 모든 후보(검은 공 제외) 경로에 상대 공이 있으면, fallback으로 검은 공(인덱스 5)을 선택
    if chosen_index is None:
        chosen_index = fallback

    targetBall_x = balls[chosen_index][0]
    targetBall_y = balls[chosen_index][1]

    # --- 각도 계산 ---
    # 흰 공과 목표공 사이의 상대적 위치로부터 각도 산출
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)
    dx = whiteBall_x - targetBall_x
    dy = whiteBall_y - targetBall_y

    radian = math.atan(width / height) if height > 0 else 0
    angle = (180.0 / math.pi) * radian

    if whiteBall_x == targetBall_x:
        angle = 0 if whiteBall_y < targetBall_y else 180
    elif whiteBall_y == targetBall_y:
        angle = 90 if whiteBall_x < targetBall_x else 270

    if whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(width / height)
        angle = (180.0 / math.pi) * radian + 179
    elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(height / width) if width != 0 else 0
        angle = (180.0 / math.pi) * radian + 89
    elif whiteBall_x > targetBall_x and whiteBall_y < targetBall_y:
        radian = math.atan(height / width) if width != 0 else 0
        angle = (180.0 / math.pi) * radian + 269

    # --- 파워 결정 ---
    shot_distance = math.sqrt(dx ** 2 + dy ** 2)
    power = 100

    ##############################
    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    #
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')