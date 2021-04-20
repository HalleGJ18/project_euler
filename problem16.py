#project euler #16
#sum of the digits of 2^1000

num = 2**1000
print(num)

digits = [int(d) for d in str(num)]
print(digits)

total = 0

for i in digits:
    total += i

print("total: {}".format(total))
