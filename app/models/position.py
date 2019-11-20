#!/usr/bin/env python3


class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def up(self) -> "Position":
        x = self.x
        y = self.y
        return Position(x - 1, y)

    def down(self) -> "Position":
        x = self.x
        y = self.y
        return Position(x + 1, y)

    def left(self) -> "Position":
        x = self.x
        y = self.y
        return Position(x, y - 1)

    def right(self) -> "Position":
        x = self.x
        y = self.y
        return Position(x, y + 1)

    def __str__(self):
        string = "(" + str(self.x) + ", " + str(self.y) + ")"
        return string

    def __iadd__(self, direction: tuple) -> "Position":
        x = self.x + direction[0]
        y = self.y + direction[1]
        new_position = Position(x, y)
        return new_position
