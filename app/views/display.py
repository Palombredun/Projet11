import pygame
from pygame.locals import *

import config.settings as cst


class Display:
    def __init__():
        self.macgyver = pygame.image.load("resources/MacGyver.png").convert()
        self.enemy = pygame.image.load("resources/enemy.png").convert()
        self.ether = pygame.image.load("resources/ether.png").convert()
        self.needle = pygame.image.load("resources/needle.png").convert()
        self.tube = pygame.image.load("resources/tube.jpg").convert()

        self.left = pygame.image.load("resources/left.jpg").convert()
        self.right = pygame.image.load("resources/right.jpg").convert()
        self.up = pygame.image.load("resources/up.jpg").convert()
        self.down = pygame.image.load("resources/down.jpg").convert()

        self.left_down = pygame.image.load("resources/left_down.jpg").convert()
        self.left_right = pygame.image.load("resources/left_right.jpg").convert()
        self.left_up = pygame.image.load("resources/left_up.jpg").convert()
        self.right_down = pygame.image.load("resources/right_down.jpg").convert()
        self.up_down = pygame.image.load("resources/up_down.jpg").convert()
        self.up_right = pygame.image.load("resources/up_right.jpg").convert()

        self.left_right_down = pygame.image.load(
            "resources/left_right_down.jpg"
        ).convert()
        self.left_up_down = pygame.image.load(
            "resources/left_up_down.jpg"
        ).convert()
        self.left_up_right = pygame.image.load(
            "resources/left_up_right.jpg"
        ).convert()
        self.up_right_down = pygame.image.load(
            "resources/up_right_down.jpg"
        ).convert()

    def draw_maze(self, tree: "Tree", hero: "Hero"):
        pygame.init()
        pygame.display.set_mode((64 * cst.LENGTH, 64 * cst.WIDTH))

        i, j = 0
        for leaf_path in tree.leafs:
            for index in range(len(leaf_path) + 1):
                current_path = leaf_path[:index]
                if current_path[-1] == "l":
                    j += -1
                elif current_path[-1] == "r":
                    j += 1
                elif current_path[-1] == "u":
                    i += 1
                elif current_path[-1] == "d":
                    i += -1

                current = tree.huffman_traversal(current_path)

                if current.left and current.right:
                    pass
                if current.left and current.up:
                    pass
                if current.left and current.down:
                    pass
                if current.up and current.right:
                    pass
                if current.up and current.down:
                    pass
                if current.left and current.right and current.down:
                    pass
                if current.left and current.up and current.down:
                    pass
                if current.left and current.up and current.right:
                    pass
                if current.up and current.right and current.down:
                    pass
