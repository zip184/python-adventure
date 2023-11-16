# Python Adventure

This is an example of a file that I can edit and have updated to github anytime I finish a "draft"

## Here's a subtitle

Here's some paragraph text
- Here's some bullet points
- 1
- 2
- 3

### Here's a sub-sub-title

Numbered list
1. one
2. two
3. three

## Project Information

Collaborated on GitHub
Why?
“Source Control” generally allows multiple programmers to work on the same program, without having to send each other files manually. 
Push your changes up
Pull others changes down
This keeps a history of all of the changes that were made to the program. You can checkout any point in the repos history if you wanted to. Think of the history feature in google docs.
This Project Uses Object-Oriented Programming
What are Objects?
Objects (called “classes” in python) combine data & code to make the code look cleaner by only using one variable or command that has dozens of lines of code within it.
Data: Objects can group variables together. (Like AdventureChoice groups button text + the next AdventureNode)
Code: Objects can store code methods / functions as well, that have access to that data. (self.x variables in python)
Why I needed it
Separation of concerns. Object-oriented programming helped separate the GUI (graphical user interface) from the story or game code.
interface.py defined the AdventureUserInterface class, painted the window with images & text, and also listened for button clicks
gui-app-poc.py defined the actual story or game, and states variables (like wealth & exp) 
adventure.py defined AdventureChoice & AdventureNode classes, which are the main data structure that defines the story
Allowed one person to focus on the story or game design (gui-app-poc.py), and another person to focus on the game engine (interface.py & adventure.py)
Keeps the code from becoming a mess. This prevented the story code from being mixed together with creating labels, buttons, and frames.
Extensibility: 
If someone wanted to make a completely different game interface from the same story (like a VR game), they could just write a different interface file, and it would still work with the same story code.
If someone wanted to make a 2nd game/story, with the same GUI written for this app, they could write their own app file and not have to write their own interface.
Both of these would be much harder to do if the code was mixed together
This Program uses the Model View Controller (MVC) design pattern.
adventure.py is the model
interface.py is the view
gui-app-poc is the controller


### Requirements

This program requires python3, and pip3
python3 is the newest version of python
pip3 is the command line tool to install python 3 modules

### How to install

`pip3 install -r requirements.txt`

### How to run

`python3 app.py`

### How to updates the pip library requirements file

`pip3 freeze > requirements.txt`