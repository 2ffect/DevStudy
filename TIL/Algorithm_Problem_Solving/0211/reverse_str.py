문자열 뒤집기
s = 'Reverse this strings'
s = s[::-1]
print(s)

문자열을 리스트로 변환 후 뒤집기
str = 'abcd'
string = list(str)
string.reverse()
result = ''.join(string)

print(result)

인풋받은 문자열을 뒤집기
txt = list(input())
N = len(txt)
for i in range(N//2):
    txt[i], txt[N-1-i] = txt[N-1-i], txt[i]
print(f'{"".join(txt)}')

# 회문 찾기
N = int(input())
txt = input()
total = 0
for j in range(8-N+1):      # 회문을 확인하는 구간의 첫 글자 인덱스
    for k in range(N//2):   # 회문의 길이 절반만큼 비교
        if txt[j+k] != txt[j+n-1-k]:
            break           # 비교 글자가 다르면 for k 구간 중지

    else:                   # break에 걸리지 않고 for k 구간 종료 시 = 회문이면 total + 1
        total += 1
