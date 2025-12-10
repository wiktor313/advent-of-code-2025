#https://adventofcode.com/2025/day/6#part2

# with open('Day6\\Resources\\Sample.csv', 'r') as file:
#     lines = [line.strip() for line in file.readlines()]
with open('Day6\\Resources\\Input.csv', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

numbers = []
for line in lines[:-1]:
    row = [int(x) for x in line.split()]
    numbers.append(row)


operators = lines[-1].split()

def calculate(numbers, operators):
    final_result = []
    row_count = len(numbers)
    
    for col in range(len(operators)):
        result = numbers[0][col]
        
        for row in range(1, row_count):
            match operators[col]:
                case '+':
                    result += numbers[row][col]
                case '-':
                    result -= numbers[row][col]
                case '*':
                    result *= numbers[row][col]
                case '/':
                    if numbers[row][col] != 0:
                        result /= numbers[row][col]
        
        final_result.append(result)
    
    return sum(final_result)


final_result = calculate(numbers, operators)
print(f"Final result after operations: {final_result}")