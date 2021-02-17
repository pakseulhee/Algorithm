def solution(brown, yellow):
    sum = brown+yellow
    answer = []
    for i in range(1, sum):
        if (i-2)*2+(sum/i-2)*2 +4 == brown:
            answer = [i, sum/i]
            answer.sort(reverse=True)
            return answer