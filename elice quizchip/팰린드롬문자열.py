n = int(input())
x = str(input())
y = x
a = list(x)
b = list(y)

a.reverse()

if a == b:
    print(1)
else:
    print(0)