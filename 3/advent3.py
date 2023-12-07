path = '3/test_input3.txt'
path = '3/input.txt'

# siffror = []
# siffror.append(1)
# siffror.append(2)
# siffror[1] = 3

# print(siffror)
# #print(siffror[0])

# siffra = '123'

lines = []
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






#read input.txt file
with open(path) as f:
    #read each line
    lines = f.readlines()
    #pretty print the array
    
    
    for line in lines:
        i = 0
        j = 0
        while j < len(line):
            if line[i].isdigit():
                j = i
                while line[j].isdigit():
                    j+=1
                
                print(line[i:j])
                if is_next_to_symbol(i,j):
                    print('found symbol next to number')
                    total_sum += int(line[i:j])
                    print(f"total_sum: {total_sum}")
                i = j
            else:
                i+=1
                j+=1
        rownum += 1
        
        #print(line)




