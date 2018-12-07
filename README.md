# Dungeon-Crawler
CS50 Final Project


Documentation for your project in the form of a Markdown file called README.md. This documentation is to be a user’s manual for your project. Though the structure of your documentation is entirely up to you, it should be incredibly clear to the staff how and where, if applicable, to compile, configure, and use your project. Your documentation should be at least several paragraphs in length. It should not be necessary for us to contact you with questions regarding your project after its submission. Hold our hand with this documentation; be sure to answer in your documentation any questions that you think we might have while testing your work.


The point of our project was to create a 2D video game only using python, with the help of a Free and Open-Source library called Pygame. We used this library a ‘pygame’ game in python that we called Dungeon Crawler. We were unable to use a Graphical User Interface in the CS50 IDE so we downloaded Visual Studio Code on our computers and set up a shared repository on Github to collaborate on our code. 
List of executables:
To download Visual Studio Code, access this link: https://code.visualstudio.com/download and choose the correct version for your computer. 
You will need to set up a Python interpreter in your Visual Studio code: 
Install and activate these extensions on Visual Studio Code: ‘Pygame Snippets’ and ‘Python’
Install Python on your computer using this link:https://www.python.org/downloads/ 
Type and execute this common line argument in the Visual Studio Code terminal to install pygame: ‘python3 -m pip install -U pygame --user’
Clone or download the Dungeon Crawler repository from the github account ‘LukeHeitman’ and access it on Visual Studio Code
Access the ‘Main’ branch on Visual Studio Code. 
Open up the template.py file. 
On this file, right click on the code window and select ‘Run Python File in Terminal.’ This will open the game window. 

Dungeon Crawler is a vertical 2D “collection” game where the main character attempts to collect keys while simultaneously avoiding monsters in order to advance through a series of levels and escape the dungeon. 

Our game begins with an intro screen that displays the objective of the game and the instructions on how to play. Once you break out of the intro screen, you are able to move the sprite, or knight, using the arrow keys. The objective of the game is to collect keys while simultaneously avoiding the monsters. If you collide with, or get touched monster you will lose a life. If you lose all of your lives the game will end. If you still have any lives left you have the opportunity to restart by pressing the ‘R’ key. 

Level design: 
In level 1, the player only has to collect keys while avoiding one monster (demon). The demon gradually speeds up after the player collects each key. 
In level 2, the player has to collect keys while avoiding the original monster in additional to two other smaller skeletons. As the player collects keys, the monsters speed up at different rates. 
In level 3, the player has to collect keys while avoiding, a demon, two small skeletons, and now an orc as well. However, now each time the player picks up a key another orc spawns. 
The players advance each level by picking up 3 keys and then going through the door. If the user makes it to the third level, gets all the keys on the third level, goes through the door and never loses all three lives then they have won the game. 
