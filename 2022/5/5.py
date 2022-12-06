import re

if __name__ == "__main__":
    file = open("input.txt", encoding='utf-8')
    lines = file.readlines()
    file.close()

    # part 1
    numberOfPiles = int(len(lines[0]) / 4)
    piles = []
    for i in range(0, numberOfPiles, 1):
        piles.append([])

    indexStart = 0
    for i in range(0, len(lines), 1):
        if len(lines[i].strip()) != 0:
            for j in range(0, numberOfPiles, 1):
                char = lines[i][1+j*4]
                if char != "" and not char.isdigit() and char != " ":
                    piles[j].insert(0, char)
        else:
            indexStart = i + 1
            break

    for i in range(indexStart, len(lines), 1):
        amount, fromPile, toPile = [int(s) for s in re.findall(r'\b\d+\b', lines[i])]
        for j in range(0, amount, 1):
            piles[toPile - 1].append(piles[fromPile - 1].pop())

    for k in range(0, numberOfPiles, 1):
        print(piles[k][-1])
    print("")

    # part 2
    numberOfPiles = int(len(lines[0]) / 4)
    piles = []
    for i in range(0, numberOfPiles, 1):
        piles.append([])

    indexStart = 0
    for i in range(0, len(lines), 1):
        if len(lines[i].strip()) != 0:
            for j in range(0, numberOfPiles, 1):
                char = lines[i][1+j*4]
                if char != "" and not char.isdigit() and char != " ":
                    piles[j].insert(0, char)
        else:
            indexStart = i + 1
            break

    for i in range(indexStart, len(lines), 1):
        amount, fromPile, toPile = [int(s) for s in re.findall(r'\b\d+\b', lines[i])]
        tempPile = []
        for j in range(0, amount, 1):
            tempPile.append(piles[fromPile - 1].pop())
        for j in range(0, amount, 1):
            piles[toPile - 1].append(tempPile.pop())

    for k in range(0, numberOfPiles, 1):
        print(piles[k][-1])
    print("")