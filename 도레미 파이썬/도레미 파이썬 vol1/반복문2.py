# range: 연속되는 숫자를 만들어 주는 시퀀스 자료형
## range(a,b) a = start , b = end => a, a+1, a+2 ... b-1 까지

### for 변수 in range(a,b):
###   <수행할 명령>

a = [1]
for i in range(2,4):
    a.append(i)

print(a)


count = 0
for i in range(10):
    count = count + 1

print(count)

# i 에 대한 언급이 없으나, i는 range에서 값을 받아오는 용도.
## for문 안에 반드시 사용 할 필요 X