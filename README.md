# Dungeon-Crawler
CS50 Final Project


The point of our project was to create a 2D video game only using python, with the help of a Free and Open-Source library called Pygame. We used this library to create ‘pygame’ in python that we called Dungeon Crawler. We were unable to use a Graphical User Interface in the CS50 IDE so we downloaded Visual Studio Code on our computers, downloaded the pygame library, and set up a shared repository on Github to collaborate on our code. 


List of executables:
First, you must download python. Access this link to choose the correct version and download it:
https://www.python.org/downloads/

Next, you must set up your IDE. We chose VSCode. To download Visual Studio Code, access this link: https://code.visualstudio.com/download and choose the correct version for your computer. 


You will need to set up a Python interpreter in your Visual Studio code: 
Install and activate these extensions on Visual Studio Code by clicked the square on the left sidebar and searching: ‘Pygame Snippets’ and ‘Python’

Type and execute this command line argument in the Visual Studio Code terminal  (Ctrl + ` to bring up) to install pygame: ‘python3 -m pip install -U pygame --user’
If this does not work, check this links to find additional, operating system specific pip commands. (If pip does not work for some strange reason, look on this site to manually download https://pip.pypa.io/en/stable/installing/ )

Clone or download the Dungeon Crawler repository from the github account ‘LukeHeitman’ and access it on Visual Studio Code (or take the zip from the CS50 IDE submission)
Access the ‘Main’ branch on Visual Studio Code. 
Open up the template.py file. 
On this file, right click on the code window and select ‘Run Python File in Terminal.’ This will open the game window. 

Dungeon Crawler is a vertical 2D “collection” game where the main character attempts to collect keys while simultaneously avoiding monsters in order to advance through a series of rooms and escape the dungeon. 

Our game begins with an intro screen that displays the objective of the game and the instructions on how to play. Once you break out of the intro screen, you are able to move the sprite, or knight, using the arrow keys. The objective of the game is to collect keys while simultaneously avoiding the monsters. If you collide with, or get touched monster you will lose a life. If you lose all of your lives the game will end. If you still have any lives left you have the opportunity to restart by pressing the ‘R’ key. 

Level design: 
In level 1, the player only has to collect keys while avoiding one monster (demon). The demon gradually speeds up after the player collects each key. 
In level 2, the player has to collect keys while avoiding the original monster in additional to two other smaller skeletons. As the player collects keys, the demon speeds up at while the skeletons stay at the same speed. 
In level 3, the player has to collect keys while avoiding, a demon, two skeletons, and now orcs as well. However, now each time the player picks up a key another orc spawns from the door. The player advance each level by picking up 3 keys and then going through the door. If the player beats the third level then they have won the game.
A screen is displayed telling the player that they have won and it displays how many seconds it took to beat the game. 
