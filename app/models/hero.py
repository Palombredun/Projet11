from .path import Path


class Hero:
    def __init__(self):
        self.path = Path("")
        self.items = set()

    def add_item(self, item):
        """
        input :
        Item name
        Check that the item is authorized, if so add it to the stash.
        During the game, if the number of item is three, victory can be completed.  
        """
        if item in ["needle", "tube", "ether"]:
            self.items.add(item)
        else:
            raise ValueError("This item is not needed")