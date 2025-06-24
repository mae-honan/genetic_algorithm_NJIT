import random
#target phrase
target="Sisters 1st"

class Phrase:
    def __init__(self):
        self.characters=[]
        #create a random string same length as target string
        for i in range(len(target)):
            #creates random guess for phrase
            character=chr(random.choice(range(32,127)))
            #appends random character to empty list
            self.characters.append(character)
            #initial fitness declared as 0
        
    def getContents(self):
        return ''.join(self.characters)
    #"Hello" -> ['H', 'e', ......]

    def getFitness(self):
        #1.count how many characters match target phrase
        #2.if target [0]('H') = self.character[0] -> add +1 to fitness counter
        #3.save and return self.fitness
        self.fitness=0
        for i in range(len(target)):
            if self.characters[i]==target[i]:
                self.fitness +=1

              

    def crossOver(self, partner):
        child=Phrase()
        #1.create a new phrase object by mixing characters from self and partner
        
        for i in range(len(self.characters)):
            if random.random() <0.5:
                child.characters[i]=self.characters[i]
            else:
                 child.characters[i] = partner.characters[i]
                #child [i] will get the partner charcter
        return child 
        
    #randomly changes some letters
    def mutate(self):
        for i in range(len(self.characters)):
            if random.random() <0.01:
             #change character to a random character
                self.characters[i]=chr(random.choice(range(32, 127)))







