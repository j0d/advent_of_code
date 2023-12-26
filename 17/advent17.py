

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

def print_path_matrix(matrix)->int:
    for row in matrix:
        for item in row:
            if item == []:
                print('.', end='')
            else:
                print('#', end='')
        print()
    return 0

# def print input matrix
def print_matrix(matrix)->int:
    for row in matrix:
        for item in row:
            print(item, end='')
        print()
    return 0

def find_next_step(y, x, dir)->(int, int, str):
    global matrix, straight_step_count
    #possible directions
    E = 'E'
    S = 'S'
    W = 'W'
    N = 'N'
    dirs = [E, S, W, N] # clockwise order
    
    
    if y == 0:
        dirs.pop(dirs.index('N'))
    elif y == len(matrix):
        dirs.pop(dirs.index('S'))
    elif x == 0:
        dirs.pop(dirs.index('W'))
    elif x == len(matrix[0]):
        dirs.pop(dirs.index('E'))

    if dir == E:
        dirs.pop(dirs.index('W'))
    elif dir == S:
        dirs.pop(dirs.index('N'))
    elif dir == W:
        dirs.pop(dirs.index('E'))
    elif dir == N:
        dirs.pop(dirs.index('S'))

    print(f"dirs: {dirs}")
    

    choices = []
    for d in dirs:
        if d == E:
            choices.append(matrix[y][x+1])
        elif d == S:
            choices.append(matrix[y+1][x])
        elif d == W:
            choices.append(matrix[y][x-1])
        elif d == N:
            choices.append(matrix[y-1][x])
    
    print(f"choices: {choices}")
    print(dirs[choices.index(min(choices))])
    
    min_choice_dir = dirs[choices.index(min(choices))]

    if min_choice_dir == E:
        x += 1
    elif min_choice_dir == S:
        y += 1
    elif min_choice_dir == W:
        x -= 1
    elif min_choice_dir == N:
        y -= 1

    print(f"y: {y}, x: {x}, dir: {min_choice_dir}")
    return (y, x, min_choice_dir)
#####################

def min_cost_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    max_steps = 3
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    inf = float('inf')

    # DP table: DP[row][col][steps][dir]
    DP = [[[[inf for _ in range(4)] for _ in range(max_steps)] for _ in range(cols)] for _ in range(rows)]

    # Base case: starting point
    for d in range(4):
        DP[0][0][0][d] = matrix[0][0]

    for i in range(rows):
        for j in range(cols):
            for s in range(max_steps):
                for d, (dx, dy) in enumerate(directions):
                    ni, nj = i - dx, j - dy
                    if 0 <= ni < rows and 0 <= nj < cols:
                        # Continue in the same direction
                        if s > 0:
                            DP[i][j][s][d] = min(DP[i][j][s][d], DP[ni][nj][s-1][d] + matrix[i][j])
                        # Switch direction
                        for nd in range(4):
                            if nd != d:
                                DP[i][j][0][d] = min(DP[i][j][0][d], DP[ni][nj][max_steps-1][nd] + matrix[i][j])

    # Answer is the minimum of the four possible directions in the last cell
    return min(DP[rows-1][cols-1][s][d] for s in range(max_steps) for d in range(4))



#### MAIN PROGRAM ####

path = '17/test_input.txt'
#path = '17/input.txt'

matrix = []

with open(path, 'r') as file:
    for line in file:
        # Strip newline character and then convert the line to a list of characters
        row = list(line.strip())

        # Adding the row to the matrix
        matrix.append(row)

#cast matrix from str to int
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = int(matrix[i][j])

print_matrix(matrix)


start_y = 0
start_x = 0
dir = 'E'

(y, x, dir) = find_next_step(start_y, start_x, dir)
print(f"y: {y}, x: {x}, dir: {dir}")


result = min_cost_path(matrix)
print("Minimum cost:", result)

