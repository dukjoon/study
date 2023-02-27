order = int(input())
def solution(order):
    order_list = []
    order = str(order)
    order_list = list(order)
    cnt = 0
    three_list = '369'
    for word in order_list:
        if word in three_list:
            cnt += 1
    return cnt

print(solution(order))