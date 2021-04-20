#sum of all primes below 2 million
primes = 0

for num in range(2,2000000):
    if all(num%i!=0 for i in range(2,num)):
       primes = primes + num
       print(num)

print("Total is", primes)

#literally takes hours do not use for large numbers
#instead use sieve of eratosthenes
