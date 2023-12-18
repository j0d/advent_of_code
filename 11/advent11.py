path = '11/test_input.txt'
path = '11/input.txt'

galaxies = []
lines = []
transposed_lines = []
total_expansion_count = 0
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


def expand_galaxy(chars) -> list:
    global total_expansion_count
    i=0
    exps = []
    while i < len(chars):
        print(chars[i])
        if '#' in chars[i]:
            print("galaxy found")
        else:
            #duplicate the line
            chars.insert(i,chars[i])
            print("expanding")
            exps.append(i)
            total_expansion_count += 1
            i+=1
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
y_expansions = expand_galaxy(lines)

print("after first expansion and galaxies lines:")
for line in lines:
    print(line)

transposed_lines = [''.join(line) for line in zip(*lines)]

print("transposed:")
for line in transposed_lines:
    print(line)

x_expansions = expand_galaxy(transposed_lines)

print("expanded transposed:")
for line in transposed_lines:
    print(line)

lines = [''.join(line) for line in zip(*transposed_lines)]  

print("transposed back after expanding:")
for line in lines:
    print(line)

galaxies = find_galaxies(lines)

print("Galaxies: ", galaxies)

i=0 
total_distance = 0
for i in range(len(galaxies)):
    j=i+1
    while j < len(galaxies):
        print(f"Galaxy {i} y,x {galaxies[i]} to {j} {galaxies[j]}")
        distance_y = galaxies[j][0]-galaxies[i][0]
        distance_x = galaxies[j][1]-galaxies[i][1]
        distance = abs(distance_x) + abs(distance_y)
        print(f"distances x {distance_x} y {distance_y} total {distance}")
        total_distance += distance
        j+=1


print("Total expansion count: ", total_expansion_count)
print("Total distance: ", total_distance)
print(f"Number of galaxies: {len(galaxies)}")
print(f"Num of x expansions: {len(x_expansions)}")
print(f"Num of y expansions: {len(y_expansions)}")
print(f"Number of galaxies: {len(galaxies)}")