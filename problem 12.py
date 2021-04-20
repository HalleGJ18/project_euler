#first triangle num to have over 500 divisors
from functools import reduce
def factors(n):
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

count = 1
#base = 1000000
#triangle = int((base*(base+1))/2)
triangle = 0 
print("triangle: ", triangle)

for count in range(1, 100000000000):
    triangle += count
    divisors = len(factors(triangle))
    print(triangle, count, divisors)
    if divisors >= 500:
        break
    count += 1
            
