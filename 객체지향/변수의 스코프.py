this_year = 2018 #int 값

def calculate_age(year_of_birth):
    return this_year - year_of_birth + 1
    #this_year는 바깥쪽에 있는 값에서 가져온다.


def next_year(year):
    next_year = 2023
    return next_year

print(f"내년은 {next_year}년 입니다.")

#scope 로 인해서 2번째 함수는 오류가 난다.

