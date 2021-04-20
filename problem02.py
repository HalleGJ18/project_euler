num1 = 1
num2 = 1
total = 0
num3 = 0

while num3 in range(0,4000000):
    num3 = num1 + num2
    if num3 % 2 == 0:
        total = total + num3
    num1 = num3
    num3 = num1 + num2
    if num3 % 2 == 0:
        total = total + num3
    num2 = num3

print(total)
