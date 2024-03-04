#Emmanuel Velazquez
#This is the final chapter.. here, the user faces the toughest foes, and hardest puzzles for the final and strongest piece of the elden ring.
def use_elden_ring_to_overcome_challenges():
    print("Welcome to the Forbidden Caverns!")

    # Use the Elden Ring shards to overcome elemental challenges and puzzles
    print("You encounter strong elemental challenges and puzzles.")
    elden_ring_decision = input("Use the Elden Ring shards to overcome challenges? (yes/no): ")

    if elden_ring_decision == "yes":
        print("The Elden Ring shards empower you, allowing you to overcome the elemental challenges.")
    else:
        print("You choose not to use the Elden Ring shards. The elemental forces prove too strong, and you face consequences.")

def battle_elemental_guardians():
    print("You face epic battles with elemental guardians.")
    print("These guardians protect the last shard of the Elden Ring.")
    battle_decision = input("Engage in the battle with elemental guardians? (yes/no): ")

    if battle_decision == "yes":
        print("You engage in epic battles and successfully defeat the elemental guardians.")
    else:
        print("You choose not to engage in the battle. The elemental guardians overwhelm you, and you face consequences.")

def uncover_hidden_chambers():
    print("You explore the forbidden caverns and uncover hidden chambers.")
    print("These chambers may contain artifacts with god-like powers and the last shard of the Elden Ring.")
    uncover_decision = input("Explore the hidden chambers? (yes/no): ")

    if uncover_decision == "yes":
        print("You successfully uncover hidden chambers, finding artifacts and the last shard of the Elden Ring.")
    else:
        print("You choose not to explore the hidden chambers. The secrets remain undiscovered, and you face consequences.")

def claim_victory():
    print("Congratulations! You have successfully completed Chapter 5.")
    print("You harness the powers of the Elden Ring, liberating Eldoria!")

def chapter_5():
    # Use the Elden Ring shards to overcome elemental challenges and puzzles
    use_elden_ring_to_overcome_challenges()

    # Battle elemental guardians
    battle_elemental_guardians()

    # Uncover hidden chambers to find artifacts and the last shard of the Elden Ring
    uncover_hidden_chambers()

    # Check if the player is successful in all actions and is ready to claim victory
    victory_decision = input("Do you wish to claim victory and liberate Eldoria? (yes/no): ")

    if victory_decision == "yes":
        claim_victory()
    else:
        print("You choose not to claim victory. The journey continues...")