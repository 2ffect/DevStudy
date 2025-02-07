# 버블정렬 : 앞 뒤로 하나씩 비교해서 큰 수 뒤로 보내기
arr = [6, 7, 2, 3, 4, 1]
N =len(arr)

for j in range(N-1): 
    # 5번만 해도 마지막 하나는 남는자리

    for i in range(N - 1 - j):

        if arr[i] > arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
# print(arr)
   
# 카운팅 정렬 : 요소의 개수를 세서 자리 찾기
arr = [6, 5, 2, 7, 8, 4, 5, 6, 1, 2, 2, 3, 5, 8, 9, 0]
N = len(arr)
# print(N)
counts = [0] * 10
# counts 배열의 의미 : arr 배열 최대값 + 1
# 각 요소의 개수 > (누적합) > 각 요소의 위치

for i in range(N):
    counts[arr[i]] += 1
# print(counts)

for i in range(1, 10):
    counts[i] = counts[i] + counts[i-1]

# 정렬 된 값들이 들어갈 배열
sorted_arr = [0] *  N
for i in range(N-1, -1, -1):
    counts[arr[i]] -= 1
    sorted_arr[counts[arr[i]]] = arr[i]

print(sorted_arr)