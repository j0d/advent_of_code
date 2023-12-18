path = '10/test_input5.txt'
#path = '10/test_input2.txt'
path = '10/input.txt'

steps = []
circled_area = []
step_count = 0
side = ''
current_x = 0
current_y = 0
last_step = ''
turn = 'S'

def take_step(direction, step_count):
    global current_x, current_y, steps, last_step
    if direction == 'R':
        steps.append([current_y,current_x+1,lines[current_y][current_x+1],step_count+1])
    elif direction == 'L':
        steps.append([current_y,current_x-1,lines[current_y][current_x-1],step_count+1])
    elif direction == 'U':
        steps.append([current_y-1,current_x,lines[current_y-1][current_x],step_count+1])
    elif direction == 'D':
        steps.append([current_y+1,current_x,lines[current_y+1][current_x],step_count+1])
    last_step = direction
    
    current_y = steps[step_count+1][0]
    current_x = steps[step_count+1][1]
    


def find_first_step(lines, step_count): #start has two and can't be at edge
    global current_x, current_y, last_step
    if lines[current_y][current_x+1] in ['-','7','J']: #check if there is a path to the right
        print("path to the right")
        take_step('R',step_count)
        return step_count+1
    if lines[current_y][current_x-1] in ['-','F','L']: #check if there is a path to the left
        print("path to the left")
        take_step('L',step_count)
        return step_count+1
    if lines[current_y+1][current_x] in ['|','L','J']: #check if there is a path to the left
        print("path down")
        take_step('D',step_count)
        return step_count+1
    if lines[current_y-1][current_x] in ['|','F','7']: #check if there is a path to the left
        print("path up")
        take_step('U',step_count)
        return step_count+1

def add_last_step(steps):   
    for step in steps:
        if step[2] == 'S':
            if steps.index(step) == 0:
                step.append('S')
                continue
            elif steps.index(step) == len(steps)-1:
                steps[0][4] = steps[steps.index(step)-1][4]
        if step[0] - steps[steps.index(step)-1][0] == 1: #down
            step.append('D')
        elif step[0] - steps[steps.index(step)-1][0] == -1: #up
            step.append('U')
        elif step[1] - steps[steps.index(step)-1][1] == 1: #right
            step.append('R')
        elif step[1] - steps[steps.index(step)-1][1] == -1: #left
            step.append('L')
        else:
            print("error")
            break

def add_turns(steps):
    for step in steps:
        last_step = step[4]
        if step[2] == 'S':
            step.append('S')
            continue
        elif last_step == 'R':
            if step[2] == '-':
                step.append('S')
            elif step[2] == '7':
                step.append('R')
            elif step[2] == 'J':
                step.append('L')
            else:
                print("right error")
        elif last_step == 'L':
            if step[2] == '-':
                step.append('S')
            elif step[2] == 'F':
                step.append('L')
            elif step[2] == 'L':
                step.append('R')
            else:
                print("left error")
        elif last_step ==  'U':
            if step[2] == 'F':
                step.append('R')
            elif step[2] == '7':
                step.append('L')
            elif step[2] == '|':
                step.append('S')
            else:
                print("up error")
        elif last_step == 'D':
            if step[2] == 'L':
                step.append('L')
            elif step[2] == 'J':
                step.append('R')
            elif step[2] == '|':
                step.append('S')
            else:
                print("down error")
        else:
            print("error")





def take_next_step(steps, step_count):
    global current_x, current_y
    
    print(f"last step: {last_step}")
    
    if last_step == 'R':
        if steps[step_count][2] == '-':
            print("right")
            step = 'R'
        elif steps[step_count][2] == '7':
            print("down")
            step = 'D'
        elif steps[step_count][2] == 'J':
            print("up")
            step = 'U'
        else:
            print("right error")
    elif last_step == 'L':
        if steps[step_count][2] == '-':
            print("left")
            step = 'L'
        elif steps[step_count][2] == 'F':
            print("down")
            step = 'D'
        elif steps[step_count][2] == 'L':
            print("up")
            step = 'U'
        else:
            print("left error")
    elif last_step ==  'U':
        if steps[step_count][2] == 'F':
            print("right")
            step = 'R'
        elif steps[step_count][2] == '7':
            print("left")
            step = 'L'
        elif steps[step_count][2] == '|':
            print("up")
            step = 'U'
        else:
            print("up error")
    elif last_step == 'D':
        if steps[step_count][2] == 'L':
            print("right")
            step = 'R'
        elif steps[step_count][2] == 'J':
            print("left")
            step = 'L'
        elif steps[step_count][2] == '|':
            print("down")
            step = 'D'
        else:
            print("down error")
    else:
        print("error")

    take_step(step, step_count)
    return step_count+1

    
def not_on_path(y, x):
    #go through all steps and check if the current x and y are on the path
    for step in steps:
        if step[0] == y and step[1] == x:
            return False
    return True

def which_side(steps):
    l_turns = 0
    r_turns = 0
    for step in steps:
        if step[5] == 'L':
            l_turns += 1
        elif step[5] == 'R':
            r_turns += 1
    if l_turns > r_turns: 
            return 'L'
    elif r_turns > l_turns:
        return 'R'
    else:
        print("error")
        return 'error'
    
