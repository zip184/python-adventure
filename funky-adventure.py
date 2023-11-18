from interface import *
from adventure import *
import random


# State Variables
wealth = 0
experience = 0
did_listen_to_radio = False

# Create Display
main_display = AdventureUserInterface("Funky Adventure!")


# Shows how to run code for every time location change event
def on_travel():
    global experience
    experience += 1
    main_display.set_exp(experience)


main_display.set_on_travel(on_travel)

# --- Counry House Nodes ---
country_house_room = AdventureNode(
    'images/funky/bedroom.png', "It's 1970. You're sitting in your hum-drum bedroom, in your hum-drum house. Your mamma said your grounded for listening to that DEVIL's music. She smashed the James Brown record your cool buddy gave you. She said not to leave your room until she gets back.")
country_life_forever = AdventureNode(
    'images/funky/crying.png', "You've decided to stay in your room. You've choosen that hum-drum life and never listen to funky music ever again!")
country_house_upstairs_hallway = AdventureNode(
    'images/funky/hallway.png', "You're upstairs in the hallway in your hum-drum house.")
country_house_bathroom = AdventureNode(
    'images/funky/bathroom.png', "You're in the bathroom. When you gotta go, you gotta go Daddy-O!")
country_house_living_room = AdventureNode(
    'images/funky/living-room.png', "You're in your living room. There's a radio, and a televison.")
country_house_tv = AdventureNode(
    'images/funky/tv.png', "You turn on the television. There's only 3 channels, and they all stink!")
country_house_radio = AdventureNode(
    'images/funky/radio.png', "You turn on the radio, there's some funky music! It's Sly and the Family Stone. It's the greatest sound you've ever heard. The radio announcer comes on and says... \n\n\"Hey man... do you have a hum-drum life? Come on down to Funky Town baby! Hurry up, the funky train is leaving the station!\"")
country_house_outside = AdventureNode(
    'images/funky/outside.png', "You go outside. All you hear is the hum-drum sound of the hum-drum town. There's nothing here for you.")

# --- Train Nodes ---
train_station = AdventureNode('images/funky/funky-train.png', "You ride your bike as fast as you can down the street towards the station. The grooves in the distance are gettin louder. When you get to the station, you see a funky train waiting at the station tracks! There's a funk band playing on top of the coal car. It's the most funky music you've ever heard!")
train_station_tracks = AdventureNode(
    'images/funky/james-brown-conductor.png', "You approach the train to hear the music better. You eye the conductor at the door to the train, and can't believe your eyes! The conductor is none other than James Brown! He yells to you... \n\n\"All Aboard the Night Train!\"")


# --- Country House Connections ---
country_house_room.choices = [
    AdventureChoice('Leave Your Room', country_house_upstairs_hallway),
    AdventureChoice('Stay in Your Room', country_life_forever)
]
country_house_upstairs_hallway.choices = [
    AdventureChoice('Go Back to Your Room', country_house_room),
    AdventureChoice('Go to the Bathroom', country_house_bathroom),
    AdventureChoice('Go Downstairs', country_house_living_room),
]
country_house_bathroom.choices = [
    AdventureChoice('Leave the bathroom', country_house_upstairs_hallway),
]
country_house_living_room.choices = [
    AdventureChoice('Turn on the TV', country_house_tv),
    AdventureChoice('Turn on the Radio', country_house_radio),
    AdventureChoice('Go Outside', country_house_outside),
    AdventureChoice('Go Upstairs', country_house_upstairs_hallway)
]
country_house_tv.choices = [
    AdventureChoice('Turn off the TV', country_house_living_room)
]


def listen_to_radio():
    global did_listen_to_radio
    if not did_listen_to_radio:
        country_house_outside.choices.append(AdventureChoice(
            'Ride your bike to the train station', train_station))
        country_house_outside.description = "You're outside your hum-drum house, but you can hear some funky grooves off in the distance towards the train station. You've got a bike in the garage."
    did_listen_to_radio = True


country_house_radio.choices = [
    AdventureChoice('Turn off the Radio', country_house_living_room)
]
country_house_radio.set_on_arrive(listen_to_radio)

country_house_outside.choices = [
    AdventureChoice('Go back inside', country_house_living_room)
]

# --- Funky Train Nodes ---
train_station.choices = [
    AdventureChoice('Approach the train', train_station_tracks)
]

# --- Set starting node ---
main_display.set_node(country_house_room)

# --- Set initial state ---
main_display.set_wealth(0)
main_display.set_exp(0)

# Start display
main_display.start()
