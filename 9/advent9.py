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



print("Input:")
with open(path, 'r') as file:
    lines = [line for line in file if line.strip()]
    print(lines)
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
        lines[i] = [int(num) for num in lines[i].split()]
        
print_pyramid(lines)

sum_of_predictions = 0        
for line in lines:
    next_num = get_prediction(line)
    print(f"whole pyramid:") 
    print_pyramid(predict_pyramid)          
    print(next_num)
    sum_of_predictions += next_num
    predict_pyramid = []

print(sum_of_predictions)
    