def check_for_circled_area(y, x):
    global circled_area
    if not_on_path(y, x):
        print(f"found a circled area at: {y}, {x} when looking from coodinates: y{step[0]} and x{step[1]}")
        circled_area.append((y,x))

def expand_circled_area(y, x):
    global circled_area
    if not_on_path(y, x) and not (y,x) in circled_area:
        print(f"found a circled area at: {y}, {x}")
        circled_area.append((y,x))
        expand_circled_area(y-1, x)
        expand_circled_area(y+1, x)
        expand_circled_area(y, x-1)
        expand_circled_area(y, x+1)
    else:
        return

#####################################################################
#####################################################################
# main

print("Input:")
with open(path, 'r') as file:
    lines = [line for line in file if line.strip()]
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')

#find starting point
for line in lines:
    for i in range(len(line)):
        if line[i] == 'S':
            current_y = lines.index(line)
            current_x = i
            steps.append([current_y,current_x,line[i],0])
            break
    print(line)


print(f"current coordinates: y:{current_y},x:{current_x}")
step_count = find_first_step(lines, step_count)
#take first step


first = True
while steps[step_count][2] != 'S' or first:
    first = False
    #print(steps)
    print(f"step_count: {step_count}")
    print(f"current coordinates: y:{current_y},x:{current_x}")

    step_count = take_next_step(steps, step_count)


print(f"furtest point: {step_count/2}")
#print(steps)
#start finding circled areas.


add_last_step(steps)
#print(steps)
add_turns(steps)
print(steps)

side = which_side(steps)
print(f"side: {side}")
if side == 'R':
    #print("side is R")
    look_for_circ = -1
elif side == 'L':
    #print("side is L")
    look_for_circ = 1
print(f"look for circ: {look_for_circ}")

for step in steps:
    if step[2] == 'S':
        continue
    #if tile to the "side" 
    if step[4] == 'R':
        eval_y = step[0]-look_for_circ
        eval_x = step[1]
        if (not_on_path(step[0]-look_for_circ, step[1])):
            print(f"found a circled area at: {step[0]-look_for_circ}, {step[1]} when looking from coodinates: y{step[0]} and x{step[1]}")
    if step[4] == 'L':
        if (not_on_path(step[0]+look_for_circ, step[1])):
            print(f"found a circled area at: {step[0]+look_for_circ}, {step[1]} when looking from coodinates: y{step[0]} and x{step[1]}")
    if step[4] == 'U':
        if (not_on_path(step[0], step[1]-look_for_circ)):
            print(f"found a circled area at: {step[0]}, {step[1]-look_for_circ} when looking from coodinates: y{step[0]} and x{step[1]}")
    if step[4] == 'D':
        if (not_on_path(step[0], step[1]+look_for_circ)):
            print(f"found a circled area at: {step[0]}, {step[1]+look_for_circ} when looking from coodinates: y{step[0]} and x{step[1]}")

print("\n\n\n")

######################
#code is finding evrerything correctly except when turning left or right. the only looking to the side before turning. Need to look after the turn also.    

#     next_step = find_next_step(lines, steps)
#     steps.append(next_step)
for step in steps:
    if step[2] == 'S':
        continue
    #if tile to the "side" 
    if step[4] == 'R':
        eval_y = step[0]-look_for_circ
        eval_x = step[1]
    if step[4] == 'L':
        eval_y = step[0]+look_for_circ
        eval_x = step[1]
    if step[4] == 'U':
        eval_y = step[0]
        eval_x = step[1]-look_for_circ
    if step[4] == 'D':
        eval_y = step[0]
        eval_x = step[1]+look_for_circ

    check_for_circled_area(eval_y, eval_x)

    #look also aftr turning
    if step[4] == 'R' and step[5] == 'R': #as look down
        eval_y = step[0]
        eval_x = step[1]+look_for_circ 
    elif step[4] == 'R' and step[5] == 'L': #as look up
        eval_y = step[0]
        eval_x = step[1]-look_for_circ
    elif step[4] == 'L' and step[5] == 'R': #as look up
        eval_y = step[0]
        eval_x = step[1]-look_for_circ
    elif step[4] == 'L' and step[5] == 'L': #as look down
        eval_y = step[0]
        eval_x = step[1]+look_for_circ 
    elif step[4] == 'U' and step[5] == 'R': #as look right
        eval_y = step[0]-look_for_circ
        eval_x = step[1]
    elif step[4] == 'U' and step[5] == 'L': #as look left
        eval_y = step[0]+look_for_circ
        eval_x = step[1]
    elif step[4] == 'D' and step[5] == 'R': #as look left
        eval_y = step[0]+look_for_circ
        eval_x = step[1]
    elif step[4] == 'D' and step[5] == 'L': #as look right
        eval_y = step[0]-look_for_circ
        eval_x = step[1]

    check_for_circled_area(eval_y, eval_x)

unique_coordinates = set(circled_area)
print(unique_coordinates)
print(len(unique_coordinates))

#Now add looking around from all found circled areas to see if it is larger area.

for coord in unique_coordinates:
    expand_circled_area(coord[0]+1, coord[1])
    expand_circled_area(coord[0]-1, coord[1])
    expand_circled_area(coord[0], coord[1]+1)
    expand_circled_area(coord[0], coord[1]-1)

unique_coordinates = set(circled_area)
print(unique_coordinates)
print(len(unique_coordinates))