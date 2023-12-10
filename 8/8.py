import pandas as pd

path = '8/test_input.txt'
path = '8/input.txt'
#path = '8/test_input2.txt'
start = []
left = []
right = []

with open(path, 'r') as file:
    lines = [line for line in file if line.strip()]
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
        print(lines[i])
        print(i)
        if i > 0:
            lines[i] = lines[i].replace(' ', '').replace('=', ',').replace('(', '').replace(')', '').split(',')       
        # 
        #     start[i] = line.split('=')[0]
        #     left[i] = line.split('=')[1].split(',')[0]
        #     right[i] = line.split('=')[1].split(',')[1]
        print(lines[i])        

instruction = lines[0][:]
print(instruction)
print(lines[1:])

#insert lines into a df with columns: start, left, right
df = pd.DataFrame(lines[1:],columns=['start', 'L', 'R'])

print(df)

inst_index = 0
inst_len = len(instruction)
next_start = 'AAA'
steps = 0

while next_start != 'ZZZ':
    print(inst_index)
    print(instruction[inst_index])
    print(next_start)
    next_start = df.loc[df['start'] == next_start, instruction[inst_index]].iloc[0]
        
    steps += 1
    #increase index 1 mod len(instruction)
    inst_index = (inst_index +1) % inst_len
    
print(steps)