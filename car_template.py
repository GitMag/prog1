"""
COMP.CS.100 Programming 1 code template
Fill in all TODOs in this file
Car driving program
"""
from math import sqrt


def menu():
    """
    This is a text-based menu. You should ONLY TOUCH TODOs inside the menu.
    TODOs in the menu call functions that you have implemented and take care
    of the return values of the function calls.
    """

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(tank_size, fill_amount, current_fuel_level):
    """
    This function has three parameters which are all FLOATs:
      (1) the size of the tank
      (2) the amount of gas that is requested to be filled in
      (3) the amount of gas in the tank currently

    The parameters have to be in this order.
    The function returns one FLOAT that is the amount of gas in the
    tank AFTER the filling up.

    The function does not print anything and does not ask for any
    input.
    """
    new_fuel_level = float(current_fuel_level + fill_amount)
    if new_fuel_level > tank_size:
        return tank_size
    return new_fuel_level


def drive(x, y, new_x, new_y, gas, gas_consumption):
    # pythagoran theroeum a^2 +b^2 = c^2
    # c^2 = a^2+b^2
    # sqrt(a^2+b^2) distance
    """
    This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car

    The parameters have to be in this order.
    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate

    The return values have to be in this order.
    The function does not print anything and does not ask for any
    input.
    """
    # we calculate the distance
    distance_to_drive = calculate_distance(x, y, new_x, new_y)

    gas, new_x, new_y = new_location(x, y, new_x, new_y, gas, gas_consumption, distance_to_drive)
    return gas, new_x, new_y
    # It might be usefull to make one or two assisting functions
    # to help the implementation of this function.

    # Implement your own functions here. You are required to
    # implement at least two functions that take at least
    # one parameter and return at least one value.  The
    # functions have to be used somewhere in the program.


def new_location(x, y, new_x, new_y , gas, gas_consumption, distance_to_drive):
    """
    Calculates the new location for the car based on passed on params
    :param x: float, the old x location
    :param y: float, the old y location
    :param new_x: float, the new x location
    :param new_y: float, the new y location
    :param gas: float, the ammount of gas in the tank
    :param gas_consumption: float, gas consumption per 100 km
    :param distance_to_drive: the distance the car should move
    :return: returns the gas left in the tank after driving and new x and y
    locations for the car
    """
    slope = 1
    max_distance = (gas * 100) / gas_consumption
    realistic_distance_factor = 1
    if max_distance < distance_to_drive:
        realistic_distance_factor = max_distance / distance_to_drive
        distance_to_drive = realistic_distance_factor * distance_to_drive
        slope = (new_y - y) / (new_x - x)
        if int(slope) == 0:
            slope = 1
    new_x = realistic_distance_factor * slope * new_x
    new_y = realistic_distance_factor * slope * new_y
    gas = gas - (gas_consumption * distance_to_drive) / 100
    return gas, new_x, new_y


def calculate_distance(x, y, new_x, new_y):
    """
    Calculates the distance the car should drive
    :param x: float, old x location
    :param y: float, old y location
    :param new_x: float, the new x location
    :param new_y: float, the new y location
    :return: float, the distance the car will drive
    """
    return sqrt((new_x - x) ** 2 + (new_y - y) ** 2)
    pass


def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH THIS FUNCTION.
    This function reads input from the user.
    Also, don't worry if you don't understand it.
    """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()
