n = int(input())
def solution(n):
    answer = 0
    a = n ** (1/2)
    x =[]
    for i in str(a):
        x.append(i)
    print(x)
    if x[-1] == '0':
        answer = (a+1)**2
            
    else:
        answer = -1
        
    return answer

print(solution(n))
