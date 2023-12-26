path = '15/test_input.txt'
path = '15/input.txt'


#### MAIN ####
total_sum = 0

print("Input:")
with open(path, 'r') as file:
    lines = [line for line in file if line.strip()]
    print(f"lines before strip: {lines}")
    lines = lines[0].split(',')
    for line in lines:
        print(line)
        current_value = 0
        for char in line:
            print(char)
            print(ord(char))
            current_value += ord(char)
            current_value = current_value*17 
            print(current_value)
            current_value = current_value % 256
            
            print(current_value)
        print(f"first char value: {current_value}")
        total_sum += current_value

            
            
print(total_sum)