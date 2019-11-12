#!/usr/bin/env python3


class Position:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def __repr__(self):
        return str(self.coordinates)

    def __add__(self, position: 'Position', direction: tuple):
        self.x += direction
        self.y += direction
        position.coordinates[0] += direction[0]
        position.coordinates[1] += direction[1]
        print("path :", position.path)
        print("coordinates :", position.coordinates)
        return position