# https://adventofcode.com/2025/day/7#part1

with open('Day7\\Resources\\Input.csv', 'r') as file:
    lines = [list(line.strip()) for line in file.readlines()]


def find_start_position(lines):
    for row_idx, row in enumerate(lines):
        if "S" in row:
            col_idx = row.index("S")
            return row_idx, col_idx
    return None, None


def simulate_beams(lines):
    split_count = 0
    start_row, start_col = find_start_position(lines)
    
    if start_row is None:
        return 0
    
    active_beams = [(start_row, start_col)]
    
    processed = set()
    
    while active_beams:
        new_beams = []
        
        for row, col in active_beams:
            
            if (row, col) in processed:
                continue
            processed.add((row, col))
            
            if row >= len(lines) - 1:
                continue
            
            next_row = row + 1
            
            if next_row < len(lines) and col < len(lines[next_row]):
                next_char = lines[next_row][col]
                
                if next_char == '^':
                    split_count += 1
                    
                    if col - 1 >= 0:
                        new_beams.append((next_row, col - 1))
                        
                    if col + 1 < len(lines[next_row]):
                        new_beams.append((next_row, col + 1))
                        
                else:
                    new_beams.append((next_row, col))
        
        active_beams = new_beams
    
    return split_count


final_result = simulate_beams(lines)
print(f"Final result: {final_result}")