"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""

class Character:

    def __init__(self, hero_name):

        # set hero name
        self.__name = hero_name

        # initialize items as dict with <key>=item and <value>=amount of that
        # item
        self.__items = {}

    def give_item(self, item):
        """
        Gives item with specified name to Character. If item already exist
        amount of item is increased by 1.

        :param item: str, name of item.
        """
        # check if item already exists in inventory
        if not self.has_item(item):
            # does not exist, we create item and set value (amount) to 1
            self.__items[item] = 1
        else:
            # item already exists, we increment the value of that item with 1
            self.__items[item] += 1

    def remove_item(self, item):
        """
        Removes one amount of specified item from inventory. If only one exists
        the whole item is removed.

        :param item: str, name of item.
        :return:
        """
        # remove one amount of specified <item> from items inventory
        # we check if there are more than of specified item
        if self.how_many(item) > 1:
            self.__items[item] -= 1
        else:
            # only one item in inventory, delete it completely
            del self.__items[item]

    def has_item(self, item):
        """
        Checks if item exist in inventroy. Returns True or False.

        :param item: str, name of item.
        :return: bool, value for the test if item exists or not
        """
        # function to check if specified item is in items inventory
        if item in self.__items:
            return True
        return False

    def how_many(self, item):
        """
        Returns amount of a specified item in inventory

        :param item: str, name of item
        :return: int, the amount of specified item in inventory
        """
        # searches the items inventory with <key> items and gets the amount
        # of the item as the <value>
        if self.has_item(item):
            return self.__items[item]
        else:
            # item does not exist, so 0 of that item
            return 0

    def printout(self):
        """
        Prints out al the items and their amount in the items inventory
        in a formatted way.
        """

        print(f"Name: {self.__name}")

        # check if there are items in inventory
        if len(self.__items) > 0:
            # loop trough items in inventory
            for item in sorted(self.__items):
                # get the amount of items by setting item as the key
                print(f"  {self.how_many(item)} {item}")
        else:
            # no items in inventory
            print("  --nothing--")

    def get_name(self):
        """
        Gets character name.
        :return: str, name of character
        """
        # returns the name of the hero
        return self.__name


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
