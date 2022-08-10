result = 0
sum = 0
ans = 0

while True:
    n = int(input())
    sum += n
    ans += 1
    if n == 0:
        break 

# print(sum) #0 나오면 break, sum까지 올바르게 구해짐

print(sum / (ans -1))
