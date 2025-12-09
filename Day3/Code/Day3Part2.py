#https://adventofcode.com/2025/day/3#part2
#with open('Day3\\Resources\\Sample.csv', 'r') as file:
#    data = file.readlines()
with open('Day3\\Resources\\Input.csv', 'r') as file:
    data = file.readlines()

def find_larges_joltage(joltage):
    numbers = [int(char) for char in joltage.strip() if char.isdigit()]
    n = len(numbers)
    target = 12
    
    result = []
    start = 0
    
    for i in range(target):
        remaining = target - i - 1
        max_digit = -1
        max_pos = -1
        
        for j in range(start, n - remaining):
            if numbers[j] > max_digit:
                max_digit = numbers[j]
                max_pos = j
        
        result.append(max_digit)
        start = max_pos + 1
    
    max_joltage = int(''.join(map(str, result)))
    return max_joltage

sum_of_largest = 0
for row in data:
    sum_of_largest += (find_larges_joltage(row))

print(f"Largest Joltage Sum: {sum_of_largest}")