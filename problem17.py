#project euler #17

#could probably do this recursively pretty decently

AND = 3

units = {
    "0":0,
    "1":3, 
    "2":3,
    "3":5,
    "4":4,
    "5":4,
    "6":3,
    "7":5,
    "8":5,
    "9":4
    }

teens = {
    "11":6,
    "12":6,
    "13":8,
    "14":8,
    "15":7,
    "16":7,
    "17":9,
    "18":8,
    "19":8
    }

tens = {
    "0":0, 
    "1":3, #10
    "2":6, #20
    "3":6, #30
    "4":5, #40
    "5":5, #50
    "6":5, #60
    "7":7, #70
    "8":6, #80
    "9":6  #90
    }

large = {
    "100":7,
    "1000":8
    }

total = 0

for n in range(1,1001):
    num = str(n)

    if len(num) == 1:
        print("n = {}, len = 1".format(num))
        total += units[num]

    elif len(num) == 2:
        print("n = {}, len = 2".format(num))
        if n in range(11,20):
            total += teens[num[0:2]]
        else:
            total += tens[num[0]]
            total += units[num[1]]

    elif len(num) == 3:
        print("n = {}, len = 3".format(num))
        total += units[num[0]]
        total += large["100"]
        if num not in ["100", "200", "300", "400", "500", "600", "700", "800", "900"]:
            total += AND
            if int(num[1:3]) in range(11,20):
                total += teens[num[1:3]]
            else:
                total += tens[num[1]]
                total += units[num[2]]

    else:
        print("n = {}, len = 4".format(num))
        total += units[num[0]]
        total += large["1000"]

print("total = {}".format(total))
                   
