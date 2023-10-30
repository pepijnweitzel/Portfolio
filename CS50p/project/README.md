# CarGameReek
#### Video Demo:  <URL HERE>
#### Description:
CarGameReek is a game created in PyGame to help kill the time, earn points by dodging the obstacles on the road!

### Setup
I've set up 3 globals which are used during my program: running, lost and score. Running takes care of the loop in which my game is playing, if at any point it is set to False, the game will stop. Lost will determine whether the user quit the game or lost, if lost is set to True, it will show the score obtained in the terminal. The last global variable is score, score keep track of how many points the user has obtained and shows it when the game is over. In the main function I've set up the screen with its background, the car which is being operated by the user and the obstacle.

### The loop
Every iteration in the loop the background, the car and the obstacle is loaded, during the loop depending on the users' keystrokes the screen updates in a specific way. First it will specify what speed the obstacles should be coming at depending on the current score, this is done via the calculate_speed function, then the obstacle gets moved accordingly. After that the program checks whether the obstacle is still on the correct location or perhaps on the border, if its y-value is too high a new obstacle will be created and start all over again.
Then we check for any keys pressed by the user via a pygame function, a function then gets called to get the correct adjustments for the car's location and its location gets updated. With this new location the program will check for any collision, first it will check for border collision, then it will check for obstacle collision by calling its functions. At last it will check whether to exit to program or not depending on the lost variable, the escape key or by clicking the cross on the user-interface, if not the program will update its interface and start over again.

### After the loop
When the loop has ended it will check whether the user quit, or whether the user made an obstacle collision, if it was the latter it will show the score obtained by the user in the terminal.
