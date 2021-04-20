#project euler problem 14
#longest collatz sequence

#n -> n/2 (if n is even)
#n -> 3n+1 (if n is odd)

longest = 1000000
longest_count = 0

for n in range(2, 1000001):
    num = n
    count = 0
    while n > 1:
        #print(n)
        if n%2 == 0:
            n = n/2
            count += 1
        else:
            n = (3*n)+1
            count += 1
    if count > longest_count:
        longest = num
        longest_count = count
    print("num: {}, count: {}".format(num,count))
    print("longest: {}, longest_count: {}".format(longest, longest_count))
    print("--------------------------------------")

c = input("finished... ")

#837799
