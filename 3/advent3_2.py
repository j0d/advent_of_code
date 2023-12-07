path = '3/test_input3.txt'
path = '3/input.txt'


lines = []
stars = []
rownum = 0
total_sum = 0

def is_next_to_symbol(i,j):
    
        startrow = max(rownum-1,0)
        startcol = max(i-1,0)
        endcol = min(j+1,len(lines[rownum]))
        print(f"startrow: {startrow}, startcol: {startcol}, endcol: {endcol}")

        for row in range(startrow,rownum+2):
            try:
                print(f"row: {row}")
                for col in range(startcol,endcol):
                    #print(lines[row][col])
                    if lines[row][col] not in ['0','1','2','3','4','5','6','7','8','9','.','\n']:
                        print(f'found symbol next to number at row: {row}, col: {col}')
                        return True
            except:
                print('out of bounds')

def is_next_to_star(i,j):
    
        startrow = max(rownum-1,0)
        startcol = max(i-1,0)
        endcol = min(j+1,len(lines[rownum]))
        print(f"startrow: {startrow}, startcol: {startcol}, endcol: {endcol}")

        for row in range(startrow,rownum+2):
            try:
                print(f"row: {row}")
                for col in range(startcol,endcol):
                    #print(lines[row][col])
                    if lines[row][col] == '*':
                        print(f'found star next to number at row: {row}, col: {col}')
                        return True, row, col
            except:
                print('out of bounds')
        return False, 0, 0

class star:
    #a star has a row, column and an array of numbers that are next to it

    def __init__(self, row, col, numbers):
        self.row = row
        self.col = col
        self.numbers = numbers



def add_number_to_star(star_row,star_col, number):
    for star in stars:
        if star.row == star_row and star.col == star_col:
            star.numbers.append(number) 

#read input.txt file
with open(path) as f:
    #read each line
    lines = f.readlines()
    #pretty print the array
    

for line in lines:
        i = 0
        j = 0
        while i < len(line):
            if line[i] == '*':
                print(f"found star at row: {rownum}, col: {i}")
                stars.append(star(rownum,i,[]))
            i+=1
        rownum += 1

for star in stars:
    print(f"star at row: {star.row}, col: {star.col}")
    print(len(star.numbers))

#let's start from the top again
rownum = 0
for line in lines:
    i = 0
    j = 0
    while j < len(line):
        if line[i].isdigit():
            j = i
            while line[j].isdigit():
                j+=1
            
            print(line[i:j])
            (next_to_star, row, col) = is_next_to_star(i,j)
            if next_to_star:
                print('found star next to number')
                add_number_to_star(row,col, int(line[i:j]))
            i = j
        else:
            i+=1
            j+=1
    rownum += 1
    

for star in stars:
    print(f"star at row: {star.row}, col: {star.col}")
    print(len(star.numbers))
    if len(star.numbers) == 2:
        total_sum += star.numbers[0] * star.numbers[1]
        print(f"total_sum: {total_sum}")
    print(star.numbers)
    




