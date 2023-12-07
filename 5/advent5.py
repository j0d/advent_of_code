import pandas as pd

path = '5/test_input.txt'
path = '5/input.txt'

locations = []

# Define column names
columns = ['destination', 'source', 'range_length']
conversion_steps = []


def parse_numbers(list_of_strings):
    #print(list_of_strings)
    numbers = []
    for string in list_of_strings:
        #print(string)
        if string.isdigit():
            numbers.append(int(string))
    return numbers

def map_source_to_destination(df, seed) -> int:
    translated = False
    for index, row in df.iterrows():
        if row['source'] <= seed <= row['source'] + row['range_length'] -1:
            destination = row['destination'] + (seed - row['source'])
            translated = True
    if not translated:
        destination = seed
    print(f"destination: {destination}")
    return destination
    


#read input.txt file
with open(path, 'r') as file:
    lines = [line for line in file if line.strip()]
    
    i=0
    j=0
    for i in range(len(lines)):
        line = lines[i].strip('\n')
        
        if line.startswith('seeds'):
            seeds = line.split(':')[1].split(' ')
            seeds = parse_numbers(seeds)
            print(f"seeds: {seeds}")
            df = pd.DataFrame(columns=columns)
        elif line[0].isdigit():
            #print(i)
            line = parse_numbers(line.split(' '))
            #print(line)

            #create a dataframe and read in the digit lines
            
            #add the numbers to the dataframe
            new_row = pd.DataFrame([line], columns=df.columns)
            df = pd.concat([df, new_row], ignore_index=True)
            #print(df)
        elif line[0].isalpha():
            conversion_steps.append(df)
            print(f"conversion_steps: {line}")
            df = pd.DataFrame(columns=columns)
        else:
            print("error")  
    conversion_steps.append(df)
    for seed in seeds:
        print(f"\n\nseed: {seed}")
        print(f"conversion_steps: {conversion_steps}")
        for step in conversion_steps:
            
            #for each step, map the source to the destination
            seed = map_source_to_destination(step, seed)
            print(f"seed: {seed}")

        print(f"final seed: {seed}")
        locations.append(seed)

print(f"locations: {locations}") 
print(f"min: {min(locations)}")

        
#    for seed in seeds:
                  
        
     
     #   elif line[0] in 'abcdefghijklmnopqrstuvwxyz':
            #if line starts with seeds
      #      j=0
            




