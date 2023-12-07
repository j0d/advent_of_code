path = '2/test_input2.txt'
path = '2/input.txt'


#define a class named games that has three ints called blue, red, and green
class games:
    def __init__(self, blue, red, green):
        self.blue = blue
        self.red = red
        self.green = green

    def impossible(self):
        if self.blue > 14 or self.red > 12 or self.green > 13:
            print("impossible")
            return True
        else:
            print("possible")
            return False
        
    def max(self,blue,red,green):
        if blue > self.blue:
            self.blue = blue
        if red > self.red:
            self.red = red
        if green > self.green:  
            self.green = green
        return
    
    def print(self):
        print("blue: " + str(self.blue) + " red: " + str(self.red) + " green: " + str(self.green))
        return
        

    def __str__(self):
        return "blue: " + str(self.blue) + " red: " + str(self.red) + " green: " + str(self.green)

    def __repr__(self):
        return "blue: " + str(self.blue) + " red: " + str(self.red) + " green: " + str(self.green)

    def __eq__(self, other):
        return self.blue == other.blue and self.red == other.red and self.green == other.green

    def __hash__(self):
        return hash((self.blue, self.red, self.green))

    def __lt__(self, other):
        return self.blue < other.blue and self.red < other.red and self.green < other.green

    def __gt__(self, other):
        return self.blue > other.blue and self.red > other.red and self.green > other.green

    def __le__(self, other):
        return self.blue <= other.blue and self.red <= other.red and self.green <= other.green

    def __ge__(self, other):
        return self.blue >= other.blue and self.red >= other.red and self.green >= other.green

    def __ne__(self, other):
        return self.blue != other.blue or self.red != other.red or self.green != other.green

    def __add__(self, other):
        return games(self.blue + other.blue, self.red + other.red, self.green + other.green)

    def __sub__(self, other):
        return games(self.blue - other.blue, self.red - other.red, self.green - other.green)

    def __mul__(self, other):
        return games(self.blue * other.blue, self.red * other.red, self.green * other.green)

    def __truediv__(self, other):
        return games(self.blue / other.blue, self.red / other.red, self.green / other.green)

    def __floordiv__(self, other):
        return games(self.blue // other.blue, self.red // other.red, self.green // other.green)

    def __mod__(self, other):
        return games(self.blue % other.blue, self.red % other.red, self.green % other.green)

    def __pow__(self, other):
        return games(self.blue) ** other.blue, games(self.red) ** other.red, games(self.green) ** other.green




#read input.txt file
with open(path) as f:
    #read each line
    lines = f.readlines()

array_of_games = []
total_games_prod_sum = 0

for line in lines:
    #split line into a game and populate array_of_games
    line = line.split(';')
    #get the number after 'Game:' in first string
    num_of_game = line[0].split(':')[0].split(' ')[1]
    line[0] = line[0].split(':')[1]
    impossible_count = 0

    #iterate through each game of the splitted line array (now array of games for game #)
    game = games(0,0,0)
    for i in range(0,len(line)):
        print(line[i])
        reveals = line[i].split(',')
        #if the string contains the word 'blue'
        blue = 0
        red = 0
        green = 0    
        
        for reveal in reveals:
            #print(reveal)
            if 'blue' in reveal:
                #get the number before 'blue:' in the string
                blue = reveal.split(' ')[1]
                #print(blue)
            #if the string contains the word 'red'
            if 'red' in reveal:
                #get the number after 'red:' in the string
                red = reveal.split(' ')[1]
                #print(red)
            #if the string contains the word 'green'
            if 'green' in reveal:
                #get the number after 'green:' in the string
                green = reveal.split(' ')[1]
                #print(green)

            #create a game object with the numbers and add it to array_of_games
        print(blue, red, green)
        game.max(int(blue), int(red), int(green))

    game.print()   
    total_games_prod_sum += game.blue * game.red * game.green

print(total_games_prod_sum)
#            array_of_games.append(game)

    
    #game = games(int(num_of_game), int(line[2]), int(line[4]))
    #array_of_games.append(game)
    #print(game)

#print(lines)
