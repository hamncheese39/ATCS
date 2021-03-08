import random
lastNames = ['Parsons', 'Wright', 'Norton', 'Cameron', 'Fritz', 'Page','Braun','Kline','Gibson','Browning','Bray','Trujillo', 'Benedis-Grab', 'Field', 'Harrell']


class Stat:
#has the name and level of each stat –– easy to add more if necessary
    def __init__(self, level, name):
        self.level = level
        self.name = name
#updates the stat by given percentage, and prints out the change
    def update(self, percentChange):
        if percentChange > 0:
            print(self.name + ": +" + str(percentChange) + "%")
        else:
            print(self.name + ": " + str(percentChange) + "%")
                
        self.level =  int(self.level*((percentChange/100) + 1))

class Dog:
#contains all stat classes and information about the dog
    
    def __init__(self, firstName, lastName, location, roomType, urination, defecation, energy, anger, hunger, thirst):
        self.firstName = firstName
        self.lastName = lastName
        self.location = location
        self.roomType = roomType
        self.urination = Stat(urination, "Urination")
        self.defecation = Stat(defecation, "Defecation")
        self.energy = Stat(energy, "Energy")
        self.anger = Stat(anger, "Anger")
        self.hunger = Stat(hunger, "Hunger")
        self.thirst = Stat(thirst, "Thirst")
        self.stats = [self.urination, self.defecation, self.energy, self.anger, self.hunger, self.thirst]

    def showStats(self):
    #shows the stats in a visually pleasing way
        print("Urination  Defecation  Energy  Anger  Hunger  Thirst")
        print("   ", self.urination.level, "       ", self.defecation.level, "      ",
              self.energy.level, "   ", self.anger.level, "    ", self.hunger.level, "    ", self.thirst.level)

        
def intro():
    print("Welcome to Dog Days")
    print("In this game, you will go through the world as a dog")
    print("Don't let any of your stats get above 100!")
    print("For each turn, input the number corresponding to the action you would like to make")
    name = input("What would you like your name to be? ")
    lastName = random.choice(lastNames)
    print("You were adopted by the", lastName, "family")
    print()
    return [name, lastName]

name = intro()
dog = Dog(name[0], name[1], "Parent's Bedroom", "Bedroom", 90, 75, 40, 20, 30, 40)

#my "parser" function which takes a list of actions and asks the user to input a number to determine which action they want
def getAction(options):
    x = 1
    for option in options:
        print("[" + str(x) + "] " + str(option)) 
        x += 1

    gotInput = False
    while not gotInput:
        choiceNum = input("Which action would you like to make? ")
        if choiceNum.isdigit() and int(choiceNum) <= len(options):
            choiceNum = int(choiceNum)
            gotInput=  True
        else:
            print("Please enter a valid number")
            
        
    choice = options[choiceNum-1]
    return choice

def sleep():
#sleep "scene"
    print("You curl up in a cozy little corner of the", dog.location,
          "to catch some Zsss, hopefully you dream about a squirrel. You must be really bored")
    dog.urination.update(30)
    dog.defecation.update(15)
    dog.energy.update(1/3)
    dog.anger.update(-20)
    dog.hunger.update(20)
    dog.thirst.update(20)


def waterBowl():
#water bowl scene
    print("Thirst:", dog.thirst.level," Urination:", dog.urination.level)
    print("[1] Drink")
    print("[2] Don't drink")
    drinkAction = input()
    if drinkAction == "1":
        print("That was refreshing! Hopefully I get a walk soon though because I have to pee a little more now")
        dog.thirst.update(-70)
        dog.urination.update(30)
    else:
        if dog.urination.level >= 77:
            print("Good choice! You would have died from a urinary infection if you drank anymore")
    print("Off you go, back to your bed in the living room")
    dog.location = "Living Room"

def goOut():
#asked to go out scene
    print("Energy:", dog.energy.level," Urination:", dog.urination.level, "Defecation:", dog.defecation.level)
    print("[1] Go out")
    print("[2] Don't go out")
    if input() == "1":
        print("You run to the door and prepare to get your leash on.", '"Lets Go!"')
        if dog.defecation.level > 50:
            dog.defecation.update(-75)
        if dog.urination.level > 20:
            dog.urination.update(-75)
        print('"Thanks parent. Im wiped now though"')
        dog.anger.update(-20)
        dog.energy.update(-40)
        dog.location = "Living Room"
        dog.roomType = "Room"
    else:
        print("You resist. The parent's must not want to go out either because they give up easily")
        dog.anger.update(-10)

    
