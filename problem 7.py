#what is the 10001st prime?
primes = []

for num in range(2,150000):
    if all(num%i!=0 for i in range(2,num)):
       primes.append(num)
       print(num)


print("The 10001st prime",(primes[10000]))
#104743
