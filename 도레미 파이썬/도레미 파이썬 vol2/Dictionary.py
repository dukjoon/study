# Dictionary = 사전
# 짝꿍이 있는 자료형

## {} 중괄호로 묶어서 표현

dict_zero = {}
person = {'name':'Michael', 'age':10}

### {key:value} 의 형식으로, key를 알면 value를 알 수 있다.

print(person['name']) # Michael
print(person['age']) # 10

#person = dictionary, 'age' = key

# Dictionary[key]   Dictionary에서 자료를 추가하기.

person['hometown'] = 'Seoul'

print(person['hometown'])


# del 함수로 Dictionary의 원소 삭제

del person['age']

print(person)

## Dictionary의 특징
## Key는 변할 수 없는 자료형 -> list는 안되고 tuple은 된다.

datas = {[1, 2, 3]:'Alphabet'} # error
datas = {(1, 2, 3):'Alphabet'} # ok