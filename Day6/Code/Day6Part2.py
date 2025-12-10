#https://adventofcode.com/2025/day/6#part2

#with open('Day6\\Resources\\Sample.csv', 'r') as file:
with open('Day6\\Resources\\Input.csv', 'r') as file:
    lines = [line for line in file.readlines()]

number_rows = [line.rstrip('\r\n') for line in lines[:-1]]
operators_line = lines[-1].rstrip('\r\n')


max_len = max(len(row) for row in number_rows + [operators_line])
number_rows = [row.ljust(max_len) for row in number_rows]
operators_line = operators_line.ljust(max_len)

operators = [(i, op) for i, op in enumerate(operators_line) if op in ['+', '-', '*', '/']]


def parse_problems(number_rows, operators, max_len):
    """Parse cephalopod math problems by reading columns right-to-left."""
    problems = []
    
    for i in range(len(operators) - 1, -1, -1):
        op_col, operator = operators[i]
        start_col = op_col
        end_col = operators[i + 1][0] - 1 if i < len(operators) - 1 else max_len - 1
        
        problem_numbers = []
        for col in range(end_col, start_col - 1, -1):
            column_chars = [number_rows[r][col] for r in range(len(number_rows))]
            if all(c == ' ' for c in column_chars):
                continue
            
            digits = []
            for row_idx in range(len(number_rows)):
                char = number_rows[row_idx][col]
                if char.isdigit():
                    digits.append(char)
            
            if digits:
                problem_numbers.append(int(''.join(digits)))
        
        if problem_numbers:
            problems.append((problem_numbers, operator))
    
    return problems


def calculate(problems):
    results = []
    
    for numbers, operator in problems:
        if len(numbers) == 0:
            continue
            
        result = numbers[0]
        for i in range(1, len(numbers)):
            match operator:
                case '+':
                    result += numbers[i]
                case '-':
                    result -= numbers[i]
                case '*':
                    result *= numbers[i]
                case '/':
                    if numbers[i] != 0:
                        result /= numbers[i]
        
        results.append(result)
    
    return sum(results)


problems = parse_problems(number_rows, operators, max_len)
final_result = calculate(problems)
print(f"Final result after operations: {final_result}")