# https://adventofcode.com/2025/day/12#part1

#with open('Day12\\Resources\\Sample.csv', 'r') as file:
with open('Day12\\Resources\\Input.csv', 'r') as file:
    lines = [line.strip() for line in file]
shapes = {}
i = 0
while i < len(lines):
    if ':' in lines[i] and not 'x' in lines[i]:
        shape_idx = int(lines[i].rstrip(':'))
        shape_lines = []
        i += 1
        while i < len(lines) and lines[i] and ':' not in lines[i]:
            shape_lines.append(lines[i])
            i += 1
        shapes[shape_idx] = shape_lines
    else:
        i += 1

regions = []
for line in lines:
    if 'x' in line and ':' in line:
        parts = line.split(': ')
        dims = parts[0].split('x')
        width, height = int(dims[0]), int(dims[1])
        counts = list(map(int, parts[1].split()))
        regions.append((width, height, counts))

def parse_shape(shape_lines):
    coords = []
    for r, line in enumerate(shape_lines):
        for c, char in enumerate(line):
            if char == '#':
                coords.append((r, c))
    return coords

def normalize_shape(coords):
    if not coords:
        return []
    min_r = min(r for r, c in coords)
    min_c = min(c for r, c in coords)
    return sorted([(r - min_r, c - min_c) for r, c in coords])

def rotate_90(coords):
    return normalize_shape([(c, -r) for r, c in coords])

def flip_horizontal(coords):
    return normalize_shape([(r, -c) for r, c in coords])

def get_all_orientations(shape_lines):
    coords = parse_shape(shape_lines)
    orientations = set()
    
    current = normalize_shape(coords)
    for _ in range(4):
        orientations.add(tuple(current))
        current = rotate_90(current)
    
    current = flip_horizontal(normalize_shape(coords))
    for _ in range(4):
        orientations.add(tuple(current))
        current = rotate_90(current)
    
    return [list(orient) for orient in orientations]

def can_place(grid, shape, row, col, width, height):
    for dr, dc in shape:
        r, c = row + dr, col + dc
        if r < 0 or r >= height or c < 0 or c >= width:
            return False
        if grid[r][c] != '.':
            return False
    return True

def place_shape(grid, shape, row, col, marker):
    for dr, dc in shape:
        r, c = row + dr, col + dc
        grid[r][c] = marker

def remove_shape(grid, shape, row, col):
    for dr, dc in shape:
        r, c = row + dr, col + dc
        grid[r][c] = '.'

def solve_region(width, height, present_list, shapes):
    grid = [['.' for _ in range(width)] for _ in range(height)]
    
    presents_to_place = []
    for shape_idx, count in enumerate(present_list):
        for _ in range(count):
            presents_to_place.append(shape_idx)
    
    if not presents_to_place:
        return True
    
    total_shape_area = sum(len(parse_shape(shapes[shape_idx])) for shape_idx in presents_to_place)
    if total_shape_area > width * height:
        return False
    
    all_orientations = {}
    shape_sizes = {}
    for shape_idx in set(presents_to_place):
        all_orientations[shape_idx] = get_all_orientations(shapes[shape_idx])
        shape_sizes[shape_idx] = len(parse_shape(shapes[shape_idx]))
    
    presents_to_place.sort(key=lambda x: shape_sizes[x], reverse=True)
    
    call_count = [0]
    max_calls = 10000000
    
    def backtrack(present_idx):
        call_count[0] += 1
        if call_count[0] > max_calls:
            return False
            
        if present_idx == len(presents_to_place):
            return True
        
        shape_idx = presents_to_place[present_idx]
        
        for orientation in all_orientations[shape_idx]:
            for r in range(height):
                for c in range(width):
                    if can_place(grid, orientation, r, c, width, height):
                        place_shape(grid, orientation, r, c, chr(65 + present_idx % 26))
                        if backtrack(present_idx + 1):
                            return True
                        remove_shape(grid, orientation, r, c)
        
        return False
    
    return backtrack(0)

answer = 0
for width, height, counts in regions:
    if solve_region(width, height, counts, shapes):
        answer += 1

print(f"Answer: {answer}")