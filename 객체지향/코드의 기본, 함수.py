# 4주 과정
# 코드의 불필요한 반복을 줄여주고, 더 이해하기 쉬운 코드를 만들어 주는 함수

# 함수: 자주 사용하는 코드를 의미 단위로 묶어 둔 것.

## 태어난 연도를 받아 나이를 리턴
def calculate_age(year_of_birth):
    this_year = 2022
    return this_year - year_of_birth + 1
    
age = calculate_age(1988)

def roll_dice():
    return random.randint(1, 6)

def count_down(seconds):
    while seconds >= 0:
        print(seconds)
        time.sleep(1)
        second -= 1
        # seconds = 5라고 했을 때, 5, 4, 3, 2, 1(1초 간격)

#return 값과 print가 있다.

def clock_hourly():
    while True:
        print(date.time_now)
