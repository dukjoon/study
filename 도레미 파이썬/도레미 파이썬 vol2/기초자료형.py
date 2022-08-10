# list.pop(i)
## 인덱스 i의 원소를 제거 후 그 원소를 반환 (괄호를 비울 시 마지막 원소)

my_list = [1, 2, 3, 4, 5]
print(my_list.pop(0)) #1
print(my_list.pop()) #5

my_seq = [2, 2, 2, 4, 4]
print(my_seq.count(2)) #3개


# str.split(c) 
## c를 기준으로 문자열을 쪼개서 리스트를 반환 (괄호를 비울 시 공백)
my_str = "1 2 3 4 5"
print(my_str.split())

element = "Na, Mg, Al, Si"
print(element.split(','))


# str.join(list)
## str을 기준으로 리스트를 합쳐서 문자열을 반환 (괄호를 비울 시 공백)

my_list2 = ['a', 'p', 'p', 'l', 'e']
print(''.join(my_list2))

friend = ['pat', 'mat']
print('&'.join(friend))