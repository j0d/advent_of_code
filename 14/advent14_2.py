path = '14/test_input.txt'
path = '14/input.txt'

def transpose_strings(lines) -> list:
    transposed_lines =  [''.join(line) for line in zip(*lines)]
    return transposed_lines

def swap_chars(s, index1, index2):
    if index1 < 0 or index1 >= len(s) or index2 < 0 or index2 >= len(s):
        raise ValueError("Index out of range")

    # Ensure index1 is the smaller index
    if index1 > index2:
        index1, index2 = index2, index1

    # Swap characters
    if index1 == index2:
        return s
    else:
        return s[:index1] + s[index2] + s[index1 + 1:index2] + s[index1] + s[index2 + 1:]


def drop_stones_left(line)->str:
    latest_stop = 0
    for i in range(len(line)):
        if line[i] == '#':
            latest_stop = i+1
            #print(f"last stop at {latest_stop}")
        elif line[i] == 'O':
            if i == latest_stop:
                #print(f"skipping i == latest stop {i}")
                latest_stop += 1
                continue
            elif i > (latest_stop):
                line = swap_chars(line, i, latest_stop)
                #print(f"dropped stone at {i} to {latest_stop}")
                latest_stop += 1
                #print(f"last stop at {latest_stop}")
                #print(line)
            else:
                latest_stop = i
                #print(f"last stop at {latest_stop}")
        else: #line[i] == '.':
            continue
    return line 

def calc_score(lines)->int:
    total_score = 0
    score = 0
    line_score = len(lines)
    for line in lines:
        score = 0   
        for char in line:
            if char == 'O':
                score += 1
        total_score += line_score * score
        line_score -= 1
    return total_score


#### MAIN ####


print("Input:")
with open(path, 'r') as file:
    lines = [line for line in file if line.strip()]
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
          
for line in lines:
    print(line)


i= 1
for i in range(1000):
   
    lines = transpose_strings(lines)

    new_lines = []


    for line in lines:
        new_dropped_line = drop_stones_left(line)
        #print(f" dropped line: {new_dropped_line}")
        new_lines.append(new_dropped_line)
    lines = transpose_strings(new_lines)
    #tilted north.

    print("dropped north:")
    for line in lines:
        print(line)

    new_lines = []
    #tilted left = west
    for line in lines:
        new_dropped_line = drop_stones_left(line)
        #print(f" dropped line: {new_dropped_line}")
        new_lines.append(new_dropped_line)
    lines = new_lines

    print("tilted west:")
    for line in lines:
        print(line)

    #dropping south transpose and send in reverse.
    lines = transpose_strings(lines)
    new_lines = []

    for line in lines:
        new_dropped_line = drop_stones_left(line[::-1])
        #print(f" dropped line: {new_dropped_line}")
        new_lines.append(new_dropped_line[::-1])
    lines = transpose_strings(new_lines)
    #tilted south


    print("tilted  south:")
    for line in lines:
        print(line)

    new_lines = []
    #tilted east
    for line in lines:
        new_dropped_line = drop_stones_left(line[::-1])
        #print(f" dropped line: {new_dropped_line}")
        new_lines.append(new_dropped_line[::-1])
    lines = new_lines

    print("tilted  east:")
    for line in lines:
        print(line)

    print(f"score = {calc_score(lines)}")

