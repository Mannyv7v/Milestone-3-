#Emmanuel velazquez
#Chapter 1 of video game involves speaking to locals, and the hooded figure to progres the game

def Get_Character_Name():
    character_name = input("What is your name?")    #User will be refered as this name for the rest of the game.
    return character_name

def Hooded_Figure_Intro(character_name):
    print("Welcome!",character_name, "A hooded figure approaches you.")
    print("Hooded Figure: Greetings traveler! You are the chosen one destined to break the curse on ELdoria")
    print("Hooded Figure: I am known as the guide, what is your name.", character_name,"?")


global npcName
global response
def talk_to_locals():
    print("You decide to talk to locals in Eldoria to gather info on the elden ring")
    response = ["You seek the ring... eh? Long ago, a beast was owner of the elden ring. He attempted to master its god-like powers, but became too much to handle. The ring exploded, with it still on the user's hand. Legend says the ring lives in fragments scattered thoughout the land. Heres a map to an eleged location of one of the shards.."]

    npcName = "Radahn"

    print(npcName,":,The name is",npcName, "Got time to chat?")
    answer = input(print("Press y to talk to",npcName))
    if answer == "y":
        print(npcName,":]", response)
    else:
        print(npcName,":] Goodbye!")

def Start_Chapter_2():
    print("You have recieved the map to the Whispering Woods")
    print("This concludes Chapter 1, Start Chapter 2")

def Chapter_1():
    print("Welcome to Chapter 1")
    #Get Character name
    character_name = Get_Character_Name()

    #Intro by the Hooded figure
    Hooded_Figure_Intro()

    #Talk to locals
    talk_to_locals()

    #Check if the user wants to start chapter 2
    travel_decision = input("Would you like to travel to the Whispering Woods? Yes/No?")
    if travel_decision == "Yes":
        Start_Chapter_2()
    else:
         print("You decide to stay in Eldoria, the journey continues...")