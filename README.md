80'S STYLE BATTLESHIP

Python challege to create a python game.
about the game and the requirements

This program is a computerized version of the original board game battleships, based inside a mock terminal deployed via Heroku.

As a 90's child, I used the Milton Bradley game version and bring back the classic 80s style game. One can find more info on the rules and the history of the game here on Wikipedia. https://en.wikipedia.org/wiki/Battleship_(game). As this is my game i made the grid bigger and added more ships to destroy.

Object of the game is to sink 6 random computer generated ships from the 9 x 9 grid.
Single-player version against a computerized player.
You have 30 bullets to located and Hit the 6 battleships.
if you hit all 6 you win 
if you run out of bullets you loose and GAME OVER

## WELCOME:

## HOW TO PLAY:
- vs the computer
- no. of bullets/turn to idenify and sink ships
- Selecting a row first between 1-9
- Select a column A-J
- Grid area 9 x 9
- Sink all 9 random postioned ships to win.
- Lose if all ships arent sunk or run out of bullets
- A HIT is identified by an X 
- A MISS is identified by an -
- Water represented by | |

Input your shot eg (5,B) note the capitale letter for columns.

## Design
- Color Scheme
Not required for the scope of this project.
However i added some color to enhance the visibility of the game
Used https://stackoverflow.com/questions/5762491/how-to-print-color-in-console-using-system-out-println
to apply colors to the ptint statment.

- Feel
Wanted to give the game that retro feel as its a terminal game.
With it being inspired by the 80s, the user is playing against the computer.
Trying to guess where the computer has placed 6 ships hidden.


- ICONS
A HIT is identified by an X 
A MISS is identified by an -
Water represented by ' '
X Hit Red in color 
Miss Yellow in color

Screenshot icons 

- LAYOUT
My goal with the layout of the project, when displayed within the terminal, based on the retro feel and be easy to use.



## Creating the Heroku app deployment

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

The site is deployed via Heroku. The steps to deploy are as follows:

- 1: From the dashboard, select New and then Create new app.

- 2: Enter an individual app name into the text box, select a region from the dropdown and then press Create app.

- 3: A Heroku app has now been created and the Deploy tab is opened.

- 4: Select the Settings tab.

- 5: If required, click on the Reveal Config Vars button and add.

- 6: In the Buildpacks section of the settings tab, click on Add Buildpack, select Python and then save changes.

- 7: Click on Add Buildpack again, select node.js and then save changes.

When they are on the dashboard, ensure that python is above node.js on the list

- 8: Open the Deploy tab.

- 9: In the deployment method section, select GitHub and confirm the connection.

- 10: Enter the repo-name into the text box. When the correct repo appears, click Connect.

- 11: If desired, in the Automatic deploys section, click Enable Automatic Deploys.

This then updates the deployment every time GitHub code is pushed.

- 12: To complete the process click on the Deploy Brach button in the Manual deploy section.

This will take a few seconds to complete while Heroku builds the app.

- 13: A message will appear informing you that the app was successfully deployed and a View button will bring you to the live site.

Live link: https://battleship80s.herokuapp.com/

Connect your GitHub repository and deploy as normal.

## Testing 
Capitals for rows ABCDEFGHI
Notice there was whitespacing issues all resolved.
Whitespace warning when using http://patorjk.com/

Testing
Due to the nature of the project testing has been conducted throughout its entirety, mainly through the use of running the program in the terminal and ensuring i get the output intended. Evidence of this is clear within my commits, with various debugs recorded.

Once at the finished point, limit testing has been conducted by myself, there is currently no reported issues that cause the game to break.

Validator Testing

HTML - Not within project scope.
CSS - Not within project scope.
JS - Not within project scope.
Python - One error was found when passing through the PEP8 Validator tool - no new line at end of file.
Lighthouse - Not within project scope

## Reference
Credit goes to Garrett Broughton - https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=555s&ab_channel=KnowledgeMavens
Please find a link to his video which was used in this project. 


