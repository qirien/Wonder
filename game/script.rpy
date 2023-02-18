# Wonder visual novel mystery game is (c) 2023 Metasepia Games and released under the GPL v3.0 license
# Main script, definitions, etc

# Constant variables that don't change and don't need to be saved
define you = Character("You")
define q = Character("Q", who_color="#990011")
define j = Character("J", who_color="#aa11aa")

# Begin code
label start:

    # Variables that need to be saved with the game

    # General variables
    default attributes = {}
    default bestiary = {}
    default selected_creature = ""

    python:
        bestiary = {
            "Kelpie":{"description":"A water sprite.",
                    "attributes":["water", "humanoid", "jealous"],
                    "unlocked":True},
            "Pixie":{"description":"Tiny winged creatures full of mirth and mischief.",
                    "attributes":["flying", "humanoid", "selfish"],
                    "unlocked":True},
            "Kitsune":{"description":"Wise, shapeshifting fox spirits.",
                    "attributes":["animal", "humanoid", "wise"],
                    "unlocked":True},
            "Bunyip":{"description":"Swamp creature that can look like a furry animal or a human.",
                    "attributes":["animal", "humanoid", "water", "selfish"],
                    "unlocked":True},
            "Sea Dragon":{"description":"Rare, regal aquatic dragons.",
                    "attributes":["animal", "huge", "water", "proud"],
                    "unlocked":True},
            "Kraken":{"description":"Tentacled sea creature",
                    "attributes":["water", "animal", "huge"],
                    "unlocked":False}

        }
        # Put all possible attributes into the dictionary attributes where their value is whether they are selected or not:
        # {"animal":False, "water":False}
        generate_attributes()

    # Chapter 1 plot flags
    default ch1.met_j = False
    default ch1.met_q = False
    default ch1.met_crimescene = False
    default ch1.met_morgue = False
    default ch1.victory = False
    default ch1.clues = {}
    python:
        ch1.clues = {"blood":{"found":False, "selected":False},
                     "river":{"found":False, "selected":False},
                     "footprints":{"found":False, "selected":False},
                     "body":{"found":False, "selected":False},
                     "stab_wound":{"found":False, "selected":False}
                    }

# The game starts here.

    call chapter1
    scene black
    "And that's how I defeated the Kelpie."
    #call ending
    #call credits

    return
