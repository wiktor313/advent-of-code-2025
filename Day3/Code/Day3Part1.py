#https://adventofcode.com/2025/day/3#part1
#with open('Day3\\Resources\\Sample.csv', 'r') as file:
#    data = file.readlines()
with open('Day3\\Resources\\Input.csv', 'r') as file:
    data = file.readlines()

def find_larges_joltage(joltage):
    numbers = [int(char) for char in joltage.strip() if char.isdigit()]

    max_joltage = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            joltage_value = int(str(numbers[i]) + str(numbers[j]))
            if joltage_value > max_joltage:
                max_joltage = joltage_value
    return max_joltage

sum_of_largest = 0
for row in data:
    sum_of_largest += (find_larges_joltage(row))

print(f"Largest Joltage Sum: {sum_of_largest}")