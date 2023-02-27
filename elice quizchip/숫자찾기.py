def solution(num, k):
    num = str(num)
    k = str(k)
    lst = []
    lst = list(num)
    answer = 0
    cnt = 0
    for i in lst:
        if k in lst:
            answer = int(lst.index(k)) + 1
        else:
            answer = -1
        
        
    return answer