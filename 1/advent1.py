import sys

def calibration_value_2(line):
    #initialize sum
    letter_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = ''
    charnum = 0
    
    #iterate through each character (we can only find 1 digit at each char.)
    for charnum in range(0,len(line)):
        #if char is a digit and is the first or last digit
        if line[charnum].isdigit():
            #add to sum
            digits += line[charnum]

        #if char is a letter
        for j in range(0,len(letter_digits)):
            
            #compare substring of length letter_digits[i] to letter_digits[i]
            substring = line[charnum:len(letter_digits[j])+charnum]
            #print(substring)
            if substring == letter_digits[j]:
                digits += str(j+1)
                break
            else:
                j+=1

    #print both lines to see what is happening
    print(line)
    print(digits)
    answer = int(digits[0]+digits[-1])
    print(answer)
    return answer

def calibration_value_1(line):
    #initialize sum
    digits = []
    #iterate through each character
    for char in line:
        #if char is a digit and is the first or last digit
        if char.isdigit():
            #add to sum
            digits.append(char)
    #return sum of first and last digit in digits
    answer = int(digits[0]+digits[-1])
    print(answer)
    return answer


path = '1/input.txt'
#path = '1/test_input.txt'

#read input.txt file
with open(path) as f:
    #read each line
    lines = f.readlines()
    #initialize sum
    sum_of_calibration_values = 0
    #iterate through each line
    continue_loop = 'y'

    for line in lines:
        #add to sum
        sum_of_calibration_values += calibration_value_2(line)
        if continue_loop == 'y':
            continue_loop = input("Continue? y/n")
        
print(sum_of_calibration_values)


teststring = "5qpmvbnpfiveoneeightsevenone78"
