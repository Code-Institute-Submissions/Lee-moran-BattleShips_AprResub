![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

80'S STYLE BATTLESHIP

Python challege to create a python game.
about the game and the requirements

This program is a computerized version of the original board game battleships, based inside a mock terminal deployed via Heroku.

As a child of the 90's, I used the Milton Bradley game version and bring back the classic 80s style game. One can find more info on the rules and the history of the game here on Wikipedia. https://en.wikipedia.org/wiki/Battleship_(game). As this is my game i made the grid bigger and added more ships to destroy.

Object of the game is to sink 6 random computer generated ships from the 9 x 9 grid.
Single-player version against a computerized player.
You have 12 bullets to located and Hit the battleships.
if you hit all 6 you win 
if you run out of bullets you loose 

## WELCOME:

## HOW TO PLAY:
- vs the computer
- no. of bullets/turn to idenify and sink ships
- Selecting a row first between 1-9
- Select a column A-J
- Grid area 9 x 9
- Sink all 6 random postioned ships to win.
- Lose if all ships arent sunk 
- A HIT is identified by an X 
- A MISS is identified by an -


Input your shot eg (5,B) note the capitale letter for columns.



## Creating the Heroku app deployment

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`


Connect your GitHub repository and deploy as normal.

## Testing 
caps for rows ABCDEFGHI
Notice there was whitespacing issues all resolved.
pep8online validator - screenshot no new line at end of file.

## Reference
Credit goes to Garrett Broughton - https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=555s&ab_channel=KnowledgeMavens
Please find a link to his video which was used in this project. 


