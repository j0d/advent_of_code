import pandas as pd


def print_energy_matrix(matrix)->int:
    energy = 0
    for row in matrix:
        for item in row:
            if item == []:
                print('.', end='')
            else:
                print('#', end='')
                energy += 1
        print()
    return energy

def take_ray_step(y,x,dir):
    global matrix, energy_matrix, rays


    #print_energy_matrix(energy_matrix)

    #if x or y are out of bounds, return
    if x < 0 or x >= len(matrix[0]) or y < 0 or y >= len(matrix):
        return
    
    if dir in energy_matrix[y][x]: # The energy is coming from the same direction no need to follow ray anymore
        #print(f"energy at location {y},{x} is coming {dir} already in energy_matrix {energy_matrix[y][x]}")
        return
    else: # The energy is coming from a new direction
        energy_matrix[y][x].append(dir)
        #print(f"new energy at location {y},{x} coming {dir} in energy_matrix {energy_matrix[y][x]}")
        
    
    if matrix[y][x] == '.':
        if dir == 'E':
            take_ray_step(y, x+1, dir)
        elif dir == 'S':
            take_ray_step(y+1, x, dir)
        elif dir == 'W':
            take_ray_step(y, x-1, dir)
        elif dir == 'N':
            take_ray_step(y-1, x, dir)
    elif matrix[y][x] == '/':
        if dir == 'E':
            dir = 'N'
            take_ray_step(y-1, x, dir)
        elif dir == 'S':
            dir = 'W'
            take_ray_step(y, x-1, dir)
        elif dir == 'W':
            dir = 'S'
            take_ray_step(y+1, x, dir)
        elif dir == 'N':
            dir = 'E'
            take_ray_step(y, x+1, dir)
    elif matrix[y][x] == '\\':
        if dir == 'E':
            dir = 'S'
            take_ray_step(y+1, x, dir)
        elif dir == 'S':
            dir = 'E'
            take_ray_step(y, x+1, dir)
        elif dir == 'W':
            dir = 'N'
            take_ray_step(y-1, x, dir)
        elif dir == 'N':
            dir = 'W'
            take_ray_step(y, x-1, dir)
    elif matrix[y][x] == '|':
        if dir == 'E' or dir == 'W':
            take_ray_step(y+1, x, 'S')
            rays.append([y-1, x, 'N'])
        elif dir == 'N':
            take_ray_step(y-1, x, dir)
        elif dir == 'S':
            take_ray_step(y+1, x, dir)
    elif matrix[y][x] == '-':
        if dir == 'N' or dir == 'S':
            take_ray_step(y, x+1, 'E')
            rays.append([y, x-1, 'W'])
        elif dir == 'E':
            take_ray_step(y, x+1, dir)
        elif dir == 'W':
            take_ray_step(y, x-1, dir)

def find_energy_for_start(ray_y, ray_x, ray_dir)->int:
    global matrix, energy_matrix, rays
    rays.append([ray_y, ray_x, ray_dir])
    while True:
        try:
            print(f"ray queue: {len(rays)}")
            ray_y, ray_x, ray_dir = rays.pop()
            take_ray_step(ray_y, ray_x, ray_dir)
        except IndexError:
            break
    return print_energy_matrix(energy_matrix)

#### MAIN PROGRAM ####

path = '16/test_input.txt'
path = '16/input.txt'

matrix = []

with open(path, 'r') as file:
    for line in file:
        # Strip newline character and then convert the line to a list of characters
        row = list(line.strip())

        # Adding the row to the matrix
        matrix.append(row)

# matrix now contains the data from the file as a list of lists of characters
#print(matrix)
#print(matrix[0][0])

# Creating a new matrix with the same dimensions
energy_matrix = [[[] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

print(energy_matrix)

ray_x = 0
ray_y = 0
ray_dir = 'E'
rays = []   
#rays.append([ray_y, ray_x, ray_dir])
max_count = 0 
for i in range(len(matrix[0])):
    # Creating a new matrix with the same dimensions
    energy_matrix = [[[] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    count = find_energy_for_start(0,i,'S')
    print(count)
    if count > max_count:
        max_count = count
    # Creating a new matrix with the same dimensions
    energy_matrix = [[[] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    count = find_energy_for_start(len(matrix)-1,i,'N')
    print(count)
    if count > max_count:
        max_count = count

for i in range(len(matrix)):
    # Creating a new matrix with the same dimensions
    energy_matrix = [[[] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    count = find_energy_for_start(i,0,'E')
    print(count)
    if count > max_count:
        max_count = count
    # Creating a new matrix with the same dimensions
    energy_matrix = [[[] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    count = find_energy_for_start(i,len(matrix[0])-1,'W')
    print(count)
    if count > max_count:
        max_count = count


print(max_count)
#print(matrix[6][7])
#print(energy_matrix[6][7])
#print(energy_matrix[6][6])
#print(matrix[6][7]== '\\')