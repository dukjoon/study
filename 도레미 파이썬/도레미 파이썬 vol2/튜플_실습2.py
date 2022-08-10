my_tuple = (1, 2, 3)

try:
    #여기에 인덱싱을 이용해서 Tuple의 값을 변경해봅시다.
    my_tuple[2] = '5'
    
except TypeError:
    print("Tuple은 값을 변경할 수 없습니다.")
    
try:
    #여기에 .append()를 이용해서 Tuple의 값을 추가해봅시다.
    my_tuple.append('6')
    
except AttributeError:
    print("Tuple은 값을 추가할 수 없습니다.")