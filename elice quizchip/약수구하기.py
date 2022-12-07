n = int(input())
result = []
cnt = 0
for i in range(1,n+1):
    if n % i == 0:
        result.append(i)
        cnt += 1

print(cnt)

for i in range(0,len(result)):
    print(result[i])