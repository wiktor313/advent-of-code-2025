#https://adventofcode.com/2025/day/2#part1
import csv

invalidIds = []
#data = csv.reader(open('Day2\\Resources\\Sample.csv', 'r'))
data = csv.reader(open('Day2\\Resources\\Input.csv', 'r'))
def check_id(id):
    global invalidIds
    parts = id[0].split('-')
    start = int(parts[0])
    end = int(parts[1])
    for number in range(start, end+1):
        strnumber = str(number)
        length = len(strnumber)
        if length % 2 == 0:
            half = length // 2
            first_half = strnumber[:half]
            second_half = strnumber[half:]
            if first_half == second_half and first_half[0] != '0':
                invalidIds.append(number)

for row in data:
    for id_range in row:
        if id_range.strip():
            check_id([id_range])
print(f"Sum of Invalid IDs: {sum(invalidIds)}")