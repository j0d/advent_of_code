import pandas as pd
from math import sqrt, floor, ceil  

path = '6/test_input.txt'
path = '6/input.txt'

def parse_numbers(list_of_strings):
    #print(list_of_strings)
    numbers = []
    for string in list_of_strings:
        #print(string)
        if string.isdigit():
            numbers.append(int(string))
    return numbers


total_wins = []
with open(path, 'r') as file:
    lines = [line for line in file if line.strip()]
    lines = [line.strip('\n') for line in lines]
    times = parse_numbers(lines[0].split(':')[1].split(' '))
    distances = parse_numbers(lines[1].split(':')[1].split(' '))

    #concat the list items into one string  
    times = int(''.join(map(str, times)))
    distances = int(''.join(map(str, distances)))
    print(times)
    print(distances)

    #approximation of when we can win.
    j = int(distances/times)
    j_min = j

    wins_per_race=0
    for j in range(j,times):
        distance = (times-j)*j
        print(f"{j} {distance}")
        if distance > distances:
            wins_per_race+=1
            print(f"win {wins_per_race}")
        if (times-j) < j_min:
            break
    
    total_wins.append(wins_per_race)

print(total_wins)
#print the product of all total_wins
product = 1
for win in total_wins:
    product *= win
print(product)

 
 
exit() 
    #distance = (times-j)*j
    #j^2 - j*times + distance < 0

    #plot the function and find the roots
    #roots = (-b +- sqrt(b^2 - 4ac))/2a

t1 = (times + sqrt((-times)^2 - 4*distances))/2
print(f"t1: {t1}")
t2 = (times - sqrt(times^2 - 4*distances))/2
print(f"t2: {t2}")
number_of_wins = (t1) - (t2)