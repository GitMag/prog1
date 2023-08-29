"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game.
"""


class Character:
    """
    This class defines what a character is int he game and what
    he or she can do.
    """

    # TODO: copy your Character class implementation from
    #       the previous assignment here and implement the
    #       following new methods.
    #
    #       Also note, that you have to modify at least
    #       __init__ and printout methods to conform with
    #       the new bahavior of the class.

    def __init__(self, hero_name, hero_health):

        # set hero name
        self.__name = hero_name

        # set hero health
        self.__health = hero_health

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

        # check if there are at least one item with specified name
        elif self.how_many(item) == 1:
            # only one item in inventory, delete it completely
            del self.__items[item]
        # if char doesn't have the item we do nothing

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
        print(f"Hitpoints: {self.__health}")

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

    def pass_item(self, item, target):
        """
        Passes (i.e. transfers) an item from one person (self)
        to another (target).

        :param item: str, the name of the item in self's inventory
                     to be given to target.
        :param target: Character, the target to whom the item is to
                     to be given.
        :return: True, if passing the item to target was successful.
                 False, it passing the item failed for any reason.
        """

        # we check if we have the item we want to pass:
        if self.has_item(item):
            # give one amount of item to target and remove one amount from self
            target.give_item(item)
            self.remove_item(item)
            return True

        # we don't have the item, passing was unsuccessfully
        return False

    def attack(self, target, weapon):
        """
        A character (self) attacks the target using a weapon.
        This method will also take care of all the printouts
        relevant to the attack.

        There are three error conditions:
          (1) weapon is unknown i.e. not a key in WEAPONS dict.
          (2) self does not have the weapon used in the attack
          (3) character tries to attack him/herself.
        You can find the error message to printed in each case
        from the example run in the assignment.

        The damage the target receives if the attack succeeds is
        defined by the weapon and can be found as the payload in
        the WEAPONS dict. It will be deducted from the target's
        hitpoints. If the target's hitpoints go down to zero or
        less, the target is defeated.

        The format of the message resulting from a successful attack and
        the defeat of the target can also be found in the assignment.

        :param target: Character, the target of the attack.
        :param weapon: str, the name of the weapon used in the attack
                       (must be exist as a key in the WEAPONS dict).
        :return: True, if attack succeeds.
                 False, if attack fails for any reason.
        """

        # check if weapon does not exist in WEAPONS dict
        if weapon not in WEAPONS.keys():
            print(f'Attack fails: unknown weapon "{weapon}".')
            return False

        # check if item trying to attack self
        if self == target:
            print(f"Attack fails: {self.__name} can't attack him/herself.")
            return False

        # check if char does not have weapon
        if not self.has_item(weapon):
            print(f"""Attack fails: {self.__name} doesn't have """
                  f""""{weapon}".""")
            return False

        # checks complete we can attack. Check damage amount
        damage_to_deal = WEAPONS[weapon]

        # reduce target health by damage_amount
        target.__health -= damage_to_deal
        print(f"{self.__name} attacks {target.__name} delivering"
              f" {damage_to_deal} damage.")

        # check if target died
        if target.__health < 1:
            print(f"{self.__name} successfully defeats {target.__name}.")

        return True


WEAPONS = {
    # Weapon          Damage
    # --------------   ------
    "elephant gun": 15,
    "gun": 5,
    "light saber": 50,
    "sword": 7,
}


def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)

    # Testing the pass_item method

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()

    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword")  # Conan doesn't have a sword.
    conan.attack(conan, "gun")  # A character is not allowed to attack himself.
    conan.attack(conan, "pen")  # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")  # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword")  # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")  # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()


if __name__ == "__main__":
    main()

