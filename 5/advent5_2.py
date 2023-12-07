import pandas as pd

path = '5/test_input.txt'
#path = '5/input.txt'

location = 99999999999999999

# Define column names
columns = ['destination', 'source', 'range_length']
conversion_steps = []
new_seeds = []
seeds = []

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
    #print(f"destination: {destination}")
    return destination

def calc_translation_step(df, seeds) -> new_seeds:
    k=0
    l=0
    new_seeds = []
    while k < len(seeds):
        print(f"\n\nseed: {seeds[k]}")
        print(f"range: {seeds[k+1]}")
        print(df)
        for index, row in df.iterrows():
                print(f"row_source: {row['source']} and row_range: {row['range_length']}")
                if row['source'] <= seeds[k] <= row['source'] + row['range_length'] -1:
                        new_seeds.append(row['destination'] + (seeds[k] - row['source'])) #translate the starting seed to the new seed
                        if seeds[k+1] <= row['range_length']: #if the range is big enough to cover the seed
                            new_seeds.append(new_seeds[k]+seeds[k+1]) #add the seed to the new seed as it is within the range
                        else: #if the range is not big enough to cover the range
                            seeds.append(seeds[k]+row['range_length']) #add the remaining seed back to the seed
                            seeds.append(seeds[k+1]-row['range_length']) #add the remaining range back to the seed
                            new_seeds.append(new_seeds[k]+row['range_length']) #add the first part of the range to the new seed                            
        k+=2
        print(f"Lenght of seeds: {len(seeds)}")
        print(f"seeds: {seeds}")
        print(f"new_seeds: {new_seeds}")
    return new_seeds
    


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
            #print(f"seeds: {seeds}")
            #print(f"Length of seeds: {len(seeds)}")
            df = pd.DataFrame(columns=columns)
        elif line[0].isdigit():
            #print(i)
            line = parse_numbers(line.split(' '))
            #print(line)

            #create a dataframe and read in the digit lines           
            new_row = pd.DataFrame([line], columns=df.columns)
            df = pd.concat([df, new_row], ignore_index=True)
            #print(df)
        elif line[0].isalpha():
            conversion_steps.append(df)
            #print(f"conversion_steps: {line}")
            df = pd.DataFrame(columns=columns)
        else:
            print("error")  
    conversion_steps.append(df)


### all maps read in. Now to convert the seeds    
print(f"number of conversion_steps: {len(conversion_steps)}")    
    


   #while k < len(seeds):
for step in conversion_steps:
    #if step is non empty df
    if not step.empty:
        print(f"\n\nNEW STEP seeds: {seeds}")
        print(f"step: {step}")       
        new_seeds = calc_translation_step(step, seeds)
        print(f"\n\nnew_seeds: {new_seeds}")
        seeds = new_seeds



print(f"seeds: {seeds}")
k=0
for k in range(len(seeds)):
    if seeds[k] < location:
        location = seeds[k]
    k+=2

print(f"min location: {location}") 

        
#    for seed in seeds:
                  
        
     
     #   elif line[0] in 'abcdefghijklmnopqrstuvwxyz':
            #if line starts with seeds
      #      j=0
            




