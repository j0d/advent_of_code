path = '9/test_input.txt'
path = '9/input.txt'

predict_pyramid = []

def print_pyramid(pyramid):
    for line in pyramid:
        print(line)

def get_prediction(line) -> int:
    global predict_pyramid
    predict_pyramid.append(line)
    next_line = []
    if sum(line) == 0:
        return 0
    for i in range(len(line)-1):
        diff = line[i+1]-line[i]
        next_line.append(diff)
        
    line_below = get_prediction(next_line)
    next_num = line[-1] + line_below
    print(f"Next num\t:{next_num} = {line[-1]} + {line_below}")
    return next_num

def get_prediction_both_directions(line) -> (int, int):
    global predict_pyramid
    predict_pyramid.append(line)
    next_line = []
    if sum(line) == 0:
        return 0, 0
    for i in range(len(line)-1):
        diff = line[i+1]-line[i]
        next_line.append(diff)
        
    line_below_l, line_below_r = get_prediction_both_directions(next_line)
    next_num_r = line[-1] + line_below_r
    next_num_l = line[0] - line_below_l
    print(f"Next num_r\t:{next_num_r} = {line[-1]} + {line_below_r}")
    print(f"Next num_l\t:{next_num_l} = {line[0]} - {line_below_l}")
    return (next_num_l, next_num_r)

print("Input:")
with open(path, 'r') as file:
    lines = [line for line in file if line.strip()]
    print(lines)
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
        lines[i] = [int(num) for num in lines[i].split()]
        
print_pyramid(lines)

sum_of_predictions = 0        
sum_of_predictions_l = 0        

for line in lines:
    #next_num = get_prediction(line)
    (next_num_l, next_num_r) = get_prediction_both_directions(line)

    print(f"whole pyramid:") 
    print_pyramid(predict_pyramid)          
    sum_of_predictions += next_num_r
    sum_of_predictions_l += next_num_l
    predict_pyramid = []

print(sum_of_predictions)
print(sum_of_predictions_l)

    