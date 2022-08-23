n = int(input())

big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(n):
    b = str(input())


c = b[0].lower()
b = b[1:]
sent = c + b

sent.split("A")
sent.split("B")
sent.split("C")
sent.split("D")
sent.split("E")
sent.split("F")
sent.split("G")
sent.split("H")
sent.split("I")
sent.split("J")
sent.split("K")
sent.split("L")
sent.split("M")
sent.split("N")
sent.split("O")
sent.split("P")
sent.split("Q")
sent.split("R")
sent.split("S")
sent.split("T")
sent.split("U")
sent.split("V")
sent.split("W")
sent.split("X")
sent.split("Y")
sent.split("Z")

d = sent.split(big)
print(sent)
print(d)

