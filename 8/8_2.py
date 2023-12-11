import pandas as pd
import numpy as np

path = '8/test_input.txt'
path = '8/input.txt'
#path = '8/test_input2.txt'
start = []
left = []
right = []


def follow_intruction(start, instruction):
    return df.loc[df['start'] == start, instruction].iloc[0]


def find_next_dest(next_start, steps, instruction, inst_index):
    first = True
    while not next_start.endswith('Z')or first:
        first = False
        #print(inst_index)
        #print(instruction[inst_index])
        #print(next_start)
        next_start = df.loc[df['start'] == next_start, instruction[inst_index]].iloc[0]
        steps += 1
        #increase index 1 mod len(instruction)
        inst_index = (inst_index +1) % inst_len
    return next_start, steps, inst_index

with open(path, 'r') as file:
    lines = [line for line in file if line.strip()]
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
        print(lines[i])
        print(i)
        if i > 0:
            lines[i] = lines[i].replace(' ', '').replace('=', ',').replace('(', '').replace(')', '').split(',')       
        # 
        #     start[i] = line.split('=')[0]
        #     left[i] = line.split('=')[1].split(',')[0]
        #     right[i] = line.split('=')[1].split(',')[1]
        print(lines[i])        

instruction = lines[0][:]
print(instruction)
#print(lines[1:])

#insert lines into a df with columns: start, left, right
df = pd.DataFrame(lines[1:],columns=['start', 'L', 'R'])

#print(df)

inst_index = 0
inst_len = len(instruction)
print(F"inst_len: {inst_len}")
#set next start to all starts in the df that end on an A
next_start = df['start'][df['start'].str.endswith('A')].tolist()
possible_ends = df['start'][df['start'].str.endswith('Z')].tolist()
#list of 0s with length of next_start
start_steps =  [0] * len(next_start)
first_dests = [0] * len(next_start)
first_steps = [0] * len(next_start)
inst_indexes = [0] * len(next_start)
next_steps = [0] * len(next_start)
next_end = [0] * len(next_start)

print(f"next_start: {next_start}")
print(f"possible_ends: {possible_ends}")
print(f"start_steps: {start_steps}")
steps = 0






import math

# Example starting values and step values
start_values = first_steps  # Replace with your starting values
step_values = next_steps      # Replace with your step values

#mutiply each individual value with the length of the instruction
values = [start * inst_len for start in start_values]
print(f"values: {values}")

# Compute the new values
new_values = [start + step for start, step in zip(start_values, step_values)]
print(new_values)

# Find the LCM of the new values
lcm_value = math.lcm(*values)

print("LCM of the new values:", lcm_value)

steps = first_steps[0]+next_steps[0]*lcm_value
print(steps)




#final_steps = [21883, 19667, 14681, 16897, 13019, 11911]

#step_diff = next_steps[0] - next_steps[1]
#print(diff/step_diff)


i=0
if i == 1:
    for i in range(len(next_start)):
        #Find steps from each start to next end.
        (first_dests[i], first_steps[i], inst_indexes[i]) = find_next_dest(next_start[i], 0, instruction, inst_indexes[i])
        #fint the number of steps from each end to the next end.
        #print(f"start steps found: {first_steps[i]}")
        (next_end[i], next_steps[i], inst_indexes[i]) = find_next_dest(possible_ends[i], 0, instruction, inst_indexes[i])

        print(f"possible_starts: {next_start}")
        print(f"first_dests: {first_dests}")
        print(f"first_steps: {first_steps}") #the steps it takes to get from start to first end

        print(f"possible_ends: {possible_ends}")
        print(f"next_end: {next_end}")
        print(f"next_steps: {next_steps}") #which end does the starts lead to.
        print(f"inst_indexes: {inst_indexes}")  

#ask for user input
#input("Press Enter to continue...")

