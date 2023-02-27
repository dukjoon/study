a = list(map(int,input().split()))
b = list(map(int,input().split()))
result =[]
x = len(a)
def solution(a, b):
    for i in range(0,x):
        result.append(a[i] * b[i])
        answer = sum(result)
    return answer

print(solution(a, b))