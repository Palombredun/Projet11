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
#display.draw_hero()
#display.draw_items(game.path_items)
#display.draw_enemy(game.path_enemy)


while (game.victory == False) and (game.defeat == False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.defeat = True

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or
        keys[pygame.K_RIGHT] or
        keys[pygame.K_UP] or
        keys[pygame.K_DOWN]):
        if keys[pygame.K_LEFT]:
            direction = "l"
        if keys[pygame.K_RIGHT]:
            direction = "r"
        if keys[pygame.K_UP]:
            direction = "u"
        if keys[pygame.K_DOWN]:
            direction = "d"

        if game.test_position(maze.tree, macgyver, direction):
            macgyver.path += direction

            if game.test_defeat(macgyver):
                game.defeat = True
            if game.test_victory(macgyver):
                game.victory = True
            if game.test_item(game.path_items, macgyver):
                hero.add_item(macgyver.path)