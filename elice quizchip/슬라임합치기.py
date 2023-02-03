n, k = map(int,input().split())
sum_m = 0
cnt = 0
x = list(map(int,input().split()))

while 1:
    if sum_m >= k:
        break
    elif len(x) == 1:
        break
    for i in range(0,2):
        a = min(x)
        sum_m += a 
        x.remove(min(x))
    cnt += 1


print(cnt)
