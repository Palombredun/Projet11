from app.models.tree import Tree
from app.models.hero import Hero

from app.controllers.game import Game


def test_victory_run(): 
    maze = Tree("p")
    # build maze (on a 4x4 grid)
    maze.add_node(path="", direction=(0,1), value="p")
    maze.add_node(path="r", direction=(0,1), value="p")
    maze.add_node(path="rr", direction=(1,0), value="p")
    maze.add_node(path="rru", direction=(0,1), value="p")
    maze.add_node(path="rrur", direction=(-1,0), value="p") # leaf
    maze.add_node(path="rru", direction=(1,0), value="p")
    maze.add_node(path="rruu", direction=(1,0), value="p")
    maze.add_node(path="rruu", direction=(1,0), value="p")
    maze.add_node(path="rruuu", direction=(0,1), value="p")
    maze.add_node(path="rruuur", direction=(-1,0), value="p") # leaf
    maze.add_node(path="rruuu", direction=(0,-1), value="p")
    maze.add_node(path="rruuul", direction=(0,-1), value="p")
    maze.add_node(path="rruuull", direction=(-1,0), value="p")
    maze.add_node(path="rruuulld", direction=(0,1), value="p") # leaf
    maze.add_node(path="rruuulld", direction=(-1,0), value="p")
    maze.add_node(path="rruuulldd", direction=(0,1), value="p") # leaf
       
    macgyver = Hero()
    game = Game()
    game.path_enemy = "rruuullddr"
    game.needle = "rrurd"
    game.ether = "rruuurd"
    game.tube = "rruuulldr"
    # victory_path allows to avoid to mock key inputs
    victory_path = "rrurduluurdullldrldr"

    for direction in victory_path:
        if game.test_position(maze, macgyver, direction):
            macgyver.path += direction
            is_victory = game.test_victory(macgyver)
            if is_victory == "defeat":
                game.defeat = True
            elif is_victory is True:
                game.victory = True
            if game.test_item(macgyver):
                macgyver.items += 1
    assert game.victory == True

def test_defeat_run():
    maze = Tree("p")
    # build maze (on a 4x4 grid)
    maze.add_node(path="", direction=(0,1), value="p")
    maze.add_node(path="r", direction=(0,1), value="p")
    maze.add_node(path="rr", direction=(1,0), value="p")
    maze.add_node(path="rru", direction=(0,1), value="p")
    maze.add_node(path="rrur", direction=(-1,0), value="p") # leaf
    maze.add_node(path="rru", direction=(1,0), value="p")
    maze.add_node(path="rruu", direction=(1,0), value="p")
    maze.add_node(path="rruu", direction=(1,0), value="p")
    maze.add_node(path="rruuu", direction=(0,1), value="p")
    maze.add_node(path="rruuur", direction=(-1,0), value="p") # leaf
    maze.add_node(path="rruuu", direction=(0,-1), value="p")
    maze.add_node(path="rruuul", direction=(0,-1), value="p")
    maze.add_node(path="rruuull", direction=(-1,0), value="p")
    maze.add_node(path="rruuulld", direction=(0,1), value="p") # leaf
    maze.add_node(path="rruuulld", direction=(-1,0), value="p")
    maze.add_node(path="rruuulldd", direction=(0,1), value="p") # leaf
       
    macgyver = Hero()
    game = Game()
    game.path_enemy = "rruuullddr"
    game.needle = "rrurd"
    game.ether = "rruuurd"
    game.tube = "rruuulldr"
    # victory_path allows to avoid to mock key inputs
    victory_path = "rruuullddr"

    for direction in victory_path:
        if game.test_position(maze, macgyver, direction):
            macgyver.path += direction
            is_victory = game.test_victory(macgyver)
            if is_victory == "defeat":
                game.defeat = True
            elif is_victory is True:
                game.victory = True
            if game.test_item(macgyver):
                macgyver.items += 1
    assert game.defeat == True