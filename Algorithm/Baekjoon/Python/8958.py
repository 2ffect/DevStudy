A = int(input())
list = [input() for _ in range(A)]


for i in list:
    score = 0
    total_score = 0
    for j in i:
        if j == 'O':
            score += 1
            total_score += score
        else:
            score = 0
    print(total_score)