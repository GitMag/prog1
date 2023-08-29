"""
COMP.CS.100 Programming 1
Template for task: box printing
"""

"""
:param w: 
:param h: 
:param c: 
:return: 
"""
def print_box(w, h, c):
    """we define the variables to print the square"""
    width = int(w)
    height = int(h)
    char = c
    new_line_limit = height-1
    """we print the square row by row and check if we should add a new line.
    The last line for the square should not be with a new line"""
    for i in range(height):
        print(width * char, end="")
        if i < new_line_limit:
            print()


def main():
    width = input("Enter the width of a frame: ")
    height = input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
