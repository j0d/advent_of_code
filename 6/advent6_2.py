import pandas as pd

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

 
    wins_per_race=0
    for j in range(times):
        distance = (times-j)*j
        print(f"{j} {distance}")
        if distance > distances:
            wins_per_race+=1
            print(f"win {wins_per_race}")
    total_wins.append(wins_per_race)

print(total_wins)
#print the product of all total_wins
product = 1
for win in total_wins:
    product *= win
print(product)