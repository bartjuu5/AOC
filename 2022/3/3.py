if __name__ == "__main__":
    # part 1
    file = open("input.txt", encoding='utf-8')
    sum = 0
    for line in file.readlines():
        string1, string2 = line[:len(line)//2], line[len(line)//2:]
        commonElement = set(string1).intersection(string2)
        if len(commonElement) == 1:
            if (ord(list(commonElement)[0]) > 96):
                sum += ord(list(commonElement)[0]) - 96
            else:
                sum += ord(list(commonElement)[0]) - 64 + 26
    print(sum)
    file.close()

    # part 2
    file = open("input.txt", encoding='utf-8')
    sum = 0
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        commonElement = set(lines[i].strip()).intersection(lines[i+1].strip()).intersection(lines[i+2].strip())
        if (ord(list(commonElement)[0]) > 96):
            sum += ord(list(commonElement)[0]) - 96
        else:
            sum += ord(list(commonElement)[0]) - 64 + 26
    print(sum)
    file.close()