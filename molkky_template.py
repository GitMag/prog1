"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.
"""


# TODO:
# a) Implement the class Player here.
class Player:

    def __init__(self, name):
        self.__name = name
        self.__points = 0
        self.__total_points = 0
        self.__rounds_played = 0
        self.__hit_rounds = 0

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def set_points(self, points):
        self.__points = points

    def points_tracking(self, points):
        self.__total_points += points
        self.__rounds_played += 1
        if points > 0:
            self.__hit_rounds += 1

    def hit_percentage(self):
        if self.__hit_rounds > 0:
            return round(self.__hit_rounds / self.__rounds_played * 100, 1)
        return 0.0

    def check_cheer(self, current_points):

        if self.__rounds_played != 1:
            avg_points = self.__total_points / self.__rounds_played
            if current_points > avg_points:
                print(f"Cheers {self.get_name()}!")

    def add_points(self, points):
        new_points = self.get_points() + points
        if new_points > 50:
            print(f"{self.get_name()} gets penalty points!")
            self.set_points(25)
        else:
            self.set_points(new_points)

        # we check if we need to congratulate
        if 40 <= new_points <= 49:
            points_needed = 50- new_points
            print(f"{self.get_name()} needs only {points_needed} points. It's"
                  " better to avoid knocking down the pins with"
                  " higher points.")

        # add points to point list
        self.points_tracking(points)
        self.check_cheer(points)

    def has_won(self):
        if self.get_points() == 50:
            return True
        return False


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        # TODO:
        # c) Add a supporting feedback printout "Cheers NAME!" here.

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p, hit percentage", player1.hit_percentage())  # TODO: d)
        print(player2.get_name() + ":", player2.get_points(), "p, hit percentage", player2.hit_percentage())  # TODO: d)
        print("")

        throw += 1


if __name__ == "__main__":
    main()
