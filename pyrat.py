#!/usr/bin/python
#    Copyright © 2017 Vincent Gripon (vincent.gripon@imt-atlatique.fr) and IMT Atlantique
#
#    This file is part of PyRat.
#
#    PyRat is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    PyRat is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with PyRat.  If not, see <http://www.gnu.org/licenses/>.

# Imports
from core.parameters import *
import time
import pygame
from core.GameCore import *

if args.import_keras:
    import keras

def main():
    # Start program
    print("The game starts")
    debug("Starting pygame...")
    startTime = time.time()
    pygame.init()
    debug("Defining screen object...")
    if not(args.nodrawing):
        infoObject = pygame.display.Info()
        image_icon = pygame.image.load("resources/various/pyrat.ico")
        pygame.display.set_icon(image_icon)
        pygame.display.set_caption("PyRat")
        if args.fullscreen:
            screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)
            args.window_width = infoObject.current_w
            args.window_height = infoObject.current_h
        else:
            screen = pygame.display.set_mode((args.window_width, args.window_height), pygame.RESIZABLE)
    else:
        screen = ""
        infoObject = ""
    # Run first game
    gameCore = GameCore()
    debug("Starting first game")
    gameCore.run(screen, infoObject)
    debug("Writing stats and exiting")
    result = gameCore.getStats() 
    # Print stats and exit
    print(repr(result))
    pygame.quit()
    endTime = time.time()
    print("GameTime = "+str(endTime - startTime)+" -- MeanTurnTime = "+str((endTime - startTime)/args.matches))
    
if __name__ == "__main__":
    main()
