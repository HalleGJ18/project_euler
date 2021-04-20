pals = []

for num1 in range(100,999):
    for num2 in range(100,999):
        p = num1 * num2
        rp = (str(p)[::-1])
        p = str(p)
        if p == rp:
            p = int(p)
            pals.append(p)

pals.sort(reverse = True)
print(pals[0])
