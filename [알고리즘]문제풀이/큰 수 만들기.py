def solution(number, k):
    stack = [number[0]] #list의 첫번째 수를 스택에 저장
    for num in number[1:]: #list의 남은 부분을 순회
        while len(stack) > 0 and stack[-1] < num and k > 0: #새로운 수가 stack의 마지막 숫자보다 크다면?
            k -= 1
            stack.pop() #stack안에 작은 수를 소거 (이걸 계속 반복하기 위해 while문을 사용)
        stack.append(num) #새로운 수가 stack의 마지막 수보다 크지 않다면 append

    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)