possible_starts = ['RMA', 'NXA', 'GDA', 'PLA', 'QLA', 'AAA']
first_dests = ['FQZ', 'BBZ', 'SGZ', 'MQZ', 'VHZ', 'ZZZ']
first_steps = [21883, 19667, 14681, 16897, 13019, 11911]

# DET BLIR SAMMA NUMMER EFTER VIDARE STEG (index var bara snurrigt)
# possible_ends = ['MQZ', 'ZZZ', 'SGZ', 'VHZ', 'FQZ', 'BBZ']
# next_end = ['MQZ', 'ZZZ', 'SGZ', 'VHZ', 'FQZ', 'BBZ']
# next_steps = [16897, 11911, 14681, 13019, 21883, 19667]

print(f"possible_starts: {possible_starts}")
print(f"first_dests: {first_dests}")
print(f"first_steps: {first_steps}") #the steps it takes to get from start to first end


lcm_value = math.lcm(*first_steps)

print("LCM of the new values:", lcm_value)
#answer 10151663816849

exit()
#print(f"final_steps: {final_steps}")

while len(set(final_steps)) != 1:
    i = final_steps.index(min(final_steps))
    final_steps[i] += next_steps_index[i]

    print(f"final_steps and len set of final steps: {final_steps}, {len(set(final_steps))}")
exit()

#start a timer to keep track of runtime



start_steps = first_steps.copy()

import time
start_time = time.time()
print(f"len(set(start_steps)): {len(set(start_steps))}")
first = True
take_another_step = True
#as long as start steps aren't all the same, keep going
print(f"while: {len(set(start_steps)) != 1 or first}")
while len(set(start_steps)) != 1 or first:
    #set i = the index of the lowest number in list inst_indexes
    i = start_steps.index(min(start_steps))
    take_another_step = True
    print(f"i: {i}")
    #user input
    #input("Press Enter to continue...")
    #Find first start that ends on a Z
    print(f"elapsed time: {time.time() - start_time}")
    while not next_start[i].endswith('Z') or take_another_step:
        take_another_step = False
        inst_index = inst_indexes[i]
        #print(inst_index)
        #print(instruction[inst_index])
        # print(next_start[i])
        next_start[i] = df.loc[df['start'] == next_start[i], instruction[inst_index]].iloc[0]    
        start_steps[i] += 1
        #increase index 1 mod len(instruction)
        inst_indexes[i] = (inst_index +1) % inst_len
        #print(F"inst_index: {inst_indexes[i]}")

#always multiples of instruction length
#Only 6 different values for start_steps and end steps.
#Calc length in steps of each of these. 
#Add initial steps to each of the ends. The find the lowest number of steps. which is the answer.

    print(f"next_start: {next_start}")
    print(f"possible_ends: {possible_ends}")
    print(f"start_steps: {start_steps}")
    print(f"inst_indexes: {inst_indexes}")  
    first = False

#user input
exit()
input("Press Enter to continue...")

# (next_start[i], start_steps[i], inst_indexes[i]) = find_next_dest(next_start[i], start_steps[i], instruction, inst_indexes[i])
# print(f"next_start: {next_start}")
# print(f"possible_ends: {possible_ends}")
# print(f"start_steps: {start_steps}")
# print(f"inst_indexes: {inst_indexes}")  

# exit()

while [s.endswith('z') for s in next_start]:
    for i in range(len(next_start)):
        next_start[i] = follow_intruction(next_start[i], instruction[inst_index])

    steps += 1
    #increase index 1 mod len(instruction)
    inst_index = (inst_index +1) % inst_len  


print(f"next_start: {next_start}")
print(steps)

exit()

### change to tranlate the first start until it ends on a Z. Then go on to the next. 


while next_start != 'ZZZ':
    print(inst_index)
    print(instruction[inst_index])
    print(next_start)
    next_start = df.loc[df['start'] == next_start, instruction[inst_index]].iloc[0]
        
    steps += 1
    #increase index 1 mod len(instruction)
    inst_index = (inst_index +1) % inst_len
    
print(steps)