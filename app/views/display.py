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

        self.left_right_down = pygame.image.load(
            "resources/left_right_down.jpg"
        ).convert()
        self.left_up_down = pygame.image.load("resources/left_up_down.jpg").convert()
        self.left_right_up = pygame.image.load("resources/left_right_up.jpg").convert()
        self.right_up_down = pygame.image.load("resources/right_up_down.jpg").convert()

    def explanations(self):
        print("\n\n")
        print("*******************************************")
        print("*                                         *")
        print("*                                         *")
        print("*           BIENVENUE SUR LE JEU          *")
        print("*      AIDEZ MACGYVER À S'ÉCHAPPER !      *")
        print("*                                         *")
        print("*                                         *")
        print("*******************************************")
        print("\n")
        print("Les règles sont les suivantes :")
        print("  - vous incarnez MacGyver, et commencez toujours en haut à gauche")
        print("  - votre but est de vous échapper du labyrinthe")
        print("  - vous devez récupérer les 3 objets dispersés sur la carte")
        print("    puis vous déplacer jusque sur l'ennemi")
        print("  - pour vous déplacer, utilisez les flèches directionnelles du clavier")
        print("\nBon jeu et bonne chance !")

    def defeat_message(self):
        print("\n")
        print("Vous avez perdu. Vous n'avez pas récupéré tous les objets.\n")

    def victory_message(self):
        print("\n")
        print("Félicitations vous avez gagné !\n")

    def convert(self, path: str):
        i, j = 0, 0
        for direction in path:
            if direction == "l":
                i += -1
            elif direction == "r":
                i += 1
            elif direction == "d":
                j += -1
            elif direction == "u":
                j += 1
        return i, j

    def blit_case(self, node: "Node", i: int, j: int):
        if node.left and node.right and node.up:
            self.view.blit(self.left_right_up, (self.dx * i, self.dy * j))
        elif node.left and node.up and node.down:
            self.view.blit(self.left_up_down, (self.dx * i, self.dy * j))
        elif node.left and node.right and node.down:
            self.view.blit(self.left_right_down, (self.dx * i, self.dy * j))
        elif node.right and node.up and node.down:
            self.view.blit(self.right_up_down, (self.dx * i, self.dy * j))

        elif node.left and node.up:
            self.view.blit(self.left_up, (self.dx * i, self.dy * j))
        elif node.left and node.right:
            self.view.blit(self.left_right, (self.dx * i, self.dy * j))
        elif node.left and node.down:
            self.view.blit(self.left_down, (self.dx * i, self.dy * j))
        elif node.right and node.up:
            self.view.blit(self.right_up, (self.dx * i, self.dy * j))
        elif node.up and node.down:
            self.view.blit(self.up_down, (self.dx * i, self.dy * j))
        elif node.right and node.down:
            self.view.blit(self.right_down, (self.dx * i, self.dy * j))

        elif node.left:
            self.view.blit(self.left, (self.dx * i, self.dy * j))
        elif node.right:
            self.view.blit(self.right, (self.dx * i, self.dy * j))
        elif node.up:
            self.view.blit(self.up, (self.dx * i, self.dy * j))
        elif node.down:
            self.view.blit(self.down, (self.dx * i, self.dy * j))

    def draw_maze(self, tree: "Tree"):
        # Place the first case
        if tree.root.right and not tree.root.up:
            self.view.blit(self.right, (0, 0))
        elif not tree.root.right and tree.root.up:
            self.view.blit(self.up, (0, 0))
        elif tree.root.right and tree.root.up:
            self.view.blit(self.right_up, (0, 0))

        # explore the leaves to place each case
        for path in tree.leaves:
            current_path = ""
            i, j = 0, 0
            for direction in path:
                current_path += direction
                if direction == "l":
                    i -= 1
                elif direction == "r":
                    i += 1
                elif direction == "d":
                    j += -1
                elif direction == "u":
                    j += 1
                curr = tree.huffman_traversal(current_path)
                self.blit_case(curr, i, j)
        pygame.display.flip()

    def draw_hero(self):
        """
        Place the hero on (0, 0)
        """
        self.view.blit(self.macgyver, (6, 6))
        pygame.display.flip()

    def draw_items(self, objects: dict):
        """
        input :
            - dictionnary containing, for each item, their path
        output :
            - draw the items on top of the maze
        """
        for item, path in objects.items():
            i, j = self.convert(path)
            if item == "ether":
                self.view.blit(self.ether, (self.dx * i + 4, self.dy * j + 4))
            if item == "needle":
                self.view.blit(self.needle, (self.dx * i + 4, self.dy * j + 4))
            if item == "tube":
                self.view.blit(self.tube, (self.dx * i + 4, self.dy * j + 4))
        pygame.display.flip()

    def draw_enemy(self, path_enemy: str):
        """
        input :
            - enemy's path on the tree
        output :
            - draw the enemy on top of the maze
        """
        i, j = self.convert(path_enemy)
        self.view.blit(self.enemy, (self.dx * i + 4, self.dy * j + 4))
        pygame.display.flip()

    def update(self, tree: "Tree", hero: "Hero", previous: str):
        """
        Update the visual of the game.
        """
        # remove macgyver from the previous tile
        prev = tree.huffman_traversal(previous.path)
        i, j = self.convert(previous.path)
        self.blit_case(prev, i, j)

        # blit the new tile and make macgyver appear
        curr = tree.huffman_traversal(hero.path)
        i, j = self.convert(hero.path)
        self.blit_case(curr, i, j)
        self.view.blit(self.macgyver, (self.dx * i + 6, self.dy * j + 6))

        pygame.display.flip()
