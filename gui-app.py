from interface import *
from adventure import *
import random

# State Variables
wealth = 0
experience = 0

# Create Display
main_display = AdventureUserInterface()

# Game Events


def recieve_treasure():
    global wealth, main_display
    wealth += random.randint(200, 1200)
    main_display.set_wealth(wealth)


def on_travel():
    global experience
    experience += 1
    main_display.set_exp(experience)


main_display.set_on_travel(on_travel)

# Main Nodes
forest = AdventureNode(
    'images/forest.png', "You're in a deep dark forest and it reminds you of a scary movie. Wilikers!")

sea = AdventureNode(
    'images/sea.png', "You're in the sea, and you can't swim! Gosh!")

plain = AdventureNode(
    'images/plain.png', "You're in a desert, and you forgot to bring your water bottle. Scary stuff!")

treasure_island = AdventureNode(
    'images/treasure-island.png', "You've stumbled upon Treasure Island!!!! Yarrr!")
treasure_island.set_on_arrive(recieve_treasure)

# Set node choices
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
]

treasure_island.choices = [
    AdventureChoice('go to sea', sea),
]

# Set starting node
main_display.set_choice(forest)
main_display.set_wealth(0)

# Start display
main_display.start()
