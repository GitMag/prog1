"""
COMP.CS.100 Programming 1
Code template for the hottest hit song Yogi Bear
"""

"""
Repeats a name for a specified amount of times
:param: name, str, the name to be repeated
:param: repetitions, int, the amount of repetitions in integer format
"""
def repeat_name(name, repetitions):
    """we initialize local variables"""
    n = name
    r = repetitions
    """we print a name a for a specified amount of repetitions"""
    for i in range(r):
        print(f"{n}, {n}", end="")
        if repetitions == 3:
            print(" Bear")
"""
Prints the yogi bear song with specfied verse and name of person
:param: name, str, the name to be repeated
:param: repetitions, int, the amount of repetitions in integer format
"""
def verse(verse_text, person_name):
    """Prints verse and combines repeat function to simplify printing"""
    print(verse_text)
    repeat_name(person_name, 1)
    print()
    print(verse_text)
    repeat_name(person_name, 3)
    print(verse_text)
    repeat_name(person_name, 1)
    print(" Bear", end="")
    if person_name != "Cindy":
        print("\n")


def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
