num = 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20
num2 = 20*19*18*17*16*15*14*13*12*11*10


for n in range(1,num2):
    if all(n % i == 0 for i in range(1,20)):
        print(n)

print("done")
