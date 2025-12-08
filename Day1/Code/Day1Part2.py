import csv

current_state = 50
iteration = 0
data = csv.reader(open('Day1\\Resources\\day1Input.csv', 'r'))
#data = csv.reader(open('Day1\\Resources\\day1Sample.csv', 'r'))

def change_values(state, value):
    global iteration
    distance = int(value[1:])
    
    if value[0] == 'R':
        # Ruch w prawo
        for _ in range(distance):
            state = (state + 1) % 100
            if state == 0:
                iteration += 1
    elif value[0] == 'L':
        # Ruch w lewo
        for _ in range(distance):
            state = (state - 1) % 100
            if state == 0:
                iteration += 1
    
    return state

for value in data:
    current_state = change_values(current_state, value[0])
print(f"Final State: {current_state}, Iterations: {iteration}")