"""
COMP.CS.100 Programming 1
Code template for geometric patterns.
"""
import math

PI = math.pi


def calculate_square(side1):
    """
    Calculates the area and circumfence of the square by getting inputs
     from the user
    :return: float,  the area and circumfence
    """
    circumfence = side1 * 4
    area = side1 * side1
    return circumfence, area


def calculate_rectangle(side1, side2):
    """
    Calculates the area and circumfence of the rectangle by getting inputs
     from the user
    :return: float,  the area and circumfence
    """
    circumfence = side1 * 2 + side2 * 2
    area = side1 * side2
    return circumfence, area


def calculate_circle(r):
    """
    Calculates the area and circumfence of the circle by getting inputs
     from the user
    :return: float,  the area and circumfence
    """
    circumfence = 2* PI * r
    area = PI * r * r
    return circumfence, area


def input_circle():
    """
    Gets inputs from the user to calculate the the area and cicumfence
    :return: float, the area and circumfence
    """
    while True:
        r = float(input("Enter the circle's radius: "))
        if r > 0:
            return r


def input_square():
    """
    Gets inputs from the user to calculate the the area and cicumfence
    :return: float, the area and circumfence
    """
    while True:
        side1 = float(input("Enter the length of the square's side: "))
        if side1 > 0:
            return side1


def input_rectangle():
    """
    Gets inputs from the user to calculate the the area and cicumfence
    :return: float, the area and circumfence
    """
    while True:
        side1 = float(input("Enter the length of the rectangle's side 1: "))
        if side1 > 0:
            break
    while True:
        side2 = float(input("Enter the length of the rectangle's side 2: "))
        if side2 > 0:
            break
    return side1, side2



def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            side1 = input_square()
            circ, area = calculate_square(side1)
            print(f"The circumference is {circ:.2f}")
            print(f"The surface area is {area:.2f}")
            pass

        elif answer == "r":
            side1, side2 = input_rectangle()
            circ, area = calculate_rectangle(side1, side2)
            print(f"The circumference is {circ:.2f}")
            print(f"The surface area is {area:.2f}")
            pass

        elif answer == "c":
            radius = input_circle()
            circ, area = calculate_circle(radius)
            print(f"The circumference is {circ:.2f}")
            print(f"The surface area is {area:.2f}")
            pass

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()


def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()
