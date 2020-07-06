text = open("path file here", "r")
names = text.read().split(",")
names = sorted(names)
sum = 0
letters = {"A":1,
        "B":2,
        "C":3,
        "D":4,
        "E":5,
        "F":6,
        "G":7,
        "H":8,
        "i":9,
        "J":10,
        "K":11,
        "L":12,
        "M":13,
        "N":14,
        "O":15,
        "P":16,
        "Q":17,
        "R":18,
        "S":19,
        "T":20,
        "U":21,
        "V":22,
        "W":23,
        "X":24,
        "Y":25,
        "Z":26
}

for name in names:
    temp = 0
    for letter in name:
        if letter in letters:
            temp += letters[letter]
    temp = names.index(name) * temp
    sum += temp
print(sum)