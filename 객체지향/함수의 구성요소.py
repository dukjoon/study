# 태오난 연도를 받아 나이를 리턴

#year_of_birth = 매개변수, 매개변수는 이 떄 1개이다.

def calculate_age(year_of_birth):
    this_year = 2022
    age =  this_year - year_of_birth + 1
    return age
    print(age) #실행되지 않음. return 뒤에 들어오기 때문이다.
    #주 목적(return)이 달성되었으니 뒤에 값은 실행되지 않음.
# return값은 return 뒤에 있는 값. (함수에서 구하고자 하는 값.), 중요

age = calculate_age(1998) #이 때 1998 은 인자이다.

#매개변수 = def, 함수를 정의하는 시점에서 
#인자 = 함수를 사용하는 시점

def calculate_age(year_of_birth):
    this_year = 2022
    age =  this_year - year_of_birth + 1
    print(age)
    return(age)
    #이렇게 하면 모두가 행복해짐

