import pandas as pd

path = '5/test_input.txt'
path = '5/input.txt'
#answer? 50855035
#This program now runs and total ranges stays the same. But the answer is wrong. Some translation must be wrong...
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

def add_seed(seed, range):
    global seeds
    #add the seed and range to the df of seeds
    new_seed = pd.DataFrame([[seed, range]], columns=seed_columns)
    print(f"new_seed in seeds: {new_seed}")
    seeds = pd.concat([seeds, new_seed], ignore_index=True)
    print(f"seeds in add_seed: {seeds}")
    return

def add_new_seed(seed, range):
    global new_seeds
    #add the seed and range to the df of new_seeds
    new_seed = pd.DataFrame([[seed, range]], columns=seed_columns)
    print(f"new_seed in new_seeds: {new_seed['seed'].iloc[0]}, range {new_seed['range'].iloc[0]}, seed_range_end: {new_seed['range'].iloc[0]+new_seed['seed'].iloc[0]-1}")
    new_seeds = pd.concat([new_seeds, new_seed], ignore_index=True)
    return

def get_lowest_seed_value(df):
    return df['seed'].iloc[0]

def calc_translation_step(df):
    global seeds
    k=0
    #print(df)
    #iterate through the seeds
    while k < len(seeds):
        row = seeds.iloc[k]
        print(f"seeds (start of loop): {seeds}")
        print(f"len(seeds): {len(seeds)}")
        print(f"new_seeds: {new_seeds}")
        print(f"row: {row}")
        seed = row['seed']
        seed_range = row['range']
        seed_range_end = seed + seed_range -1
        print(f"\n\nseed, seed_range, seed_range_end:\t\t\t {seed}, {seed_range},{seed_range_end}")
        #print(df)
        # Find the index of the first row where the value in the column is less than the given number
        index = (df['range_end'] >= seed).idxmax()
        print(f"index: {index}, range_start, range_end:\t {df.loc[index, 'source']}, {df.loc[index, 'range_end']}")
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
            if index == 0:
                print("seed is smaller than the source - index 0 indicates before first source")
            elif index > 0:
                print("seed is smaller than the source we are in between bands")
            if seed_range_end < df.loc[index, 'source']:
                print("falls within gap - translate to same seed")
                add_new_seed(seed, seed_range)
                k+=1
                continue
            elif seed_range_end >= df.loc[index, 'source']:  #need to split logic between index 0 and index > 0 or?
                print("Larger than gap - split up")
                add_new_seed(seed, df.loc[index, 'source']-seed) #add what fits to new seed (correct regardless of index)
                add_seed(df.loc[index, 'source'], seed + seed_range -df.loc[index, 'source']) #add the rest to the seeds
                k+=1
                continue

        #Does the seed range fall in the range of the row?
        if seed_range_end <= df.loc[index, 'range_end']:
            print("NORMAL falls within range - translate")
            #new_seed_range = row['range_length']-steps_in
            add_new_seed(df.loc[index,'destination'] + steps_in, seed_range) #translate the starting seed to the new seed
            k+=1
            continue
        elif seed_range_end > df.loc[index, 'range_end']:
            print("NORMAL - Larger than range range - split up")
            within_range = df.loc[index, 'range_end'] - seed +1
            add_new_seed(df.loc[index,'destination'] + steps_in, within_range ) #translate the seed that fits to the new seed
            add_seed(df.loc[index, 'range_end']+1, seed_range - within_range) #add what's outside back to seeds
            k+=1
            continue
            #if the range is bigger than the range of the row, add the seed to the new seeds
        

        print("error")
        exit()
    
    print(f"Lenght of seeds: {len(seeds)}")
    #print(f"seeds: {seed_list}")
    print(f"new_seeds: {new_seeds}")



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
            seeds.reset_index(drop=True, inplace=True)
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
sum_of_ranges_at_start = seeds['range'].sum()

stosp = 0
for step in conversion_steps:
#step = conversion_steps[1]
    #if step is non empty df
    if not step.empty:
        print(f"\n\nNEW STEP seeds: {seeds}")
        print(f"\n\nNEW STEP new seeds: {new_seeds}")
        print(f"step: {step}")       

        #print the sum of ranges in seeds
        print(f"sum of ranges in seeds: {seeds['range'].sum()}")

        calc_translation_step(step)
        print(f"\n\nnew_seeds: {new_seeds}")
        print(f"sum of ranges in new_seeds: {new_seeds['range'].sum()}")
        #seed_list = new_seed_list
        seeds = new_seeds.copy()
        seeds.sort_values(by='seed', inplace=True)
        seeds.reset_index(drop=True, inplace=True)
        #sort seed_list by source

        new_seeds = pd.DataFrame(columns=seed_columns)
        stosp+=1
        print(f"\n\nLen of seeds {len(seeds)} AFTER STEP new seeds: {seeds}")




print(f"seeds: {seeds}")
#print the lowest seed value
seeds.sort_values(by='seed', inplace=True)
seeds.reset_index(drop=True, inplace=True)
print(f"sum of ranges in seeds end: {seeds['range'].sum()}")
print(f"sum of ranges at start: {sum_of_ranges_at_start}")
#print seed of first row
print(f"min location: {seeds['seed'].iloc[0]}")



        
#    for seed in seeds:
                  
        
     
     #   elif line[0] in 'abcdefghijklmnopqrstuvwxyz':
            #if line starts with seeds
      #      j=0
            




