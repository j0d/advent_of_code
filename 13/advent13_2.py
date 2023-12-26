path = '13/test_input1.txt'
#path = '13/input.txt'

## YOU GET A DIFFERENT NUMBER DEPENDING ON THE CHANGE YOU MAKE. TEST PATTERN 2 CAN BE CHANGED TO A . INSTEAD IN THE FIRST ROW.


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
    
def only_one_char_diff(lines, i,j)->(bool, int, int):
    if lines[i] == lines[j]:
        return False, 0, 0
    else: #is only one char different?
        count = 0
        k=0
        diff_row_index = 0
        diff__char_index = 0
        for k in range(len(lines[i])):
            if lines[i][k] != lines[j][k]:
                count += 1
                diff_row_index = i
                diff_char_index = k
                if count > 1:
                    return False, 0,0
        return True, diff_row_index, diff_char_index


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

def replace_char_at_index(s, i, new_char):
    if i < 0 or i >= len(s):
        raise ValueError("Index is out of the range of the string")

    return s[:i] + new_char + s[i+1:]

def find_mirror_lines_with_one_flaw()->list:
    global diff_row_i, diff_char_i, pattern
    first_diff = 0
    one_diff = False
    mirror_lines = []
    max_index = len(pattern) -1
    for i in range(len(pattern)):
        j=i
        k=i+1
        mirror_row_count = 0
        while j>=0 and k<=max_index:
            if first_diff == 0:
                (one_diff, diff_row_i, diff_char_i) = only_one_char_diff(pattern, j,k)
                if one_diff:
                    first_diff += 1
            if is_mirror(pattern, j,k):
                mirror_row_count += 1
                #print(f"lines[{j}] and lines[{k}] are mirrors and mirror_row_count: {mirror_row_count}\n{lines[j]}\n{lines[k]}")                
                j -= 1
                k += 1
            elif (one_diff and first_diff == 1):
                first_diff = False
                print(f"changed char at row {diff_row_i} and char {diff_char_i}")
                #remember the diff_i.
                mirror_row_count += 1
                j -= 1
                k += 1
            else:
                break
            
        if (mirror_row_count >= min(i, max_index-k)and mirror_row_count > 0): #have we mirrored to the edge?
            if (mirror_row_count == (i+1) or mirror_row_count == (max_index-i)):
                if first_diff == 1:
                    print(f"changed char at row {diff_row_i} and char {diff_char_i}")
                    pattern[diff_row_i] = replace_char_at_index(pattern[diff_row_i], diff_char_i, '.')
                    print_pattern(pattern)
                mirror_lines.append(i+1)
                print(f"mirror between row {i} and {i+1} with {mirror_row_count} rows")
    return mirror_lines

########## MAIN ##########
lines = []
max_index = 0
total_sum = 0
diff_row_i = 0 
diff_char_i = 0

pattern_count = 0
total_lines = 0
pattern = []



with open(path, 'r') as file:
    lines = [line for line in file]

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


    mirrors = find_mirror_lines_with_one_flaw()
    if len(mirrors) > 0:
        print(f"found mirror at row {mirrors}")
        total_sum += (sum(mirrors))*100
        continue
    else:
        print(f"no mirror found - let's transpose and check columns")
        transposed_lines = [''.join(line) for line in zip(*pattern)]
        print(f"transposed pattern:")
        pattern = transposed_lines
        print_pattern(transposed_lines)
        mirrors = find_mirror_lines_with_one_flaw()
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






