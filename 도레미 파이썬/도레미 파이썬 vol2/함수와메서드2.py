# def my_func(a):
#     x = "hi!"
#     print(a)

# print(x)    # Error
#             #함수 안에서 일어난 일은 함수 밖에 영향을 주지 않는다!

x = "Hi!"       # 전역 변수: 어디서든지 사용할 수 있는 변수, 
                #           함수 밖에서 정의된 함수
def my_func():
    print(x)

my_func()
print(x)


#함수 안에서 정의된 변수는 지역 변수라고 한다. 
# 변수를 정의한 범위(들여쓰기)에서만 사용이 가능!