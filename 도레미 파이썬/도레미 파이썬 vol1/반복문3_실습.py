#while을 이용해서 "i 년째 수감중입니다."를 출력해봅시다.
#while문이 종료된 후에는, "감옥에서 석방되었습니다!"를 출력해봅시다.

i = 0
while i < 10:
    i = i+1
    print(i,end='')
    print("년째 수감 중입니다.")

    if i == 10:
        print("감옥에서 석방되었습니다!")