import sys

sys.setrecursionlimit(5000)

with open('Day11\\Resources\\Input.csv', 'r') as file:
    devices = {}
    for line in file:
        line = line.strip()
        if ': ' in line:
            key, rest = line.split(': ')
            devices[key] = rest.split()
        elif line:
            key = line.split(':')[0]
            devices[key] = []

memo = {}

def count_path(current, target, devices):
    if current == target:
        return 1
    
    if (current, target) in memo:
        return memo[(current, target)]
    
    total_paths = 0
    for neighbor in devices.get(current, []):
        total_paths += count_path(neighbor, target, devices)
    
    memo[(current, target)] = total_paths
    return total_paths

path1 = (count_path('svr', 'dac', devices) * count_path('dac', 'fft', devices) * count_path('fft', 'out', devices))

path2 = (count_path('svr', 'fft', devices) * count_path('fft', 'dac', devices) * count_path('dac', 'out', devices))

answer = path1 + path2
print(f"Answer: {answer}")