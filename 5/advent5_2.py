import pandas as pd

path = '5/test_input.txt'
path = '5/input.txt'
#path = '5/test_input3.txt' #adding seeds in the beginning and in the end. removing 0 in the first conversion step

location = 99999999999999999

# Define column names
columns = ['destination', 'source', 'range_length']
seed_columns = ['seed', 'range']
conversion_steps = []
#new_seed_list = []
#seed_list = []
seeds = pd.DataFrame(columns=seed_columns)
new_seeds = pd.DataFrame(columns=seed_columns)

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
    global seeds
    #add the seed and range to the df of seeds
    new_seed = pd.DataFrame([[seed, range]], columns=seed_columns)
    #print(f"new_seed: {new_seed}")
    seeds = pd.concat([seeds, new_seed], ignore_index=True)
    return

def add_new_seed(seed, range):
    global new_seeds
    #add the seed and range to the df of seeds
    new_seed = pd.DataFrame([[seed, range]], columns=seed_columns)
    #print(f"new_seed: {new_seed}")
    new_seeds = pd.concat([seeds, new_seed], ignore_index=True)
    return

def get_lowest_seed_value(df):
    return df['seed'].iloc[0]


def calc_translation_step2(df, seeds):
    k=0
    #print(df)
    #iterate through the seeds
    for index, row in seeds.iterrows():
        #print(f"seeds: {seeds}")
        #print(f"new_seeds: {new_seeds}")
        #print(f"row: {row}")
        seed = row['seed']
        seed_range = row['range']
        seed_range_end = seed + seed_range -1
        #print(f"\n\nseed, seed_range_end:\t\t\t {seed}, {seed_range_end}")
        #print(df)
        # Find the index of the first row where the value in the column is less than the given number
        index = (df['range_end'] >= seed).idxmax()
        #print(f"index: {index}, range_start, range_end:\t {df.loc[index, 'source']}, {df.loc[index, 'range_end']}")
        steps_in = seed - df.loc[index, 'source'] #negative if before lowest source

        if index == 0: #check for the case that it is larger than the last range
            #print("index is 0")
            highest_index = df.index.max()
            #print(f"highest_index: {highest_index}")
            if seed > df.loc[highest_index, 'range_end']:
                #print("seed is larger than last range translated to same seed")
                add_new_seed(seed, seed_range)
                k+=1
                continue

        if seed < df.loc[index, 'source']:
            # print(f"index: {index}")
            # print("seed is smaller than the source - index 0 indicates before first source")
            # print("we are in between bands, this index gives higher source than seed")
            if seed_range_end < df.loc[index, 'source']:
                #print("falls within gap - translate to same seed")
                add_new_seed(seed, seed_range)
                k+=1
                continue
            elif seed_range_end >= df.loc[index, 'source']:
                #print("Larger than gap - split up")
                add_new_seed(seed, df.loc[index, 'source']-seed) #add what fits to new seed
                add_seed(df.loc[index, 'source'], seed + seed_range -df.loc[index, 'source']) #add the rest to the seeds
                k+=1
                continue

        #Does the seed range fall in the range of the row?
        if seed_range_end > df.loc[index, 'range_end']:
            #print("Larger than range range - split up")
            add_new_seed(seed, df.loc[index, 'range_end']-seed+1) #add what fits to new seed
            add_seed(df.loc[index, 'range_end']+1, seed_range_end-(df.loc[index, 'range_end'])) #add the rest to the seeds
            k+=1
            continue
            #if the range is bigger than the range of the row, add the seed to the new seeds
        elif seed_range_end <= df.loc[index, 'range_end']:
            #print("falls within range - translate")
            #new_seed_range = row['range_length']-steps_in
            add_new_seed(df.loc[index,'destination'] + steps_in, seed_range) #translate the starting seed to the new seed
            k+=1
            continue

        print("error")
        exit()
    
    print(f"Lenght of seeds: {len(seeds)}")
    #print(f"seeds: {seed_list}")
    print(f"new_seeds: {new_seeds}")



        


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
        for index, row in df.iterrows():
            print(f"row_source: {row['source']} and row_range: {row['range_length']}")
            print(f"seed: {seed} and seed_range: {seed_range}")
            if translated:
                break
            print(f"index: {index}")
            #case 1: seed is below smallest source and range does not cover source (add to handle case going into first band)
            if seed < row['source'] and seed + seed_range <= row['source'] and index == 0:
                print("case1")
                add_new_seed(seed, seed_range)
                translated = True
                k+=1
            #case 2: seed is less than smallest source but range covers source
            elif seed < row['source'] and seed + seed_range > row['source'] and index == 0: #if start of seed not in range but range covers source
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
            else :
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
            #create a dataframe for the seed list where every even number is the seed and every odd number is the range
            seeds = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
            seeds = pd.DataFrame(seeds, columns=seed_columns)
            seeds.sort_values(by='seed', inplace=True)
            df = pd.DataFrame(columns=columns)
        elif line[0].isdigit():
            #print(i)
            line = parse_numbers(line.split(' '))
            #print(line)

            #create a dataframe and read in the digit lines           
            new_row = pd.DataFrame([line], columns=df.columns)
            df = pd.concat([df, new_row], ignore_index=True)
            #calculate a new column in the df as source + range_length
            #print(df)
        elif line[0].isalpha():
            df['range_end'] = df['source'] + df['range_length'] -1
            df.sort_values(by='source', inplace=True)
            df.reset_index(drop=True, inplace=True)
            conversion_steps.append(df)
            #print(f"conversion_steps: {line}")
            df = pd.DataFrame(columns=columns)
        else:
            print("error")  
    df['range_end'] = df['source'] + df['range_length'] -1
    conversion_steps.append(df)


### all maps read in. Now to convert the seeds    
print(f"number of conversion_steps: {len(conversion_steps)}")   
print(f"first conversion_step: {conversion_steps[1]}") 
print(f"seeds: {seeds}")


stosp = 0
for step in conversion_steps:
#step = conversion_steps[1]
    #if step is non empty df
    if not step.empty:
        print(f"\n\nNEW STEP seeds: {seeds}")
        print(f"step: {step}")       
        calc_translation_step2(step, seeds)
        print(f"\n\nnew_seeds: {new_seeds}")
        #seed_list = new_seed_list
        seeds = new_seeds.copy()
        #sort seed_list by source

        new_seed_list = []
        stosp+=1
        print(f"\n\nLen of seeds {len(seeds)} AFTER STEP new seeds: {seeds}")




print(f"seeds: {seeds}")
#print the lowest seed value
seeds.sort_values(by='seed', inplace=True)
#print seed of first row
print(f"min location: {seeds['seed'].iloc[0]}")



        
#    for seed in seeds:
                  
        
     
     #   elif line[0] in 'abcdefghijklmnopqrstuvwxyz':
            #if line starts with seeds
      #      j=0
            




