# [카카오 인턴] 키패드 누르기

# 시작 시간 : 19:30
# 종료 시간 : 19:55 성공

def solution(numbers, hand):
    answer = []
    lt = [3, 0]
    rt = [3, 2]

    for num in numbers:
        if num in [1, 4, 7]:
            answer.append('L')
            if num == 1:
                lt = [0, 0]
            elif num == 4:
                lt = [1, 0]
            elif num == 7:
                lt = [2, 0]

        elif num in [3, 6, 9]:
            answer.append('R')
            if num == 3:
                rt = [0, 2]
            elif num == 6:
                rt = [1, 2]
            elif num == 9:
                rt = [2, 2]

        elif num in [2, 5, 8, 0]:
            if num == 2:
                if (abs(lt[0] - 0) + abs(lt[1] - 1)) > (abs(rt[0] - 0) + abs(rt[1] - 1)):
                    answer.append('R')
                    rt = [0, 1]
                elif (abs(lt[0] - 0) + abs(lt[1] - 1)) < (abs(rt[0] - 0) + abs(rt[1] - 1)):
                    answer.append('L')
                    lt = [0, 1]
                elif (abs(lt[0] - 0) + abs(lt[1] - 1)) == (abs(rt[0] - 0) + abs(rt[1] - 1)):
                    if hand == 'right':
                        answer.append('R')
                        rt = [0, 1]
                    else:
                        answer.append('L')
                        lt = [0, 1]

            elif num == 5:
                if (abs(lt[0] - 1) + abs(lt[1] - 1)) > (abs(rt[0] - 1) + abs(rt[1] - 1)):
                    answer.append('R')
                    rt = [1, 1]
                elif (abs(lt[0] - 1) + abs(lt[1] - 1)) < (abs(rt[0] - 1) + abs(rt[1] - 1)):
                    answer.append('L')
                    lt = [1, 1]
                elif (abs(lt[0] - 1) + abs(lt[1] - 1)) == (abs(rt[0] - 1) + abs(rt[1] - 1)):
                    if hand == 'right':
                        answer.append('R')
                        rt = [1, 1]
                    else:
                        answer.append('L')
                        lt = [1, 1]

            elif num == 8:
                if (abs(lt[0] - 2) + abs(lt[1] - 1)) > (abs(rt[0] - 2) + abs(rt[1] - 1)):
                    answer.append('R')
                    rt = [2, 1]
                elif (abs(lt[0] - 2) + abs(lt[1] - 1)) < (abs(rt[0] - 2) + abs(rt[1] - 1)):
                    answer.append('L')
                    lt = [2, 1]
                elif (abs(lt[0] - 2) + abs(lt[1] - 1)) == (abs(rt[0] - 2) + abs(rt[1] - 1)):
                    if hand == 'right':
                        answer.append('R')
                        rt = [2, 1]
                    else:
                        answer.append('L')
                        lt = [2, 1]

            elif num == 0:
                if (abs(lt[0] - 3) + abs(lt[1] - 1)) > (abs(rt[0] - 3) + abs(rt[1] - 1)):
                    answer.append('R')
                    rt = [3, 1]
                elif (abs(lt[0] - 3) + abs(lt[1] - 1)) < (abs(rt[0] - 3) + abs(rt[1] - 1)):
                    answer.append('L')
                    lt = [3, 1]
                elif (abs(lt[0] - 3) + abs(lt[1] - 1)) == (abs(rt[0] - 3) + abs(rt[1] - 1)):
                    if hand == 'right':
                        answer.append('R')
                        rt = [3, 1]
                    else:
                        answer.append('L')
                        lt = [3, 1]

    return ''.join(answer)
