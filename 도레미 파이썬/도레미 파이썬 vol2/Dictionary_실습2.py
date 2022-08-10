my_dict = {}
my_dict[(1)] = "Integer"
my_dict[('a')] = "String"
my_dict[(1,2,3)] = "Tuple"

print(my_dict)

try:
    my_dict[[1,2,3]] = "List"
    #여기에 [1, 2, 3] → "List"의 대응관계를 만들어봅시다.
    
    
except TypeError:
    print("List는 Dictionary의 Key가 될 수 없습니다.")

   
