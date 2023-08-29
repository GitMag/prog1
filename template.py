"""
COMP.CS.100 Programming 1
Code template for "replacing grades" program
"""


def convert_grades(grades_list):
    """
    Converts all grades over 0 to 6 and saves conversion to input list
    :param grades_list:
    :return: None
    """
    i = 0
    while i < len(grades_list):
        if grades_list[i] > 0:
            grades_list[i] = 6
        i += 1


def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
