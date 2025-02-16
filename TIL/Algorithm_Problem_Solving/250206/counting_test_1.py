'''
0 <= DATA[i] <=4
'''

data = [0, 4, 1, 3, 1, 2, 4, 1]
N = len(data)

# counts 개수 설정 시 주의.
counts = [0] * (max(data) + 1)

#정렬 된 데이터를 받을 리스트
temp = [0] * N

# 1단계
# data[i]를 하나씩 꺼내와서 
# data[i] == counts[data[i]] 일때 해당 인덱스에 +1
for i in range(N):
    counts[data[i]] += 1

# 2단계
# count[i] 까지의 합계 구하기
for i in range(1, len(counts)):
    counts[i] += counts[i-1]
print(counts)


for i in range(N-1, -1, -1):
    counts[data[i]] -= 1
    temp[counts[data[i]]] = data[i]
print(temp)