A "design document" for your project in the form of a Markdown file called DESIGN.md that discusses, technically, how you implemented your project and why you made the design decisions you did. Your design document should be at least several paragraphs in length. Whereas your documentation is meant to be a user’s manual, consider your design document your opportunity to give the staff a technical tour of your project underneath its hood.


The majority of our code is in our template.py file. In this template file we declare some constants to be used regarding the height and width of the window. This way it is easier to put certain x and y coordinates in perspective throughout the code. We have constants to represent the game map, as the background border tiles are 16 pixels and the game tiles that the sprites can move and spawn on are 32 pixels. We also have constants to represent some colors and a constant to represent a default font that we will use in our game that is drawn on from our assets folder. 

All of our game functionality is in our ‘main’ function. We have a variable called FPSCLOCK that we are able to “tick” a specific number of frames per second depending on different scenarios. We load an mp3 file from our Assets folder and set this song to play forever by passing in the “-1” value in pygame. Our game begins with an intro screen in which we display the name “Dungeon Crawler” and display a short backstory, objective, and instructions on how to play the game.

We have a separate file for all of our sprites called sprites.py. 