def checkBowl():
#check bowl scene, etc.
    print("You walk up to the kitchen where you know your trusty bowl is")
    dog.location = "Kitchen"
    print('"Will there be anything this time? Only fate will tell"')
    
    if random.random() < .8:
        print("Oh no! It's true! Nothing's there. My parents don't love me")
        dog.anger.update(25)
        print("Just looking at my reflection in the empty bowl makes me hungrier...")
        dog.hunger.update(15)
        print("At least there's some water")
        waterBowl()
        

    else:
        print('"Lookie here! Is this a trick?" Before you can answer that question,')
        print("you are snout deep in a bowl full of rock-like kibble with some pieces of actual good food on top")
        print('"That was delicious. But where did it all go..."')

        dog.anger.update(-75)
        dog.energy.update(40)
        dog.hunger.update(-60)
        dog.thirst.update(30)

        print('"Golly! I am a thirsty pup!" "Should I get some agua?"')
        waterBowl()
        
    

def begWalk():
    print("You go to the nearest adult and put on your best puppy eyes")
    print("'They've got to take me out, right?' I have to pee, and I'm just oh so cute")
    print()
    if random.random() < .8:
        print('Parent: "Okji,', dog.firstName, 'we jhg goong oot now, park shgs ahA RAT, hasgi sedl walk TREAT"')
        print('"OMG! Yes treat, park, rat, my name! We must be going out"')
        if dog.defecation.level > 50:
            dog.defecation.update(-75)
        if dog.urination.level > 20:
            dog.urination.update(-75)
        dog.anger.update(-20)
        dog.energy.update(-40)
        dog.location = "Living Room"
    else:
        print('Parent: "oghhh ugh, come', dog.firstName, 'come here plaesg, awww triad lanzy, aww sowwy')
        print('"No, I dont want to "come here" I want you to take me out!')
        dog.anger.update(10)
        if dog.anger.level > 50:               
            print("[1] Bark")
            print("[2] Cuddle up with your parent")
            begWalkAction = input()
            if begWalkAction == "1":
                print("All right, here goes it. Hopefully they don't get mad")
                if random.random() < .67:
                    print('Parent: "', dog.firstName, ' Im come ing, wayt thur go sfhs Leash, I fhs ajd Treat"')
                    print('"Yes! we are going out!"')
                    if dog.defecation.level > 50:
                        dog.defecation.update(-75)
                    if dog.urination.level > 20:
                        dog.urination.update(-75)
                    dog.anger.update(-30)
                    dog.energy.update(-40)
                    dog.location = "Living Room"
                else:
                    print('Parent: "Ugh oghugh pleeas come, tirsd pls le me sfuhf now"')
                    print('"Aw shucks, guess I have to wait now, I dislike my owners sometimes" :(')
                    dog.anger.update(30)
                    
        else:
            print("You are not angry enough to bark at them")
            print("Time to cuddle up!")
            dog.anger.update(50)
            dog.location = "Parent's Bedroom"
            
        
        
def begFood():
    print("You go to the nearest adult and put on your best puppy eyes")
    print('"God I am hungry! Why dont they feed me more! Im a growing dog!"')
    if dog.hunger.level > 90 or random.random() < .6:
        print("The parent walks toward the sacred room full of food")
        print('"Here we go!" *lip licking intensifies*')
        print('Parent: "Good hgkd! Here dhg go! Tasty enjoy"')
        dog.anger.update(-75)
        dog.energy.update(40)
        dog.hunger.update(-60)
        dog.thirst.update(30)
        print('"That was delicious! Even though it is the same food everytime"')
        print('"Now I am a bit thirstier"')
        waterBowl()
        
    else:
        print('Parent: "Go out?? wand tas go out? park, rat"')
        print('"No! Im hungry, I want food!"')
        print("You slink away back to your bed, much angrier and hungrier than before")
        dog.anger.update(30)
        dog.hunger.update(15)
        dog.location = "Living Room"

def window():
    print("My god, you are bored")
    print("Or are you just too lazy to go outside even though you want to?")
    print("Either way looking outside makes you want to go out more")
    dog.energy.update(30)
    print('"Oh look! Here comes parent. I guess they think I want to go out..."')
    goOut()
    

