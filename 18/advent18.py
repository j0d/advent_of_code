def create_matrix(max_y, min_y, max_x, min_x):
    matrix = []
    for i in range(max_y - min_y + 1):
        matrix.append([])
        for j in range(max_x - min_x + 1):
            matrix[i].append('.')
    return matrix

# def print input matrix
def print_matrix(matrix)->int:
    for row in matrix:
        for item in row:
            print(item, end='')
        print()
    return 0

### MAIN PROGRAM ####

path = '18/test_input.txt'
path = '18/input.txt'

#directions = ['R','L','U','D']
R = (0,1)
L = (0,-1)
U = (-1,0)
D = (1,0)

matrix = []

print("Input:")
print("Input:")
with open(path, 'r') as file:
    lines = [line for line in file if line.strip()]
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
        lines[i] = lines[i].split(' ') 


print(f"lines after strip: {lines}")
max_y = 0
min_y = 0
max_x = 0
min_x = 0
current_y = 0
current_x = 0

for i in range(len(lines)):
    if lines[i][0] == 'R':
        current_x = current_x + int(lines[i][1])
        if current_x > max_x:
            max_x = current_x
    elif lines[i][0] == 'L':
        current_x = current_x - int(lines[i][1])
        if current_x < min_x:
            min_x = current_x
    elif lines[i][0] == 'D':
        current_y = current_y + int(lines[i][1])
        if current_y > max_y:
            max_y = current_y
    elif lines[i][0] == 'U':
        current_y = current_y - int(lines[i][1])
        if current_y < min_y:
            min_y = current_y

print(f"max_y: {max_y}, min_y: {min_y}, max_x: {max_x}, min_x: {min_x}")

matrix = create_matrix(max_y, min_y, max_x, min_x)


print(f"matrix size: {len(matrix)}x{len(matrix[0])}")
current_x = -min_x
current_y = -min_y
#print_matrix(matrix)

last_dir = 'R'
for line in lines:
    print(f"dir {line[0]} steps {line[1]}")
    for i in range(int(line[1])): # take steps
        if line[0] == 'R':
            current_x += 1
            matrix[current_y][current_x] = '-'
        elif line[0] == 'L':
            current_x -= 1
            matrix[current_y][current_x] = '-'
        elif line[0] == 'D':
            current_y += 1
            matrix[current_y][current_x] = '|'
        elif line[0] == 'U':
            current_y -= 1
            matrix[current_y][current_x] = '|'
        if i == 0:
            if last_dir == 'R' and line[0] == 'D':
                matrix[current_y-1][current_x] = '7'
            elif last_dir == 'R' and line[0] == 'U':
                matrix[current_y+1][current_x] = 'J'
            elif last_dir == 'L' and line[0] == 'D':
                matrix[current_y-1][current_x] = 'F'
            elif last_dir == 'L' and line[0] == 'U':
                matrix[current_y+1][current_x] = 'L'
            elif last_dir == 'D' and line[0] == 'R':
                matrix[current_y][current_x-1] = 'L'
            elif last_dir == 'D' and line[0] == 'L':
                matrix[current_y][current_x+1] = 'J'
            elif last_dir == 'U' and line[0] == 'R':
                matrix[current_y][current_x-1] = 'F'
            elif last_dir == 'U' and line[0] == 'L':
                matrix[current_y][current_x+1] = '7'
            
    last_dir = line[0]

#real input ends with U and starts L
matrix[current_y][current_x] = '7'
#test input needs F
#matrix[current_y][current_x] = 'F'

print_matrix(matrix)

#write matrix to file

#find dug area.
total_area_dug = 0
inside = 0
last_turn = ''
#loop through matrix to count dug area
for i in range(len(matrix)):
    inside = 0
    for j in range(len(matrix[0])):
        if matrix[i][j] == '7' and last_turn == 'L':
            inside = 1-inside
        if matrix[i][j] == 'J' and last_turn == 'F':
            inside = 1-inside
        if matrix[i][j] in ['L','J','F','7']:
            last_turn = matrix[i][j]
            total_area_dug += 1
        if matrix[i][j] == '-':
            total_area_dug += 1
        if matrix[i][j] == '|':
            inside = 1 - inside
            total_area_dug += 1
        if matrix[i][j] in ['.'] and inside == 1:
            total_area_dug += inside
            matrix[i][j] = '#'

print(total_area_dug)

with open('18/output.txt', 'w') as file:
    for row in matrix:
        for item in row:
            file.write(item)
        file.write('\n')
