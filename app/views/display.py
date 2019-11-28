import pygame
from pygame.locals import *

import config.settings as cst


class Display:
    def __init__(self):
        pygame.init()
        self.view = pygame.display.set_mode((64*cst.LENGTH, 64*cst.WIDTH))

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

    def draw_maze(self, tree: "Tree", hero: "Hero", path_enemy: str, path_object: str, ):
        i, j = 0, 0
        for leaf_path in tree.leaves:
            for index in range(1, len(leaf_path) + 2):
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

                if current.left and current.up and current.right:
                    self.view.blit(self.left_up_right, (64*i, 64*j))
                elif current.left and current.up and current.down:
                    self.view.blit(self.left_up_down, (64*i, 64*j))
                elif current.left and current.right and current.down:
                    self.view.blit(self.left_right_down, (64*i, 64*j))
                elif current.up and current.right and current.down:
                    self.view.blit(self.up_right_down, (64*i, 64*j))

                elif current.left and current.up:
                    self.view.blit(self.left_up, (64*i, 64*j))
                elif current.left and current.right:
                   self.view.blit( self.left_right, (64*i, 64*j))
                elif current.left and current.down:
                    self.view.blit(self.left_down, (64*i, 64*j))
                elif current.up and current.right:
                    self.view.blit(self.up_right, (64*i, 64*j))
                elif current.up and current.down:
                    self.view.blit(self.up_down, (64*i, 64*j))
                elif current.right and current.down:
                    self.view.blit(self.right_down, (64*i, 64*j))

                elif current.left:
                    self.view.blit(self.left, (64*i, 64*j))
                elif current.right:
                    self.view.blit(self.right, (64*i, 64*j))
                elif current.up:
                    self.view.blit(self.up, (64*i, 64*j))
                elif current.down:
                    self.view.blit(self.down, (64*i, 64*j))
                
        pygame.display.flip()