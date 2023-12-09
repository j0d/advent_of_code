

# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456

import pandas as pd

path = '7/test_input.txt'
path = '7/input.txt'
#path = '7/test_input2.txt'

def find_multiple_occurrences(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Finding characters that appear more than once
    multiple_occurrences = [char for char, count in char_count.items() if count > 1]
    # finding the count of such multiple occurence characters
    multiple_occurrences_count = [count for char, count in char_count.items() if count > 1]
    if multiple_occurrences_count == []:
        multiple_occurrences_count = [0]
    return multiple_occurrences, multiple_occurrences_count

# Define the custom order
order = "AKQJT98765432"
# Create a dictionary mapping each character to its custom rank
order_dict = {char: i for i, char in enumerate(order)}

def get_custom_rank(s, order_dict=order_dict, max_length=5):
    # Calculate the rank of the string based on the custom order
    rank = 0
    for i, char in enumerate(s):
        char_rank = order_dict.get(char, len(order_dict))
        rank += char_rank * (len(order_dict) ** (max_length - i - 1))
    return rank

def high_card_value(hand):
    #assign a hex value to each card where A=14, K=13, Q=12, J=11, T=10, 9=9, 8=8, 7=7, 6=6, 5=5, 4=4, 3=3, 2=2
    hand = hand.replace('A','e')
    hand = hand.replace('K','d')
    hand = hand.replace('Q','c')
    hand = hand.replace('J','1') #Joker
    hand = hand.replace('T','a')
    hand = hand.replace('T','a')
    
    #create a hex number for each card by concatenating the hex values
    #print(hand)
    #print(int(hand, 16))
    return hand


with open(path, 'r') as file:
    lines = [line for line in file if line.strip()]
    for i in range(len(lines)):
        line = lines[i].strip('\n')
        lines[i] = line.split(' ')
        print(line)        

#insert lines into a df with columns: hand, bid
df = pd.DataFrame(lines,columns=['hand', 'bid'])
#insert lines into a df with columns: hand, bid
print(lines)
print(df)

#cast bid column to int
df['bid'] = df['bid'].astype('int64')

#add strength column to df
# add two columns to the dataframe strength and rank
df['strength'] = 0
df['strength'] = df['strength'].astype('int64')
df['hexrank'] = 0
df['hexrank'] = df['hexrank'].astype('int64')
df['rank'] = 0
df['rank'] = df['rank'].astype('int64')
df['totalrank'] = 0
df['totalrank'] = df['totalrank'].astype('int64')
df['winning'] = 0
df['winning'] = df['winning'].astype('int64')

print(df)


#iterate through the hands in the df
for index, row in df.iterrows(): 
    joker_count = 0
    print(row)
    (multiple_occurencies, counts) = find_multiple_occurrences(row['hand'])
    print(multiple_occurencies)
    print(counts)
    #print(type(counts))
    highest_count = max(counts)
    hex_hand = high_card_value(row['hand'])
    #print(f"hex_value: {hex_hand}")
    df.at[index, 'rank'] = int(hex_hand,16)
    df.at[index, 'hexrank'] = hex_hand

    if 'J' in row['hand']:
        if 'J' in multiple_occurencies:
            joker_count = counts[multiple_occurencies.index('J')]
        else:
            joker_count = 1

        print('joker')
        print(f"joker_count: {joker_count}")


    if highest_count == 5: #five of a kind
        print('five of a kind')
        df.at[index, 'strength'] = 7
    elif highest_count == 4: #four of a kind
        print('four of a kind')
        df.at[index, 'strength'] = 6
    elif highest_count == 3: #three of a kind AND
        print('three of a kind')
        if len(multiple_occurencies) == 2: #full house
            df.at[index, 'strength'] = 5
        else:   #three of a kind ONLY
            df.at[index, 'strength'] = 4
    elif len(multiple_occurencies) == 2: #two pair
        print('two pair')
        df.at[index, 'strength'] = 3
    elif len(multiple_occurencies) == 1: #one pair
        print('one pair')
        df.at[index, 'strength'] = 2
    else: #high card
        print('high card')
        df.at[index, 'strength'] = 1

    #iterate through the jokers :)
    
    #go through the cases where there is a joker
    if joker_count == 5:
        print("five jokers")
        #already correct.
    elif joker_count == 4:
        #makes five of a kind
        df.at[index, 'strength'] = 7
    elif joker_count == 3:
        if len(multiple_occurencies) == 2: 
            #five of a kind
            df.at[index, 'strength'] = 7
        elif len(multiple_occurencies) == 1:
            #makes four of a kind
            df.at[index, 'strength'] = 6
        else:
            print('error')
            exit()
    elif joker_count == 2:
        if highest_count == 3:  #2 jokers and three of a kind
            #makes five of a kind
            df.at[index, 'strength'] = 7
        elif len(multiple_occurencies) == 2: #2 jokers and two pair
            #makes four of a kind
            df.at[index, 'strength'] = 6
        elif len(multiple_occurencies) == 1: #only jokers
            #makes three of a kind
            df.at[index, 'strength'] = 4
        else:
            print('error')
            exit()
    elif joker_count == 1: 
        if highest_count == 4:
            #makes five of a kind
            df.at[index, 'strength'] = 7
        elif highest_count == 3:
            #makes four of a kind
            df.at[index, 'strength'] = 6
        elif len(multiple_occurencies) == 2:
            #makes full house
            df.at[index, 'strength'] = 5
        elif len(multiple_occurencies) == 1:
            #makes three of a kind
            df.at[index, 'strength'] = 4
        elif len(multiple_occurencies) == 0:
            #makes one pair
            df.at[index, 'strength'] = 2


    print(df)




      




#sort df after strength ascending and rank descending
df = df.sort_values(by=['strength', 'rank'], ascending=True)
print(df)

#add totalrank column to df with number 1 to len of df rows
df['totalrank'] = range(1, len(df) + 1)
print(df)

#calc winning column as the product of totalrank and bid
df['winning'] = df['totalrank'] * df['bid']

print(df)

#sum the winning column as total winnings
total_winnings = df['winning'].sum()
print(f"total_winnings: {total_winnings}")  

