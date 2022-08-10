# 다음은 표준어로 "밥 먹었어요?"가 담긴 변수 greeting입니다.
greeting = "밥 먹었어요?" #전역변수

# 이를 print로 출력하면 다음과 같습니다.
print("서울 :",greeting)

# 함수 busan을 선언하고, 그 안에 변수 greeting에 "밥 뭇나?"를 넣어봅시다.
def busan():
    greeting = "밥 뭇나?"   #지역변수
    print("부산 :",greeting)
# 함수 busan을 실행해보세요.        함수 실행 방법 = 함수이름
busan()

# 변수 greeting을 출력해보세요.
print(greeting)
