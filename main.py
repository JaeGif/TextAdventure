# Author: Jae
# Version: 0.1
# Date Started: May 31, 22
# Date Completed: NA
# Main Function: brings together the graphics modules and the modules.py file to make the full game
# Notes: main function encapsulating the aspects of gameplay
from modules import *

if __name__ == '__main__':
    print('So the adventure begins\n Hello {} This is a generic game intro,'.format(player.name),
          'anyway lets get to fighting something!')
    input()
    enemy_encounter(bug)
