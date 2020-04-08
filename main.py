import pygame
from pygame.locals import *

from app.models.hero import Hero
from app.models.labyrinth import Labyrinth

from app.controllers.game import Game

from app.views.display import Display


game = Game()
maze = Labyrinth()
maze.generate_maze()
game.place_enemy(maze.tree.leaves)
game.place_objects(maze.tree.leaves)
items = {"needle": game.needle, "tube": game.tube, "ether": game.ether}

macgyver = Hero()
display = Display()

display.draw_maze(maze.tree)
display.draw_hero()
display.draw_enemy(game.path_enemy)
display.draw_items(items)
display.explanations()

while (game.victory == False) and (game.defeat == False):
    for event in pygame.event.get():
        # determin if X was clicked
        if event.type == pygame.QUIT:
            game.defeat = True
        if event.type == pygame.KEYDOWN:
            # determine if a directional key was pressed
            if event.key == pygame.K_RIGHT:
                direction = "r"
            elif event.key == pygame.K_LEFT:
                direction = "l"
            elif event.key == pygame.K_UP:
                direction = "d"
            elif event.key == pygame.K_DOWN:
                direction = "u"
            if game.test_position(maze.tree, macgyver, direction):
                prev = macgyver.path
                macgyver.path += direction

                is_victory = game.test_victory(macgyver)
                if is_victory == "defeat":
                    game.defeat = True
                    display.defeat_message()
                elif is_victory is True:
                    game.victory = True
                    display.victory_message()
                if game.test_item(macgyver):
                    macgyver.items += 1
                display.update(maze.tree, macgyver.path, prev)
