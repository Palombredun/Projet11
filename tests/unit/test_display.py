import pytest
import pygame

from app.views.display import Display


@pytest.fixture(scope="module")
def view():
    return Display()


def test_init_display(view):
    assert view.dx == 40
    assert view.dy == 40


def test_convert(view):
    path = "uuurrddl"
    i, j = view.convert(path)
    assert (i, j) == (1, 1)
