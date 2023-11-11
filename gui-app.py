from display import *
from adventure import *


forest = AdventureNode(
    'images/forest.png', "You're in a deep dark forest and it reminds you of a scary movie. Wilikers!")
sea = AdventureNode(
    'images/sea.png', "You're in the sea, and you can't swim! Gosh!")
plain = AdventureNode(
    'images/plain.png', "You're in a desert, and you forgot to bring your water bottle. Scary stuff!")

forest.choices = [
    AdventureChoice('go to sea', sea),
    AdventureChoice('go to plain', plain),
]

sea.choices = [
    AdventureChoice('go to forest', forest),
    AdventureChoice('go to plain', plain),
]

plain.choices = [
    AdventureChoice('go to sea', sea),
    AdventureChoice('go to forest', forest),
]

main_display = MainDisplay()

main_display.set_choice(forest)

main_display.start()
