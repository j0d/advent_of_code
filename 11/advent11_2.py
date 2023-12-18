path = '11/test_input.txt'
path = '11/input.txt'

galaxies = []
lines = []
transposed_lines = []

y_expansions = []
x_expansions = []

def find_galaxies(chars) -> list:
    i=0
    gals = []
    while i < len(chars):
        print(chars[i])
        if '#' in chars[i]:
            for j in range(len(chars[i])):
                if chars[i][j] == '#':
                    gals.append((i,j))
                    print("found one at ", i, j)
        i+=1 
    return gals


def find_expandsions(chars) -> list:
    i=0
    exps = []
    while i < len(chars):
        print(chars[i])
        if '#' in chars[i]:
            print("galaxy found")
        else:
            #duplicate the line
            exps.append(i)
            #chars.insert(i,chars[i])
            print("expanding")
        i+=1 
    return exps 

#####################################################################
#####################################################################
# main

print("Input:")
with open(path, 'r') as file:
    lines = [line for line in file if line.strip()]
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
        
        

#find starting point
y_expansions = set(find_expandsions(lines))
y_expansions = sorted(y_expansions)

print("after first expansion and galaxies lines:")
for line in lines:
    print(line)

transposed_lines = [''.join(line) for line in zip(*lines)]

print("transposed:")
for line in transposed_lines:
    print(line)

x_expansions = set(find_expandsions(transposed_lines))
x_expansions = sorted(x_expansions)

print("expanded transposed:")
for line in transposed_lines:
    print(line)

lines = [''.join(line) for line in zip(*transposed_lines)]  

print("transposed back after expanding:")
for line in lines:
    print(line)

galaxies = find_galaxies(lines)

galaxies = sorted(galaxies)
print("Galaxies: ", galaxies)

expansion_coefficient = 1000000-1
total_expansion_count = 0
i=0 
total_distance = 0
for i in range(len(galaxies)):
    j=i+1
    while j < len(galaxies):
        print(f"Galaxy {i} y,x {galaxies[i]} to {j} {galaxies[j]}")
        start, end = sorted([galaxies[i][0],galaxies[j][0]])
        distance_y = end-start
        y_range = set(range(start,end))
        start, end = sorted([galaxies[i][1], galaxies[j][1]])
        distance_x = end-start
        x_range = set(range(start,end))
        #how many expansions are there between the two galaxies
        
        #find the intersection of the two ranges
        expansion_count_y = len(y_range.intersection(y_expansions))
        expansion_count_x = len(x_range.intersection(x_expansions))
        print("y range: ", y_range)
        print("y expansions: ", y_expansions)
        print("expansion count y: ", expansion_count_y)
        print("x range: ", x_range)
        print("x expansions: ", x_expansions)
        print("expansion count x: ", expansion_count_x)
        

        #distance_y = galaxies[j][0]-galaxies[i][0]
        #distance_x = galaxies[j][1]-galaxies[i][1]
        total_expansion_count += expansion_count_y + expansion_count_x
        distance = abs(distance_x) + abs(distance_y)
        print(f"distances x {distance_x} y {distance_y} total {distance}")
        total_distance += distance
        j+=1

print("Total expansion count: ", total_expansion_count)
total_distance += total_expansion_count*expansion_coefficient
print("Total distance: ", total_distance)
print(f"Num of x expansions: {len(x_expansions)}")
print(f"Num of y expansions: {len(y_expansions)}")
print(f"Number of galaxies: {len(galaxies)}")

