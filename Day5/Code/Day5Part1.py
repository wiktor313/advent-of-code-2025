#https://adventofcode.com/2025/day/5#part1
#with open('Day5\\Resources\\Sample.csv', 'r') as file:
with open('Day5\\Resources\\Input.csv', 'r') as file:
    data = [line.strip() for line in file.readlines()]
def check_fresh_ranges(data):
    fresh_ranges = []
    for row in data:
        if "-" in row:
            parts = row.split("-")
            fresh_ranges.append((int(parts[0]), int(parts[1])))
    return fresh_ranges
result = check_fresh_ranges(data)

def check_fresh(data, ranges):
    fresh_count = 0
    for row in data:
        if "-" not in row and row.strip():
            number = int(row)
            is_fresh = False 
            for range_start, range_end in ranges:
                if range_start <= number <= range_end:
                    is_fresh = True
                    break
            if is_fresh:
                fresh_count += 1
    return fresh_count

print(f"Number of fresh items: {check_fresh(data, result)}")