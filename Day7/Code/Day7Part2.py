#https://adventofcode.com/2025/day/7#part2

#with open('Day7\\Resources\\Sample.csv', 'r') as file:
with open('Day7\\Resources\\Input.csv', 'r') as file:
    lines = [list(line.strip()) for line in file.readlines()]


def find_start_position(lines):
    """Znajduje pozycję S."""
    for row_idx, row in enumerate(lines):
        if "S" in row:
            col_idx = row.index("S")
            return row_idx, col_idx
    return None, None


def count_timelines(lines):
    """Liczy wszystkie możliwe timeline'y (unikalne ścieżki przez manifold)."""
    start_row, start_col = find_start_position(lines)
    
    if start_row is None:
        return 0
    
    # Słownik: (row, col) -> liczba timeline'ów które dotarły do tej pozycji
    current_positions = {(start_row, start_col): 1}
    final_positions = {}
    
    while current_positions:
        next_positions = {}
        
        for (row, col), count in current_positions.items():
            # Sprawdź czy cząstka może spaść dalej
            next_row = row + 1
            
            # Jeśli jesteśmy w ostatnim wierszu lub poza siatką
            if next_row >= len(lines) or col >= len(lines[next_row]):
                final_positions[(row, col)] = final_positions.get((row, col), 0) + count
                continue
            
            next_char = lines[next_row][col]
            
            if next_char == '^':
                # Splitter - każdy timeline rozdziela się na dwa
                if col - 1 >= 0:
                    left_pos = (next_row, col - 1)
                    next_positions[left_pos] = next_positions.get(left_pos, 0) + count
                
                if col + 1 < len(lines[next_row]):
                    right_pos = (next_row, col + 1)
                    next_positions[right_pos] = next_positions.get(right_pos, 0) + count
            else:
                # Pusta przestrzeń - cząstka spada w dół
                down_pos = (next_row, col)
                next_positions[down_pos] = next_positions.get(down_pos, 0) + count
        
        current_positions = next_positions
    
    # Suma wszystkich timeline'ów które dotarły do końca
    return sum(final_positions.values())


final_result = count_timelines(lines)
print(f"Final result: {final_result}")