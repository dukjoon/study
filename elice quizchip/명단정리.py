words_u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(input())

x = str(input())

for i in x:
    if i in words_u:
        x.split(i)
    print(x.split(i))
