# return vs print

def calculate_age(year_of_birth):
    this_year = 2022
    return this_year - year_of_birth + 1

age = calculate_age(1998)
print(calculate_age(1998))

# return은 함수 안에서만 사용된다. 함수의 결과물이기 때문
# 
