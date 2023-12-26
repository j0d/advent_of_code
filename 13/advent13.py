path = '13/test_input1.txt'
path = '13/input.txt'

lines = []
max_index = 0
total_sum = 0

def print_pattern(pattern):
    for line in pattern:
        print(line)

def read_next_pattern(lines)->list:
    first_pattern = []
    for line in lines:
        if line == '\n':
            break
        else:
            first_pattern.append(line.strip())
    return first_pattern

def is_mirror(lines, i,j)->bool:
    if lines[i] == lines[j]:
        return True
    else:
        return False
    
def find_mirror_lines(lines)->list:
    mirror_lines = []
    max_index = len(lines) -1
    for i in range(len(lines)):
        j=i
        k=i+1
        mirror_row_count = 0
        while j>=0 and k<=max_index:
            if is_mirror(lines, j,k):
                mirror_row_count += 1
                #print(f"lines[{j}] and lines[{k}] are mirrors and mirror_row_count: {mirror_row_count}\n{lines[j]}\n{lines[k]}")                
            j -= 1
            k += 1
            
        if (mirror_row_count >= min(i, max_index-k)and mirror_row_count > 0): #have we mirrored to the edge?
            if (mirror_row_count == (i+1) or mirror_row_count == (max_index-i)):
                mirror_lines.append(i+1)
                print(f"mirror between row {i} and {i+1} with {mirror_row_count} rows")
    return mirror_lines


with open(path, 'r') as file:
    lines = [line for line in file]

pattern_count = 0
total_lines = 0

while len(lines) > 0:
    print(f"lines left: {len(lines)}")
    print(f"total sum: {total_sum}")

    pattern = read_next_pattern(lines)
    lines = lines[len(pattern)+1:]
    pattern_count += 1
    total_lines += len(pattern)+1
    print(f"pattern:")
    print_pattern(pattern)
    print(f"pattern length: {len(pattern)}")


    mirrors = find_mirror_lines(pattern)
    if len(mirrors) > 0:
        print(f"found mirror at row {mirrors}")
        total_sum += (sum(mirrors))*100
        continue
    else:
        print(f"no mirror found - let's transpose and check columns")
        transposed_lines = [''.join(line) for line in zip(*pattern)]
        print(f"transposed pattern:")
        print_pattern(transposed_lines)
        mirrors = find_mirror_lines(transposed_lines)
        #print(f"mirrors: {mirrors}")

        if len(mirrors) > 0:
            print(f"found mirror at row {mirrors}")
            total_sum += (sum(mirrors))
        else:
            print("error")
            exit(1)

    


print(f"total lines: {total_lines}")
print(f"total patterns: {pattern_count}")
print(f"total sum: {total_sum}")






