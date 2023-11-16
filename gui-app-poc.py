from interface import *
from adventure import *
import random


# State Variables
wealth = 0
experience = 0

# Create Display
main_display = AdventureUserInterface()


# Shows how to run code for every time location change event
def on_travel():
    global experience
    experience += 1
    main_display.set_exp(experience)


main_display.set_on_travel(on_travel)

# --- Main Nodes ---
forest = AdventureNode(
    'images/forest.png', "You're in a deep dark forest and it reminds you of a scary movie. Get out quick!")

sea = AdventureNode(
    'images/sea.png', "You're in the sea, and you can't swim! Get to land quickly!")

plain = AdventureNode(
    'images/plain.png', "You're in a desert, and you're suffering from dehydration. Be careful!")

# Example of node that updates state


def recieve_treasure():
    global wealth, main_display
    wealth += random.randint(200, 1200)
    main_display.set_wealth(wealth)


treasure_island = AdventureNode(
    'images/treasure-island.png', "You've stumbled upon Treasure Island!!!! Yarrr!")
treasure_island.set_on_arrive(recieve_treasure)

finish_line = AdventureNode(
    'images/finish-line.png', "You win! Thanks For Playing!")

# --- Define Node Connections ---
forest.choices = [
    AdventureChoice('go to plain', plain),
    AdventureChoice('go to sea', sea),
]

sea.choices = [
    AdventureChoice('go to forest', forest),
    AdventureChoice('go to plain', plain),
    AdventureChoice('go to island', treasure_island)
]

plain.choices = [
    AdventureChoice('go to forest', forest),
    AdventureChoice('go to sea', sea),
    AdventureChoice('win the game', finish_line)
]

treasure_island.choices = [
    AdventureChoice('go to sea', sea),
]

# --- Set starting node ---
main_display.set_node(forest)

# --- Set initial state ---
main_display.set_wealth(0)
main_display.set_exp(0)

# Start display
main_display.start()
