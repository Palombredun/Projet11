import pygame
from pygame.locals import *

from app.models.hero import Hero
from app.models.labyrinth import Labyrinth

from app.controllers.game import Game

from app.views.display import Display


game = Game()
maze = Labyrinth()
macgyver = Hero()
display = Display(maze, macgyver, game.path_enemy, game.path_objects)


while game.is_victory(macgyver) is False:
    for event in pygame.event.get():
        if event.type == pygame.KEY_DOWN:
            if event.type == pygame.K_q:
                break
            else:
                if event.type == pygame.K_LEFT:
                    if maze.test_position(macgyver, "l"):
                        if macgyver.path in game.path_objects:
                            macgyver.add_item(item)
                            game.test_victory(macgyver)
                        macgyver.path += "l"
                elif event.type == pygame.K_RIGHT:
                    if maze.test_position(macgyver, "r"):
                        if macgyver.path in game.path_objects:
                            macgyver.add_item(item)
                            game.test_victory(macgyver)
                        macgyver.path += "r"
                elif event.type == pygame.K_UP:
                    if maze.test_position(macgyver, "u"):
                        if macgyver.path in game.path_objects:
                            macgyver.add_item(item)
                            game.test_victory(macgyver)
                        macgyver.path += "u"
                elif event.type == pygame.K_DOWN:
                    if maze.test_position(macgyver, "d"):
                        if macgyver.path in game.path_objects:
                            macgyver.add_item(item)
                            game.test_victory(macgyver)
                        macgyver.path += "d"
                display.update(hero)