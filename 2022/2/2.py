if __name__ == "__main__":
    # part 1
    file = open("input.txt", encoding='utf-8')
    score = 0
    for line in file.readlines():
        opp, me = line.strip().split(" ")
        if (opp == 'A' and me == 'X'):
            score += 4
        elif (opp == 'A' and me == 'Y'):
            score += 8
        elif (opp == 'A' and me == 'Z'):
            score += 3
        elif (opp == 'B' and me == 'X'):
            score += 1
        elif (opp == 'B' and me == 'Y'):
            score += 5
        elif (opp == 'B' and me == 'Z'):
            score += 9
        elif (opp == 'C' and me == 'X'):
            score += 7
        elif (opp == 'C' and me == 'Y'):
            score += 2
        elif (opp == 'C' and me == 'Z'):
            score += 6
    print(score)
    file.close()

    # part 2
    file = open("input.txt", encoding='utf-8')
    score = 0
    for line in file.readlines():
        opp, me = line.strip().split(" ")
        if (opp == 'A' and me == 'X'):
            score += 3
        elif (opp == 'A' and me == 'Y'):
            score += 4
        elif (opp == 'A' and me == 'Z'):
            score += 8
        elif (opp == 'B' and me == 'X'):
            score += 1
        elif (opp == 'B' and me == 'Y'):
            score += 5
        elif (opp == 'B' and me == 'Z'):
            score += 9
        elif (opp == 'C' and me == 'X'):
            score += 2
        elif (opp == 'C' and me == 'Y'):
            score += 6
        elif (opp == 'C' and me == 'Z'):
            score += 7
    print(score)
    file.close()