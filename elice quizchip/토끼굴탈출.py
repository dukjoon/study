n = int(input())
x = str(input())

upper_w = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_w = 'abcdefghijklmnopqrstuvwxyz'
nums_w = '1234567890'

result_u = ''
result_l = ''
result_n = ''

for c in x:
    if c in upper_w:
        result_u += c
    elif c in lower_w:
        result_l += c
    elif c in nums_w:
        result_n += c

print(len(result_u), len(result_l), len(result_n))