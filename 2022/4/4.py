if __name__ == "__main__":
    # part 1 + 2
    file = open("input.txt", encoding='utf-8')
    fullyContains = 0
    partlyContains = 0
    for line in file.readlines():
        list1, list2 = line.strip().split(',')
        array1 = [*range(int(list1.split("-")[0]), int(list1.split("-")[1]) + 1, 1)]
        array2 = [*range(int(list2.split("-")[0]), int(list2.split("-")[1]) + 1, 1)]
        if set(array1).issubset(set(array2)) or set(array2).issubset(set(array1)):
            fullyContains += 1
        if len(set(array1).intersection(array2)) > 0:
            partlyContains += 1
    print(fullyContains)
    print(partlyContains)
    file.close()