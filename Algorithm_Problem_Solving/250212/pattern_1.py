txt = 'TTTTTATTAATA'
pattern = 'TTA'

N = len(txt)
M = len(pattern)

i = j = 0
cnt = 0
result = 0

while i < N and j < M:
    if txt[i] != pattern[j]: # 다르면
        i = i - j + 1           # i - j 비교를 시작 위치
        j = 0
    else:                   # 같으면
        i += 1
        j += 1
    if j == M:              # 패턴을 찾으면 cnt +1
        cnt += 1
        i = i - j + 1
        j = 0


print(cnt)