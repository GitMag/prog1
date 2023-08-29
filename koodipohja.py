"""
COMP.CS.100 Programming 1
Assignment "Improved Box Printing" code template
"""

# TODO: the definition of print_box goes here unless it goes after main.


def print_box(width, height, border_mark="#", inner_mark=" "):
    """
    We print a box with different outer and inner characters according to user
    selection. We assume default characters if not input is typed.
    :param width: int, width of the box
    :param height: int, height of the box
    :param border_mark: str,the mark used to draw the outer box
    :param inner_mark: str, the mark used to draw the inner box
    :return:
    """
    inner_box_width = width - 2
    for row in range(height):
        if row == 0 or row == height - 1:
            print(width * border_mark)
            continue
        else:
            print(border_mark, end="")
            print(inner_box_width * inner_mark, end="")
            print(border_mark)


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


# TODO: the definition of print_box could also go here, it is up to you.


if __name__ == "__main__":
    main()
