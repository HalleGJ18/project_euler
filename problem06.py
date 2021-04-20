sumofsq = 0
sqofsum = 0

for i in range(0,101):
    sumofsq = sumofsq + i*i


num = 0
for i in range(0,101):
    num = num + i

print(num)
sqofsum = num*num

diff = sqofsum - sumofsq
print(sumofsq)
print(sqofsum)

print(diff)

