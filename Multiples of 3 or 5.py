def solution(number):
    answer = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            answer.append(i)
    return sum(answer)
