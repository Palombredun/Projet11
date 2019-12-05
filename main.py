import pygame
from pygame.locals import *

from app.models.hero import Hero
from app.models.labyrinth import Labyrinth

from app.controllers.game import Game

from app.views.display import Display


game = Game()
maze = Labyrinth()
game.place_enemy(maze.tree.leaves)
game.place_objects(maze.tree.leaves)

macgyver = Hero()
display = Display()

display.draw_maze(maze.tree)
display.draw_hero()
display.draw_items(game.path_objects)
display.draw_enemy(game.path_enemy)




while game.defeat is False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.defeat = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        move = game.test_position(maze.tree, macgyver, "left")
        if move:
            macgyver.path += "l"
    if keys[pygame.K_RIGHT]:
        move = game.test_position(maze.tree, macgyver, "right")
        if move:
            macgyver.path += "r"
    if keys[pygame.K_UP]:
        move = game.test_position(maze.tree, macgyver, "up")
        if move:
            macgyver.path += "u"
    if keys[pygame.K_DOWN]:
        move = game.test_position(maze.tree, macgyver, "down")
        if move:
            macgyver.path += "d"