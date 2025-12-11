# https://adventofcode.com/2025/day/10#part2

from pulp import *

#with open('Day10\\Resources\\Sample.csv', 'r') as file:
with open('Day10\\Resources\\Input.csv', 'r') as file:
    targets = []
    all_buttons = []
    
    for line in file:
        button_str = line.split(']', 1)[1].split('{', 1)[0].strip()
        buttons = []
        for part in button_str.split('(')[1:]:
            numbers_str = part.split(')')[0]
            numbers = [int(x) for x in numbers_str.split(',')]
            buttons.append(numbers)
        all_buttons.append(buttons)
        
        target_str = line.split('{')[1].split('}')[0]
        target = [int(x) for x in target_str.split(',')]
        targets.append(target)

def find_min_presses(target, buttons):
    n_buttons = len(buttons)
    n_counters = len(target)
    
    prob = LpProblem("MinPresses", LpMinimize)
    
    x = [LpVariable(f"x{i}", lowBound=0, cat='Integer') for i in range(n_buttons)]
    
    prob += lpSum(x)
    
    for counter in range(n_counters):

        affecting_buttons = [i for i in range(n_buttons) if counter in buttons[i]]
        if affecting_buttons:
            prob += lpSum([x[i] for i in affecting_buttons]) == target[counter]
        else:
            if target[counter] != 0:
                return -1
    
    prob.solve(PULP_CBC_CMD(msg=0))
    
    if prob.status == 1:
        return int(value(prob.objective))
    else:
        return -1

answer = 0
total_rows = len(targets)
for idx, (target, buttons) in enumerate(zip(targets, all_buttons)):
    progress = (idx + 1) / total_rows * 100
    if (idx + 1) % max(1, total_rows // 10) == 0 or idx == 0:
        print(f"Progress: {progress:.0f}% (Row {idx + 1}/{total_rows})")
    
    min_presses = find_min_presses(target, buttons)
    if min_presses != -1:
        answer += min_presses

print(f"Answer: {answer}")