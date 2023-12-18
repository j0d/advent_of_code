path = '10/test_input.txt'
path = '10/test_input2.txt'
path = '10/input.txt'

steps = []
current_x = 0
current_y = 0
last_step = ''

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

def take_next_step(steps, step_count):
    global current_x, current_y
    # if steps[step_count][0] - steps[step_count-1][0] == 1: #down
    #     print("down")
    #     last_step = 'D'
    # if steps[step_count][0] - steps[step_count-1][0] == -1: #up
    #     print("up")
    #     last_step = 'U'
    # if steps[step_count][1] - steps[step_count-1][1] == 1: #right
    #     print("right")
    #     last_step = 'R'
    # if steps[step_count][1] - steps[step_count-1][1] == -1: #left
    #     print("left")
    #     last_step = 'L'
    
    #last_step = steps[step_count][2]
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
            #steps.append([1,2,'-'])
            break
    print(line)
#print(lines[0][0])
print(f"path: {steps}")
print(f"starting point: {steps[0]}")
print(f"next point: {steps[0]}")
print(f"next point symbol: {steps[0][2]}")


step_count = 0
first = True
print(steps[0])
print(f"current coordinates: y:{current_y},x:{current_x}")
step_count = find_first_step(lines, step_count)
#take first step




print(steps)
print(step_count)
print(f"current coordinates: y:{current_y},x:{current_x}")

#find_next_step(lines, steps, step_count)



while steps[step_count][2] != 'S' or first:
    first = False
    #print(steps)
    print(f"step_count: {step_count}")
    print(f"current coordinates: y:{current_y},x:{current_x}")

    step_count = take_next_step(steps, step_count)


print(f"furtest point: {step_count/2}")
    


#     next_step = find_next_step(lines, steps)
#     steps.append(next_step)
    