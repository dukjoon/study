n = int(input())
s = str(input())

big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'

s_big, s_small, s_num = '', '', ''

for i in s:
    if i in big:
        s_big += i

    elif i in small:
        s_small += i

    elif i in num:
        s_num += i

print(len(s_big),end=' ')
print(len(s_small),end=' ')
print(len(s_num))