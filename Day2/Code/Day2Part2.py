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
        is_invalid = False
        
        for pattern_length in range(1, length // 2 + 1):
            if length % pattern_length == 0:
                repetitions = length // pattern_length
                pattern = strnumber[:pattern_length]
                
                if pattern * repetitions == strnumber and pattern[0] != '0':
                    is_invalid = True
                    break
        
        if is_invalid:
            invalidIds.append(number)
        

for row in data:
    for id_range in row:
        if id_range.strip():
            check_id([id_range])
print(f"Sum of Invalid IDs: {sum(invalidIds)}")