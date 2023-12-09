import pandas as pd

path = '5/test_input.txt'
path = '5/input.txt'

location = 99999999999999999

# Define column names
columns = ['destination', 'source', 'range_length']
seed_columns = ['seed', 'range']
conversion_steps = []
new_seed_list = []
seed_list = []

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

def add_seed(seed, range):
    seed_list.append(pd.DataFrame([[seed,range]], columns=seed_columns))
    return

def add_new_seed(seed, range):
    new_seed_list.append(pd.DataFrame([[seed,range]], columns=seed_columns))
    return

def get_lowest_seed_value(df):
    return df['seed'].iloc[0]

#think the bug is now in sorting of seeds only :)
def calc_translation_step(df, seeds):
    k=0
    l=0
    while k < len(seed_list):
        #seed_list[k].sort_values(by='seed', inplace=True) #this one is wrong
        seed = seed_list[k]['seed'].iloc[0]
        seed_range = seed_list[k]['range'].iloc[0]
        print(f"\n\nseed: {seed}")
        print(f"range: {seed_range}")
        print(df)
        translated = False 
        before_lowest_source = True
        for index, row in df.iterrows():
            print(f"row_source: {row['source']} and row_range: {row['range_length']}")
            print(f"seed: {seed} and seed_range: {seed_range}")
            if translated:
                break

            #case 1: seed is below smallest source and range does not cover source (this can happen later too - BUG fix)
            if seed < row['source'] and seed + seed_range <= row['source'] and before_lowest_source:
                print("case1")
                translated = True
                k+=1
            #case 2: seed is less than smallest source but range covers source
            elif seed < row['source'] and seed + seed_range > row['source']: #if start of seed not in range but range covers source
                print("case2")
                print("range entering a band")
                add_seed(row['source'], seed+seed_range-row['source'])
                #seeds.append(row['source'])
                #seeds.append(seed_start+seed_range-row['source'])
                add_new_seed(seed, seed_range-(row['source']-seed))
                #new_seeds.append(seed)
                #new_seeds.append(seed_range-(row['source']-seed))
                translated = True
                k+=1
            #case 3: seed is in a range
            elif row['source'] <= seed <= row['source'] + row['range_length'] -1:
                print("case3")
                before_lowest_source = False
                steps_in = seed - row['source']
                translated = True
                k+=1
                if seed_range <= (row['range_length']-steps_in): #if the range is big enough to cover the seed
                    new_seed_range = seed_range #add the range to the new seed as it is within the range
                else: #if the range is not big enough to cover the range
                    add_seed(row['source']+row['range_length'],seed_range-row['range_length']+steps_in) #add the remaining seed and range back to the seed with start at the end of the range)
                    new_seed_range = row['range_length']-steps_in #add the first part of the range to the new seed 
                add_new_seed(row['destination'] + steps_in, new_seed_range) #translate the starting seed to the new seed
            #case 4: seed is above the range
            elif seed > row['source'] + row['range_length'] -1:
                print("case4") 
                #continue to next row               
            else:
                print("error")
                exit()       
        if not translated:
            print("case5")
            add_new_seed(seed, seed_range) #if the seed is not translated, add it to the new seeds
            k+=1

        #seed_list.sort(key=get_lowest_seed_value)
        
        print(f"Lenght of seeds: {len(seed_list)}")
        print(f"seeds: {seed_list}")
        print(f"new_seeds: {new_seed_list}")
    return





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
            l=0
            while l < len(seeds):
                add_seed(seeds[l], seeds[l+1])
                l+=2
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
            df.sort_values(by='source', inplace=True)
            conversion_steps.append(df)
            #print(f"conversion_steps: {line}")
            df = pd.DataFrame(columns=columns)
        else:
            print("error")  
    conversion_steps.append(df)


### all maps read in. Now to convert the seeds    
print(f"number of conversion_steps: {len(conversion_steps)}")   
print(f"first conversion_step: {conversion_steps[1]}") 
print(f"seeds: {seed_list}")


stosp = 0
for step in conversion_steps:
    #if step is non empty df
    if not step.empty:
        print(f"\n\nNEW STEP seeds: {seed_list}")
        print(f"step: {step}")       
        calc_translation_step(step, seed_list)
        print(f"\n\nnew_seeds: {new_seed_list}")
        #seed_list = new_seed_list
        seed_list = [df.copy() for df in new_seed_list]
        new_seed_list = []
        stosp+=1
        print(f"\n\nAFTER STEP new seeds: {seed_list}")
    



print(f"seeds: {seed_list}")

for seed in seed_list:
    if seed['seed'].iloc[0] < location:
        location = seed['seed'].iloc[0]

print(f"min location: {location}") 

        
#    for seed in seeds:
                  
        
     
     #   elif line[0] in 'abcdefghijklmnopqrstuvwxyz':
            #if line starts with seeds
      #      j=0
            




