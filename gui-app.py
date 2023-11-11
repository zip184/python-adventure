from display import *
from adventure import *


forest = AdventureNode('images/forest.png', 'your in a forest')
sea = AdventureNode('images/sea.png', 'your in a sea')
plain = AdventureNode('images/plain.png', 'your on a plain')

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