def move():
# move rooms scene
    rooms = ["Kitchen", "Living Room", "Parent's Bedroom", "Bathroom", "Sibling's Bedroom"]
    print("Current Location:", dog.location)
    print("Let's go explore!")
    print("You can move to:")
    roomOptions = []
    for room in rooms:
        if room != dog.location:
            roomOptions.append(room)
    newRoom = getAction(roomOptions)
    dog.location = newRoom
    if dog.location == "Kitchen":
        print("You walk past your mother and see that she is cooking")
        print('"Are there any scraps for me?" You check quickly without drawing attention')
        if random.random() < .5:
            print("Oh wow there are a couple of chicken and lettuce just for you!")
            dog.hunger.update(-30)
            dog.defecation.update(10)
            dog.anger.update(-10)
        else:
            print("Nope nothing here for me. Guess I'll just wait around here to see if any other scraps drop")
        
    elif dog.location == "Living Room":
        print("You see no one here but some peace and quiet in an open space here will be nice")
        print("So you lie down and consider questions like: Why does every day feel the same?")
        dog.anger.update(-20)
    elif dog.location == "Parent's Bedroom":
        print("Your dad is lying down, maybe taking a nap or on the phone")
        if dog.energy.level < 40:
            print("So you go and curl up next to him")
            dog.anger.update(-10)
            dog.energy.update(10)
        else:
            print("Energy:", dog.energy.level)
            print("[1] Bark at him to get up and play with you")
            print("[2] Curl up next to him and get some pets")
            if input() == "1":
                print('"BARK! BARK! bark RUFF!"')
                print("Your dad - Greg", dog.lastName, "- gets up and starts looking for a ball")
                print("You wrestle, run, jump, hide, tug, and pant for 20 minutes straight")
                print('"Phew that was exhausting"')
                dog.energy.update(-60)
                dog.anger.update(-10)
                dog.hunger.update(20)
                dog.thirst.update(30)
                print("Let's check for water")
                waterBowl()
    elif dog.location == "Bathroom":
        print("Someone left the door to the bathroom open so it was easy to get in stealthily")
        print("You have some pretty great options. Do you want to:")
        toiletAct = getAction(["Tear up the garbage", "Drink the toilet water", "Leave"])
        if toiletAct == "Tear up the garbage":
            print("There's a couple tissues and interesting things in the trash can")
            print("After sniffing around and leaving a mess, you quickly regret everything")
            print("So you run out of the bathroom and hide, hoping that your parents don't blame you fro the mess")
            print("You're afraid to move and you already lost all you energy")
            dog.location = "Living Room"
            dog.energy.update(-30)
        elif toiletAct == "Drink the toilet water":
            print("There's an interesting smell coming from the big bowl in the middle")
            print("You're thirsty enough to at least give it a taste")
            print('*lick, lick* "Yuck"')
            print("You throw up on the ground, that was disgusting")
            dog.energy.update(-50)
            dog.hunger.update(-20)
            print("You rush to your parent's bedroom to show them")
            dog.location = "Parent's Bedroom"

        else:
            print("Good choice! there's nothing good to do in there anyways")
            dog.location = "Living Room"

    elif dog.location == "Sibling's Bedroom":
        print("I never really liked this sibling")
        if dog.urination.level >= 65:
            print("You need to pee, so you decide to just do it here")
            dog.urination.update(-75)
        if dog.defecation.level >= 80:
            print("You need to poo, so you do it here as well")
            print("'This'll show him'")
            dog.defecation.update(-75)
        if dog.energy.level >= 40:
            print("Let's run around and mess stuff up!")
            dog.energy.update(-30)
            print("Phew, you're tired")
        print("For good or for bad you curl up, on their bed until they get back")
        dog.location = "Sibling's Bedroom"
        

def main():
# main "engine"
    dayNum = 1
    alive = True
    while alive:
        print("Day:", dayNum)
        for timeNum in range(8):
            hour = (timeNum*2+8)%12
            if hour == 0:
                hour = 12
            if timeNum < 3:
                print("Time: " + str(hour) + ":00am")
            else:
                print("Time: " + str(hour) + ":00pm")
            dog.showStats()
            actionOptions = []
            if dog.energy.level <= 60:
                actionOptions.append("Sleep")
            if dog.hunger.level > 50 or dog.thirst.level > 70:
                 actionOptions.append("Check bowl")
            if dog.hunger.level > 65:
                actionOptions.append("Beg for food")
            if dog.energy.level >= 60 or dog.urination.level >= 60 or dog.defecation.level >= 75:
                actionOptions.append("Beg for walk")
            if dog.location == "Living Room":
                actionOptions.append("Look out window")
            actionOptions.append("Move rooms")

            action = getAction(actionOptions)
            actionsDict[action]()

            print()
            dog.urination.update(10)
            dog.defecation.update(10)
    
            dog.energy.update(10)
            dog.anger.update(10)

            dog.hunger.update(20)
            dog.thirst.update(30)
            
            print()
            for stat in dog.stats:
                if stat.level > 100:
                    alive = False
                    deathStat = stat

            if alive == False:
                break

        dayNum += 1
#ending scene
    print("You died because your", deathStat.name, "stat reached a level of", deathStat.level)
    print("   " + str("_"*(len(dog.firstName) + 4)) + "   ")
    print("  /" + str(" "*(len(dog.firstName) + 4)) + "\  ")
    print(" / RIP " + str(dog.firstName) + " \ ")
    print("/__" + str("_"*(len(dog.firstName) + 4)) + "__\ ")
    print("|  " + str(" "*(len(dog.firstName) + 4)) + "  |")
    print("|  " + str(" "*(len(dog.firstName) + 4)) + "  |")
    print("|  " + str(" "*(len(dog.firstName) + 4)) + "  |")
    print("|  " + str(" "*(len(dog.firstName) + 4)) + "  |")
    print("|__" + str("_"*(len(dog.firstName) + 4)) + "__|")
    print(str("\|/"*((len(dog.firstName) + 10)//3)))

actionsDict = {"Sleep": sleep, "Check bowl": checkBowl,
               "Beg for walk": begWalk, "Beg for food": begFood,
               "Look out window": window, "Move rooms": move}

main()
