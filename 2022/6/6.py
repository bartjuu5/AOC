from collections import Counter

BLOCK_SIZE_PART_1 = 4
BLOCK_SIZE_PART_2 = 14


def isUniqueChars(string):
    isUnique = False
    freq = Counter(string)
    if (len(freq) == len(string)):
        isUnique = True
    return isUnique

if __name__ == "__main__":
    file = open("input.txt", encoding='utf-8')
    lines = file.readlines()
    file.close()

    line = lines[0]
    for i in range(0, len(line), 1):
        if isUniqueChars(line[i:i+BLOCK_SIZE_PART_1]):
            print(i+BLOCK_SIZE_PART_1)
            break

    for i in range(0, len(line), 1):
        if isUniqueChars(line[i:i+BLOCK_SIZE_PART_2]):
            print(i+BLOCK_SIZE_PART_2)
            break