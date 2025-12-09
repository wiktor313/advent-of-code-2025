#https://adventofcode.com/2025/day/2#part1
import csv

invalid_ids = []
#data = csv.reader(open('Day2\\Resources\\Sample.csv', 'r'))
data = csv.reader(open('Day2\\Resources\\Input.csv', 'r'))
def check_id(id):
    global invalid_ids
    parts = id[0].split('-')
    start = int(parts[0])
    end = int(parts[1])
    for number in range(start, end+1):
        str_number = str(number)
        length = len(str_number)
        if length % 2 == 0:
            half = length // 2
            first_half = str_number[:half]
            second_half = str_number[half:]
            if first_half == second_half and first_half[0] != '0':
                invalid_ids.append(number)

for row in data:
    for id_range in row:
        if id_range.strip():
            check_id([id_range])
print(f"Sum of Invalid IDs: {sum(invalid_ids)}")