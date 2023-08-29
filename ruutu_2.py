"""
COMP.CS.100 Programming 1
Print a box with input error checking
"""


def print_box(w, h, c):
    """
    :param w: int, width of the box
    :param h: int, height of the box
    :param c: str, the character used to print the box
    :return:
    """
    """we define the variables to print the square"""
    width = int(w)
    height = int(h)
    char = c
    new_line_limit = height-1
    """we print the square row by row and check if we should add a new line.
    The last line for the square should not be with a new line"""
    print()
    for i in range(height):
        print(width * char, end="")
        if i < new_line_limit:
            print()


def read_input(text):
    """
    Reads the inputs of the user and retries until a valid input has been
    entered
    :param text: str, the text to display in the input field
    :return: returns the input typed by the user
    """
    while True:
        # we catch an excpetion if conversion of input to int is not possible
        try:
            value = int(input(text))
            if value > 0:
                return value
        except ValueError:
            # we pass and ask for new input until valid input has been inputted
            pass


def main():
        width = read_input("Enter the width of a frame: ")
        height = read_input("Enter the height of a frame: ")
        mark = input("Enter a print mark: ")
        print_box(width, height, mark)


if __name__ == "__main__":
    main()
