#https://adventofcode.com/2025/day/2#part2
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
        is_invalid = False
        
        for pattern_length in range(1, length // 2 + 1):
            if length % pattern_length == 0:
                repetitions = length // pattern_length
                pattern = str_number[:pattern_length]
                
                if pattern * repetitions == str_number and pattern[0] != '0':
                    is_invalid = True
                    break
        
        if is_invalid:
            invalid_ids.append(number)
        

for row in data:
    for id_range in row:
        if id_range.strip():
            check_id([id_range])
print(f"Sum of Invalid IDs: {sum(invalid_ids)}")