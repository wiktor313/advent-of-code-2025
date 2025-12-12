# https://adventofcode.com/2025/day/11#part1

#with open('Day11\\Resources\\Sample.csv', 'r') as file:
with open('Day11\\Resources\\Input.csv', 'r') as file:
    devices = {}
    for line in file:
        key, rest = line.split(': ')
        values = rest.split()
        devices[key] = values

def count_path(current, target, devices, visited):
    if current == target:
        return 1
    if current in visited:
        return 0
    
    visited.add(current)
    total_paths = 0
    for neighbor in devices.get(current, []):
        total_paths += count_path(neighbor, target, devices, visited)
    visited.remove(current)
    
    return total_paths

answer = count_path('you', 'out', devices, set())
print(f"Answer: {answer}")