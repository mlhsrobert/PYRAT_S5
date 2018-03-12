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

from core.parameters import *
import pygame
import random
import datetime
from pygame import locals
from core.MazeInfo import *
from player.Player import *
from player.AIPlayer import *
from player.HumanPlayer import *
from player.InactivePlayer import *
from display.PlayerDisplay import *

class Display:
    
    def __init__(self, screen, mazeInfo):
        self.__screen = screen
        self.__window_width, self.__window_height = pygame.display.get_surface().get_size()
        self.__font_sizes = [50, 25, 50, 25, 50, 50, 50]
               
            
        self.__maze = mazeInfo.getMaze()
        (self.__width, self.__height) = mazeInfo.getMazeSize()
        self.__piecesOfCheese = mazeInfo.getPiecesOfCheese() 
              

    def image_of_maze(self):
        for i in range(self.__width):
            for j in range(self.__height):
                self.__maze_image.blit(self.__image_tile[self.__tiles[i][j]], (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y - self.__scale * (j+1)))
        for i in range(self.__width):
            for j in range(self.__height):
                if not((i-1,j) in self.__maze[(i,j)]):
                    self.__maze_image.blit(self.__image_wall, (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y - self.__scale * (j+1)))
                elif self.__maze[(i,j)][(i-1,j)] > 1:
                    self.__maze_image.blit(self.__image_mud, (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y - self.__scale * (j+1)))
                if not((i+1,j) in self.__maze[(i,j)]):
                    self.__maze_image.blit(pygame.transform.rotate(self.__image_wall, 180), (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y - self.__scale * (j+1)))
                elif self.__maze[(i,j)][(i+1,j)] > 1:
                    self.__maze_image.blit(pygame.transform.rotate(self.__image_mud, 180), (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y - self.__scale * (j+1)))
                if not((i,j+1) in self.__maze[(i,j)]):
                    self.__maze_image.blit(pygame.transform.rotate(self.__image_wall, 270), (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y - self.__scale * (j+1)))
                elif self.__maze[(i,j)][(i,j+1)] > 1:
                    self.__maze_image.blit(pygame.transform.rotate(self.__image_mud, 270), (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y - self.__scale * (j+1)))
                if not((i,j-1) in self.__maze[(i,j)]):
                    self.__maze_image.blit(pygame.transform.rotate(self.__image_wall, 90), (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y - self.__scale * (j+1)))
                elif self.__maze[(i,j)][(i,j-1)] > 1:
                    self.__maze_image.blit(pygame.transform.rotate(self.__image_mud, 90), (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y - self.__scale * (j+1)))
        for i in range(self.__width):
            self.__maze_image.blit(pygame.transform.rotate(self.__image_wall, 270), (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y))
            self.__maze_image.blit(pygame.transform.rotate(self.__image_wall, 90), (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y - self.__scale * (self.__height + 1)))
        for j in range(self.__height):
            self.__maze_image.blit(self.__image_wall, (self.__offset_x + self.__scale * self.__width , self.__window_height - self.__offset_y - self.__scale * (j+1)))
            self.__maze_image.blit(pygame.transform.rotate(self.__image_wall, 180), (self.__offset_x - self.__scale, self.__window_height - self.__offset_y - self.__scale * (j+1)))
        for i in range(self.__width+1):
            for j in range(self.__height+1):
                self.__maze_image.blit(self.__image_corner, (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y - self.__scale * j))
                self.__maze_image.blit(pygame.transform.rotate(self.__image_corner, 90), (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y - self.__scale * (j+1)))
                self.__maze_image.blit(pygame.transform.rotate(self.__image_corner, 180), (self.__offset_x + self.__scale * (i-1), self.__window_height - self.__offset_y - self.__scale * (j+1)))
                self.__maze_image.blit(pygame.transform.rotate(self.__image_corner, 270), (self.__offset_x + self.__scale * (i-1), self.__window_height - self.__offset_y - self.__scale * j))
    
    def draw_pieces_of_cheese(self):
        for (i,j) in self.__piecesOfCheese:
            self.__screen.blit(self.__image_cheese, (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y - self.__scale * (j+1)))
    
    def draw_players(self,ratDisplay, pythonDisplay):
        i, j = ratDisplay.getLocation()
        self.__screen.blit(ratDisplay.getStaticImage(), (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y - self.__scale * (j+1)))
        i, j = pythonDisplay.getLocation()
        self.__screen.blit(pythonDisplay.getStaticImage(), (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y - self.__scale * (j+1)))
    
    
    def drawPlayersAnimate(self, ratDrawLocation, pythonDrawLocation, ratImage, pythonImage):
        i, j = ratDrawLocation
        self.__screen.blit(ratImage, (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y - self.__scale * (j+1)))
        i, j = pythonDrawLocation
        self.__screen.blit(pythonImage, (self.__offset_x + self.__scale * i, self.__window_height - self.__offset_y - self.__scale * (j+1)))
    
    def draw_text(self,text, color, max_size, index_size, x, y):
        if index_size > 6:
            index_size = 6        
        font = pygame.font.SysFont("monospace", self.__font_sizes[index_size])    
        label = font.render(text, 1, color)
        while(label.get_rect().width > max_size):
            self.__font_sizes[index_size] = self.__font_sizes[index_size] - 1
            font = pygame.font.SysFont("monospace", self.__font_sizes[index_size])
            label = font.render(text, 1, color)
        pygame.draw.rect(self.__screen, (0,0,0), (x - label.get_rect().width // 2, y, label.get_rect().width,label.get_rect().height))
        self.__screen.blit(label, (x - label.get_rect().width // 2,y))
        
    def drawScores(self, player, max_size, index_size, x, y):
        if player.isAlive():
            self.draw_text(player.getScoreStr(), (255,255,255), max_size, index_size, x, y + 50)
            self.draw_text(player.getName(), (255,255,255), max_size, index_size+ 5, x, y)
            self.draw_text(player.getMovesStr(), (0,255,0), max_size, index_size + 1, x, y + 150)
            self.draw_text(player.getMissStr(), (255,0,0), max_size, index_size + 1, x, y + 180)
            self.draw_text(player.getMudStr(), (255,0,0), max_size, index_size + 1, x, y + 210)
       
    def display_exit(self):
        pygame.quit()
    
    def init_coords_and_images(self, ratDisplay, pythonDisplay):
            
        scale = int(min((self.__window_height - 50) / self.__height, self.__window_width * 2/3 / self.__width))
        offset_x = self.__window_width // 2 - int(self.__width / 2 * scale)
        offset_y = max(25, self.__window_height // 2 - int(scale * self.__height / 2))
        scale_portrait_w = int(self.__window_width / 6)
        scale_portrait_h = int(self.__window_width / 6 * 800 / 541)
    
        self.__image_cheese = pygame.transform.smoothscale(pygame.image.load("resources/gameElements/cheese.png"),(scale, scale))
        self.__image_corner = pygame.transform.smoothscale(pygame.image.load("resources/gameElements/corner.png"),(scale, scale))
        ratDisplay.initStaticImage("resources/gameElements/rat.png", (scale, scale))
        ratDisplay.initMovingImage("resources/gameElements/movingRat.png", (scale, scale))
        ratDisplay.initPortraitImage("resources/illustrations/rat.png",(scale_portrait_w, scale_portrait_h))
        pythonDisplay.initStaticImage("resources/gameElements/python.png", (scale, scale))
        pythonDisplay.initMovingImage("resources/gameElements/movingPython.png", (scale, scale))
        pythonDisplay.initPortraitImage("resources/illustrations/python_left.png", (scale_portrait_w, scale_portrait_h))
        self.__image_wall = pygame.transform.smoothscale(pygame.image.load("resources/gameElements/wall.png"),(scale, scale))
        self.__image_mud = pygame.transform.smoothscale(pygame.image.load("resources/gameElements/mud.png"),(scale, scale))
        image_tile = []
        for i in range(10):
            image_tile.append(pygame.transform.smoothscale(pygame.image.load("resources/gameElements/tile"+str(i+1)+".png"),(scale, scale)))
        tiles = []
        for i in range(self.__width):
            tiles.append([])
            for j in range(self.__height):
                tiles[i].append(random.randrange(10))
           
        self.__scale = scale
        self.__offset_x = offset_x
        self.__offset_y = offset_y
        self.__tiles = tiles
        self.__image_tile = image_tile
    
    def build_background(self, ratDisplay, pythonDisplay):
        self.__screen.fill((0, 0, 0))
        self.__font_sizes = [50, 25, 50, 25, 50, 50, 50]
        self.__maze_image = self.__screen.copy()
        self.image_of_maze()
    
        if ratDisplay.isAlive():
            self.__maze_image.blit(ratDisplay.getPortraitImage() , (int(self.__window_width /12 - ratDisplay.getPortraitImage().get_rect().width / 2), 15))
        if pythonDisplay.isAlive():
            self.__maze_image.blit(pythonDisplay.getPortraitImage(), (int(self.__window_width * 11 / 12 - pythonDisplay.getPortraitImage().get_rect().width / 2), 15))     
        
    def checkEventQuit(self, event, q3QuitFromCore):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
            q3QuitFromCore.put("")
            return True
        else:
            return False
        
    def checkEventVideoResize(self, event, ratDisplay, pythonDisplay):
        if event.type == pygame.VIDEORESIZE or (event.type == pygame.KEYDOWN and event.key == pygame.K_f):
            if event.type == pygame.KEYDOWN and not(self.__screen.get_flags() & 0x80000000):
                self.__screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)
                self.__window_width, self.__window_height = infoObject.current_w, infoObject.current_h
            else:
                if event.type == pygame.VIDEORESIZE:
                    self.__window_width, self.__window_height = event.w, event.h
                self.__screen = pygame.display.set_mode((self.__window_width, self.__window_height),pygame.RESIZABLE)
            self.init_coords_and_images(ratDisplay, pythonDisplay)
            self.build_background(ratDisplay, pythonDisplay)        
   
    def checkEventKey(self, event, ratPlayer, pythonPlayer):
        if event.type == pygame.KEYDOWN :                
            if event.key == pygame.K_LEFT:
                ratPlayer.putHumanDecision("L")
            if event.key == pygame.K_RIGHT:
                ratPlayer.putHumanDecision("R")
            if event.key == pygame.K_UP:
                ratPlayer.putHumanDecision("U")
            if event.key == pygame.K_DOWN:
                ratPlayer.putHumanDecision("D")
            if event.key == pygame.K_KP4:
                pythonPlayer.putHumanDecision("L")
            if event.key == pygame.K_KP6:
                pythonPlayer.putHumanDecision("R")
            if event.key == pygame.K_KP8:
                pythonPlayer.putHumanDecision("U")
            if event.key == pygame.K_KP5:
                pythonPlayer.putHumanDecision("D")        
    
    def playerWithJoystick(self, ratPlayer, pythonPlayer):
        debug("Trying to initialize Joystick",2)
        pygame.joystick.init()
        try:
            j0 = pygame.joystick.Joystick(0)
            j0.init()
            print('Enabled joystick: ' + j0.get_name() + ' with ' + str(j0.get_numaxes()) + ' axes', file=sys.stderr)
            j1 = pygame.joystick.Joystick(1)
            j1.init()
            print('Enabled joystick: ' + j1.get_name() + ' with ' + str(j1.get_numaxes()) + ' axes', file=sys.stderr)
        except pygame.error:        
            ()            
        debug("Processing joysticks",2)
        try:
            x , y = j0.get_axis(3), j0.get_axis(4)
            if x < -0.7:
                ratPlayer.putHumanDecision("L")
            if x > 0.7:
                ratPlayer.putHumanDecision("R")
            if y < -0.7:
                ratPlayer.putHumanDecision("U")
            if y > 0.7:
                ratPlayer.putHumanDecision("D")
        except:
            ()
        try:
            x , y = j1.get_axis(3), j1.get_axis(4)
            if x < -0.7:
                pythonPlayer.putHumanDecision("L")
            if x > 0.7:
                pythonPlayer.putHumanDecision("R")
            if y < -0.7:
                pythonPlayer.putHumanDecision("U")
            if y > 0.7:
                pythonPlayer.putHumanDecision("D")
        except:
            ()         
    
        
    def receiveUpdateFromCore(self, turnTime, playerDisplay, playerGameInfo, newPlayerLocation):
        playerDisplay.updateGameInfo(playerGameInfo)
        
        if not(args.desactivate_animations):                             
            if newPlayerLocation != playerDisplay.getNextLocation():
                playerDisplay.setTimeToGo(pygame.time.get_ticks() + turnTime * self.__maze[playerDisplay.getNextLocation()][newPlayerLocation])
                playerDisplay.updateLocation()
                
        playerDisplay.setNextLocation(newPlayerLocation)
        
        if args.desactivate_animations:
            playerDisplay.updateLocation()
                
    
    def run (self, q1DrawingInfo, q2QuitFromDisplay, q3QuitFromCore, q4Text, ratPlayer, pythonPlayer, infoObject):
    
        debug("Create player display",2)
        ratDisplay = PlayerDisplay(ratPlayer)
        pythonDisplay = PlayerDisplay(pythonPlayer)
        
        debug("Starting rendering",2)
        self.init_coords_and_images(ratDisplay, pythonDisplay)
         
        debug("Defining constants",2)
        turnTime = args.turn_time
        clock = pygame.time.Clock()
    
        debug("Building background image",2)
        self.build_background(ratDisplay, pythonDisplay)
    
        starting_time = pygame.time.get_ticks()
    
        text_info = ""
    
        debug("Starting main loop",2)
        while q3QuitFromCore.empty():
            debug("Checking events",2)
            for event in pygame.event.get():
                if self.checkEventQuit(event, q3QuitFromCore):
                    break                
                self.checkEventVideoResize(event, ratDisplay, pythonDisplay)               
                self.checkEventKey(event, ratPlayer, pythonPlayer)
            
            self.playerWithJoystick(ratPlayer, pythonPlayer)            
                
            debug("Looking for updates from core program",2)
            while not(q1DrawingInfo.empty()):
                self.__piecesOfCheese, (newRatLocation, ratGameInfo), (newPythonLocation, pythonGameInfo)= q1DrawingInfo.get()
                self.receiveUpdateFromCore(turnTime, ratDisplay, ratGameInfo, newRatLocation)    
                self.receiveUpdateFromCore(turnTime, pythonDisplay, pythonGameInfo, newPythonLocation) 
                
            debug("Starting draw",2)
            self.__screen.fill((0, 0, 0))
            self.__screen.blit(self.__maze_image, (0, 0))
            
            self.draw_pieces_of_cheese()
            
            if not(args.desactivate_animations):                               
                ratDrawLocation, ratImage = ratDisplay.processMoveAnimation(self.__maze, turnTime)
                pythonDrawLocation, pythonImage = pythonDisplay.processMoveAnimation(self.__maze, turnTime)                
                self.drawPlayersAnimate(ratDrawLocation, pythonDrawLocation, ratImage, pythonImage)
            else:
                self.draw_players(ratDisplay, pythonDisplay)
                
            self.drawScores(ratDisplay, self.__window_width / 6, 0, int(self.__window_width / 12), self.__window_width / 3)
            self.drawScores(pythonDisplay, self.__window_width / 6, 2, int(11 * self.__window_width / 12), self.__window_width / 3)
            
            if not(q4Text.empty()):
                text_info = q4Text.get()
                
            if text_info != "":
                self.draw_text(text_info, (255,255,255), self.__window_width, 4, self.__window_width // 2, 25)
                
            if pygame.time.get_ticks() - starting_time < args.preparation_time:
                remaining = args.preparation_time - pygame.time.get_ticks() + starting_time
                if remaining > 0:
                    self.draw_text("Starting in " + str(remaining // 1000) + "." + (str(remaining % 1000)).zfill(3), (255,255,255), self.__window_width, 4, self.__window_width // 2, 25)
    
            debug("Drawing on screen",2)
            pygame.display.flip()
            if not(args.desactivate_animations):
                clock.tick(60)
            else:
                if not(args.synchronous):                
                    clock.tick(1000/turnTime)
        debug("Exiting rendering", 2)
        q2QuitFromDisplay.put("quit")

    
    
