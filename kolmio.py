"""
Ohjelmointi 1 / Programming 1
Trangle's Area when the Sides Are Known
"""

from math import sqrt


def area(a, b, c):
    """
    :param a: float, lenght of side 1
    :param b: float, lenght of side 2
    :param c: float, lenght of side 3
    :return: returns the area of the triangle calculated from side 1, 2 and 3
    """
    # we calculate s
    s = (a + b + c) / 2
    # we calculate the area of the triangle
    triangle_area = sqrt(s*(s-a)*(s-b)*(s-c))
    return triangle_area

def main():
    side1 = input("Enter the length of the first side: ")
    side2 = input("Enter the length of the second side: ")
    side3 = input("Enter the length of the third side: ")

    print(f"The triangle's area is {area(float(side1),float(side2),float(side3)):.1f}")


if __name__ == "__main__":
    main()
