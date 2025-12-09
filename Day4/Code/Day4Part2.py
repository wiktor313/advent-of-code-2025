#https://adventofcode.com/2025/day/4#part2
#with open('Day4\\Resources\\Sample.csv', 'r') as file:
#    data = [list(line.strip()) for line in file.readlines()]  # list() zamienia string na listę
with open('Day4\\Resources\\Input.csv', 'r') as file:
    data = [list(line.strip()) for line in file.readlines()]

def check_access(data, row, col):
    rows = len(data)
    cols = len(data[0]) if rows > 0 else 0
    number_of_rolls = 0
    
    for r in range(-1, 2):
        for n in range(-1, 2):
            if r == 0 and n == 0:
                continue
            
            new_row = row + r
            new_col = col + n
            
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if data[new_row][new_col] == '@':
                    number_of_rolls += 1
    
    return number_of_rolls

total_accessible_rolls = 0

while True:
    accessible_in_round = []
    
    for row_idx in range(len(data)):
        for col_idx in range(len(data[row_idx])):
            if data[row_idx][col_idx] == '@':
                neighbor_count = check_access(data, row_idx, col_idx)
                if neighbor_count < 4:
                    accessible_in_round.append((row_idx, col_idx))

    if len(accessible_in_round) == 0:
        break

    for row_idx, col_idx in accessible_in_round:
        data[row_idx][col_idx] = '.'
        total_accessible_rolls += 1

print(f"\nTotal accessible rolls removed: {total_accessible_rolls}")

