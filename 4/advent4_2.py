path = '4/test_input.txt'
path = '4/input.txt'

#define a class named card that has two attributes: its number, it's winning numbers and its number of copies
class card:
    def __init__(self, number, num_of_winning_numbers, copies):
        self.number = number
        self.num_of_winning_numbers = num_of_winning_numbers
        self.copies = copies

def parse_numbers(list_of_strings):
    print(list_of_strings)
    numbers = []
    for string in list_of_strings:
        #print(string)
        if string.isdigit():
            numbers.append(int(string))
    return numbers

#read input.txt file
with open(path) as f:
    #read each line
    lines = f.readlines()

array_of_cards = []
points = 0

for line in lines:
    #split line into a game and populate array_of_games
    #strip of newline if it exists
    line = line.strip('\n')
    line = line.split(':')
    print(line[0])
    cardnum = line[0].split(' ')[-1]
    print(cardnum)
   
    numbers = line[1].split('|')
    
    winning_numbers = parse_numbers(numbers[0].split(' '))
    card_numbers = parse_numbers(numbers[1].split(' '))
    
    #create sets of card_number and winning_numbers and find intersection
    card_numbers_set = set(card_numbers)
    winning_numbers_set = set(winning_numbers)
    print(card_numbers_set)
    print(winning_numbers_set)
    intersection = card_numbers_set.intersection(winning_numbers_set)
    print(intersection)

    #count to number of matches
    num_of_winning_numbers = len(intersection)
    print(f"num_of_winning_numbers: {num_of_winning_numbers}")
    
    array_of_cards.append(card(cardnum, num_of_winning_numbers, 1))


i=0
for i in range(0,len(array_of_cards)):
    card = array_of_cards[i]
    j=i+1
    k=0
    #print(f"card: {card.number}, num_of_winning_numbers: {card.num_of_winning_numbers}, copies: {card.copies}")
    for k in range(0,card.copies):
        j=i+1
        for j in range(j,j+card.num_of_winning_numbers):
            array_of_cards[j].copies += 1


total_num_of_cards = 0
for card in array_of_cards:
    print(f"card: {card.number}, num_of_winning_numbers: {card.num_of_winning_numbers}, copies: {card.copies}")
    total_num_of_cards += card.copies
     
print(total_num_of_cards)