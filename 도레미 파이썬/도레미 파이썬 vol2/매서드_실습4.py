# 대기시간이 담긴 리스트가 인자로 주어지면 조건을 만족하도록
# 타야하는 대기시간의 순서가 담긴 리스트를 반환하는 함수 neverland()를 작성해봅시다.
queue = [30, 10, 20, 50, 40, 60]
var = queue.pop(1)
print(var)  # 인덱스 2에 해당하는 값 추출

def neverland(a):
    return a.sort()


print(neverland(queue))


# 확인을 위한 코드입니다.
# 대기시간이 담긴 리스트 queue를 자유롭게 수정해보세요!
queue = [30, 10, 20, 50, 40, 60]
print(neverland(queue))
