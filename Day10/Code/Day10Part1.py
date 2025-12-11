# https://adventofcode.com/2025/day/10#part1

#with open('Day10\\Resources\\Sample.csv', 'r') as file:
with open('Day10\\Resources\\Input.csv', 'r') as file:
    target_states = []
    all_buttons = []
    
    for line in file:
        target_str = line.strip().split('[')[1].split(']')[0]
        target = [c == '#' for c in target_str]
        target_states.append(target)
        
        button_str = line.split(']', 1)[1].split('{', 1)[0].strip()
        buttons = []
        for part in button_str.split('(')[1:]:
            numbers_str = part.split(')')[0]
            numbers = [int(x) for x in numbers_str.split(',')]
            buttons.append(numbers)
        all_buttons.append(buttons)

def find_solution(target, buttons):
    n = len(buttons)
    min_presses = float('inf')
    best_solution = None
    
    for mask in range(1 << n):
        state = [False] * len(target)
        
        for i in range(n):
            if mask & (1 << i):
                for pos in buttons[i]:
                    state[pos] = not state[pos]
        
        if state == target:
            pressed = [i for i in range(n) if mask & (1 << i)]
            if len(pressed) < min_presses:
                min_presses = len(pressed)
                best_solution = pressed
    
    return best_solution

answer = 0
for idx, (target, buttons) in enumerate(zip(target_states, all_buttons)):
    solution = find_solution(target, buttons)
    if solution:
        answer += len(solution)
    else:
        continue
print(f"Answer: {answer}")