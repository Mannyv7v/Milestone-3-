#Emmaunel Velazquez
#Chapter 4 is about consulting a knowledgable seer for the next elden ring location x
def consult_seer():
    print("Welcome to the Mystic Citadel!")

    # Consult the seer to gain cryptic insights
    print("You approach the magical seer in the floating city.")
    seer_decision = input("Consult the seer for insights? (yes/no): ")

    if seer_decision == "yes":
        print("The seer provides cryptic insights about the next Elden Ring shard.")
        print("The seer also mentions forbidden caverns as the alleged location of the last shard.")
    else:
        print("You decide not to consult the seer. The journey continues without additional insights.")

def engage_in_rituals():
    print("You decide to engage in rituals to unlock the latent powers of the Elden Ring shards.")
    print("Performing the rituals may enhance your abilities. What action do you take?")
    rituals_decision = input("Engage in rituals? (yes/no): ")

    if rituals_decision == "yes":
        print("You successfully perform rituals and unlock latent powers.")
    else:
        print("You choose not to engage in rituals. Your powers remain as they were.")

def start_chapter_5():
    print("Congratulations! You have successfully completed Chapter 4.")
    print("Welcome to Chapter 5!")

def chapter_4():
    # Consult the seer and gain insights
    consult_seer()

    # Engage in rituals to unlock latent powers
    engage_in_rituals()

    # Check if the player is ready to start Chapter 5
    continue_journey = input("Do you wish to continue your journey to Chapter 5? (yes/no): ")

    if continue_journey == "yes":
        start_chapter_5()
    else:
        print("You decide to stay in the Mystic Citadel. The journey continues...")