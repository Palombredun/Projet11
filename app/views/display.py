import pygame
from pygame.locals import *

import config.settings as cst


class Display:
    def __init__(self):
        pygame.init()
        self.view = pygame.display.set_mode((32 * cst.LENGTH, 32 * cst.WIDTH))

        self.macgyver = pygame.image.load("resources/MacGyver.png").convert()
        self.enemy = pygame.image.load("resources/enemy.png").convert_alpha()
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
        self.left_up_down = pygame.image.load("resources/left_up_down.jpg").convert()
        self.left_up_right = pygame.image.load("resources/left_up_right.jpg").convert()
        self.up_right_down = pygame.image.load("resources/up_right_down.jpg").convert()

    def draw_maze(self, tree: "Tree"):

        if tree.root.right and not tree.root.down:
            self.view.blit(self.right, (0, 0))
        elif not tree.root.right and tree.root.down:
            self.view.blit(self.down, (0, 0))
        elif tree.root.right and tree.root.down:
            self.view.blit(self.right_down, (0, 0))

        for path in tree.leaves:
            current_path = ""
            i, j = 0, 0
            for direction in path:
                current_path += direction

                if direction == "l":
                    i += -1
                elif direction == "r":
                    i += 1
                elif direction == "u":
                    j += -1
                elif direction == "d":
                    j += 1

                current_node = tree.huffman_traversal(current_path)

                if current_node.left and current_node.up and current_node.right:
                    self.view.blit(self.left_up_right, (32 * i, 32 * j))
                elif current_node.left and current_node.up and current_node.down:
                    self.view.blit(self.left_up_down, (32 * i, 32 * j))
                elif current_node.left and current_node.right and current_node.down:
                    self.view.blit(self.left_right_down, (32 * i, 32 * j))
                elif current_node.up and current_node.right and current_node.down:
                    self.view.blit(self.up_right_down, (32 * i, 32 * j))

                elif current_node.left and current_node.up:
                    self.view.blit(self.left_up, (32 * i, 32 * j))
                elif current_node.left and current_node.right:
                    self.view.blit(self.left_right, (32 * i, 32 * j))
                elif current_node.left and current_node.down:
                    self.view.blit(self.left_down, (32 * i, 32 * j))
                elif current_node.up and current_node.right:
                    self.view.blit(self.up_right, (32 * i, 32 * j))
                elif current_node.up and current_node.down:
                    self.view.blit(self.up_down, (32 * i, 32 * j))
                elif current_node.right and current_node.down:
                    self.view.blit(self.right_down, (32 * i, 32 * j))

                elif current_node.left:
                    self.view.blit(self.left, (32 * i, 32 * j))
                elif current_node.right:
                    self.view.blit(self.right, (32 * i, 32 * j))
                elif current_node.up:
                    self.view.blit(self.up, (32 * i, 32 * j))
                elif current_node.down:
                    self.view.blit(self.down, (32 * i, 32 * j))

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
        previous = tree.huffman_traversal(hero.path[:-1])

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

        if previous.left and previous.up and previous.right:
            self.view.blit(self.left_up_right, (32 * i, 32 * j))
        elif previous.left and previous.up and previous.down:
            self.view.blit(self.left_up_down, (32 * i, 32 * j))
        elif previous.left and previous.right and previous.down:
            self.view.blit(self.left_right_down, (32 * i, 32 * j))
        elif previous.up and previous.right and previous.down:
            self.view.blit(self.up_right_down, (32 * i, 32 * j))
        elif previous.left and previous.up:
            self.view.blit(self.left_up, (32 * i, 32 * j))
        elif previous.left and previous.right:
            self.view.blit(self.left_right, (32 * i, 32 * j))
        elif previous.left and previous.down:
            self.view.blit(self.left_down, (32 * i, 32 * j))
        elif previous.up and previous.right:
            self.view.blit(self.up_right, (32 * i, 32 * j))
        elif previous.up and previous.down:
            self.view.blit(self.up_down, (32 * i, 32 * j))
        elif previous.right and previous.down:
            self.view.blit(self.right_down, (32 * i, 32 * j))
        elif previous.left:
            self.view.blit(self.left, (32 * i, 32 * j))
        elif previous.right:
            self.view.blit(self.right, (32 * i, 32 * j))
        elif previous.up:
            self.view.blit(self.up, (32 * i, 32 * j))
        elif previous.down:
            self.view.blit(self.down, (32 * i, 32 * j))

        for direction in hero.path:
            i, j = 0, 0
            if direction == "l":
                i += -1
            elif direction == "r":
                i += 1
            elif direction == "u":
                j += -1
            elif direction == "d":
                j += 1
        self.view.blit(self.macgyver, (6 + 32 * i, 6 + 32 * j))
        pygame.display.flip()