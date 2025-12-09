#https://adventofcode.com/2025/day/1#part1
import csv

current_state = 50
iteration = 0
data = csv.reader(open('Day1\\Resources\\Input.csv', 'r'))
#data = csv.reader(open('Day1\\Resources\\Sample.csv', 'r'))

def change_values(state, value):
    global iteration
    if value[0] == 'R':
        state = (state + int(value[1:])) % 100
    elif value[0] == 'L':
        state = (state - int(value[1:])) % 100
    
    if state == 0:
        iteration += 1
    
    return state

for value in data:
    current_state = change_values(current_state, value[0])
print(f"Final State: {current_state}, Iterations: {iteration}")