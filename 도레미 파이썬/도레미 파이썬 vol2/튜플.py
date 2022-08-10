# 여러 자료를 담는 자료형이 필요할 때
## 대부분 리스트를 이용, 그러나 값이 바뀔 위험이 있다.
### list = var 과 비슷
### tuple = const와 비슷, 값이 바뀌지 않으며 여러 자료를 담을 수 있음

tuple_zero = ()
tuple_one = (1,) #값이 한개밖에 없을때는 , 필수
tuple_ = (1, 2, 3, 4, 5)

my_tuple = ('t', 'w', 'i', 'c', 'e')
print('t' in my_tuple) #True
print(len(my_tuple)) #5 (길이 확인)


#연산자로 더하기 가능, 곱하기 가능
my_tuple2 = ('i', 'c', 'e')
print(('e', 'l') + my_tuple2)
print(my_tuple2 * 2)

#자료 추가, 삭제, 변경 불가 => error 뜬다.
print(my_tuple.append('!'))
print(my_tuple.remove('w'))
my_tuple[1] = 's'