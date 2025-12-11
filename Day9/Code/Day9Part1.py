# https://adventofcode.com/2025/day/9#part1

#with open('Day9\\Resources\\Sample.csv', 'r') as file:
with open('Day9\\Resources\\Input.csv', 'r') as file:
    coordinates = []
    for line in file:
        x, y = map(int, line.strip().split(','))
        coordinates.append((x, y))

max_area = 0
best_pair = None

for i in range(len(coordinates)-1):
    for j in range(i+1, len(coordinates)):
        p1, p2 = coordinates[i], coordinates[j]
        
        width = abs(p2[0] - p1[0]) + 1
        height = abs(p2[1] - p1[1]) + 1
        
        area = width * height
        
        if area > max_area:
            max_area = area
            best_pair = (p1, p2)

print(f'Biggest area: {max_area}')
print(f'Best pair: {best_pair[0]} and {best_pair[1]}')
