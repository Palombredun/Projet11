from app.models.hero import Hero
from app.models.labyrinth import Labyrinth

from app.controllers.game import Game

# from app.views.display import Display


game = Game()
maze = Labyrinth()
game.place_enemy(maze.tree.leaves)
game.place_objects(maze.tree.leaves)

macgyver = Hero()
display = Display()

display.draw_maze(maze.tree, macgyver.path, game.path_enemy, game.path_objects)


while game.victory is False or game.defeat is False:
    # get keys touched by player
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.KEY_Q:
                break
            elif event.type == pygame.KEY_LEFT:
                move = game.test_position(maze, macgyver, "left")
                if move:
                    hero.path += "l"
            elif event.type == pygame.KEY_RIGHT:
                move = game.test_position(maze, macgyver, "right")
                if move:
                    hero.path += "r"
            elif event.type == pygame.KEY_UP:
                move = game.test_position(maze, macgyver, "up")
                if move:
                    hero.path += "u"
            elif event.type == pygame.KEY_DOWN:
                move = game.test_position(maze.tree, macgyver, "down")
                if move:
                    hero.path += "d"