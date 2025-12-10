#https://adventofcode.com/2025/day/5#part2
#with open('Day5\\Resources\\Sample.csv', 'r') as file:
with open('Day5\\Resources\\Input.csv', 'r') as file:
    data = [line.strip() for line in file.readlines()]

def count_unique_fresh_ids(data):
    ranges = []
    
    for row in data:
        if "-" in row:
            start, end = map(int, row.split("-"))
            ranges.append((start, end))
    
    if not ranges:
        return 0
    
    ranges.sort()
    merged = [ranges[0]]
    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    
    total = sum(end - start + 1 for start, end in merged)
    return total

total_fresh = count_unique_fresh_ids(data)
print(f"Total unique fresh ingredient IDs: {total_fresh}")