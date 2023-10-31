current_place = "start"
experience = 0
wealth = 0


def ask(prompt, options):
    print(prompt)
    for i, option in enumerate(options):
        print(str(i) + ": " + option)
    while True:
        choice = input("Enter a number to choose: ")
        try:
            choice = int(choice)
            if choice < 0 or choice >= len(options):
                raise ValueError()
            return choice
        except ValueError:
            print("Invalid input, try again.")


# Massive game loop
while True:
    if current_place == "start":
        print("You are in a forest located somewhere in New England. What do you do?")
        while True:
            choice = ask("Choose an action:", [
                         "Explore the forest", "Follow a path", "Climb a tree", "Check wealth"])
            if choice == 0:
                print("You travel through the forest and find a river.")
                current_place = "river"
                experience += 1
                break
            elif choice == 1:
                print("You follow a path and come to a bridge. Along the way you discover a key card with the name: Tim Richards on it")
                current_place = "bridge"
                experience += 1
                wealth += 200
                break
            elif choice == 2:
                print("You climb a tree and get a better view of the area.")
                experience += 1
            else:
                print("You currently have", wealth, "coins.")
    elif current_place == "river":
        print("You come to a river. What do you do?")
        while True:
            choice = ask("Choose an action:", [
                         "Cross the river", "Follow the river", "Build a raft", "Turn back", "Check wealth"])
            if choice == 0:
                print("You swim across the river safely.")
                current_place = "bridge"
                experience += 10
                break
            elif choice == 1:
                print("You follow the river and find a hidden cave.")
                current_place = "cave"
                experience += 2
                break
            elif choice == 2:
                print(
                    "You build a raft, which sinks immediately and you are forced to walk back to the riverbank.")
                current_place = "river"
                experience -= 1
                break
            elif choice == 4:
                print("You currently have", wealth, "coins.")
            else:
                print("You turn back and decide to start over.")
                current_place = "start"
                experience += 1
                break
    elif current_place == "bridge":
        print("You come to a bridge over a deep ravine. What do you do?")
        while True:
            choice = ask("Choose an action:", [
                         "Cross the bridge", "Climb down into the ravine", "Turn back", "Check wealth"])
            if choice == 0:
                print("You cross the bridge safely.")
                current_place = "cave"
                experience += 2
                break
            elif choice == 1:
                print("You climb down into the ravine and find a treasure chest.")
                current_place = "treasure"
                experience += 10
                break
            elif choice == 3:
                print("You currently have", wealth, "coins.")
    elif current_place == "cave":
        print("You find yourself in a dark cave. What do you do?")
        while True:
            choice = ask("Choose an action:", [
                         "Explore the cave", "Leave the cave", "Check wealth"])
            if choice == 0:
                print("You explore the cave and find a hidden passage.")
                current_place = "tunnel"
                experience += 2
                break
            elif choice == 1:
                print("You leave the cave and find yourself back at the river.")
                current_place = "river"
                experience += 1
                break
            else:
                print("You currently have", wealth, "coins.")
    elif current_place == "treasure":
        print("You find a treasure chest. What do you do?")
        while True:
            choice = ask("Choose an action:", [
                         "Open the chest", "Leave the chest", "Check wealth"])
            if choice == 0:
                print(
                    "You open the chest and find a lot of gold. You decide to circle back and explore the cave you saw earlier.")
                current_place = "cave"
                experience += 5
                wealth += 500
                break
            elif choice == 1:
                print("You leave the chest behind and find yourself back at the bridge.")
                current_place = "bridge"
                experience += 1
                break
            else:
                print("You currently have", wealth, "coins.")
    elif current_place == "tunnel":
        print("You find a secret tunnel. What do you do?")
        while True:
            choice = ask("Choose an action:", [
                         "Follow the tunnel", "Leave the tunnel", "Check wealth"])
            if choice == 0:
                print(
                    "You follow the tunnel and come across what seems to be a small, rural town.")
                current_place = "town"
                experience += 250
                break
            elif choice == 1:
                print("You leave the tunnel and find yourself back in the cave.")
                current_place = "cave"
                experience += 1
                break
            else:
                print("You currently have", wealth, "coins.")
    elif current_place == "town":
        print("Once at this town, what do you do?")
        while True:
            choice = ask("Choose an action:", [
                         "Explore the town", "Buy some supplies", "Rest in a dorm", "Leave the town", "Check wealth"])
            if choice == 0:
                print(
                    "You explore the town and find a cafeteria. You think to yourself, is this some sort of school?")
                experience += 1
                break
            elif choice == 1:
                print(
                    "You buy some food to fill your growling stomach, and store the rest in your pocket.")
                wealth -= 50
                experience += 5
                print("This cost you 50 coins and you currently have",
                      wealth, "coins remaining.")
            elif choice == 2:
                print("You rest in a dorm and build up your strength.")
                wealth -= 50
                experience += 3
                print("This cost you 50 coins and you currently have",
                      wealth, "coins remaining.")
            elif choice == 3:
                print("You leave the school and continue your journey.")
                current_place = "to be continued"
                experience += 2
                break
            else:
                print("You currently have", wealth, "coins.")
    else:
        print("Error: invalid room name")

# Final results of the game (need to add more steps to the adventure before I add these)
    if current_place == "death":
        print("You have died! Game over.")
        break
    elif current_place == "wealth":
        print("You have become rich enough to pay for a bus ride to New York! Congratulations, you win!")
        break
    elif current_place == "to be continued":
        print("The game is over for now, see you after the next update!")
        break
    if wealth < 0:
        print("You are now broke and in debt to services at the school")

# Player's endgame stats
    print("Current experience:", experience)
    print("Current wealth:", wealth)
