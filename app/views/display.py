import pygame
from pygame.locals import *

import config.settings as cst


class Display:
    def __init__(self):
        pygame.init()
        self.dx = 40
        self.dy = 40

        self.view = pygame.display.set_mode((self.dx * cst.LENGTH, self.dy * cst.WIDTH))

        self.macgyver = pygame.image.load("resources/MacGyver.png").convert()
        self.enemy = pygame.image.load("resources/enemy.png").convert()
        self.ether = pygame.image.load("resources/ether.png").convert()
        self.needle = pygame.image.load("resources/needle.png").convert()
        self.tube = pygame.image.load("resources/tube.png").convert()

        self.left = pygame.image.load("resources/left.jpg").convert()
        self.right = pygame.image.load("resources/right.jpg").convert()
        self.up = pygame.image.load("resources/up.jpg").convert()
        self.down = pygame.image.load("resources/down.jpg").convert()

        self.left_down = pygame.image.load("resources/left_down.jpg").convert()
        self.left_right = pygame.image.load("resources/left_right.jpg").convert()
        self.left_up = pygame.image.load("resources/left_up.jpg").convert()
        self.right_down = pygame.image.load("resources/right_down.jpg").convert()
        self.up_down = pygame.image.load("resources/up_down.jpg").convert()
        self.right_up = pygame.image.load("resources/right_up.jpg").convert()

        self.left_right_down = pygame.image.load("resources/left_right_down.jpg").convert()
        self.left_up_down = pygame.image.load("resources/left_up_down.jpg").convert()
        self.left_right_up = pygame.image.load("resources/left_right_up.jpg").convert()
        self.right_up_down = pygame.image.load("resources/right_up_down.jpg").convert()

    def draw_maze(self, tree: "Tree"):
        # Place the first case
        if tree.root.right and not tree.root.up:
            self.view.blit(self.right, (0, 0))
        elif not tree.root.right and tree.root.up:
            self.view.blit(self.up, (0, 0))
        elif tree.root.right and tree.root.up:
            self.view.blit(self.right_up, (0, 0))

        #explore the leaves to place each case
        for path in tree.leaves:
            current_path = ""
            i, j = 0, 0
            for direction in path:
                current_path += direction

                if direction == "d":
                    j += -1
                elif direction == "u":
                    j += 1
                elif direction == "l":
                    i -= 1
                elif direction == "r":
                    i += 1

                curr = tree.huffman_traversal(current_path)
                if curr.left and curr.right and curr.up:
                    self.view.blit(self.left_right_up, (self.dx * i, self.dy * j))
                elif curr.left and curr.up and curr.down:
                    self.view.blit(self.left_up_down, (self.dx * i, self.dy * j))
                elif curr.left and curr.right and curr.down:
                    self.view.blit(self.left_right_down, (self.dx * i, self.dy * j))
                elif curr.right and curr.up and curr.down:
                    self.view.blit(self.right_up_down, (self.dx * i, self.dy * j))

                elif curr.left and curr.up:
                    self.view.blit(self.left_up, (self.dx * i, self.dy * j))
                elif curr.left and curr.right:
                    self.view.blit(self.left_right, (self.dx * i, self.dy * j))
                elif curr.left and curr.down:
                    self.view.blit(self.left_down, (self.dx * i, self.dy * j))
                elif curr.right and curr.up:
                    self.view.blit(self.right_up, (self.dx * i, self.dy * j))
                elif curr.up and curr.down:
                    self.view.blit(self.up_down, (self.dx * i, self.dy * j))
                elif curr.right and curr.down:
                    self.view.blit(self.right_down, (self.dx * i, self.dy * j))



                elif curr.left:
                    self.view.blit(self.left, (self.dx * i, self.dy * j))
                elif curr.right:
                    self.view.blit(self.right, (self.dx * i, self.dy * j))
                elif curr.up:
                    self.view.blit(self.up, (self.dx * i, self.dy * j))
                elif curr.down:
                    self.view.blit(self.down, (self.dx * i, self.dy * j))

        pygame.display.flip()

    def draw_hero(self):
        """
        Place the hero on (0, 0)
        """
        self.view.blit(self.macgyver, (6, 6))
        pygame.display.flip()

    def draw_items(self, path_items: dict):
        """
        input :
            - dictionnary containing, for each item, their path
        output :
            - draw the items on top of the maze
        """
        for item, path in path_items.items():
            i, j = 0, 0
            for direction in path:
                if direction == "l":
                    i += -1
                elif direction == "r":
                    i += 1
                elif direction == "u":
                    j += -1
                elif direction == "d":
                    j += 1
            if item == "ether":
                self.view.blit(self.ether, (6 + 32 * i, 6 + 32 * j))
            if item == "needle":
                self.view.blit(self.needle, (6 + 32 * i, 6 + 32 * j))
            if item == "tube":
                self.view.blit(self.tube, (6 + 32 * i, 6 + 32 * j))
        pygame.display.flip()

    def draw_enemy(self, path_enemy: str):
        """
        input :
            - enemy's path on the tree
        output :
            - draw the enemy on top of the maze
        """

        for direction in path_enemy:
            i, j = 0, 0
            if direction == "l":
                i += -1
            elif direction == "r":
                i += 1
            elif direction == "u":
                j += -1
            elif direction == "d":
                j += 1
        self.view.blit(self.enemy, (6 + 32 * i, 6 + 32 * j))
        pygame.display.flip()

    def update(self, tree: "Tree", hero: "Hero"):
        """

        """
        curr = tree.huffman_traversal(hero.path[:-1])

        i, j = 0, 0
        for direction in hero.path[:-1]:
            if direction == "l":
                i += -1
            elif direction == "r":
                i += 1
            elif direction == "u":
                j += -1
            elif direction == "d":
                j += 1

        if curr.left and curr.right and curr.up and not curr.down:
            self.view.blit(self.left_right_up, (32 * i, 32 * j))
        elif curr.left and curr.up and curr.down:
            self.view.blit(self.left_up_down, (32 * i, 32 * j))
        elif curr.left and curr.right and curr.down:
            self.view.blit(self.left_right_down, (32 * i, 32 * j))
        elif curr.right and curr.up and curr.down:
            self.view.blit(self.right_up_down, (32 * i, 32 * j))
        
        elif curr.left and curr.up:
            self.view.blit(self.left_up, (32 * i, 32 * j))
        elif curr.left and curr.right:
            self.view.blit(self.left_right, (32 * i, 32 * j))      
        elif curr.left and curr.down:
            self.view.blit(self.left_down, (32 * i, 32 * j))        
        elif curr.right and curr.up:
            self.view.blit(self.right_up, (32 * i, 32 * j))
        elif curr.up and curr.down:
            self.view.blit(self.up_down, (32 * i, 32 * j))
        elif curr.right and curr.down:
            self.view.blit(self.right_down, (32 * i, 32 * j))
        
        elif curr.left:
            self.view.blit(self.left, (32 * i, 32 * j))
        elif curr.right:
            self.view.blit(self.right, (32 * i, 32 * j))
        elif curr.up:
            self.view.blit(self.up, (32 * i, 32 * j))
        elif curr.down:
            self.view.blit(self.down, (32 * i, 32 * j))

        for direction in hero.path:
            i, j = 0, 0
            if direction == "d":
                i += -1
            elif direction == "u":
                i += 1
            elif direction == "l":
                j += -1
            elif direction == "r":
                j += 1
        self.view.blit(self.macgyver, (6 + 32 * i, 6 + 32 * j))
        pygame.display.flip()