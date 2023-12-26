path = '15/test_input.txt'
path = '15/input.txt'



def calc_hash_value(line)->int:
    current_value = 0
    for char in line:
        #print(char)
        #print(ord(char))
        current_value += ord(char)
        current_value = current_value*17 
        #print(current_value)
        current_value = current_value % 256        
    return current_value
 
def add_to_box(chars, box_index, focal_length):
    global boxes
    replaced = False
    if len(boxes[box_index]) == 0:
        boxes[box_index].append(chars + ' ' + str(focal_length))
    else:
        for i in range(len(boxes[box_index])):
            print(f"box[{i}]: {boxes[box_index][i]}")
            if boxes[box_index][i].startswith(chars):
                boxes[box_index][i] = (chars + ' ' + str(focal_length))
                replaced = True
        if not replaced:
            boxes[box_index].append(chars + ' ' + str(focal_length))
    return

def remove_from_box(chars, box_index):
    global boxes
    box = boxes[box_index]
    i=0
    print(f"items in box: {box}, number of items: {len(box)}")
    for i in range(len(box)):
        if box[i].startswith(chars):
            boxes[box_index].pop(i)
            return
    return

def calc_box_focal_value(box)->int:
    focal_value = 0
    i = 0
    for i in range(len(box)):
        focal_value += (i+1) * int(box[i].split(' ')[1])
    return focal_value

def calc_focusing_power()->int:
    i=0
    total_focal_value = 0
    for i in range(len(boxes)):
        box = boxes[i]
        total_focal_value += (i+1) * calc_box_focal_value(box)
    return total_focal_value

#### MAIN ####
total_sum = 0

# create a list with 256 items
boxes = [[] for _ in range(256)]
print(len(boxes))

print("Input:")
with open(path, 'r') as file:
    lines = [line for line in file if line.strip()]
    print(f"lines before strip: {lines}")
    lines = lines[0].split(',')
    
    
    
    for line in lines:
        focal_length = 0
        print(line)
        try:
            pos = line.index('-')
            action = '-'
        except ValueError:
            pos = line.find('=')
            action = '='
            focal_length = int(line[pos+1:])
        chars = line[:pos]
        print(chars)
        print(f"action: {action}")
        print(f"focal_length: {focal_length}")


        box_index = calc_hash_value(chars)
        print(f"box to alter: {box_index} with action {action} and boxlength {len(boxes[box_index])}")   
        if action == '-':
            #remove from box if label present
            remove_from_box(chars, box_index)
        elif action == '=':
            add_to_box(chars, box_index, focal_length)

        print(f"boxes: {boxes}")


focusing_power = calc_focusing_power()
            
            
print(focusing_power)