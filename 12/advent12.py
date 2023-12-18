path = '12/test_input.txt'
#path = '12/input.txt'

def place_char(char):
    global output, output_index
    output = output[:output_index] + char + output[output_index+1:]
    output_index += 1
    return        


def place_value(value):
    global output, output_index
    value_str = str(value)
    for i in range(value):
        output = output[:output_index] + value_str + output[output_index+1:]
        output_index += 1
    print(f"output: {output}")
    return

def number_of_options(eval_string, values) -> int:
    global values_placed, output, output_index
    options = 0
    i=0
    first_eval_section = eval_string.split('.')[0]
    print(f"eval_string: {eval_string}, first_eval_section: {first_eval_section} and remaining values: {values}")
    #for i in range(len(values)):
    first_value = values[0]
    
    if(len(values) == 1):
        return_value = 1
    else:
        return_value = 0    

    #remove all dots in the beginning.
    if eval_string[0] == '.':
        number_of_options(eval_string[1:],values)

    if first_value == len(first_eval_section): #place value.
        place_value(first_value)
        values_placed += 1 #each time a value is place the number of options should be recorded. He it should not increase.
        print("value == len(eval_string) = place value")
        return return_value
    
    elif first_value < len(first_eval_section):
        print(f"first two values sum: {sum(values[0:2])}")
        if first_value == 1 and len(first_eval_section) == 2:
            print("value == 1 and len(eval_string) == 2") #two options.
            row_options.append(2)
            values_placed += 1
            place_value(first_value)
            place_char('?')
            print(f"output: {output}")
            return return_value+2 
        elif sum(values[0:2]) >= len(first_eval_section): #first number needs to be placed only
            print("two numbers >= length as len eval string => only one fits")
            print(f"eval_string[1:]: {eval_string[1:]}")
            number_of_options(eval_string[1:], values[i+1:]) 
            return 0
        elif sum(values[0:2])+1 < len(first_eval_section): #continue looking
            print("first two numbers smaller than len eval string")
            #look at the first char after the first value length
            if eval_string[first_value] == '?': 
                # next char is question mark. Value can potentially be placed further in the string.
                print("next char is question mark")
                place_value(first_value)
                placed = number_of_options(eval_string[first_value:], values[i+1:])
                if placed: #could the next value be placed further in the string?
                    print("next value could not be placed further in the string")
                    return 0

            elif eval_string[first_value] == '.': #next char is dot. Value must be placed. (can't happen as we have split on dot and then len(first_eval) equals value see above)
                print("next char is dot")
                values_placed += 1
                number_of_options(eval_string[first_value:], values[i+1:])
            elif eval_string[first_value] == '#': #next char is number. Value can't be placed.
                print("next char is number")
                if eval_string[0] == '?': #Must be a dot continue to next char
                    place_char('.')
                    print("place dot")
                    number_of_options(eval_string[1:], values) #continue.
                elif eval_string[0] == '#' or eval_string[0] == '.':
                    print("can't happen (dot's should be removed) and if number is first and after len value it is fail.")
                    print("next char is number")
            


            #number_of_options(eval_string[first_value:], values[i+1:])
            values_placed += 1
            return 0
        elif sum(values[0:2])+1 == len(eval_string): #have to place both values - should be recursive?
            print("first two numbers equal length as len eval string+space between place one value and eval rest (which should be place only)")
            place_value(first_value)
            values_placed += 1
            place_char('.')
            number_of_options(eval_string[first_value+1:], values[i+1:]) 
            print(f"output: {output}")  
            return 0
    
    
    


    
    return options



#####################################################################
#####################################################################
# main
total_options = 0
output = []
output_index = 0
row_index = 0

eval_string = ''
print("Input:")
with open(path, 'r') as file:
    lines = [line for line in file if line.strip()]
    for row_index in range(5): #range(len(lines)): #for each row#
        row_options = []
        values_placed = 0
        output_index = 0
        lines[row_index] = lines[row_index].strip('\n')

        record, values = lines[row_index].split(' ')
        values = values.split(',')
        values = [int(value) for value in values]
        print(f"record: {record}, values: {values}")
        j=0
        output = record
        print(f"record: {record.split('.')}")


        for eval_string in record.split('.'):
            if eval_string == '':
                place_char('.')
                continue
            total_options += number_of_options(eval_string, values[values_placed:])
            print(f"row_options: {row_options}")
            print(f"total_options: {total_options}")
            place_char('.')

        print(f"record: {record}, values: {values} Evaluted string: {output}\n\n")

        continue

        for k in range(len(record)): #for each character in record#
            while j < len(values): #for each value in values#
                l = 0
                #print(f"record[{k}]: {record[k]}")
                eval_string = ''
                while record[l] == '?':
                    eval_string= eval_string+(record[l])
                    l += 1 

                

                
                print(f"eval_string: {eval_string}")
                print(f"values[{j}]: {values[j]}")
                # if values[j] larger than len(eval_string)
                if values[j] > len(eval_string):
                    print(f"values[{j}] > len(eval_string)")
                elif values[j] == len(eval_string):
                    print(f"values[{j}] == len(eval_string)")
                    print("one option")
                    j += 1
                elif values[j] < len(eval_string):
                    print(f"values[{j}] < len(eval_string)")
                    print("place first value and eval rest")
                    j += 1
        break