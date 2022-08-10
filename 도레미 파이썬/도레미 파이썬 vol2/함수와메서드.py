# 함수의 구조
# len(): 그 자료의 길이를 알려줌
# int(): 정수형으로 변환
# str(): 문자열로 변환해서 알려줌


## 함수의 종류
## 내장 함수
## print(), len(), max(), int()

a = input()
print(a)

print(max(1, 2, 3, 4, 5))
print(min([1, 2, 3, 4, 5]))

print(sum((1, 2, 3, 4, 5)))
print(len("Triangle"))

# def 함수이름 (매개변수):       매개변수 = 함수 안에서 사용되는 변수
#   <수행할 명령>
#   ...
#   return 반환값

def plusDouble(a, b):
    c = a + b
    return 2*c
print(plusDouble(3, 4))
