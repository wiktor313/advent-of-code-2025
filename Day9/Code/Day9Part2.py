# https://adventofcode.com/2025/day/9#part1

#with open('Day9\\Resources\\Sample.csv', 'r') as file:
with open('Day9\\Resources\\Input.csv', 'r') as file:
    coordinates = []
    for line in file:
        x, y = map(int, line.strip().split(','))
        coordinates.append((x, y))

edges = []
for i in range(len(coordinates)):
    p1 = coordinates[i]
    p2 = coordinates[(i + 1) % len(coordinates)]
    edges.append((p1, p2))

def is_valid_rectangle(rx1, ry1, rx2, ry2):
    for (ex1, ey1), (ex2, ey2) in edges:
        if ex1 == ex2:
            if rx1 < ex1 < rx2:
                edge_y_min, edge_y_max = min(ey1, ey2), max(ey1, ey2)
                overlap_start = max(edge_y_min, ry1)
                overlap_end = min(edge_y_max, ry2)
                if overlap_start < overlap_end:
                    return False
        
        elif ey1 == ey2:
            if ry1 < ey1 < ry2:
                edge_x_min, edge_x_max = min(ex1, ex2), max(ex1, ex2)
                overlap_start = max(edge_x_min, rx1)
                overlap_end = min(edge_x_max, rx2)
                if overlap_start < overlap_end:
                    return False
    
    mid_x = (rx1 + rx2) / 2.0
    mid_y = (ry1 + ry2) / 2.0
    inside = False
    
    for (ex1, ey1), (ex2, ey2) in edges:
        if (ey1 > mid_y) != (ey2 > mid_y):
            intersect_x = (ex2 - ex1) * (mid_y - ey1) / (ey2 - ey1) + ex1
            if mid_x < intersect_x:
                inside = not inside
    
    return inside

pairs_with_area = []
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        p1, p2 = coordinates[i], coordinates[j]
        
        width = abs(p1[0] - p2[0]) + 1
        height = abs(p1[1] - p2[1]) + 1
        area = width * height
        
        pairs_with_area.append((area, p1, p2))

pairs_with_area.sort(reverse=True)

max_area = 0
best_pair = None

for area, p1, p2 in pairs_with_area:
    if area <= max_area:
        break
    
    rx1, rx2 = min(p1[0], p2[0]), max(p1[0], p2[0])
    ry1, ry2 = min(p1[1], p2[1]), max(p1[1], p2[1])
    
    if is_valid_rectangle(rx1, ry1, rx2, ry2):
        max_area = area
        best_pair = (p1, p2)
        break

print(f'Biggest area: {max_area}')
print(f'Best pair: {best_pair[0]} and {best_pair[1]}')