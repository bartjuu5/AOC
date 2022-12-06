if __name__ == "__main__":
    # part 1 + 2
    file = open("input.txt", encoding='utf-8')
    totalCalories = []
    calories = 0
    for line in file.readlines():
        try:
            calories += int(line)
        except:
            totalCalories.append(calories)
            calories = 0
    totalCalories.sort()
    print(totalCalories[-1])
    print(totalCalories[-1] + totalCalories[-2] + totalCalories[-3])